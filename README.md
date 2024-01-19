# About
This setup provides a way to add/delete/complete and edit tasks from your note taking app without the need to interact with any other software or promise yourself you'll do it later

# Setup
## wrapper.ps1
- Add your note taking executable file to the $applicationPath variable
e.g
```
$applicationPath = 'C:\path\to\your\obsidian\application\Obsidian.exe'
```
- Change ``C:\Python311\python.exe`` to your default python executable

## credentials.json
- Follow this [tutorial](https://developers.google.com/workspace/guides/create-credentials#desktop-app) to get your credentials.json file. Remember to download the json and replace the current credentials.json file.

## python
- Install the dependencies
```
pip install -r requirements.txt
```

# Steps to run
cd to the repository
## python
- You could run the test.py file with
```bash
python text.py
```
## powershell
- You can run the logic using powershell
```powershell
./wrapper.ps1
```
### Note
```
I plan on adding support for other os in the future
```

# Futher steps
You can transform the logic into an executable file for easier access or to replace your default text editor shortcut

## Windows
https://www.advancedinstaller.com/convert-powershell-to-exe.html

# Bug reports
If you encounter any issues with the documentation or have suggestions for improving the project, please feel free to open an issue!