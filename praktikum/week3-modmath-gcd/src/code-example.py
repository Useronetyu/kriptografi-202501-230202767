# -*- coding: utf-8 -*-
"""
File ini berisi implementasi fungsi-fungsi untuk praktikum Minggu 3.
Mencakup Aritmetika Modular, Algoritma Euclidean (GCD),
Extended Euclidean Algorithm (Modular Inverse), dan Logaritma Diskrit sederhana.
"""

# === Langkah 1: Aritmetika Modular ===

def mod_add(a, b, n):
    """Menghitung (a + b) mod n."""
    return (a + b) % n

def mod_sub(a, b, n):
    """Menghitung (a - b) mod n."""
    return (a - b) % n

def mod_mul(a, b, n):
    """Menghitung (a * b) mod n."""
    return (a * b) % n

def mod_exp(base, exp, n):
    """Menghitung (base^exp) mod n menggunakan eksponensiasi modular."""
    return pow(base, exp, n)

# === Langkah 2: GCD & Algoritma Euclidean ===

def gcd(a, b):
    """
    Menghitung Greatest Common Divisor (GCD) dari a dan b
    menggunakan Algoritma Euclidean.
    """
    while b != 0:
        a, b = b, a % b
    return a

# === Langkah 3: Extended Euclidean Algorithm & Modular Inverse ===

def egcd(a, b):
    """
    Menghitung GCD(a, b) serta koefisien x dan y sehingga ax + by = GCD(a, b).
    Mengembalikan tuple (g, x, y).
    """
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def modinv(a, n):
    """
    Menghitung invers modular dari a mod n.
    Mengembalikan invers jika ada, jika tidak mengembalikan None.
    """
    g, x, _ = egcd(a, n)
    if g != 1:
        # Invers modular tidak ada jika a dan n tidak koprima
        return None
    return x % n

# === Langkah 4: Logaritma Diskrit (Discrete Log) ===

def discrete_log(a, b, n):
    """
    Menyelesaikan logaritma diskrit sederhana.
    Mencari x sehingga a^x ≡ b (mod n) dengan metode brute-force.
    """
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    # Tidak ditemukan solusi
    return None

# === Fungsi Utama untuk Eksekusi & Pengujian ===

if __name__ == "__main__":
    print("--- Pengujian Aritmetika Modular ---")
    print("7 + 5 mod 12 =", mod_add(7, 5, 12))
    print("7 - 5 mod 12 =", mod_sub(7, 5, 12))
    print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
    print("7^128 mod 13 =", mod_exp(7, 128, 13))
    print("-" * 20)
    
    print("\n--- Pengujian GCD & Algoritma Euclidean ---")
    print("gcd(54, 24) =", gcd(54, 24))
    print("gcd(48, 180) =", gcd(48, 180))
    print("-" * 20)

    print("\n--- Pengujian Invers Modular ---")
    print("Invers 3 mod 11 =", modinv(3, 11))
    print("Invers 7 mod 26 =", modinv(7, 26))
    print("Invers 4 mod 10 =", modinv(4, 10)) # Harusnya None karena gcd(4, 10) != 1
    print("-" * 20)

    print("\n--- Pengujian Logaritma Diskrit ---")
    print("Mencari x untuk 3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))
    print("Mencari x untuk 2^x ≡ 3 (mod 13), x =", discrete_log(2, 3, 13))
    print("-" * 20)