# Customer Segmentation and Clustering with Streamlit

Aplikasi web sederhana untuk melakukan segmentasi dan klasterisasi pelanggan menggunakan model K-Prototypes. Aplikasi ini memungkinkan pengguna untuk meng-upload data pelanggan dalam bentuk file Excel, kemudian melakukan preprocessing data, prediksi klaster, dan penamaan segmen berdasarkan hasil klasterisasi.

## Fitur

- Upload file Excel untuk memuat data pelanggan.
- Preprocessing data untuk encoding kategori dan standardisasi data numerik.
- Prediksi klaster menggunakan model K-Prototypes.
- Menamai segmen pelanggan berdasarkan hasil klasterisasi.
- Menampilkan hasil klasterisasi dan segmen pelanggan.
- Download hasil segmentasi dalam format CSV.

## Instalasi

Untuk menjalankan aplikasi ini di komputer lokal, pastikan kamu sudah menginstal Python dan beberapa dependensi yang diperlukan. Berikut langkah-langkah instalasinya:

1. **Clone repository** atau salin file ke direktori lokal:
    ```bash
    git clone <URL_REPOSITORY>
    ```

2. **Install dependencies** yang diperlukan:
    ```bash
    pip install -r requirements.txt
    ```
## Menjalankan Aplikasi

1. Pastikan file model `cluster.pkl` ada di folder `model/` pada direktori yang sama dengan aplikasi.
2. Jalankan aplikasi menggunakan Streamlit:
    ```bash
    streamlit run app.py
    ```

## Struktur Data

Aplikasi ini mengharuskan data pelanggan dalam format Excel dengan kolom-kolom berikut:

- **Jenis Kelamin**: Kategori (Pria/Wanita)
- **Profesi**: Kategori (Ibu Rumah Tangga, Mahasiswa, Pelajar, Professional, Wiraswasta)
- **Tipe Residen**: Kategori (Cluster/Sector)
- **Umur**: Numerik
- **NilaiBelanjaSetahun**: Numerik

## Proses

1. **Preprocessing Data**:
    - Kategori `Jenis Kelamin`, `Profesi`, dan `Tipe Residen` akan di-encode menggunakan angka (0, 1, dst.).
    - Data numerik seperti `Umur` dan `NilaiBelanjaSetahun` akan di-standardisasi berdasarkan nilai rata-rata dan deviasi standar yang sudah ditentukan.

2. **Prediksi Klaster**:
    - Model K-Prototypes akan digunakan untuk memprediksi klaster pelanggan berdasarkan fitur yang sudah diproses.

3. **Segmentasi**:
    - Setelah klaster ditemukan, segmen pelanggan akan diberi label sesuai dengan hasil klaster:
        - 0: Diamond Young Member
        - 1: Diamond Senior Member
        - 2: Silver Member
        - 3: Gold Young Member
        - 4: Gold Senior Member

## Output

Setelah proses segmentasi, aplikasi akan menampilkan:

- **Tabel dengan hasil segmentasi**: Tabel yang menunjukkan data pelanggan beserta klaster dan segmennya.
- **Download button**: Pengguna dapat mengunduh hasil segmentasi dalam format CSV.