# Tugas4KPPPL

🧠 Tes Minat Bakat AI Berbasis Gemini
Sebuah aplikasi web sederhana untuk membantu siswa menemukan jurusan kuliah yang sesuai berdasarkan tes minat bakat. Sistem ini menggunakan Gemini AI (via Google Generative AI API) untuk:

Menghasilkan pertanyaan reflektif secara dinamis.

Memberikan rekomendasi jurusan berdasarkan jawaban siswa.

🚀 Teknologi yang Digunakan
Python (Flask): Backend API dan routing.

- Google Generative AI (gemini-1.5-flash): Untuk generate pertanyaan dan inferensi jurusan.

- HTML-CSS-JS: Antarmuka pengguna.

- dotenv: Manajemen API key secara aman.

---------------------

🧩 Fitur Utama
🔄 Pertanyaan Otomatis: AI membuat pertanyaan minat bakat berbentuk esai.

💡 Rekomendasi Jurusan: Berdasarkan analisis jawaban siswa.

📊 Respons Interaktif: Hasil ditampilkan secara real-time di browser.

📁 Struktur Folder
arduino
Copy
Edit
project/
├── server.py
├── .env
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── requirements.txt
📝 Contoh Pertanyaan dari AI
Apa kegiatan yang paling kamu nikmati di waktu luang, dan mengapa kamu menyukainya?

📌 Catatan
Model yang digunakan adalah gemini-1.5-flash karena gemini-pro tidak tersedia di v1beta.

API key harus dijaga dan tidak dibagikan secara publik.
