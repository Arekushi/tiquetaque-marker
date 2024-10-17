from datetime import datetime
from config.config import settings


def is_day_off():
    today = datetime.today().date()
    days_off = [datetime.strptime(day_off, '%d/%m/%Y').date() for day_off in settings.VARS.days_off]
    
    return today in days_off


def get_today():
    return datetime.today().strftime("%d/%m/%Y")
