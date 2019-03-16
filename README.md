## python_light_audio_helper (tested only on macOS)

install env and activate
```bash
    sudo pip3 install virtualenv
    python3 -m venv env
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
    sudo pip3 install -r requirements.txt
```

if you have libs but code didn't work, run:
```bush
    sudo pip3 install --upgrade speechrecognition
    sudo pip3 install --upgrade pyaudio 
```
it's have to work now. 