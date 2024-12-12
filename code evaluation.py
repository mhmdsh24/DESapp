from Crypto.Cipher import DES
from app import desv2
import pandas as pd


test_df = pd.read_csv("DES_Test_Cases.csv") 

def evaluate_encrypt_function(encrypt):
    """
    Evaluates a custom DES encryption function by comparing its output to PyCryptodome.
    """
    for index, row in test_df.iterrows():
        plaintext = row["Plaintext"]
        key = row["Key"]
        
        # Encrypt using your custom function
        custom_ciphertext,_ = encrypt(plaintext, key)
        
        # Encrypt using a trusted library for validation
        trusted_cipher = DES.new(bytes.fromhex(key), DES.MODE_ECB)
        trusted_ciphertext = trusted_cipher.encrypt(bytes.fromhex(plaintext)).hex().upper()
        
        # Compare results
        if custom_ciphertext == trusted_ciphertext:
            print(f"Test {index + 1}: PASS")
        else:
            print(f"Test {index + 1}: FAIL")
            print(f"Plaintext: {plaintext}, Key: {key}")
            print(f"Expected: {trusted_ciphertext}, Got: {custom_ciphertext}")

def evaluate_decrypt_function(decrypt):
    """
    Evaluates a custom DES decryption function by comparing its output to PyCryptodome.
    """
    for index, row in test_df.iterrows():
        ciphertext = row["Plaintext"]
        key = row["Key"]
        
        # decrypt using your custom function
        custom_plaintext,_ = decrypt(ciphertext, key)
        
        # decrypt using a trusted library for validation
        trusted_cipher = DES.new(bytes.fromhex(key), DES.MODE_ECB)
        trusted_ciphertext = trusted_cipher.decrypt(bytes.fromhex(ciphertext)).hex().upper()
        
        # Compare results
        if custom_plaintext == trusted_ciphertext:
            print(f"Test {index + 1}: PASS")
        else:
            print(f"Test {index + 1}: FAIL")
            print(f"Plaintext: {ciphertext}, Key: {key}")
            print(f"Expected: {trusted_ciphertext}, Got: {custom_plaintext}")


print("Encryption:")
evaluate_encrypt_function(desv2.encrypt)

print("Decryption:")
evaluate_decrypt_function(desv2.decrypt)


