import bcrypt
import base64
hashed_password = bcrypt.hashpw(
                        "1234567".encode("utf-8"),
                        bcrypt.gensalt())
print(hashed_password)
print("After")

hashed_password = bcrypt.hashpw(
                        "1234567".encode("utf-8"),
                        bcrypt.gensalt())
print(hashed_password)