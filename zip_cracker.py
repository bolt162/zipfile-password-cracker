import sys
import zipfile
import os
from threading import Thread

def crack_zip(z, password):
	try:
		z.extractall(pwd=password.encode('utf-8'))
		print("[+] Password: " + password)
		exit(0)
	except Exception as e:
		pass

def main():
	if len(sys.argv) == 3:
		dicfile = sys.argv[2]
		d = open(dicfile, 'r')
		z = zipfile.ZipFile(sys.argv[1])
		for line in d.readlines():
			password = line.strip('\n')
			t = Thread(target=crack_zip, args=(z, password))
			t.start()
	else:
		print("[-] Usage: python3 zip_cracker.py <zipfile.zip> <dictionary.txt>")


if __name__ == '__main__':
	main()