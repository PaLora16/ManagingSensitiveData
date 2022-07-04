from decrypt import decrypt
from config import pavels_config

if __name__ == "__main__":
    # encrypted name from the config file
    enrypt_mes = pavels_config().get_scotch()

    # decrypt
    decrypt_mes = decrypt(enrypt_mes)

    print(f"Pavels favourite scotch is {decrypt_mes}")
