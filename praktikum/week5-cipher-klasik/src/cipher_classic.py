import math

# ==========================================
# 1. CAESAR CIPHER
# ==========================================
def caesar_encrypt(plaintext, key):
    """
    Enkripsi Caesar Cipher: Menggeser huruf sebanyak 'key'.
    Rumus: C = (P + K) mod 26
    """
    result = ""
    for char in plaintext:
        if char.isalpha():
            # Tentukan base (65 untuk A-Z, 97 untuk a-z)
            base = 65 if char.isupper() else 97
            # Lakukan pergeseran
            shifted = (ord(char) - base + key) % 26
            result += chr(shifted + base)
        else:
            # Jika bukan huruf (spasi/angka), biarkan tetap
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    """
    Dekripsi Caesar Cipher: Menggeser balik huruf.
    Rumus: P = (C - K) mod 26
    """
    return caesar_encrypt(ciphertext, -key)


# ==========================================
# 2. VIGENERE CIPHER
# ==========================================
def vigenere_encrypt(plaintext, key):
    """
    Enkripsi Vigenere: Menggunakan kunci kata untuk menggeser.
    """
    result = []
    key = key.lower()
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            # Hitung shift berdasarkan huruf kunci saat ini
            shift = ord(key[key_index % len(key)]) - 97
            
            # Enkripsi karakter
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(encrypted_char)
            
            # Pindah ke huruf kunci berikutnya
            key_index += 1
        else:
            result.append(char)
            
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    """
    Dekripsi Vigenere: Mengembalikan geseran berdasarkan kunci.
    """
    result = []
    key = key.lower()
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            shift = ord(key[key_index % len(key)]) - 97
            
            # Dekripsi karakter (kurangi shift)
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(decrypted_char)
            
            key_index += 1
        else:
            result.append(char)
            
    return "".join(result)


# ==========================================
# 3. TRANSPOSITION CIPHER (Columnar)
# ==========================================
def transpose_encrypt(plaintext, key):
    """
    Enkripsi Transposisi: Menulis pesan dalam kolom.
    """
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key):
    """
    Dekripsi Transposisi: Mengembalikan posisi kolom ke baris.
    Logic ini agak kompleks untuk menghitung 'kotak kosong' di grid.
    """
    # Hitung jumlah kolom, baris, dan kotak yang tidak terisi (shaded boxes)
    num_of_cols = int(math.ceil(len(ciphertext) / float(key)))
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        
        # Jika kolom habis, atau kita berada di area shaded box, pindah baris
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
            
    return ''.join(plaintext)


# ==========================================
# MAIN PROGRAM
# ==========================================
def main():
    print("="*50)
    print("      IMPLEMENTASI CIPHER KLASIK (WEEK 5)")
    print("      Nama : Mochamad Ilham Hansyil Alfauzi")
    print("      NIM  : 2320202767")
    print("="*50 + "\n")

    # --- UJI COBA 1: CAESAR ---
    print("[1] CAESAR CIPHER")
    text_caesar = "ILHAM STUDENT"
    key_caesar = 5
    
    enc_caesar = caesar_encrypt(text_caesar, key_caesar)
    dec_caesar = caesar_decrypt(enc_caesar, key_caesar)
    
    print(f"    Plaintext  : {text_caesar}")
    print(f"    Key        : {key_caesar}")
    print(f"    Ciphertext : {enc_caesar}")
    print(f"    Decrypted  : {dec_caesar}")
    print("-" * 50)

    # --- UJI COBA 2: VIGENERE ---
    print("[2] VIGENERE CIPHER")
    text_vig = "TEKNIK INFORMATIKA"
    key_vig = "ILHAM"
    
    enc_vig = vigenere_encrypt(text_vig, key_vig)
    dec_vig = vigenere_decrypt(enc_vig, key_vig)
    
    print(f"    Plaintext  : {text_vig}")
    print(f"    Key        : {key_vig}")
    print(f"    Ciphertext : {enc_vig}")
    print(f"    Decrypted  : {dec_vig}")
    print("-" * 50)

    # --- UJI COBA 3: TRANSPOSISI ---
    print("[3] TRANSPOSITION CIPHER")
    text_trans = "KEAMANAN DATA"
    key_trans = 4
    
    enc_trans = transpose_encrypt(text_trans, key_trans)
    dec_trans = transpose_decrypt(enc_trans, key_trans)
    
    print(f"    Plaintext  : {text_trans}")
    print(f"    Key        : {key_trans}")
    print(f"    Ciphertext : {enc_trans}")
    print(f"    Decrypted  : {dec_trans}")
    print("=" * 50)

if __name__ == "__main__":
    main()