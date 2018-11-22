import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
pya = pyaudio.PyAudio()

print("\nPython speech_recognition microphone devices:")
micnames = sr.Microphone.list_microphone_names()
for i in range(0, len(micnames)):
    print('{}: {}'.format(i, micnames[i]))

print("\nPyaudio output devices (missing indices are not output devices):")
info = pya.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range (0, numdevices):
    if pya.get_device_info_by_host_api_device_index(0, i).get('maxOutputChannels') > 0:
        print('{}: {}'.format(i, pya.get_device_info_by_host_api_device_index(0, i).get('name')))
