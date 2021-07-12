import subprocess
import webbrowser

try:
    # webbrowser.open("http://saudkhan.net")
    completed = subprocess.run(["python","app.py"], capture_output=True, text=True, check=True)
    print(completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)