import os  # <--- [TAMBAHAN PENTING] Untuk manajemen file/folder
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta, timezone

# ==========================================
# FUNGSI PEMBUATAN SERTIFIKAT
# ==========================================
def create_certificate():
    print("="*60)
    print("      SIMULASI PEMBUATAN SERTIFIKAT DIGITAL (PKI)")
    print("      Nama : Mochamad Ilham Hansyil Alfauzi")
    print("      NIM  : 2320202767")
    print("="*60 + "\n")

    # ---------------------------------------------------------
    # [PERBAIKAN] MENYIAPKAN FOLDER OUTPUT
    # ---------------------------------------------------------
    # Kita tentukan nama folder output
    output_folder = "src"
    
    # Cek apakah folder 'src' ada. Jika tidak ada, buat folder tersebut.
    # exist_ok=True artinya tidak akan error jika folder sudah ada.
    if not os.path.exists(output_folder):
        print(f"[INFO] Folder '{output_folder}' tidak ditemukan. Membuat folder baru...")
        os.makedirs(output_folder, exist_ok=True)

    # ---------------------------------------------------------
    # LANGKAH 1: Membangkitkan Pasangan Kunci (Key Pair)
    # ---------------------------------------------------------
    print("[1/4] Membangkitkan Private Key RSA 2048-bit...")
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    print("      -> Private Key berhasil dibuat.")

    # ---------------------------------------------------------
    # LANGKAH 2: Menentukan Identitas (Subject & Issuer)
    # ---------------------------------------------------------
    print("[2/4] Menentukan Atribut Identitas Sertifikat...")
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Jawa Tengah"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"Kebumen"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Universitas Nahdlatul Ulama"),
        x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, u"Teknik Informatika"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"ilham-hansyil.local"),
        x509.NameAttribute(NameOID.EMAIL_ADDRESS, u"ilham.hansyil@student.univ.ac.id"),
    ])

    # ---------------------------------------------------------
    # LANGKAH 3: Membangun & Menandatangani Sertifikat
    # ---------------------------------------------------------
    print("[3/4] Menandatangani Sertifikat Digital...")
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.now(timezone.utc))
        .not_valid_after(datetime.now(timezone.utc) + timedelta(days=365))
        .add_extension(
            x509.SubjectAlternativeName([x509.DNSName(u"ilham-hansyil.local")]),
            critical=False,
        )
        .sign(private_key, hashes.SHA256())
    )
    print("      -> Sertifikat berhasil ditandatangani.")

    # ---------------------------------------------------------
    # LANGKAH 4: Menyimpan ke File
    # ---------------------------------------------------------
    print("[4/4] Menyimpan file Private Key dan Certificate...")
    
    # [PERBAIKAN] Menggunakan os.path.join agar path aman di Windows/Linux/Mac
    key_path = os.path.join(output_folder, "private_key.pem")
    cert_path = os.path.join(output_folder, "certificate.pem")

    # Simpan Private Key
    with open(key_path, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        ))
    
    # Simpan Sertifikat
    with open(cert_path, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))

    print("\n" + "="*60)
    print("STATUS: SUKSES")
    print("="*60)
    print(f"1. File Key  : {key_path} (RAHASIA!)")
    print(f"2. File Cert : {cert_path} (PUBLIK)")
    print("-" * 60)
    print("DETAIL SERTIFIKAT YANG DIBUAT:")
    print(f"Serial Number : {cert.serial_number}")
    print(f"Issuer        : {cert.issuer.rfc4514_string()}")
    print(f"Subject       : {cert.subject.rfc4514_string()}")
    print(f"Valid Until   : {cert.not_valid_after_utc}")
    print("="*60)

if __name__ == "__main__":
    create_certificate()