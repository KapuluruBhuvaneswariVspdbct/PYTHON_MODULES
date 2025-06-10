import sys
original_stdin=sys.stdin
original_stdout=sys.stdout
original_stderr=sys.stderr

sys.stdin=open("inp.txt","r",encoding="utf-8")
data=sys.stdin.read()
sys.stdout=open("op.txt","a",encoding="utf-8")
sys.stdout.write(data)
with open("k.txt","a",encoding="utf-8") as f:
    sys.stderr=f
    sys.stderr.write("None Error")
sys.stdin.close()
sys.stdout.close()
sys.stderr.close()
sys.tdin=original_stdin
sys.stdout=original_stdout
sys.stderr=original_stderr
print(sys.platform)
print(sys.version)
print(sys.argv)
print(sys.path)
print('sys' in sys.modules)
print(sys.getsizeof(5))
print(sys.getrecursionlimit())
print(sys.setrecursionlimit(3))
print(sys.flags)
