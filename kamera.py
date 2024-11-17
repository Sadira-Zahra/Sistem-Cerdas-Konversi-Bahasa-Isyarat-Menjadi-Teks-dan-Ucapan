import cv2

# Membuka kamera (0 biasanya untuk kamera default)
cap = cv2.VideoCapture(0)

# Cek apakah kamera berhasil dibuka
if not cap.isOpened():
    print("Tidak dapat membuka kamera!")
    exit()

while True:
    # Membaca frame dari kamera
    ret, frame = cap.read()
    
    # Jika berhasil membaca frame
    if not ret:
        print("Gagal membaca frame!")
        break
    
    # Membalik gambar secara horizontal untuk menghilangkan efek mirror
    frame = cv2.flip(frame, 1)
    
    # Menampilkan frame
    cv2.imshow('Kamera', frame)
    
    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Melepaskan kamera dan menutup jendela
cap.release()
cv2.destroyAllWindows()
