#!/usr/bin/python3

import hashlib, requests

def checkname (name):
        name_sha1 = hashlib.sha1(name.encode('UTF-8 ')).hexdigest()
        response = requests.get("https://api.pwnedpasswords.com/range/" + name_sha1[0:5])

        for line in response.text.splitlines():
                hash, count = line.split(":")
                if hash.lower() == name_sha1[5:]:
                        return int(count)
        return 0

names = open("imiona_ok.txt", "r").read().splitlines()

a=[]
for n in names:
        a.append([n.lower(),checkname(n.lower())])

aa = sorted(a, key=lambda  l:l[1])
for n in aa:
        print (n[0], " - ", n[1])
