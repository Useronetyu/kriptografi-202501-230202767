from Crypto.Cipher import DES, AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# ==========================================
# 1. DEMO DES (Legacy / Tidak Aman)
# ==========================================
def demo_des():
    print("\n" + "="*50)
    print("[1] DEMO DES (Data Encryption Standard)")
    print("="*50)
    
    # 1. Buat Kunci: DES menggunakan kunci 8 byte (64 bit)
    # Catatan: Hanya 56 bit yang efektif digunakan.
    key = get_random_bytes(8)
    
    # 2. Inisialisasi Cipher (Mode ECB - Electronic Codebook)
    cipher_encrypt = DES.new(key, DES.MODE_ECB)
    
    # 3. Siapkan Plaintext
    # DES bekerja pada blok 8 byte. Kita gunakan 'pad' agar panjang data pas.
    data = b"ILHAM_DES_TEST"
    plaintext_padded = pad(data, DES.block_size)
    
    print(f"Plaintext Asli   : {data}")
    print(f"Padded Plaintext : {plaintext_padded}")
    
    # 4. Enkripsi
    ciphertext = cipher_encrypt.encrypt(plaintext_padded)
    print(f"Ciphertext (Hex) : {ciphertext.hex()}")
    
    # 5. Dekripsi
    cipher_decrypt = DES.new(key, DES.MODE_ECB)
    decrypted_padded = cipher_decrypt.decrypt(ciphertext)
    
    # Hilangkan padding (unpad)
    decrypted_data = unpad(decrypted_padded, DES.block_size)
    print(f"Decrypted        : {decrypted_data}")


# ==========================================
# 2. DEMO AES-128 (Standar Modern)
# ==========================================
def demo_aes():
    print("\n" + "="*50)
    print("[2] DEMO AES-128 (Advanced Encryption Standard)")
    print("="*50)
    
    # 1. Buat Kunci: AES-128 menggunakan kunci 16 byte (128 bit)
    key = get_random_bytes(16)
    
    # 2. Inisialisasi Cipher (Mode EAX - Encrypt-then-Authenticate)
    # Mode EAX memberikan keamanan data (kerahasiaan) dan integritas.
    cipher = AES.new(key, AES.MODE_EAX)
    
    # 3. Siapkan Plaintext
    data = b"Pesan Rahasia AES Ilham Hansyil - 2320202767"
    print(f"Plaintext        : {data}")
    
    # 4. Enkripsi & Digest (Tag)
    # 'ciphertext' adalah data terenkripsi
    # 'tag' digunakan untuk memverifikasi bahwa data tidak diubah (integritas)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    
    print(f"Ciphertext (Hex) : {ciphertext.hex()}")
    print(f"Tag Integritas   : {tag.hex()}")
    print(f"Nonce (Unik)     : {cipher.nonce.hex()}")
    
    # 5. Dekripsi & Verifikasi
    # Kita butuh 'nonce' yang sama untuk mendekripsi
    cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
    
    try:
        decrypted_data = cipher_dec.decrypt_and_verify(ciphertext, tag)
        print(f"Decrypted        : {decrypted_data.decode('utf-8')}")
    except ValueError:
        print("Error: Integritas data gagal! Kunci salah atau data dimodifikasi.")


# ==========================================
# 3. DEMO RSA (Asimetris / Public Key)
# ==========================================
def demo_rsa():
    print("\n" + "="*50)
    print("[3] DEMO RSA (Rivest-Shamir-Adleman)")
    print("="*50)
    
    print("Sedang membangkitkan pasangan kunci RSA 2048-bit...")
    print("(Ini mungkin memakan waktu beberapa detik)")
    
    # 1. Generate Pasangan Kunci (2048 bit)
    key_pair = RSA.generate(2048)
    
    public_key = key_pair.publickey()
    private_key = key_pair
    
    print(f"Public Key (n, e) dibangkitkan.")
    print(f"Private Key (n, d) dibangkitkan.")
    
    # 2. Siapkan Plaintext
    data = b"Kunci Sesi Rahasia Untuk Server"
    print(f"\nPlaintext        : {data}")
    
    # 3. Enkripsi dengan PUBLIC KEY
    # Menggunakan padding OAEP (Optimal Asymmetric Encryption Padding) agar aman
    encryptor = PKCS1_OAEP.new(public_key)
    ciphertext = encryptor.encrypt(data)
    
    print(f"Ciphertext (Hex) : {ciphertext.hex()[:64]}... (dipotong karena panjang)")
    print(f"Panjang Cipher   : {len(ciphertext)} bytes")
    
    # 4. Dekripsi dengan PRIVATE KEY
    decryptor = PKCS1_OAEP.new(private_key)
    decrypted_data = decryptor.decrypt(ciphertext)
    
    print(f"Decrypted        : {decrypted_data.decode('utf-8')}")


# ==========================================
# PROGRAM UTAMA
# ==========================================
if __name__ == "__main__":
    print("Mochamad Ilham Hansyil Alfauzi - 2320202767")
    print("Praktikum Kriptografi Week 6")
    
    demo_des()
    demo_aes()
    demo_rsa()