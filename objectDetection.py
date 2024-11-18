import cv2

def main(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Video tidak bisa dibuka.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Tidak ada frame yang dibaca dari video.")
            break

        # Mengubah frame ke grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Menggunakan thresholding untuk memisahkan objek dari latar belakang
        _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

        # Menemukan kontur pada mask
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:  # Filter berdasarkan area kontur
                # Mendapatkan bounding rectangle
                x, y, w, h = cv2.boundingRect(contour)
                # Menggambar bounding rectangle di sekitar objek
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # Menambahkan teks di dalam bounding rectangle
                cv2.putText(frame, "Bentuk Ditemukan", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

         # Mengubah ukuran frame output
        frame_resized = cv2.resize(frame, (854, 480))  # Ganti dengan ukuran yang diinginkan

        # Menampilkan frame dengan bounding rectangle
        cv2.imshow('Video', frame_resized)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Ganti 'video.mp4' dengan path video Anda
main("C:/Users/Asus/Downloads/object_video.mp4")