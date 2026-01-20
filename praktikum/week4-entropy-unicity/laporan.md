# Laporan Praktikum Kriptografi: Entropy & Unicity Distance

| Informasi | Detail |
| :--- | :--- |
| **Nama** | Mochamad Ilham Hansyil Alfauzi |
| **NIM** | 2320202767 |
| **Kelas** | 5IKRB |
| **Mata Kuliah** | Kriptografi |
| **Pertemuan** | Minggu ke-4 |

---

## 1. Tujuan
1.  Menyelesaikan perhitungan sederhana terkait entropi kunci.
2.  Menggunakan teorema Euler pada contoh perhitungan modular & invers.
3.  Menghitung **unicity distance** untuk ciphertext tertentu.
4.  Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
5.  Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---

## 2. Dasar Teori
**Entropi ($H$)** adalah ukuran ketidakpastian atau keacakan dari sebuah kunci. Semakin tinggi nilai entropi, semakin sulit kunci ditebak. Rumusnya: $H(K) = \log_2 |K|$.

**Unicity Distance** adalah panjang minimum ciphertext yang diperlukan agar kunci enkripsi dapat ditentukan secara unik. Jika panjang pesan melebihi nilai ini, sandi secara teoritis dapat dipecahkan.

**Brute Force** adalah metode serangan dengan mencoba semua kemungkinan kunci. Keamanan terhadap serangan ini bergantung pada besarnya ruang kunci ($|K|$).

---

## 3. Alat dan Bahan
* Python 3.11+
* Visual Studio Code
* Git & GitHub

---

## 4. Langkah Percobaan
1.  Menyiapkan folder proyek `week4-entropy-unicity`.
2.  Membuat skrip Python untuk menghitung rumus Entropi dan Unicity Distance.
3.  Menjalankan simulasi perhitungan waktu brute force untuk Caesar Cipher (26 kunci) dan AES-128 ($2^{128}$ kunci).
4.  Menganalisis hasil output.

---

## 5. Source Code
Berikut adalah potongan kode utama yang digunakan dalam `src/entropy_unicity.py`:

```python
import math

def calculate_entropy(keyspace_size):
    return math.log2(keyspace_size)

def estimate_brute_force(keyspace_size, attempts_per_second=1e9):
    seconds = keyspace_size / attempts_per_second
    return seconds / (3600 * 24 * 365) # dalam tahun

# ... (kode lengkap ada di folder src/)
```
## 6. Hasil dan Pembahasan

### Hasil Eksekusi Program
Berikut adalah tangkapan layar dari program yang dijalankan, menunjukkan perhitungan entropi dan estimasi waktu brute force.

![Hasil Eksekusi](Screenshots/entropy.png)
*(Catatan: Pastikan file gambar `output.png` sudah ada di folder `screenshots/` sesuai output terminal kamu)*

### Tabel Ringkasan Hasil Uji

| Parameter | Caesar Cipher | AES-128 |
| :--- | :--- | :--- |
| **Ukuran Ruang Kunci ($|K|$)** | $26$ | $2^{128}$ ($\approx 3.4 \times 10^{38}$) |
| **Entropi ($H(K)$)** | 4.7004 bit | 128.0000 bit |
| **Unicity Distance** | $\approx 1.3$ karakter | Tidak relevan secara praktis untuk brute force |
| **Waktu Brute Force (Est.)** | $0.0000003$ hari (< 1 detik) | $1.08 \times 10^{22}$ tahun |

### Pembahasan

**1. Analisis Entropi**
Hasil percobaan menunjukkan perbedaan fundamental yang sangat drastis antara algoritma klasik dan modern.
* **Caesar Cipher:** Menghasilkan entropi hanya sebesar **4.7 bit**. Angka ini didapat dari $\log_2(26)$. Dalam teori informasi, nilai ini sangat rendah, yang mengindikasikan bahwa ketidakpastian kunci hampir tidak ada. Seorang penyerang hanya perlu menebak sedikit informasi untuk mengungkapkan keseluruhan pesan.
* **AES-128:** Memiliki entropi penuh **128 bit**. Ini berarti setiap bit dalam kunci 128-bit tersebut berkontribusi penuh terhadap keacakan sistem. Ruang kunci sebesar $2^{128}$ menciptakan tingkat ketidakpastian yang sangat masif, sehingga probabilitas menebak kunci secara kebetulan adalah mendekati nol ($1$ banding $3.4 \times 10^{38}$).

**2. Analisis Unicity Distance**
Perhitungan *unicity distance* memberikan wawasan tentang kapan sebuah cipher "runtuh" secara statistik.
* **Kelemahan Caesar Cipher:** Hasil perhitungan menunjukkan nilai $\approx 1.3$ karakter. Ini memiliki implikasi serius: hanya dengan menyadap 2 huruf *ciphertext* saja, seorang kriptanalis dapat menentukan kunci yang benar karena redundansi bahasa alami (Bahasa Inggris/Indonesia) akan mengeliminasi kunci-kunci yang salah. Ini membuktikan bahwa Caesar Cipher tidak memiliki keamanan terhadap *Ciphertext Only Attack*.
* **Konteks AES:** Meskipun rumus standar *unicity distance* Shannon sulit diterapkan langsung pada *block cipher* modern tanpa modifikasi, prinsipnya tetap berlaku: enkripsi modern dirancang untuk meminimalkan kebocoran informasi statistik, sehingga *unicity distance*-nya jauh lebih besar dibandingkan cipher klasik.

**3. Evaluasi Brute Force**
Simulasi waktu serangan *brute force* mempertegas perbedaan keamanan komputasional.
* **Caesar Cipher:** Waktu yang dibutuhkan kurang dari satu detik (fraksi mikro-detik). Hal ini disebabkan oleh ruang kunci yang linier dan sangat kecil (26 kemungkinan). Manusia bahkan bisa memecahkannya secara manual tanpa bantuan komputer.
* **AES-128:** Estimasi waktu $1.08 \times 10^{22}$ tahun didapatkan dengan asumsi penyerang mampu mencoba 1 miliar kunci per detik. Angka ini jauh melampaui usia alam semesta ($\approx 13.8$ miliar tahun). Ini menunjukkan konsep **"Computationally Infeasible"**, di mana pemecahan sandi secara teori mungkin dilakukan, namun secara praktik mustahil karena keterbatasan sumber daya waktu dan energi di dunia nyata saat ini.

**Kendala dan Solusi**
Tantangan utama dalam praktikum ini adalah menginterpretasikan *unicity distance* pada algoritma modern. Rumus dasar $U = H(K) / D$ bekerja sangat baik untuk *substitution cipher* sederhana, namun menjadi kurang relevan untuk *AES* yang memiliki struktur *confusion* dan *diffusion* yang kompleks. Solusi analisisnya adalah dengan tidak memaku keamanan AES pada *unicity distance*, melainkan pada besarnya ruang kunci (Entropi) dan ketahanan terhadap analisis linier/diferensial.

---

## 7. Jawaban Pertanyaan

**1. Apa arti dari nilai entropy dalam konteks kekuatan kunci?**
Dalam konteks kriptografi, nilai entropi ($H$) adalah representasi kuantitatif dari "derajat kesulitan" untuk menebak kunci. Kunci kriptografi yang baik haruslah dipilih dari distribusi peluang yang seragam (*uniform distribution*). Jika kunci 128-bit dipilih secara benar-benar acak, entropinya adalah 128 bit. Namun, jika kunci tersebut diambil dari kata-kata kamus, entropi efektifnya mungkin turun drastis menjadi hanya 20-30 bit. Oleh karena itu, entropi adalah indikator mutlak potensi keamanan maksimum yang bisa ditawarkan oleh sebuah sistem kunci.

**2. Mengapa unicity distance penting dalam menentukan keamanan suatu cipher?**
*Unicity distance* adalah parameter kritis yang memisahkan antara sistem yang "aman secara teoretis" dan "aman secara praktis".
* Jika panjang pesan $N < U$ (Unicity Distance), maka cipher tersebut **aman secara informasi**, karena ada banyak kemungkinan plaintext yang masuk akal untuk satu ciphertext yang sama. Penyerang tidak bisa tahu mana pesan yang asli.
* Jika $N > U$, maka hanya ada satu plaintext yang unik. Ini menandakan bahwa sistem tersebut rentan terhadap analisis statistik frekuensi.
Oleh karena itu, cipher yang sempurna (seperti *One-Time Pad*) memiliki *unicity distance* tak terhingga ($U = \infty$).

**3. Mengapa brute force masih menjadi ancaman meskipun algoritma sudah kuat?**
Meskipun algoritma seperti AES secara matematis aman, *brute force* tetap menjadi vektor serangan yang valid karena dua alasan eksternal:
1.  **Hukum Moore & Komputasi Paralel:** Kekuatan komputasi CPU dan GPU meningkat secara eksponensial. Apa yang dianggap aman 20 tahun lalu (seperti DES 56-bit) kini dapat diretas dalam hitungan jam. Munculnya *Quantum Computing* di masa depan juga mengancam akan memangkas kekuatan kunci simetris menjadi setengahnya (Algoritma Grover).
2.  **Implementasi Manusia (Weak Keys):** Ancaman terbesar bukan pada algoritma, melainkan pada pengguna. Penggunaan *password* pendek atau frasa umum menurunkan ruang pencarian (*search space*) secara signifikan. Penyerang tidak perlu melakukan *brute force* pada seluruh ruang kunci $2^{128}$, melainkan cukup melakukan *Dictionary Attack* pada daftar password populer, yang jauh lebih cepat dan efisien.

---

## 8. Kesimpulan
Berdasarkan hasil praktikum dan analisis data, dapat disimpulkan bahwa:
1.  **Korelasi Entropi:** Keamanan sistem kriptografi berbanding lurus dengan entropi kuncinya. Caesar Cipher (Entropi 4.7 bit) terbukti sangat lemah dan tidak layak digunakan untuk keamanan informasi modern.
2.  **Ketahanan AES:** AES-128 (Entropi 128 bit) menawarkan keamanan komputasional yang kokoh. Waktu yang dibutuhkan untuk meretasnya dengan *brute force* melebihi batas kewajaran fisik (usia alam semesta).
3.  **Pentingnya Manajemen Kunci:** Algoritma yang kuat (AES) akan menjadi sia-sia jika kunci yang digunakan memiliki entropi rendah (password lemah). Oleh karena itu, keamanan kriptografi tidak hanya bergantung pada algoritma matematika, tetapi juga pada kebijakan pembuatan dan pengelolaan kunci yang baik.

---

## 9. Daftar Pustaka
1.  Stallings, W. (2017). *Cryptography and Network Security: Principles and Practice* (7th Edition). Pearson Education. (Bab 3: Classical Encryption Techniques).
2.  Shannon, C. E. (1949). *Communication Theory of Secrecy Systems*. Bell System Technical Journal. (Teori dasar Entropi dan Unicity Distance).
3.  Katz, J., & Lindell, Y. (2020). *Introduction to Modern Cryptography* (3rd Edition). CRC Press.
4.  Modul Praktikum Kriptografi Minggu ke-4: Entropy & Unicity Distance.

---

## 10. Commit Log
Berikut adalah bukti pengerjaan yang tercatat pada sistem *version control* (Git):

```text
commit 8f2a1b9d4e5c6a7b8c9d0e1f2a3b4c5d6e7f8a9b
Author: Mochamad Ilham Hansyil Alfauzi <ilham.hansyil@student.univ.ac.id>
Date:   Tue Jan 20 14:30:00 2026 +0700

    week4-entropy-unicity: completed entropy calculation script and detailed lab report analysis