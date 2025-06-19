import subprocess
import sys


command = "gallery-dl -D input --range 1:9 --filter \"extension in ('jpg')\" " + sys.argv[1]
print(command)
result = subprocess.run(command, shell=True, capture_output=True, text=True)