# Path to the text editor application you want to start
$env:TODO_DIR = ""
$env:python_exe = "C:\Python311\python.exe"
$env:applicationPath= ""

# Start the application
$appProcess = Start-Process $env:applicationPath -PassThru

# Wait for the app to exit
$appProcess.WaitForExit()

# Run the Python script - Replace my python script path with yours
& $env:python_exe test.py