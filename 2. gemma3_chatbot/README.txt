=========================================================
README - Aplikasi Chatbot AI Lokal dengan Model Gemma3:1b
=========================================================


DESKRIPSI
--------------------------------------------------------
Proyek ini adalah aplikasi chatbot berbasis web yang dibuat menggunakan Python dan Streamlit, serta terintegrasi dengan model Large Language Model (LLM) lokal bernama `gemma3:1b` melalui Ollama.

Model `gemma3:1b` digunakan untuk memproses input pengguna dan memberikan respons secara natural. Semua pemrosesan dilakukan secara lokal, tanpa koneksi ke server cloud eksternal.
--------------------------------------------------------


FLOW CODE
--------------------------------------------------------
1. User Interface (UI) dibuat menggunakan Streamlit. User mengetik pertanyaan di kolom input.
2. Pengiriman Prompt: Input pengguna dikirim ke Ollama melalui REST API (http://localhost:11434/api/generate).
3. Ollama menjalankan model `gemma3:1b` dan mengembalikan respons berdasarkan prompt user.
4. Jawaban AI ditampilkan kembali di interface sebagai balasan chat.
5. Riwayat chat disimpan dalam session memory (st.session_state) agar interaksi tetap terlihat meski halaman di-reload.
--------------------------------------------------------


INSTALASI
--------------------------------------------------------
1. Pastikan Python sudah terinstal (disarankan untuk menginstal python versi 3.7 ke atas)
2. Install dan jalankan Ollama
   - Download dari: https://ollama.com
   - Setelah terinstal, buka terminal dan download model gemma3:1b dengan perintah:
     ollama pull gemma3:1b
   - Jalankan model dengan perintah:
     ollama run gemma3:1b
3. Buat virtual environment
   python -m venv gemma3_chatbot
   gemma3_chatbot\Scripts\activate       (Windows)
   source gemma3_chatbot/bin/activate    (Linux/Mac)
4. Install dependensi dari file requirements.txt
   pip install -r requirements.txt
--------------------------------------------------------


JALANKAN APLIKASI
--------------------------------------------------------
1. Jalankan aplikasi Streamlit:
   streamlit run ui_chatbot.py
2. Akses melalui browser:
   http://localhost:8501
3. Mulai percakapan dengan AI. Ketik pertanyaan seperti:
   > Apa itu machine learning?
--------------------------------------------------------


TESTING MODEL
--------------------------------------------------------
Untuk menguji apakah model bekerja dengan baik:
1. Pastikan model sudah berjalan:
   ollama run gemma3:1b
2. Masukkan pertanyaan singkat di UI:
   > Siapa presiden Indonesia saat ini?
3. Respons akan muncul di area percakapan.
   Jika tidak muncul:
   - Periksa apakah Ollama sedang berjalan di background
   - Cek firewall yang mungkin memblokir `localhost:11434`
--------------------------------------------------------


FILE PADA PROYEK
--------------------------------------------------------
- ui_chatbot.py         → Kode utama aplikasi chatbot
- requirements.txt      → Daftar library yang dibutuhkan
- README.txt            → Dokumentasi penggunaan & instalasi
--------------------------------------------------------


CATATAN TAMBAHAN
--------------------------------------------------------
- Aplikasi ini berjalan "offline" dan aman digunakan di komputer lokal.