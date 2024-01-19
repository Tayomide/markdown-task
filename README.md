# About
This setup provides a way to add/delete/complete and edit tasks from your note-taking app without the need to interact with any other software(like google tasks) or promise yourself you'll do it later

# Setup
## wrapper.ps1
- Add your note-taking executable file to the $applicationPath variable
e.g
```
$applicationPath = 'C:\path\to\your\obsidian\application\Obsidian.exe'
```
- Change ``C:\Python311\python.exe`` to your default python executable

## credentials.json
- Follow this [tutorial](https://developers.google.com/workspace/guides/create-credentials#desktop-app) to get your credentials.json file. Remember to download the JSON and replace the current credentials.json file.

## python
- Install the dependencies
```
pip install -r requirements.txt
```

# Steps to run
cd to the repository
## python
- You can run the test.py file with
```bash
python text.py
```
## PowerShell
- You can run the logic using Powershell
```PowerShell
./wrapper.ps1
```
### Note
```
I plan on adding support for other OS in the future
```

# Further steps
You can transform the logic into an executable file for easier access or to replace your default text editor shortcut

## Windows
https://www.advancedinstaller.com/convert-powershell-to-exe.html

# End Result
![image](https://github.com/Tayomide/markdown-task/assets/70061548/2e3d5d8b-0662-466d-b5f1-dadd26dc2212)

# Bug reports
If you encounter any issues with the documentation or have suggestions for improving the project, please feel free to open an issue!
