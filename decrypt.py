import os
import pyaes

name = "arquivo.txt.lock"
file = open(name, "rb")
data = file.read()
file.close()

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(data)
os.remove(name)

new_file = "arquivo.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
