import requests 


def get_phone(phone):
    phone = requests.get('http://localhost:5000/api?action=phone&name=Urban')
    return phone.text


def get_name(name):
    name = requests.get('http://localhost:5000/api?action=phone&name=Urban')
    return name.text
