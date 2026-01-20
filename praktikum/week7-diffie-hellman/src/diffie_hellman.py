import random

# ==========================================
# KONFIGURASI UMUM
# ==========================================
def get_public_parameters():
    """
    Mengembalikan bilangan prima (p) dan generator (g).
    Untuk simulasi ini, kita gunakan angka kecil agar mudah dipahami.
    Dalam praktiknya, p harus bilangan prima sangat besar (misal 2048 bit).
    """
    p = 23  # Modulus (Prime Number)
    g = 5   # Base (Generator)
    return p, g

# ==========================================
# 1. SIMULASI NORMAL (AMAN)
# ==========================================
def simulation_normal(p, g):
    print("\n" + "="*60)
    print(f"1. SIMULASI PERTUKARAN KUNCI NORMAL (P={p}, G={g})")
    print("="*60)

    # 1. Alice & Bob memilih Private Key (Rahasia)
    # Range: 1 sampai p-1
    a = random.randint(1, p-1) 
    b = random.randint(1, p-1)
    
    print(f"[Private] Alice : {a}")
    print(f"[Private] Bob   : {b}")

    # 2. Menghitung Public Key
    # Rumus: g^private mod p
    A = pow(g, a, p)
    B = pow(g, b, p)

    print(f"[Public]  Alice -> Mengirim A={A} ke Bob")
    print(f"[Public]  Bob   -> Mengirim B={B} ke Alice")
    print("-" * 60)

    # 3. Menghitung Shared Secret (Kunci Bersama)
    # Alice pakai Public Bob (B) dan Private sendiri (a): B^a mod p
    secret_Alice = pow(B, a, p)
    
    # Bob pakai Public Alice (A) dan Private sendiri (b): A^b mod p
    secret_Bob = pow(A, b, p)

    print(f"[Secret]  Alice menghitung : {secret_Alice}")
    print(f"[Secret]  Bob menghitung   : {secret_Bob}")

    if secret_Alice == secret_Bob:
        print(f">> SUKSES: Kunci rahasia SAMA ({secret_Alice}). Komunikasi Aman.")
    else:
        print(">> ERROR: Kunci tidak cocok!")

# ==========================================
# 2. SIMULASI SERANGAN MITM (MAN-IN-THE-MIDDLE)
# ==========================================
def simulation_mitm(p, g):
    print("\n" + "="*60)
    print("2. SIMULASI SERANGAN MITM (EVE MENGINTAI)")
    print("="*60)

    # 1. Setup Awal
    a = random.randint(1, p-1) # Alice Private
    b = random.randint(1, p-1) # Bob Private
    e = random.randint(1, p-1) # Eve Private (Penyerang)

    # Public Keys Asli
    A = pow(g, a, p)
    B = pow(g, b, p)
    
    # Public Key Palsu milik Eve
    E = pow(g, e, p)

    print(f"[Info] Alice Private: {a}, Bob Private: {b}")
    print(f"[Info] Eve (Hacker) Private: {e}, Public Eve: {E}")
    print("-" * 60)

    # 2. Proses Intersepsi (Penyadapan)
    print("STATUS: Eve berada di tengah jalur komunikasi...")
    
    # -- Arah Alice ke Bob --
    print(f"1. Alice mengirim A={A} untuk Bob...")
    print(f"   (!) Eve MENCEGAT A. Eve mengirim E={E} ke Bob (Menyamar sbg Alice).")
    
    # -- Arah Bob ke Alice --
    print(f"2. Bob mengirim B={B} untuk Alice...")
    print(f"   (!) Eve MENCEGAT B. Eve mengirim E={E} ke Alice (Menyamar sbg Bob).")
    print("-" * 60)

    # 3. Perhitungan Kunci yang Dimanipulasi
    
    # Alice tertipu (menggunakan E milik Eve, mengira punya Bob)
    secret_Alice_Eve = pow(E, a, p)
    
    # Bob tertipu (menggunakan E milik Eve, mengira punya Alice)
    secret_Bob_Eve = pow(E, b, p)

    # Eve menghitung kunci masing-masing
    secret_Eve_Alice = pow(A, e, p) # Kunci Eve dengan Alice
    secret_Eve_Bob   = pow(B, e, p) # Kunci Eve dengan Bob

    print(f"[Hasil] Kunci Alice (dikira aman) : {secret_Alice_Eve}")
    print(f"[Hasil] Kunci Bob   (dikira aman) : {secret_Bob_Eve}")
    print(f"[Hasil] Kunci Eve dengan Alice    : {secret_Eve_Alice}")
    print(f"[Hasil] Kunci Eve dengan Bob      : {secret_Eve_Bob}")
    
    print("-" * 60)
    if secret_Alice_Eve != secret_Bob_Eve:
        print(">> KESIMPULAN: Alice dan Bob punya kunci BERBEDA.")
        print(">> BAHAYA: Eve bisa membaca/mengubah semua pesan di tengah!")

# ==========================================
# MAIN PROGRAM
# ==========================================
if __name__ == "__main__":
    print("Nama : Mochamad Ilham Hansyil Alfauzi")
    print("NIM  : 2320202767")
    print("Tugas: Week 7 - Diffie Hellman")
    
    p, g = get_public_parameters()
    
    simulation_normal(p, g)
    simulation_mitm(p, g)