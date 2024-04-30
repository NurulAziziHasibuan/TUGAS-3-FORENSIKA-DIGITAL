import requests
import os
import base64
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

# 1. Periksa metadata pada https://journal.ittelkom-sby.ac.id/jaiit/
url = "https://journal.ittelkom-sby.ac.id/jaiit/"
response = requests.get(url)
template = "JURNAL TEMPLATE ISSN P-ISSN: ISSN 2716-1935 JAIIT dikelola dan diterbitkan oleh LPPM ITTelkom Surabaya Jl. Ketintang No. 156, Surabaya 60231 Jawa Timur, Indonesia Email: [email protected] e-ISSN : 2716-1927; p-ISSN : 2716-1935"

# 2. Kode script, pilih salah satu jurnal PDF, edit metadata, dan sesuaikan dengan paper yang dipilih
# Untuk tujuan demonstrasi, kita akan menggunakan file PDF contoh
file_pdf = "sample.pdf"
pdf = PdfReader(file_pdf)
pdf_baru = PdfWriter()

# Tambahkan halaman baru di awal dokumen
halaman_baru = canvas.Canvas("halaman_baru.pdf", pagesize=letter)
halaman_baru.drawString(100, 750, "Halaman Baru")  # Tambahkan teks pada koordinat (100, 750)
halaman_baru.save()
pdf_halaman_baru = PdfReader("halaman_baru.pdf")
pdf_baru.add_page(pdf_halaman_baru.pages[0])  

# Tambahkan halaman baru di akhir dokumen
halaman_terakhir = pdf.pages[-1]
pdf_baru.add_page(halaman_terakhir)

# Tambahkan teks metadata pada halaman baru
halaman_baru = canvas.Canvas("halaman_baru.pdf", pagesize=letter)
halaman_baru.drawString(100, 750, template)  # Tambahkan teks metadata pada koordinat (100, 750)
halaman_baru.save()
pdf_halaman_baru = PdfReader("halaman_baru.pdf")
pdf_baru.add_page(pdf_halaman_baru.pages[0])

# Simpan PDF yang diubah
file_pdf_terubah = "modified_sample.pdf"
with open(file_pdf_terubah, "wb") as f:
    pdf_baru.write(f)

# 3. Dekode script
pdf_terdecod = PdfReader(file_pdf_terubah)

# Output script: 2 file PDF, file PDF asli dan file PDF yang diubah dengan halaman awal dan akhir yang ditambahkan
print("File PDF Asli:", file_pdf)
print("File PDF yang Diubah:", file_pdf_terubah)
