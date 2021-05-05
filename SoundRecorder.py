import speech_recognition

class SoundRecorder:
    def __init__(self,Microphone=None):
        if Microphone == None:
            self.mic = speech_recognition.Microphone()
        else: # for predefined mic object
            self.mic = Microphone
        self.audio = None
        self.defaultfilename = 'RecordedAudio.wav'

    def record(self): # automatically ends when there's no sound
        with speech_recognition.Microphone() as src:
            print("Listening...")
            self.audio = speech_recognition.Recognizer().listen(src)

    def save_wav(self,filename=None): # bitrate: mic's default setting
        if filename == None: 
            filename = self.defaultfilename
        with open(filename,'wb') as f:
            f.write(self.audio.get_wav_data())

def main():
    SR = SoundRecorder()
    SR.record()
    import time # avoid loading for module use
    SR.save_wav('{}.wav'.format(time.strftime('%Y-%m-%d_%H-%M-%S')))

if __name__ == "__main__":
    main()