**Konversi-Bahasa-Isyarat-Menjadi-Teks-dan-Ucapan**

**Abstrak:** 

 Proyek ini menggunakan jaringan saraf konvolusional (CNN) untuk mengembangkan sistem pengenalan bahasa isyarat Amerika (ASL) berbasis kamera secara real-time. Metode ini dirancang untuk mengenali gerakan tangan dengan mendeteksi posisi dan orientasi tangan dari gambar kamera, sehingga dapat mengklasifikasikan isyarat ASL dengan akurat. Gambar tangan terlebih dahulu melalui proses penyaringan sebelum diklasifikasikan, memungkinkan CNN untuk dilatih secara optimal pada gambar yang sudah dikalibrasi dan mencapai akurasi tinggi dalam pengenalan isyarat secara otomatis. 
 
 Hasil...
 
https://github.com/user-attachments/assets/e08b7872-115d-484c-a7c1-8a90480af9cc



**Penjelasan:**

 Bahasa Isyarat Amerika digunakan oleh penyandang tuli dan bisu (D&B) untuk berkomunikasi menggunakan gerakan tangan sebagai bahasa nonverbal yang dipahami secara visual. Proyek kami bertujuan untuk membuat model yang dapat mengenali isyarat ejaan jari, memungkinkan pembentukan kata lengkap melalui penggabungan setiap gerakan tangan.
 Berikut merupakan isyarat masing masing huruf :


![Spanish_SL](https://user-images.githubusercontent.com/99630855/201489493-585ffe5c-f460-402a-b558-0d03370b4f92.jpg)


**Penjelasan metode yang digunakan :**

Metode berbasis penglihatan menggunakan webcam komputer sebagai perangkat input untuk mengamati informasi tangan dan/atau jari. Metode ini hanya memerlukan kamera, sehingga menciptakan interaksi alami antara manusia dan komputer tanpa perangkat tambahan, sehingga lebih hemat biaya. Tantangan utama dalam deteksi tangan berbasis penglihatan meliputi beragam variasi tampilan tangan manusia yang sangat luas akibat banyaknya gerakan tangan, kemungkinan warna kulit yang berbeda, serta variasi sudut pandang, skala, dan kecepatan kamera dalam menangkap adegan.

 ![1pic](https://github.com/user-attachments/assets/f65fab12-b053-482d-94a9-3db38d61291d)
 

**Proses data:**

Pada pendekatan deteksi tangan ini, pertama-tama kita mendeteksi tangan dari gambar yang diperoleh melalui webcam, dan untuk mendeteksi tangan, kita menggunakan pustaka MediaPipe yang digunakan untuk pemrosesan gambar. Setelah menemukan tangan dari gambar, kita mendapatkan area yang menjadi fokus (Region of Interest/ROI), kemudian kita memotong area tersebut dan mengonversi gambar menjadi gambar abu-abu menggunakan pustaka OpenCV. Setelah itu, kita menerapkan gaussian blur. Filter ini dapat dengan mudah diterapkan menggunakan pustaka OpenCV (Open Computer Vision). Selanjutnya, gambar abu-abu diubah menjadi gambar biner dengan menggunakan metode threshold dan adaptive threshold.

**Convolutional Neural Network (CNN)**

CNN (Convolutional Neural Network) adalah jenis jaringan saraf yang sangat berguna dalam menyelesaikan masalah pada bidang computer vision. CNN terinspirasi dari proses persepsi visual yang terjadi di korteks visual pada otak kita. Jaringan ini menggunakan filter atau kernel untuk memindai setiap nilai piksel pada gambar dan melakukan perhitungan dengan menetapkan bobot yang sesuai untuk mendeteksi fitur tertentu. CNN terdiri dari beberapa lapisan, seperti lapisan konvolusi, lapisan max pooling, lapisan flatten, lapisan dense, lapisan dropout, dan lapisan jaringan saraf sepenuhnya terhubung (fully connected). Kombinasi lapisan-lapisan ini membentuk alat yang sangat kuat untuk mengidentifikasi fitur pada gambar. Lapisan awal mendeteksi fitur-fitur tingkat rendah yang kemudian secara bertahap mulai mendeteksi fitur tingkat tinggi yang lebih kompleks.


**Konversi teks menjadi bahasa :**

Model ini menerjemahkan gerakan yang dikenali menjadi kata-kata. Menggunakan pustaka pyttsx3 untuk mengonversi kata-kata yang dikenali tersebut menjadi ucapan yang sesuai. Output text-to-speech ini adalah solusi sederhana, tetapi sangat berguna karena dapat mensimulasikan dialog dalam kehidupan nyata. 

**Kebutuhan projek :**

**Kebutuhan perangkat keras:**

Webcam 

**Kebutuhan perangkat lunak:**

Sistem Operasi: Windows 8 and Above 

IDE: PyCharm 

Bahasa Pemrograman: Python 3.9 5 

Pustaka Phyton: OpenCV, NumPy, Keras,mediapipe,Tensorflow 
