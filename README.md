## python_light_audio_helper (tested only on macOS)

install env and activate
```bash
    sudo pip install virtualenv
    python -m venv env
    source env/bin/activate
```

install brew if macOS
```bash
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
and Xcode ...

then install
```bash
    brew install portaudio
```

then install
```bash 
    sudo pip install -r requirements.txt
```

if you have libs but code didn't work, run:
```bush
    sudo pip install --upgrade speechrecognition
    sudo pip install --upgrade pyaudio 
```
it's have to work now. 
