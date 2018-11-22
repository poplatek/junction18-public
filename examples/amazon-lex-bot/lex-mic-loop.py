import boto3
import speech_recognition as sr
import pyaudio
import json


def play_audio(pya, soundbytes, output_device_index, rate=16000):
    ''' Lex/Polly PCM response audio is by default 16kHz '''
    stream = pya.open(output_device_index=output_device_index, format=pya.get_format_from_width(
        width=2), channels=1, rate=rate, output=True)
    stream.write(soundbytes)
    stream.stop_stream()
    stream.close()


lex_client = boto3.client('lex-runtime')

recognizer = sr.Recognizer()
pya = pyaudio.PyAudio()

# Check out the device ids using list-audio-devices.py
SPEECH_RECOGNITION_MIC_DEVICE = 0
PYAUDIO_OUTPUT_DEVICE = 1

# Publish your Lex bot, and write the name and alias (points to a version) here
LEX_BOT_NAME = 'TestBot'
LEX_BOT_ALIAS = 'latest'

# Higher threshold catches less noise, and makes automatic recoding more precise, but
# too high threshold begins to miss potential voice recordings.
# It's also possible to use the automatic calibration (r.adjust_for_ambient_noise(source)),
# but it doesn't seem to work too well.
recognizer.energy_threshold = 200
recognizer.dynamic_energy_threshold = False

# Amazon Lex only accepts 16kHz or 8kHz
with sr.Microphone(device_index=SPEECH_RECOGNITION_MIC_DEVICE, sample_rate=16000) as mic_source:

    while True:

        print('Speak (automatically detects when to start and stop recording):')
        audio = recognizer.listen(mic_source)

        print('Audio captured, now sending to Lex...')

        wavdata = audio.get_wav_data()

        # Write to file for debugging (easy way to check the volume levels)
        with open('recorded-voice.wav', 'wb') as wavfile:
            wavfile.write(wavdata)

        try:
            # The session can be changed with the userId -parameter
            # (you can have parallel conversations for different users)
            user_id = 'mycustomer1'

            lex_result = lex_client.post_content(
                botName=LEX_BOT_NAME,
                botAlias=LEX_BOT_ALIAS,
                userId=user_id,
                sessionAttributes={},  # key: value
                requestAttributes={},  # key: value
                contentType='audio/l16; rate={}; channels=1'.format(
                    audio.sample_rate),
                inputStream=wavdata,
                accept='audio/pcm')

            print('Lex:\n', json.dumps(lex_result,
                                       indent=2, default=lambda o: '<not serializable>'))

            play_audio(
                pya, lex_result['audioStream'].read(), PYAUDIO_OUTPUT_DEVICE)

        except Exception as e:
            print('ERROR:')
            print(e)
