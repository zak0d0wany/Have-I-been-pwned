#!/usr/bin/python3

import hashlib, requests, sys

passwd = sys.argv[1]

passwd_sha1 = hashlib.sha1(passwd.encode('UTF-8')).hexdigest()

response = requests.get('https://api.pwnedpasswords.com/range/' + passwd_sha1[0:5])


for line in response.text.splitlines():
        hash, count = line.split(":")
        if hash.lower() == passwd_sha1[5:]:
            print("Found: ",count)
            exit()
print("good password")