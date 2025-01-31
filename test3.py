import re
import subprocess

pro =subprocess.Popen(
    "/challenge/run",
    stdin.subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    encoding='utf-8'
)

while True :
    line = pro.stdout.readline().strip()
