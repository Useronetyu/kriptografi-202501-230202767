import hashlib
import time

def md5_hash(text):
    """
    Fungsi bantu untuk mengubah text menjadi MD5 hash.
    """
    return hashlib.md5(text.encode()).hexdigest()

def dictionary_attack(target_hash, dictionary_list):
    """
    Melakukan serangan Dictionary Attack:
    Mencocokkan hash dari setiap kata di kamus dengan hash target.
    """
    print(f"[!] Memulai serangan Dictionary Attack...")
    print(f"[!] Target Hash : {target_hash}")
    print(f"[!] Jumlah Kata : {len(dictionary_list)} kata di kamus")
    print("-" * 50)
    
    start_time = time.time()
    attempts = 0
    found = False

    for word in dictionary_list:
        attempts += 1
        
        # 1. Hashing kata dari kamus
        word_hash = md5_hash(word)
        
        # 2. Bandingkan dengan target (Pencocokan)
        if word_hash == target_hash:
            end_time = time.time()
            duration = end_time - start_time
            
            print(f"\n[SUCCESS] PASSWORD DITEMUKAN! 🎉")
            print(f"==================================")
            print(f"Password Asli : {word}")
            print(f"Hash MD5      : {word_hash}")
            print(f"Waktu         : {duration:.6f} detik")
            print(f"Percobaan     : {attempts} kali")
            print(f"==================================")
            found = True
            break
            
    if not found:
        print("\n[FAILED] Password tidak ditemukan di dictionary ini.")

if __name__ == "__main__":
    print("="*60)
    print("      SIMULASI SERANGAN KRIPTOGRAFI (MD5 CRACKING)")
    print("      Nama : Mochamad Ilham Hansyil Alfauzi")
    print("      NIM  : 2320202767")
    print("="*60 + "\n")

    # ==========================================
    # SKENARIO SERANGAN
    # ==========================================
    
    # 1. Target: Hash ini didapat dari "Database Bocor"
    # Password aslinya adalah "ilham123"
    target_leaked_hash = "8b3260d5b59740263303681422784570"
    
    # 2. Dictionary: Daftar kata yang umum dipakai orang
    # Dalam serangan nyata, file ini (misal: rockyou.txt) bisa berisi jutaan kata.
    common_passwords = [
        "123456", "password", "12345678", "qwerty", "123456789",
        "12345", "1234", "111111", "1234567", "dragon",
        "admin", "admin123", "root", "user", "guest",
        "ilham", "ilham_ganteng", "ilham123", "hansyil", # <-- Password ada di sini
        "rahasia", "bismillah", "sayang", "doraemon"
    ]

    # 3. Jalankan Serangan
    dictionary_attack(target_leaked_hash, common_passwords)
    
    print("\n[ANALISIS]")
    print("MD5 sangat cepat. Komputer modern bisa mengecek miliaran hash/detik.")
    print("Tanpa 'Salt', password mudah ditebak dengan teknik ini.")
    print("="*60)