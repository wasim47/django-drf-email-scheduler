
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import send_email

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(send_email, 'cron', day='*', hour=0, minute=1)
	scheduler.start()