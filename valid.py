import re
from datetime import datetime

def valid_email(email):
    return re.match(r"^[\w\-]+@[\w\-]+\.\w+$", email)


def valid_password(password, confirm_password):
    if password != confirm_password:
        return False, "Passwords do not match"
    if len(password) < 8:
        return False, "Password must be at least 8 chars"
    return True, ""


def valid_phone(phone):
    return re.match(r"^[0][1][0125][0-9]{8}$", phone)
    
def valid_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except:
        return None


