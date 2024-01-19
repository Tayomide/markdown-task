# Path to the text editor application you want to start
$applicationPath = 'C:\path\to\your\obsidian\application\Obsidian.exe'

# Start the application
$appProcess = Start-Process $applicationPath -PassThru

# Wait for the app to exit
$appProcess.WaitForExit()

# Run the Python script - Replace my python script path with yours
C:\Python311\python.exe test.py
