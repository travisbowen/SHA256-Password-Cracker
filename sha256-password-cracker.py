from pwn import *

hashToCrack = input("Enter hash needed to be cracked:\n ").strip("\n").replace(" ", "")
password_file = input("Enter filename of passwords to compare to hash: ex.passwordList.txt\n ")


# Prints the hash that is being cracked
with log.progress("Attempting to crack: {}".format(hashToCrack)) as progress:
  # Enter filename of password dictionary file to compare against hash
  with open(password_file.strip("\n"), "r", encoding='latin-1') as password_list:
    for password in password_list:
      password = password.strip('\n').encode('latin-1')
      # Calculates the sha256 sum of a string - returns hex-encoded
      password_hash = sha256sumhex(password)
      progress.status('Hacking ‍💻.....')
      if password_hash == hashToCrack:
        progress.success("[+] Password found: {}".format(password.decode('latin-1')))
        exit()
    progress.failure("[X] Password hash not found!")
