import subprocess

proc = subprocess.Popen("test.sh")
print(proc.pid)
print(proc.wait())