import shutil
import logging
import schedule

logging.basicConfig(filename=logs.txt,level=INFO,datefmt='%Y-%m-%d %H:%M:%S')
def check_disk():
    disk = shutil.disk_usage("/")
    per_used = (disk.total -disk.free)/disk.total*100
    print(per_used)
    if per_used > 75:
        logging.warning("disk full")
    elif per_used > 95:
        logging.warning("critical disk full")

check_disk()

schedule.every(10).seconds.do(check_disk) #cron_setup 


while True:
    schedule.run_pending()
