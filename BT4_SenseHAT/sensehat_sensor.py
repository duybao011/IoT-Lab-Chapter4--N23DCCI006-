from sense_emu import SenseHat
import time

sense = SenseHat()

try:
    while True:
        temp = sense.get_temperature()
        hum = sense.get_humidity()
        press = sense.get_pressure()
        print(f'Temp: {temp:.1f}°C | Humidity: {hum:.1f}% | Pressure: {press:.1f} mbar')
        time.sleep(1)
except KeyboardInterrupt:
    sense.clear()
    print('Dừng đọc cảm biến.')
