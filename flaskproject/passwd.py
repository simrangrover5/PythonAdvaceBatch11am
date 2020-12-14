import pickle
from cryptography.fernet import Fernet

key = Fernet.generate_key()
key_ = Fernet(key)
cipher = key_.encrypt(b"simran")
text = key_.decrypt(cipher)
with open("mypass.pkl", "wb") as fp:
    pickle.dump(cipher, fp)

with open("mypass.pkl", "rb") as fp:
    text = pickle.load(fp)
    password = key_.decrypt(text).decode()
    print(password)    


# store password in another file and store key in another file
