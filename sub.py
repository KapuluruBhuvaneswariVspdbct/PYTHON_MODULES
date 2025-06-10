import subprocess
from subprocess import Popen,PIPE
s=subprocess.run(["dir"],shell=True,capture_output=True,check=True,text=True)
print(s.returncode)
print(s.stdout)
print(s.stderr)

s=subprocess.check_output("echo helloworld",shell=True,text=True)
print(s)

e=Popen("echo hello",stdin=PIPE,stdout=PIPE,shell=True)
p=Popen("findstr h",stdin=e.stdin,stdout=PIPE,shell=True)
print(p.stdout)