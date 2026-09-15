from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

# Original flag
flag = "cybercamp{your_flag_here}"

# Key MUST be 16, 24, or 32 bytes long for AES
key = b"this is a key123"

# Initialization vector
iv = b"this is an iv456"

# Create a new AES cipher object
cipher = AES.new(key, AES.MODE_CBC, iv=iv)

# Encrypt the flag
encrypted_flag = cipher.encrypt(pad(flag.encode(), AES.block_size))

# Encode the encrypted flag as base64 so it can be printed and provided to the participants
encrypted_flag_b64 = b64encode(encrypted_flag).decode('utf-8')

print(f"Encrypted flag: {encrypted_flag_b64}")

