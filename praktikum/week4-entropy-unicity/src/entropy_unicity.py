import math

def calculate_entropy(keyspace_size):
    """
    Menghitung entropi kunci H(K) = log2(|K|)
    
    Parameter:
    keyspace_size (int/float): Ukuran ruang kunci total.
    """
    if keyspace_size <= 0:
        return 0
    return math.log2(keyspace_size)

def calculate_unicity_distance(entropy_k, redundancy=0.75, alphabet_size=26):
    """
    Menghitung Unicity Distance U = H(K) / (R * log2(|A|))
    
    Parameter:
    entropy_k (float): Nilai entropi kunci.
    redundancy (float): Redundansi bahasa (default Inggris ~0.75 atau 3.2 bit/huruf).
    alphabet_size (int): Jumlah karakter dalam alfabet (default 26 untuk A-Z).
    """
    if redundancy <= 0 or alphabet_size <= 0:
        return float('inf')
    
    # R * log2(|A|)
    denominator = redundancy * math.log2(alphabet_size)
    
    if denominator == 0:
        return float('inf')
        
    return entropy_k / denominator

def estimate_brute_force(keyspace_size, attempts_per_second=1e9):
    """
    Mengestimasi waktu brute force.
    
    Parameter:
    keyspace_size (int/float): Ukuran ruang kunci.
    attempts_per_second (float): Kecepatan percobaan kunci per detik (default 1 Miliar).
    
    Return:
    (float, float): Waktu dalam hari, Waktu dalam tahun.
    """
    if attempts_per_second <= 0:
        return float('inf'), float('inf')

    total_seconds = keyspace_size / attempts_per_second
    
    days = total_seconds / (3600 * 24)
    years = days / 365
    
    return days, years

def main():
    print("="*60)
    print("   EVALUASI KEKUATAN KUNCI: ENTROPY & UNICITY DISTANCE")
    print("="*60 + "\n")

    # --- KASUS 1: CAESAR CIPHER ---
    # Ruang kunci: 26 (A-Z)
    keyspace_caesar = 26
    
    h_caesar = calculate_entropy(keyspace_caesar)
    u_caesar = calculate_unicity_distance(h_caesar)
    
    # Asumsi komputer lambat/manusia: 1 juta operasi per detik (1e6)
    bf_caesar_days, _ = estimate_brute_force(keyspace_caesar, 1e6)

    print(f"[1] CAESAR CIPHER (Classical)")
    print(f"    - Ruang Kunci (|K|) : {keyspace_caesar}")
    print(f"    - Entropy (H)       : {h_caesar:.4f} bit")
    print(f"    - Unicity Distance  : {u_caesar:.4f} karakter")
    print(f"    - Est. Brute Force  : {bf_caesar_days:.10f} hari (Speed: 1 jt/detik)")
    print("-" * 60)

    # --- KASUS 2: AES-128 ---
    # Ruang kunci: 2^128
    keyspace_aes = 2**128
    
    h_aes = calculate_entropy(keyspace_aes)
    
    # Unicity distance dihitung secara teoritis (meskipun kurang relevan untuk block cipher)
    u_aes = calculate_unicity_distance(h_aes) 
    
    # Asumsi superkomputer: 1 Miliar operasi per detik (1e9)
    bf_aes_days, bf_aes_years = estimate_brute_force(keyspace_aes, 1e9)

    print(f"[2] AES-128 (Modern Standard)")
    print(f"    - Ruang Kunci (|K|) : 2^128 (approx 3.4 x 10^38)")
    print(f"    - Entropy (H)       : {h_aes:.4f} bit")
    print(f"    - Unicity Distance  : {u_aes:.4f} karakter (Teoritis)")
    print(f"    - Est. Brute Force  : {bf_aes_years:.2e} tahun (Speed: 1 Miliar/detik)")
    
    print("\n" + "="*60)
    print("KESIMPULAN:")
    print("Caesar Cipher sangat lemah (bisa dipecahkan instan).")
    print("AES-128 sangat kuat (butuh waktu melebihi usia alam semesta).")
    print("="*60)

if __name__ == "__main__":
    main()