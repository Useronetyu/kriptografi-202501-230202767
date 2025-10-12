# -*- coding: utf-8 -*-
"""
Program Sederhana untuk Enkripsi dan Dekripsi menggunakan Caesar Cipher.
"""

def encrypt(text, key):
    """
    Fungsi untuk mengenkripsi teks menggunakan Caesar Cipher.

    Args:
        text (str): Teks asli yang akan dienkripsi (plaintext).
        key (int): Jumlah pergeseran (kunci).

    Returns:
        str: Teks yang sudah dienkripsi (ciphertext).
    """
    result = ""
    
    # Loop melalui setiap karakter dalam teks
    for i in range(len(text)):
        char = text[i]
        
        # Enkripsi karakter uppercase
        if (char.isupper()):
            # Rumus enkripsi: E(x) = (x + n) mod 26
            # Mengubah karakter ke ASCII, menggeser, dan kembali ke karakter
            result += chr((ord(char) + key - 65) % 26 + 65)
        # Enkripsi karakter lowercase
        elif (char.islower()):
            result += chr((ord(char) + key - 97) % 26 + 97)
        # Jika bukan huruf (spasi, angka, simbol), biarkan apa adanya
        else:
            result += char
            
    return result

def decrypt(text, key):
    """
    Fungsi untuk mendekripsi teks yang dienkripsi dengan Caesar Cipher.

    Args:
        text (str): Teks terenkripsi (ciphertext).
        key (int): Jumlah pergeseran yang sama dengan saat enkripsi.

    Returns:
        str: Teks asli yang sudah didekripsi (plaintext).
    """
    # Untuk dekripsi, kita hanya perlu mengenkripsi dengan kunci negatif
    # atau menggunakan kunci (26 - key).
    return encrypt(text, 26 - key)

# --- Main Program Execution ---
if __name__ == "__main__":
    # Program akan berjalan jika file ini dieksekusi secara langsung
    
    print("========================================")
    print("      PROGRAM CAESAR CIPHER             ")
    print("========================================")
    
    try:
        # Meminta input dari pengguna
        plaintext = input("Masukkan Teks         : ")
        key = int(input("Masukkan Kunci (angka)  : "))
        
        # Validasi kunci agar berada dalam rentang 1-25
        if not (1 <= key < 26):
            print("\nError: Kunci harus berupa angka antara 1 dan 25.")
        else:
            # Melakukan enkripsi dan dekripsi
            encrypted_text = encrypt(plaintext, key)
            decrypted_text = decrypt(encrypted_text, key)
            
            # Menampilkan hasil
            print("----------------------------------------")
            print(f"Plaintext             : {plaintext}")
            print(f"Kunci                 : {key}")
            print(f"Hasil Enkripsi        : {encrypted_text}")
            print(f"Hasil Dekripsi        : {decrypted_text}")
            print("========================================")

    except ValueError:
        print("\nError: Input kunci tidak valid. Harap masukkan angka.")
    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}")
