from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# ==========================================
# FUNGSI-FUNGSI UTAMA
# ==========================================

def generate_keys():
    """Membangkitkan pasangan kunci RSA 2048-bit"""
    print("1. GENERATING KEYS (RSA 2048-bit)...")
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()
    print("   [+] Pasangan kunci berhasil dibuat.")
    return private_key, public_key

def sign_message(message, private_key):
    """
    Membuat Tanda Tangan Digital.
    Proses: Hash Pesan -> Enkripsi Hash dengan Private Key
    """
    print(f"\n2. SIGNING MESSAGE: '{message.decode()}'")
    
    # 1. Buat Hash dari pesan (SHA-256)
    h = SHA256.new(message)
    
    # 2. Buat Tanda Tangan (Sign)
    signature = pkcs1_15.new(private_key).sign(h)
    
    print(f"   [+] Hash SHA-256 : {h.hexdigest()}")
    print(f"   [+] Signature    : {signature.hex()[:64]}... (dipotong)")
    return signature

def verify_signature(message, signature, public_key):
    """
    Verifikasi Tanda Tangan.
    Proses: Decrypt Signature dengan Public Key -> Bandingkan dengan Hash Pesan
    """
    print(f"\n3. VERIFYING MESSAGE: '{message.decode()}'")
    
    h = SHA256.new(message)
    
    try:
        # Verifikasi
        pkcs1_15.new(public_key).verify(h, signature)
        print("   [SUCCESS] Tanda tangan VALID.")
        print("             -> Pesan Otentik (Asli dari pengirim).")
        print("             -> Integritas Terjamin (Tidak ada perubahan).")
    except (ValueError, TypeError):
        print("   [FAILED]  Tanda tangan TIDAK VALID!")
        print("             -> PERINGATAN: Pesan telah dimodifikasi atau kunci salah.")

# ==========================================
# PROGRAM UTAMA
# ==========================================

def main():
    print("="*60)
    print("      PRAKTIKUM DIGITAL SIGNATURE (RSA)")
    print("      Nama : Mochamad Ilham Hansyil Alfauzi")
    print("      NIM  : 2320202767")
    print("="*60 + "\n")

    # 1. Setup Kunci
    private_key, public_key = generate_keys()

    # ----------------------------------------
    # SKENARIO 1: NORMAL (VALID)
    # ----------------------------------------
    print("\n" + "-"*40)
    print("SKENARIO 1: Verifikasi Pesan Asli")
    print("-"*40)
    
    original_msg = b"Ini adalah pesan rahasia dari Ilham."
    
    # Ilham menandatangani pesan
    signature = sign_message(original_msg, private_key)
    
    # Penerima memverifikasi pesan
    verify_signature(original_msg, signature, public_key)

    # ----------------------------------------
    # SKENARIO 2: SERANGAN TAMPERING (MODIFIKASI)
    # ----------------------------------------
    print("\n" + "-"*40)
    print("SKENARIO 2: Simulasi Serangan (Tampering)")
    print("-"*40)
    
    # Penyerang mengubah pesan di tengah jalan
    fake_msg = b"Ini adalah pesan rahasia dari Ilham. (TAPI PALSU)"
    
    print(f"   [!] Hacker mengubah pesan menjadi: '{fake_msg.decode()}'")
    print("   [!] Penerima mencoba memverifikasi pesan palsu dengan signature lama...")
    
    # Verifikasi akan gagal karena Hash(Pesan Palsu) != Decrypt(Signature)
    verify_signature(fake_msg, signature, public_key)
    
    print("\n" + "="*60)

if __name__ == "__main__":
    main()
    