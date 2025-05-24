=======================================
README - Klasifikasi Pesan Customer ISP
=======================================

DESKRIPSI
---------------------------------------
Proyek ini membangun model Machine Learning untuk mengklasifikasikan pesan dari pelanggan ISP ke dalam tiga kategori utama:
1. Information - untuk permintaan informasi (produk, promo, billing, dll)
2. Request     - untuk permintaan layanan (relokasi, reset, teknisi, dll)
3. Problem     - untuk pengaduan masalah (koneksi, modem, pembayaran, dll)
---------------------------------------

METODE
---------------------------------------
Model yang digunakan adalah Multinomial Naive Bayes, dikombinasikan dengan TF-IDF Vectorizer untuk mengubah teks menjadi fitur numerik.
Pipeline digunakan untuk menyusun alur preprocessing dan training secara efisien.
---------------------------------------

FLOW CODE
---------------------------------------
1. Load dataset dari file CSV
2. Bersihkan teks (lowercase, hapus angka, tanda baca)
3. Lakukan pelabelan kategori berdasarkan teks
4. Split dataset menjadi training (80%) dan testing (20%)
5. Bangun pipeline: TF-IDF + MultinomialNB
6. Latih model pada data training
7. Evaluasi model menggunakan accuracy, precision, recall
8. Simpan dataset training dan testing ke file CSV
9. Tampilkan hasil klasifikasi (actual vs predicted)
---------------------------------------

INSTALASI
---------------------------------------
1. Buat virtual environment
   python -m venv msg_class
   msg_class\Scripts\activate		(Windows)
   source msg_class/bin/activate	(Linux/macOS)

2. Install requirements
   pip install -r requirements.txt
---------------------------------------

JALANKAN DAN UJI MODEL
---------------------------------------
1. Jalankan skrip utama Python (misal: classify_msg.py atau dari notebook)
2. Setelah training, model akan mengevaluasi hasil prediksi
3. Output berupa metrik evaluasi dan hasil prediksi disimpan dalam:
   - hasil_klasifikasi.csv
   - dataset_training.csv
   - dataset_testing.csv
---------------------------------------

CATATAN
---------------------------------------
Dataset harus memiliki kolom teks pesan ('message') yang akan digunakan untuk klasifikasi.

