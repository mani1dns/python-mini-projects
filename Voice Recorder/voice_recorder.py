import sounddevice
from scipy.io.wavfile import write
fs=44100
seconds = int(input("Enter the time duration in seconds that you want to record : "))
print("recording...")
record_voice = sounddevice.rec(int(seconds * fs), samplerate=fs, channels=2)
sounddevice.wait()
write("sound.wav", fs, record_voice)
print("recording finished...")