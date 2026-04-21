from sense_emu import SenseHat
import time

sense = SenseHat()

# Định nghĩa màu
r = [255, 0, 0]    # Đỏ
w = [255, 255, 255]# Trắng
b = [0, 0, 0]      # Tắt (đen)

# Trái tim 8x8 (Đã thiết kế lại)
heart = [
    b, r, r, b, b, r, r, b,
    r, w, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    b, r, r, r, r, r, r, b,
    b, b, r, r, r, r, b, b,
    b, b, b, r, r, b, b, b,
    b, b, b, b, b, b, b, b,
]

sense.set_pixels(heart)
print('Biểu tượng trái tim đã hiển thị.')
time.sleep(5)
sense.clear()
