#!/usr/bin/env python3
# Jalankan: python3 build.py  -> menghasilkan folder situs statis.
# Ubah KONFIGURASI di bawah, tambah artikel di daftar ARTIKEL, lalu jalankan ulang.
import os, sys

# ===== KONFIGURASI =====
SITE   = "Rawat Mobil"
DOMAIN = "https://domain-anda.com"          # tanpa garis miring di akhir
EMAIL  = "email@domain-anda.com"            # WAJIB email aktif milik Anda
PUB    = "ca-pub-8476774265191060"
OUT    = sys.argv[1] if len(sys.argv) > 1 else "situs"

# ===== ARTIKEL (ganti dengan tulisan ORISINAL Anda; tambah sebanyak mungkin) =====
ARTIKEL = [
 dict(slug="cara-cek-tekanan-ban-mobil", date="2026-11-11",
  title="Cara Mengecek Tekanan Ban Mobil dengan Benar",
  desc="Langkah mengecek tekanan angin ban mobil, kapan waktu terbaik, dan angka mana yang harus diikuti.",
  body="""
<p>Tekanan ban yang tepat memengaruhi keselamatan, kestabilan, konsumsi bahan bakar, dan umur ban. Pengecekannya sederhana dan bisa dilakukan sendiri dalam beberapa menit.</p>
<h2>Gunakan angka dari pabrikan, bukan dari sisi ban</h2>
<p>Angka yang tercetak di dinding ban adalah tekanan maksimum yang sanggup ditahan ban, bukan tekanan yang dianjurkan. Tekanan yang benar biasanya tertera di stiker pada rangka pintu pengemudi, di tutup tangki bahan bakar, atau di buku manual. Angka itu sering dibedakan untuk ban depan dan belakang, serta untuk beban normal dan beban penuh.</p>
<h2>Cek saat ban dalam keadaan dingin</h2>
<p>Ban yang baru dipakai berjalan akan memanas dan tekanannya naik. Karena itu, cek sebelum berkendara atau setelah mobil diam setidaknya beberapa jam. Jika terpaksa mengecek setelah perjalanan jauh, jangan mengurangi angin hanya karena angkanya terlihat lebih tinggi dari anjuran.</p>
<h2>Langkah pengecekan</h2>
<ol>
<li>Buka tutup pentil ban dan simpan agar tidak hilang.</li>
<li>Tekan alat ukur tekanan ke pentil dengan mantap sampai tidak ada desisan udara.</li>
<li>Baca angkanya dan bandingkan dengan angka pada stiker pabrikan.</li>
<li>Tambah atau kurangi angin secara bertahap, lalu ukur ulang.</li>
<li>Pasang kembali tutup pentil. Jangan lupa cek ban serep jika ada.</li>
</ol>
<h2>Satuan yang sering dijumpai</h2>
<p>Tekanan ban umumnya dinyatakan dalam PSI, bar, atau kPa. Sebagai patokan, 1 bar sama dengan sekitar 14,5 PSI atau 100 kPa. Pastikan satuan alat ukur Anda sama dengan satuan pada stiker.</p>
<h2>Seberapa sering sebaiknya dicek?</h2>
<p>Biasakan mengecek setidaknya sebulan sekali dan sebelum perjalanan jauh. Ban kehilangan tekanan secara alami seiring waktu, dan perubahan suhu udara juga memengaruhinya. Sekalian periksa kondisi tapak, adanya benjolan, retak, atau benda asing yang menancap.</p>
<h2>Tanda tekanan tidak ideal</h2>
<p>Tekanan terlalu rendah membuat ban cepat aus di sisi luar, mobil terasa berat dan boros. Tekanan terlalu tinggi membuat bagian tengah tapak cepat aus dan kenyamanan berkurang. Jika sering kehilangan angin padahal tidak ada paku yang terlihat, minta bengkel memeriksa pentil dan pelek.</p>
<p>Mobil modern punya sistem pemantau tekanan ban (TPMS) yang menyalakan lampu peringatan saat tekanan terlalu rendah. Sistem ini membantu, tetapi tidak menggantikan pengecekan manual berkala.</p>
"""),
]

# ===== HALAMAN WAJIB =====
HALAMAN = {
"tentang": ("Tentang Kami", f"Mengenal {SITE}: siapa kami, tujuan situs, dan cara kami menulis.", f"""
<p>{SITE} adalah situs edukasi independen yang menjelaskan perawatan mobil dengan bahasa sederhana untuk pengemudi sehari-hari di Indonesia.</p>
<h2>Tujuan kami</h2>
<p>Banyak pemilik mobil bingung membedakan perawatan rutin, saran pencegahan, dan perbaikan. Kami menulis panduan praktis agar Anda bisa memahami pekerjaannya dan berbicara dengan bengkel secara lebih percaya diri.</p>
<h2>Cara kami menulis</h2>
<ul><li>Artikel ditulis sendiri oleh tim kami dan diperiksa ulang sebelum terbit.</li>
<li>Kami mengutamakan buku manual dan spesifikasi pabrikan sebagai sumber utama.</li>
<li>Kami memperbarui artikel jika ada informasi yang berubah.</li></ul>
<h2>Transparansi</h2>
<p>Situs ini ditampilkan dengan iklan dari Google AdSense untuk membiayai operasionalnya. Iklan tidak memengaruhi isi artikel. Kami tidak menjual jasa bengkel, suku cadang, atau asuransi.</p>
<p>Punya saran atau menemukan kesalahan? Hubungi kami lewat halaman <a href="/kontak.html">Kontak</a>.</p>"""),
"kontak": ("Kontak", f"Hubungi tim {SITE} untuk saran, koreksi, atau kerja sama.", f"""
<p>Kami senang mendengar masukan dari pembaca.</p>
<p><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p>Anda dapat menghubungi kami untuk koreksi artikel, saran topik, pertanyaan tentang kebijakan privasi, atau permintaan kerja sama. Kami berusaha membalas dalam 2–3 hari kerja.</p>
<p>Catatan: kami tidak dapat mendiagnosis kendaraan secara pribadi. Untuk masalah pada mobil Anda, hubungi bengkel resmi atau mekanik terpercaya.</p>"""),
"privasi": ("Kebijakan Privasi", f"Kebijakan privasi {SITE}: data apa yang dikumpulkan, cookie, dan iklan Google AdSense.", f"""
<p>Terakhir diperbarui: 11 November 2026. Kebijakan ini menjelaskan bagaimana {SITE} ({DOMAIN}) memperlakukan informasi pengunjung.</p>
<h2>Informasi yang dikumpulkan</h2>
<p>Kami tidak meminta Anda mendaftar dan tidak menjual data pribadi. Seperti kebanyakan situs, server kami dapat mencatat data teknis standar seperti alamat IP, jenis browser, halaman yang dibuka, dan waktu kunjungan untuk keamanan dan analisis lalu lintas. Jika Anda mengirim email kepada kami, alamat dan isi pesan hanya dipakai untuk membalas Anda.</p>
<h2>Cookie</h2>
<p>Cookie adalah berkas kecil yang disimpan di perangkat Anda. Kami dan mitra iklan memakai cookie untuk menampilkan dan mengukur iklan. Anda dapat mengatur atau menghapus cookie lewat pengaturan browser.</p>
<h2>Google AdSense dan iklan pihak ketiga</h2>
<p>Kami memakai Google AdSense. Google sebagai vendor pihak ketiga memakai cookie untuk menayangkan iklan berdasarkan kunjungan Anda ke situs ini dan situs lain. Penggunaan cookie iklan memungkinkan Google dan mitranya menampilkan iklan yang relevan bagi Anda.</p>
<p>Anda dapat memilih keluar dari iklan yang dipersonalisasi lewat <a href="https://adssettings.google.com" rel="noopener" target="_blank">Pengaturan Iklan Google</a>. Informasi lebih lanjut tentang cara Google menggunakan data tersedia di <a href="https://policies.google.com/technologies/partner-sites" rel="noopener" target="_blank">policies.google.com/technologies/partner-sites</a>.</p>
<h2>Tautan ke situs lain</h2>
<p>Artikel kami dapat berisi tautan ke situs lain. Kami tidak bertanggung jawab atas kebijakan privasi situs tersebut.</p>
<h2>Anak-anak</h2>
<p>Situs ini tidak ditujukan untuk anak di bawah 13 tahun dan kami tidak dengan sengaja mengumpulkan data mereka.</p>
<h2>Perubahan kebijakan</h2>
<p>Kami dapat memperbarui kebijakan ini sewaktu-waktu. Perubahan akan ditampilkan di halaman ini beserta tanggal pembaruan. Pertanyaan? Hubungi <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
"syarat": ("Syarat dan Ketentuan", f"Syarat dan ketentuan penggunaan situs {SITE}.", f"""
<p>Dengan mengakses {SITE}, Anda menyetujui syarat berikut.</p>
<h2>Penggunaan konten</h2>
<p>Seluruh teks dan gambar di situs ini dilindungi hak cipta. Anda boleh mengutip singkat dengan mencantumkan sumber dan tautan ke halaman asal. Menyalin artikel secara utuh tanpa izin tidak diperbolehkan.</p>
<h2>Akurasi informasi</h2>
<p>Kami berusaha menyajikan informasi yang akurat, tetapi tidak menjamin kelengkapan atau keterkinian seluruhnya. Spesifikasi dan interval servis berbeda tiap kendaraan; selalu rujuk buku manual.</p>
<h2>Batasan tanggung jawab</h2>
<p>Kami tidak bertanggung jawab atas kerugian yang timbul dari penggunaan informasi di situs ini. Lihat juga <a href="/disclaimer.html">Disclaimer</a>.</p>
<h2>Tautan eksternal</h2>
<p>Kami tidak mengendalikan dan tidak bertanggung jawab atas isi situs pihak ketiga yang tertaut.</p>
<h2>Perubahan</h2>
<p>Syarat ini dapat diubah sewaktu-waktu. Penggunaan situs setelah perubahan berarti Anda menerimanya.</p>"""),
"disclaimer": ("Disclaimer", f"Disclaimer {SITE}: informasi bersifat edukasi dan bukan pengganti nasihat profesional.", f"""
<p>Informasi di {SITE} bersifat edukasi umum dan bukan nasihat teknis, hukum, atau profesional.</p>
<p>Kendaraan memiliki spesifikasi dan interval perawatan yang berbeda. Untuk keputusan perawatan atau perbaikan, ikuti buku manual pabrikan dan konsultasikan dengan mekanik atau bengkel resmi yang berkualifikasi.</p>
<p>Jika Anda menduga kendaraan tidak aman dikendarai, hentikan di tempat aman dan hubungi bantuan profesional. Kami tidak bertanggung jawab atas kerusakan atau kerugian akibat tindakan yang Anda ambil berdasarkan isi situs ini.</p>
<p>Situs ini menampilkan iklan pihak ketiga (Google AdSense). Keberadaan iklan bukan merupakan rekomendasi dari kami terhadap produk atau layanan yang diiklankan.</p>"""),
}

CSS = """:root{--bg:#f6f7f8;--card:#fff;--ink:#16191c;--muted:#5f6b76;--line:#dfe3e7;--accent:#d98e00;--dark:#16191c}
@media(prefers-color-scheme:dark){:root{--bg:#101316;--card:#1a1f24;--ink:#eceff2;--muted:#9aa5af;--line:#2b333a;--accent:#f2a900;--dark:#0b0d0f}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:18px/1.75 Georgia,'Times New Roman',serif}
a{color:inherit}:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.wrap{max-width:760px;margin:0 auto;padding:0 20px}
header{background:var(--dark);color:#eceff2;font-family:system-ui,sans-serif}
.bar{display:flex;justify-content:space-between;align-items:center;gap:16px;min-height:60px;flex-wrap:wrap}
.logo{font-weight:800;text-decoration:none;font-size:1.15rem}.logo b{color:var(--accent)}
nav a{margin-left:18px;text-decoration:none;font-size:.95rem;opacity:.9}nav a:hover{color:var(--accent)}
h1,h2{font-family:system-ui,sans-serif;line-height:1.25}h1{font-size:clamp(1.8rem,5vw,2.5rem);margin:40px 0 8px}
h2{font-size:1.4rem;margin:2em 0 .4em}p,li{margin:0 0 1em}ul,ol{padding-left:22px}
.meta{color:var(--muted);font:.9rem system-ui,sans-serif;margin-bottom:24px}
.hero{padding:48px 0 8px}.hero p{color:var(--muted);font-size:1.1rem}
.list a{display:block;background:var(--card);border:1px solid var(--line);border-left:4px solid var(--accent);padding:18px 22px;margin-bottom:16px;text-decoration:none;border-radius:4px}
.list strong{font:700 1.15rem system-ui,sans-serif;display:block}.list span{color:var(--muted);font-size:.97rem}
main{padding-bottom:48px}article a,.page a{color:#0b6bcb}
footer{background:var(--dark);color:#9aa5af;padding:32px 0;font:.92rem system-ui,sans-serif}
footer a{margin-right:18px;color:#cfd6dc}"""

def shell(title, desc, path, body, extra=""):
    url = DOMAIN + path
    return f"""<!DOCTYPE html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{url}"><meta name="robots" content="index,follow">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:type" content="website">
<meta name="google-adsense-account" content="{PUB}">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={PUB}" crossorigin="anonymous"></script>
<link rel="stylesheet" href="/style.css">{extra}</head>
<body><header><div class="wrap bar"><a class="logo" href="/">RAWAT<b>MOBIL</b></a>
<nav><a href="/">Beranda</a><a href="/#artikel">Artikel</a><a href="/tentang.html">Tentang</a><a href="/kontak.html">Kontak</a></nav></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap"><p>© 2026 {SITE}. Informasi edukasi independen tentang perawatan mobil.</p>
<a href="/privasi.html">Kebijakan Privasi</a><a href="/syarat.html">Syarat &amp; Ketentuan</a><a href="/disclaimer.html">Disclaimer</a><a href="/tentang.html">Tentang</a><a href="/kontak.html">Kontak</a></div></footer>
</body></html>"""

def write(rel, content):
    p = os.path.join(OUT, rel); os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    open(p, "w", encoding="utf-8").write(content)

urls = ["/"]
write("style.css", CSS)

# Beranda
items = "".join(f'<a href="/artikel/{a["slug"]}.html"><strong>{a["title"]}</strong><span>{a["desc"]}</span></a>' for a in ARTIKEL)
home = f"""<section class="hero"><h1>Perawatan mobil, dijelaskan sederhana.</h1>
<p>Panduan independen untuk memahami perawatan rutin mobil: ban, rem, aki, oli, dan cairan, tanpa istilah yang membingungkan.</p></section>
<h2 id="artikel">Artikel terbaru</h2><div class="list">{items}</div>"""
write("index.html", shell(f"{SITE} | Panduan Perawatan Mobil untuk Pengemudi Sehari-hari", "Panduan independen perawatan mobil rutin: ban, rem, aki, oli, dan cairan dalam bahasa sederhana.", "/", home))

# Artikel
for a in ARTIKEL:
    path = f"/artikel/{a['slug']}.html"; urls.append(path)
    ld = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{a["title"]}","datePublished":"{a["date"]}","author":{{"@type":"Organization","name":"{SITE}"}},"publisher":{{"@type":"Organization","name":"{SITE}"}}}}</script>'
    body = f'<article><h1>{a["title"]}</h1><div class="meta">Diterbitkan {a["date"]} · {SITE}</div>{a["body"]}<p class="meta">Catatan: informasi bersifat umum. Selalu rujuk buku manual kendaraan Anda. Lihat <a href="/disclaimer.html">Disclaimer</a>.</p></article>'
    write(path.lstrip("/"), shell(f'{a["title"]} | {SITE}', a["desc"], path, body, ld))

# Halaman wajib
for slug, (t, d, b) in HALAMAN.items():
    path = f"/{slug}.html"; urls.append(path)
    write(path.lstrip("/"), shell(f"{t} | {SITE}", d, path, f'<div class="page"><h1>{t}</h1>{b}</div>'))

# ads.txt, robots, sitemap, 404
write("ads.txt", f"google.com, pub-{PUB.split('pub-')[1]}, DIRECT, f08c47fec0942fa0\n")
write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
      "".join(f"<url><loc>{DOMAIN}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
write("404.html", shell(f"Halaman tidak ditemukan | {SITE}", "Halaman tidak ditemukan.", "/404.html",
      '<h1>Halaman tidak ditemukan</h1><p>Halaman yang Anda cari tidak ada. Kembali ke <a href="/">beranda</a>.</p>'))
print("Selesai:", OUT, "-", len(urls), "halaman")
