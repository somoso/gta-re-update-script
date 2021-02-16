# gta-re-update-script
Scripts to update my Steam copies of GTA to the RE version and add a desktop shortcut


## Usage instruction

### Powershell

Standard Windows Powershell script. To use, run `update-re.ps1`. A bit inflexible, but is great if you just want to download and run.

### Python3

More customisable, has more extensibility. Once I get GTA 3/VC running on my Mac, I'll update the Python3 script further to support those cases.

Use `steam.ini.example` as a baseline for your `steam.ini`. Mainly used for non-Windows OSes if there isn't a flexible way to grab Steam install directory easily.

Use `rc.ini` to tweak what files get downloaded and if you want the shortcut to the desktop.


## Warning Note

**Please do not run this script automatically, as it downloads files from the web and automatically extracts it to your directory. This is a security risk if you are just blindly updating it without checking the github repo**.

The GTA RE github repo can be found here: https://github.com/GTAmodding/re3/

Ensure the repo is sound and that the Github actions is building sensible builds before running the script.

## Todo

* ~Make python version~
* ~Move config variable out into a seperate file (ini)~
* Add some sort of file or a marker to indicate when the script was last run to avoid aggressively throttling the server.
  * Make the time limit something to like a week
* Backup user saves into a user specified config directory (just in case a build breaks something and user needs to redownload)
