import os
from os import system

cnt = 0

while True:
    with open("a.txt", "w") as f:
        f.write(str(cnt))
    cnt += 1
    system("git add .")
    system("git commit -m \"upd\" ")
    print("commit ++")
    system("git push")
