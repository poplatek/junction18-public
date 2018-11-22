import boto3
import pyaudio

def polly(polly_client, text):
    polly_response = polly_client.synthesize_speech(
        OutputFormat='pcm', Text=text, VoiceId='Matthew')
    return polly_response['AudioStream'].read()

def play_audio(pya, soundbytes, output_device_index, rate=16000):
    ''' Lex/Polly PCM response audio is by default 16kHz '''
    stream = pya.open(output_device_index=output_device_index, format=pya.get_format_from_width(
        width=2), channels=1, rate=rate, output=True)
    stream.write(soundbytes)
    stream.stop_stream()
    stream.close()

polly_client = boto3.client('polly')
pya = pyaudio.PyAudio()

# Check out the device ids using list-audio-devices.py
# The defaults here are for Jabra USB speaker+mic
PYAUDIO_OUTPUT_DEVICE = 1

audiodata = polly(polly_client, 'Polly wants a cracker')
play_audio(pya, audiodata, PYAUDIO_OUTPUT_DEVICE)
