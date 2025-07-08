from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/pertanyaan", methods=["GET"])
def get_pertanyaan():
    try:
        prompt = """
Anda adalah seorang ahli psikometri dan konselor pendidikan.

Buat 1 pertanyaan untuk tes minat dan bakat siswa SMA yang memancing eksplorasi terhadap kepribadian, minat, atau cara berpikir siswa. Jawaban siswa harus dalam bentuk esai singkat.

Output: hanya pertanyaan, tanpa penjelasan tambahan.
"""
        response = model.generate_content(prompt)
        response_text = getattr(response, "text", "").strip()
        return jsonify({"pertanyaan": response_text})
    except Exception as e:
        print(f"[ERROR] Pertanyaan gagal: {e}")
        return jsonify({"error": "Gagal mengambil pertanyaan", "debug": str(e)}), 500

@app.route("/rekomendasi", methods=["POST"])
def rekomendasi():
    try:
        pertanyaan = request.json.get("pertanyaan", "")
        jawaban = request.json.get("jawaban", "")
        if not jawaban:
            return jsonify({"error": "Jawaban tidak boleh kosong"}), 400

        prompt = f"""
Peran: Anda adalah seorang pakar konselor pendidikan dan karier.

Tugas: Berdasarkan jawaban siswa terhadap sebuah pertanyaan tes minat bakat, berikan rekomendasi 3 jurusan kuliah yang paling sesuai.

Konteks:
- Pertanyaan: "{pertanyaan}"
- Jawaban siswa: "{jawaban}"

Format output: hanya dalam bentuk list JSON, seperti ini:
[
  {{ "jurusan": "Psikologi", "alasan": "..." }},
  {{ "jurusan": "Teknik Informatika", "alasan": "..." }},
  {{ "jurusan": "Sastra Inggris", "alasan": "..." }}
]
"""
        response = model.generate_content(prompt)
        raw = response.text.strip()

        match = re.search(r'\[.*\]', raw, re.DOTALL)
        if not match:
            return jsonify({"error": "Format JSON tidak ditemukan", "raw_output": raw}), 500

        json_str = match.group(0)
        hasil = json.loads(json_str)
        return jsonify({"rekomendasi": hasil})
    except Exception as e:
        print(f"[ERROR] Rekomendasi gagal: {e}")
        return jsonify({"error": "Gagal memproses rekomendasi", "debug": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
