from cryptography.fernet import Fernet

# opening the key
with open('filekey.key', 'rb') as filekey:
	key = filekey.read()

# using the generated key
fernet = Fernet(key)

# opening the original file to encrypt
with open('important.txt', 'rb') as file:
	original = file.read()
	
# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and
# writing the encrypted data
with open('important.txt', 'wb') as encrypted_file:
	encrypted_file.write(encrypted)

