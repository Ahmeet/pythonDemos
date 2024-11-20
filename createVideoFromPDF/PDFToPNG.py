import os
from pdf2image import convert_from_path

# PDF dosyasının yolu
pdf_path = r"C:\Users\intra\Desktop\PDF MEA Regional Marketing Summit 2024 (agenda) (3).pdf"

# Çıkış dizini (PNG dosyalarının kaydedileceği yer)
output_folder = r"C:\Users\intra\Desktop\vscode_workspace\pythonDemos\createVideoFromPDF"
os.makedirs(output_folder, exist_ok=True)

# PDF'i PNG'ye dönüştür
images = convert_from_path(pdf_path)

# Her sayfayı PNG olarak kaydet
for i, img in enumerate(images):
    img_path = f"{output_folder}page_{i+1}.png"
    img.save(img_path, "PNG")
    print(f"Sayfa {i+1} kaydedildi: {img_path}")

print("Tüm sayfalar başarıyla PNG'ye dönüştürüldü!")
