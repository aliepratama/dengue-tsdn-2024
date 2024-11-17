<p align="center">
<img src="https://dataacademy.co.id/wp-content/uploads/2024/10/Asset-1.png" width="75"/>
<img src="https://sayyidahnuraruni.files.wordpress.com/2015/04/logo-uty-png.png" width="75"/>
</p>

## **Sistem deteksi dini demam berdarah dan klasifikasi nyamuk Aedes aegypti**

> ### **Tim SudahMakanNasPad** (Universitas Teknologi Yogyakarta)
1. Muhammad Ali Pratama Putra
2. M. Ridha Ansari Adriansyah
3. Jati Kurniawan Yusuf Saputra

## Persyaratan Sistem

Pastikan Anda memiliki perangkat lunak berikut yang sudah terpasang:
- **Python** (versi 3.12 atau lebih baru)
- **pip** (Pengelola paket Python)
- **Virtualenv** (opsional tetapi disarankan)

---

## Langkah-Langkah Instalasi

### 1. Kloning Repository
Kloning repository proyek ke komputer Anda menggunakan perintah berikut:
```bash
git clone https://github.com/aliepratama/dengue-tsdn-2024.git
```

### 2. Instalasi
Instalasi modul yang digunakan
```shell
python -m venv myenv
myenv\scripts\activate.bat
pip install -r requirements.txt
```

### 3. Menjalankan Projek
Cara menjalankan dapat dilakukan sebagai berikut
```shell
flask run
```

### Perlu diperhatikan

- Pastikan untuk mengubah value pada file `.env` anda menggunakan template pada file `.envexample`
```
USE_NGROK=<True | False>
NGROK_AUTHTOKEN=<Isi token anda>
ROBOFLOW_API_KEY=<Isi token anda>
```

### Demo Prototype


https://github.com/user-attachments/assets/3ab920ee-c1ee-45aa-bbc0-5a9b4468f68a

