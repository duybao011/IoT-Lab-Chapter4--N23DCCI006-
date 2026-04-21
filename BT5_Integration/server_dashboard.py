import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv

temps, hums, dists = [], [], []
with open('wokwi_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        temps.append(float(row['temperature']))
        hums.append(float(row['humidity']))
        dists.append(float(row['distance']))

fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

axes[0].plot(temps, 'r-')
axes[0].axhline(y=30, color='orange', linestyle='--')
axes[0].set_ylabel('Temp (°C)')
axes[0].set_title('Server Room Dashboard')

axes[1].plot(hums, 'b-')
axes[1].axhline(y=80, color='orange', linestyle='--')
axes[1].set_ylabel('Humidity (%)')

axes[2].plot(dists, 'g-')
axes[2].axhline(y=30, color='red', linestyle='--')
axes[2].set_ylabel('Distance (cm)')
axes[2].set_xlabel('Sample')

plt.tight_layout()
plt.savefig('server_dashboard.png', dpi=150)
print('Saved: server_dashboard.png')
