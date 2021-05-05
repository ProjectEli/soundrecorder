# soundrecorder
Simple sound recorder module for recording wav files

# Dependencies
* [speech_recognition](https://github.com/Uberi/speech_recognition#readme)

# Usage
Before use, put `soundrecorder.py` file at callable directory
```py
import soundrecorder, time
SR = soundrecorder.SoundRecorder()
SR.record() # automatically stops when there is no sound
SR.save_wav('{}.wav'.format(time.strftime('%Y-%m-%d_%H-%M-%S')))
```

# Todo
- [ ] Audio visualization
