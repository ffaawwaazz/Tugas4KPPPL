function mulaiTes() {
  fetch('/pertanyaan')
    .then(res => {
      if (!res.ok) throw new Error('Gagal mengambil pertanyaan');
      return res.json();
    })
    .then(data => {
      document.getElementById('pertanyaan').innerText = data.pertanyaan;
      document.getElementById('pertanyaan-container').classList.remove('hidden');
      document.getElementById('hasil-container').classList.add('hidden');
      document.getElementById('jawaban').value = '';
    })
    .catch(err => {
      alert('Terjadi kesalahan saat mengambil pertanyaan: ' + err.message);
    });
}

function kirimJawaban() {
  const jawaban = document.getElementById('jawaban').value.trim();
  const pertanyaan = document.getElementById('pertanyaan').innerText;

  if (!jawaban) {
    alert("Silakan isi jawaban terlebih dahulu.");
    return;
  }

  fetch('/rekomendasi', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ pertanyaan, jawaban })
  })
    .then(res => {
      if (!res.ok) throw new Error('Gagal meminta rekomendasi');
      return res.json();
    })
    .then(data => {
      if (data.rekomendasi) {
        document.getElementById('hasil').innerHTML = data.rekomendasi.map((r) =>
          `<p><strong>${r.jurusan}</strong>: ${r.alasan}</p>`
        ).join('');
        document.getElementById('hasil-container').classList.remove('hidden');
      } else {
        throw new Error("Format rekomendasi tidak sesuai");
      }
    })
    .catch(err => {
      alert('Terjadi kesalahan saat mengirim jawaban: ' + err.message);
    });
}
