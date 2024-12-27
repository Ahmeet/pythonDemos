import pandas as pd
import numpy as np

# 1. Excel Dosyasını Yükle
file_path = r'C:\Users\intra\Desktop\vscode_workspace\pythonDemos\ExcelCategory\Personel Bilgileri.xlsx'  # Kaydettiğiniz dosyanın adı
data = pd.ExcelFile(file_path)
df = data.parse('Sayfa1')

# 2. Kolon İsimlerini Düzenle
df.columns = ['Name_Department', 'Title', 'Phone', 'Extra1', 'Extra2']

# 3. Departmanları Tespit Et ve Veriyi Temizle
# Departmanları tespit et
df['Is_Department'] = df['Title'].isna() & df['Phone'].isna()

# Departmanları yukarıdan aşağıya doldurun
df['Department'] = np.where(df['Is_Department'], df['Name_Department'], np.nan)
df['Department'] = df['Department'].ffill()

# Sadece çalışan verilerini filtrele
employees = df[~df['Is_Department']].copy()

# Fotoğraf sütunu ekle
employees['Photo'] = 'Fotoğraf Eklenecek'

# 4. Departman Bazlı Sayfalar Oluşturma
# Departman adlarını kısaltma fonksiyonu
def shorten_name(name, max_length=31):
    return name[:max_length]

# Excel'e yazma
output_file = 'Departmanlara_Gore.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for i, (department, group) in enumerate(employees.groupby('Department')):
        # Sayfa adını kısalt ve numaralandır
        sheet_name = shorten_name(f"{i+1}_{department}")
        group.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Excel dosyası '{output_file}' olarak başarıyla oluşturuldu.")


