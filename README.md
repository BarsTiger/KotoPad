# KotoPad

KotoPad is free, open-source and multifunctional SoundPad/Soundux analog that uses VB-Cable written on PyQt5 with many useful features and fixes to problems present in Soundpad and Soundux, found by me as an active user of these programs

## 📥 Installation

Download [latest windows release build from this direct link](https://github.com/BarsTiger/KotoPad/releases/latest/download/KotoPad.zip) or choose version from [releases tab](https://github.com/BarsTiger/KotoPad/releases). Unpack KotoPad.zip where do you want to be app installed.

Download VB-CABLE from [here](https://vb-audio.com/Cable/) or use [this direct link to archive](https://download.vb-audio.com/Download_CABLE/VBCABLE_Driver_Pack43.zip). Unpack VBCABLE_Driver_Pack43.zip and launch VBCABLE_Setup_x64.exe as an administrator. Press `Install driver` and restart your PC if KotoPad won't work.

Download [VLC Media Player (windows)](https://www.videolan.org/vlc/) and install it.

Run KotoPad.exe from folder you have unpacked or create shortcut for it. In settings of your Discord/Teamspeak/Zoom/Teams or any app choose CABLE Output as microphone. Also you can set it as default in settings. 

Set up devices on settings tab, turn on micro restreaming if you need other people to hear you. 

## ❗ Need to know

There are two play methods and each of them has pros and cons depending on what type of sound you are trying to play.

Direct stream method is default and preferred if playing files from YouTube, Spotify URL or long files from your hard drive. It CAN cut last second of audio but doesn't need long time to load file first time.

Download and convert method can cause long first load time and app crashes when playing sound at first time, but it doesn't cut last second of audio. Use it when you are trying to play short files from your hard drive.

|                                                              |                     Direct stream method                     |                 Download and convert method                  |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|             Load time for files from hard drive              |                              0s                              |           Depends on file size, couple of seconds            |
|  Load time for files from hard drive if they played already  |                              0s                              |                         0s (cached)                          |
|         Load time for files from YouTube and Spotify         |                 8-10s, depends on connection                 |        Depends on file size, can take couple minutes         |
| Load time for files from YouTube and Spotify if they played already |                 8-10s, depends on connection                 |                 0s, because of cache in temp                 |
|                      Cuts end of sound                       |                           Can cut                            |                         Doesn't cut                          |
|                        Can crash app                         |                              No                              | Yes, but better to wait couple of minutes when downloading song from Spotify or YouTube, after that app will unlagg |
|                  Needs internet connection                   |            Every time you play the file from web             |    Only when you are playing file from web for first time    |
|                        Recommended if                        | Streaming from link or YouTube/Spotify and you cannot wait for file to fully download. Also it is recommended for playing long files from your hard drive | Playing short files from hard drive or if first method doesn't work properly for YouTube link. Also you can use this if you can wait for song from Spotify to load for couple of minutes and save it in cache to play it instantly next time |

## 🔨 Building custom release for Windows

Use Python 3.10

```
git clone https://github.com/BarsTiger/KotoPad
cd KotoPad
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pyinstaller KotoPad.spec
```
