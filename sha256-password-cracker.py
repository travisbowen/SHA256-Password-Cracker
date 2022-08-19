from pwn import *
import sys

hashToCrack = input("Enter hash needed to be cracked:\n ")

# Prints the hash that is being cracked
with log.progess("Attempting to crack: {}!\n".format(hashToCrack)) as p:
    # Enter filename of password dictionary file to compare against hash
    with open(input("Enter filename of passwords to compare to hash: ex.passwordList.txt\n ").strip("\n"), "r", encoding='latin-1') as password_list:
        for password in password_list:
            password = password.strip('\n').encode('latin-1')
            # Calculates the sha256 sum of a string; returns hex-encoded
            password_hash = sha256sumhex(password)
            p.status("Trying password: {} hashed as {}".format(
                password.decode('latin-1'), password_hash))
            if password_hash == hashToCrack:
                p.success(
                    "[+] Password found: {}".format(password.decode('latin-1')))
                exit()
        p.failure("[X] Password hash not found!")
