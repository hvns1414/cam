import cv2
import numpy as np

# ASCII karakter seti (karanlıktan aydınlığa)
ASCII_CHARS = "@%#*+=-:. "

# Kamerayı aç
cap = cv2.VideoCapture(0)

def frame_to_ascii(frame, width=80):
    # Gri tonlamaya çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Boyutu ayarla
    height, orig_width = gray.shape
    aspect_ratio = height / orig_width
    new_height = int(aspect_ratio * width * 0.55)
    resized = cv2.resize(gray, (width, new_height))
    
    # ASCII’ye çevir
    ascii_str = ""
    for row in resized:
        for pixel in row:
            ascii_str += ASCII_CHARS[int(pixel) * len(ASCII_CHARS) // 256]  # int() ile Overflow önlendi
        ascii_str += "\n"
    return ascii_str

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        ascii_frame = frame_to_ascii(frame)
        print("\033[H\033[J", end="")  # Terminali temizle
        print(ascii_frame)
except KeyboardInterrupt:
    cap.release()
    print("Çıkış yapıldı.")
