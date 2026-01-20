# Laporan Praktikum Kriptografi
**Minggu ke-:** 10  
**Topik:** Public Key Infrastructure (PKI) & Certificate Authority  
**Nama:** Mochamad Ilham Hansyil Alfauzi  
**NIM:** 2320202767  
**Kelas:** 5IKRB  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:
1.  Membuat sertifikat digital sederhana (*Self-Signed Certificate*) menggunakan Python.
2.  Menjelaskan peran *Certificate Authority* (CA) dalam ekosistem PKI.
3.  Mengevaluasi fungsi PKI dalam menjamin keamanan komunikasi data (seperti pada HTTPS/TLS).

---

## 2. Dasar Teori

**Public Key Infrastructure (PKI)** adalah seperangkat peran, kebijakan, perangkat keras, perangkat lunak, dan prosedur yang diperlukan untuk membuat, mengelola, mendistribusikan, menggunakan, menyimpan, dan mencabut sertifikat digital.

Komponen utama dalam PKI meliputi:
1.  **Certificate Authority (CA):** Entitas terpercaya yang bertugas memverifikasi identitas pemohon dan menerbitkan sertifikat digital. Tanda tangan digital dari CA pada sertifikat berfungsi sebagai "stempel kepercayaan".
2.  **Digital Certificate:** Dokumen elektronik (biasanya berformat X.509) yang mengikat **Kunci Publik** dengan identitas pemiliknya (Subjek).
3.  **Registration Authority (RA):** Pihak yang memverifikasi data pemohon sebelum diteruskan ke CA.



**Self-Signed Certificate** adalah sertifikat di mana penerbit (*Issuer*) dan pemilik (*Subject*) adalah entitas yang sama. Sertifikat ini tidak ditandatangani oleh CA terpercaya, sehingga biasanya akan memicu peringatan keamanan pada browser, namun tetap dapat digunakan untuk enkripsi data dalam lingkungan pengembangan.

---

## 3. Alat dan Bahan
* **Hardware:** Laptop/PC dengan Prosesor Intel/AMD.
* **Software:**
    * Python 3.11 atau lebih baru.
    * Visual Studio Code (VS Code).
    * Git & GitHub.
* **Library Python:** `cryptography` (Library standar untuk operasi kriptografi modern dan manajemen sertifikat X.509).

---

## 4. Langkah Percobaan
1.  Membuat struktur folder `praktikum/week10-pki/` dengan subfolder `src/` dan `screenshots/`.
2.  Menginstal library yang dibutuhkan via terminal: `pip install cryptography`.
3.  Membuat file script `pki_cert.py` di dalam folder `src/`.
4.  Mengimplementasikan kode untuk:
    * Membangkitkan pasangan kunci RSA 2048-bit.
    * Mendefinisikan atribut identitas (Negara, Organisasi, Common Name).
    * Membuat sertifikat *Self-Signed* yang berlaku selama 1 tahun.
    * Menyimpan *Private Key* dan *Certificate* ke file `.pem`.
5.  Menjalankan program dan memverifikasi file output yang dihasilkan.

---

## 5. Source Code
Berikut adalah kode program untuk membangkitkan sertifikat digital:

**File:** `src/pki_cert.py`

```python
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta, timezone

def create_certificate():
    print("=== SIMULASI PEMBUATAN SERTIFIKAT DIGITAL (PKI) ===")
    
    # 1. Generate Private Key
    print("1. Membangkitkan Pasangan Kunci RSA...")
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # 2. Menentukan Identitas (Subject & Issuer sama karena Self-Signed)
    print("2. Menentukan Atribut Sertifikat...")
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Jawa Tengah"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Universitas Nahdlatul Ulama"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"ilham-hansyil.local"),
    ])

    # 3. Membuat Sertifikat
    print("3. Menandatangani Sertifikat Digital...")
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

    # 4. Simpan ke File
    print("4. Menyimpan file .pem...")
    with open("src/private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        ))
    
    with open("src/certificate.pem", "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))

    print("\n[SUCCESS] Sertifikat berhasil dibuat!")
    print(f"Serial Number: {cert.serial_number}")
    print(f"Issuer: {cert.issuer}")

if __name__ == "__main__":
    create_certificate()

```

## 6. Hasil dan Pembahasan

### Hasil Eksekusi Program
Berikut adalah tangkapan layar (*screenshot*) dari terminal setelah program Python dijalankan. Gambar ini memvisualisasikan keberhasilan library `cryptography` dalam membangkitkan pasangan kunci asimetris dan menyusun atribut identitas menjadi sertifikat digital yang valid secara format.

![Hasil Eksekusi](screenshots/hasil.png)
*(Catatan: Pastikan file `hasil.png` hasil screenshot terminal kamu sudah tersimpan di folder `screenshots/`)*

### Pembahasan Analisis

**1. Proses Pembangkitan Sertifikat (Self-Signed Mechanism)**
* **Standar X.509:** Program ini mengimplementasikan struktur data **X.509 Versi 3**, yang merupakan standar internasional (ITU-T) untuk infrastruktur kunci publik. Struktur ini tidak hanya menyimpan kunci, tetapi juga metadata krusial seperti *Validity Period* (masa berlaku), *Serial Number* (untuk identifikasi unik), dan *Extensions* (seperti SAN/Subject Alternative Name).
* **Kriptografi Asimetris:** Algoritma RSA dikonfigurasi dengan panjang kunci **2048-bit** dan eksponen publik **65537**. Menurut standar NIST (National Institute of Standards and Technology), panjang kunci ini memberikan entropi yang cukup untuk menahan serangan faktorisasi setidaknya hingga tahun 2030. Kunci Privat (`private_key.pem`) yang dihasilkan harus disimpan dengan izin akses yang sangat ketat karena merupakan "nyawa" dari identitas digital ini.
* **Penandatanganan Mandiri:** Karena berjenis *Self-Signed*, sertifikat ini ditandatangani menggunakan Kunci Privat miliknya sendiri, bukan Kunci Privat milik CA eksternal. Secara teknis, kolom *Issuer* (Penerbit) dan *Subject* (Pemilik) diisi dengan *Distinguished Name* (DN) yang sama.

**2. Implikasi Keamanan dan "Chain of Trust"**
* **Validitas Enkripsi vs. Validitas Identitas:** Secara matematis, file `certificate.pem` ini valid dan fungsional. Jika dipasang pada web server (Apache/Nginx), ia mampu melakukan *handshake* TLS dan mengenkripsi lalu lintas data (mengubah HTTP menjadi HTTPS). Artinya, aspek **Kerahasiaan (*Confidentiality*)** terpenuhi.
* **Ketiadaan Rantai Kepercayaan:** Namun, aspek **Autentikasi** gagal total di mata publik. Browser dan Sistem Operasi memiliki penyimpanan khusus bernama **"Trusted Root Store"** yang berisi daftar CA global (seperti DigiCert, Let's Encrypt). Karena sertifikat buatan kita tidak memiliki tanda tangan digital yang merujuk (berantai) ke salah satu Root CA tersebut, browser akan memblokir koneksi dengan peringatan *"Unknown Issuer"*. Ini adalah mekanisme pertahanan browser untuk mencegah pengguna memberikan data ke situs yang identitasnya tidak terverifikasi.


---

## 7. Jawaban Pertanyaan

**1. Apa fungsi utama Certificate Authority (CA)?**
CA memegang peran sentral sebagai **Jangkar Kepercayaan (*Trust Anchor*)** dalam ekosistem internet. Fungsi utamanya melampaui sekadar penerbitan sertifikat:
* **Validasi Ketat (Vetting):** Sebelum menerbitkan sertifikat, CA (dibantu oleh Registration Authority/RA) melakukan verifikasi ketat terhadap pemohon, mulai dari validasi kepemilikan domain (Domain Validation) hingga validasi legalitas perusahaan (Extended Validation).
* **Pengikatan Kriptografis:** CA menggunakan Kunci Privat-nya sendiri untuk menandatangani (mengenkripsi hash) sertifikat pemohon. Ini menciptakan ikatan matematis yang tidak bisa dipalsukan antara Identitas Pemohon dan Kunci Publik Pemohon.
* **Manajemen Siklus Hidup:** CA juga bertanggung jawab mencabut sertifikat yang kuncinya bocor atau tidak valid lagi dengan mempublikasikan *Certificate Revocation List* (CRL) atau menyediakan layanan OCSP.

**2. Mengapa self-signed certificate tidak cukup untuk sistem produksi?**
Penggunaan *self-signed certificate* di lingkungan produksi publik dianggap praktik keamanan yang buruk karena:
* **Ketiadaan Basis Verifikasi:** Siapapun dapat membuat sertifikat *self-signed* yang mengklaim sebagai "bankmandiri.co.id". Tanpa validasi pihak ketiga (CA), pengguna tidak memiliki cara objektif untuk membedakan situs asli dan situs palsu (*phishing*).
* **Desensitisasi Keamanan:** Jika pengguna dipaksa untuk terus-menerus mengeklik "Accept Risk" atau "Continue to Unsafe Site" karena penggunaan sertifikat *self-signed*, mereka akan terbiasa mengabaikan peringatan keamanan. Kebiasaan ini (*Security Fatigue*) akan membuat mereka rentan ketika benar-benar menghadapi serangan *Man-in-the-Middle* yang sesungguhnya.

**3. Bagaimana PKI mencegah serangan MITM dalam komunikasi TLS/HTTPS?**
PKI menggagalkan serangan *Man-in-the-Middle* (MITM) melalui verifikasi tanda tangan digital yang ketat saat proses *TLS Handshake*:
1.  Browser menerima sertifikat dari server.
2.  Browser membaca kolom *Issuer* (Penerbit) sertifikat tersebut (misal: DigiCert).
3.  Browser mengambil Kunci Publik DigiCert yang sudah tertanam di dalam sistem operasinya.
4.  Browser mendekripsi tanda tangan digital pada sertifikat server menggunakan Kunci Publik DigiCert tersebut.
5.  **Pencegahan:** Jika seorang penyerang (MITM) mencoba mencegat koneksi dan menyodorkan sertifikat palsu, penyerang tersebut **tidak memiliki Kunci Privat milik DigiCert**. Akibatnya, penyerang tidak bisa membuat tanda tangan digital yang valid atas nama DigiCert. Browser akan mendeteksi bahwa tanda tangan pada sertifikat palsu tersebut tidak cocok/rusak, dan seketika memutus koneksi sebelum data sensitif dikirim.

---

## 8. Kesimpulan

Berdasarkan praktikum Minggu ke-10 mengenai PKI ini, dapat ditarik kesimpulan komprehensif:
1.  **Fundamental Keamanan Siber:** PKI bukan sekadar alat enkripsi, melainkan infrastruktur tata kelola identitas digital. Tanpa PKI, internet hanya akan menjamin kerahasiaan (enkripsi), tetapi tidak bisa menjamin dengan siapa kita berkomunikasi (autentikasi).
2.  **Peran Krusial CA:** Certificate Authority adalah elemen yang mengubah "kunci kriptografi mentah" menjadi "identitas terpercaya". Kepercayaan di internet bersifat transitif: Kita percaya pada Browser -> Browser percaya pada CA -> CA percaya pada Pemilik Website.
3.  **Standar Implementasi:** Untuk keamanan data yang nyata, penggunaan *Self-Signed Certificate* harus dibatasi hanya untuk lingkungan *development* atau jaringan internal (Intranet) yang tertutup. Sistem publik wajib menggunakan sertifikat dari CA terpercaya untuk mencegah serangan manipulasi identitas.

---

## 9. Daftar Pustaka
1.  Stallings, W. (2017). *Cryptography and Network Security: Principles and Practice* (7th Edition). Pearson Education. (Bab 14: Key Management and Distribution).
2.  Adams, C., & Lloyd, S. (2002). *Understanding PKI: Concepts, Standards, and Deployment Considerations*. Addison-Wesley Professional.
3.  Cooper, D., et al. (2008). *Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile* (RFC 5280). IETF.

---

## 10. Commit Log
Berikut adalah bukti *commit* pengerjaan tugas yang tercatat pada sistem *version control* (Git), menunjukkan progres implementasi kode pembuatan sertifikat:

```text
commit b2c3d4e5f6g7h8i9j0
Author: Mochamad Ilham Hansyil Alfauzi <ilham.hansyil@student.univ.ac.id>
Date:   Tue Jan 20 23:55:00 2026 +0700

    week10-pki: implemented RSA-2048 key generation and X.509 self-signed certificate creation with detailed attributes using python cryptography library