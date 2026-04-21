from sense_emu import SenseHat
import time

sense = SenseHat()

def map_value(val, in_min, in_max, out_max=8):
    result = int((val - in_min) / (in_max - in_min) * out_max)
    return max(0, min(out_max, result))

def draw_bar(y_start, y_end, cols, color):
    for y in range(y_start, y_end + 1):
        for x in range(8):
            sense.set_pixel(x, y, color if x < cols else [0,0,0])

try:
    while True:
        # Bắt sự kiện Joystick trước
        for event in sense.stick.get_events():
            if event.action == 'pressed' and event.direction == 'middle':
                sense.show_message(f"{temp:.1f}C", text_colour=[255, 255, 255])
                time.sleep(0.5)

        print("\n--- NHẬP THÔNG SỐ TỪ SERVER ---")
        temp = float(input("Nhập Nhiệt độ (°C): "))
        hum = float(input("Nhập Độ ẩm (%): "))

        sense.clear()
        
        # Vẽ bar nhiệt độ (0-2)
        temp_cols = map_value(temp, 15, 40)
        draw_bar(0, 2, temp_cols, [255, 0, 0])

        # Vẽ bar độ ẩm (3-5)
        hum_cols = map_value(hum, 20, 90)
        draw_bar(3, 5, hum_cols, [0, 0, 255])

        # Trạng thái (6-7)
        if temp > 30:
            draw_bar(6, 7, 8, [255, 0, 0])
            sense.show_message('HOT!', text_colour=[255, 0, 0], scroll_speed=0.08)
        elif hum > 80:
            draw_bar(6, 7, 8, [255, 255, 0])
        else:
            draw_bar(6, 7, 8, [0, 255, 0])

except KeyboardInterrupt:
    sense.clear()

