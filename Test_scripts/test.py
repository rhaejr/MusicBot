import subprocess

proc = subprocess.Popen("/Test_scripts/test.sh")
print(proc.pid)
print(proc.wait())