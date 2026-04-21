import psutil
from datetime import datetime
from time import sleep

log_file = open('system_log.txt', 'w')

try:
    while True:
        cpu_list = psutil.cpu_percent(interval=None, percpu=True)
        cpu_avg = sum(cpu_list) / len(cpu_list)

        ram = psutil.virtual_memory()
        ram_used_mb = ram.used // (1024 ** 2)
        ram_total_mb = ram.total // (1024 ** 2)
        ram_pct = ram.percent

        disk = psutil.disk_usage('/')
        disk_pct = disk.percent

        if cpu_avg >= 70:
            status = 'CRITICAL'
        elif cpu_avg >= 30:
            status = 'WARNING'
        else:
            status = 'NORMAL'

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        line = (
            f'[{now}] CPU: {cpu_avg:.1f}% | '
            f'RAM: {ram_used_mb}/{ram_total_mb} MB ({ram_pct}%) | '
            f'Disk: {disk_pct}% | {status}'
        )

        print(line)

        if status != 'NORMAL':
            print(f'  ⚠ {status}: CPU đang ở {cpu_avg:.1f}%')

        log_file.write(line + '\n')
        log_file.flush()

        sleep(1)

except KeyboardInterrupt:
    print('\nDừng giám sát.')

finally:
    log_file.close()
    print('Log saved to system_log.txt')

