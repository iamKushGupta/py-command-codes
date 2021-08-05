# "netsh wlan show profile" is just an example, you may input any Windows command.
import subprocess

command = "netsh wlan show profile"
subprocess.call(command, shell=True) # If you want the output on Terminal.
# subprocess.Popen(command, shell=True) # Uncomment if you want the command to be executed in background.
