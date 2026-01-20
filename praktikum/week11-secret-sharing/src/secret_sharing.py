import random
import sys

# ==========================================
# KONFIGURASI UMUM
# ==========================================
# [REVISI] Menggunakan Prime yang JAUH LEBIH BESAR (Mersenne 521)
# Agar muat menampung kalimat panjang seperti "Ilham-Hansyil-Secret-Key-2026"
FIELD_PRIME = 2**521 - 1 

def _eval_at(poly, x, prime):
    """Mengevaluasi nilai polinomial f(x)"""
    accum = 0
    for coeff in reversed(poly):
        accum = (accum * x + coeff) % prime
    return accum

def split_secret(secret_string, threshold, num_shares, prime=FIELD_PRIME):
    """
    Memecah rahasia menjadi N shares (Mekanisme Splitting)
    """
    # 1. Ubah string rahasia menjadi integer besar
    secret_int = int.from_bytes(secret_string.encode('utf-8'), 'big')
    
    # Cek apakah rahasia muat di dalam Field Prime
    if secret_int >= prime:
        raise ValueError(f"Rahasia terlalu panjang! (Size: {secret_int.bit_length()} bits).")

    # 2. Buat Polinomial acak
    coeffs = [secret_int] 
    for _ in range(threshold - 1):
        coeffs.append(random.SystemRandom().randint(0, prime - 1))
    
    # 3. Hitung titik koordinat (x, y)
    shares = []
    for x in range(1, num_shares + 1):
        y = _eval_at(coeffs, x, prime)
        share_str = f"{x}-{hex(y)[2:]}"
        shares.append(share_str)
        
    return shares

def recover_secret(shares_list, prime=FIELD_PRIME):
    """
    Menyatukan kembali rahasia (Mekanisme Rekonstruksi Lagrange)
    """
    if len(shares_list) < 2:
        return None
    
    x_s = []
    y_s = []
    try:
        for s in shares_list:
            parts = s.split('-')
            x_s.append(int(parts[0]))
            y_s.append(int(parts[1], 16))
    except:
        return None 

    accum = 0
    for j in range(len(y_s)):
        numerator, denominator = 1, 1
        for m in range(len(x_s)):
            if j == m:
                continue
            numerator = (numerator * -x_s[m]) % prime
            denominator = (denominator * (x_s[j] - x_s[m])) % prime
        
        lagrange_coeff = numerator * pow(denominator, -1, prime)
        accum = (accum + y_s[j] * lagrange_coeff) % prime
    
    try:
        byte_len = (accum.bit_length() + 7) // 8
        return accum.to_bytes(byte_len, 'big').decode('utf-8')
    except:
        return "[GIBBERISH/SAMPAH - DEKRIPSI GAGAL]"

# ==========================================
# MAIN PROGRAM
# ==========================================
def main():
    print("="*60)
    print("      SIMULASI SHAMIR'S SECRET SHARING (MANUAL)")
    print("      Nama : Mochamad Ilham Hansyil Alfauzi")
    print("      NIM  : 2320202767")
    print("="*60 + "\n")

    secret = "Ilham-Hansyil-Secret-Key-2026"
    k = 3 # Threshold
    n = 5 # Total Shares

    print(f"[INFO] Rahasia Asli : {secret}")
    print(f"[INFO] Skema (k, n) : {k} dari {n}")
    print("-" * 60)

    # 1. SPLITTING
    print("\n[1] MEMECAH RAHASIA...")
    try:
        shares = split_secret(secret, k, n)
        for s in shares:
            # Kita potong tampilan output biar terminal gak penuh
            print(f"    Share : {s[:30]}... (panjang)")
            
    except Exception as e:
        print(f"    [ERROR FATAL] {e}")
        return

    # 2. REKONSTRUKSI VALID
    print("\n" + "-"*60)
    print(f"[2] UJI 1: Menggabungkan {k} Share (CUKUP)")
    print("-" * 60)
    
    subset_valid = shares[:k] 
    print(f"    Input : {len(subset_valid)} bagian kunci")
    result_valid = recover_secret(subset_valid)
    print(f"    [HASIL] : {result_valid}")

    # 3. REKONSTRUKSI INVALID
    print("\n" + "-"*60)
    print(f"[3] UJI 2: Menggabungkan {k-1} Share (KURANG)")
    print("-" * 60)
    
    subset_invalid = shares[:k-1] 
    print(f"    Input : {len(subset_invalid)} bagian kunci")
    result_invalid = recover_secret(subset_invalid)
    
    print(f"    [HASIL] : {result_invalid}")
    if result_invalid != secret:
        print("    [STATUS] AMAN! Rahasia tidak terbaca karena share kurang.")

    print("\n" + "="*60)

if __name__ == "__main__":
    main()