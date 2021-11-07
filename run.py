#!/usr/bin/env python3
import yagmail
import getpass
import os

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

os.system('clear')

print(cy+"[+] Send Email Tool V1.0")
print("")

fromm = input('[+] From : '+gr)
print(""+cy)

password = getpass.getpass()
print("")

too = input('[+] To : '+gr)
print(""+cy)

sub = input('[+] Email Subject : '+gr)
print(""+cy)

massage = input('[+] Enter the Body : '+gr)
print(""+cy)

yagmail.SMTP(fromm, password).send(to=too, subject=sub, contents=massage)

print("[+] Sent Successfully...")

# Author - AnonyVox
