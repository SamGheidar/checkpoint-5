import requests 


def get_phone(vaiable1):
    phone = requests.get(f'http://localhost:5000/api?action=phone&name={vaiable1}')
    return phone.text


def get_name(vaiable2):
    name = requests.get(f'http://localhost:5000/api?action=phone&name={vaiable2}')
    return name.text
