import os
from dotenv import load_dotenv
from urllib.parse import urlparse
import requests


def is_bitlink(url, header):
    request_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}'
    try:
        response = requests.get(request_url, headers=header)
        response.raise_for_status()
    except:
        return False
    return True


def shorten_url(url, header):
    request_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    payload = {"long_url": f"{url}"}

    response = requests.post(request_url, headers=header, json=payload)
    response.raise_for_status()
    return response.json()["id"]


def count_clicks(url, header):
    request_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary'

    response = requests.get(request_url, headers=header)
    response.raise_for_status()
    return response.json()["total_clicks"]


def main():
    autorization_data = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}
    input_url = input('Input your URL: ')
    parse = urlparse(input_url)
    formatted_url = parse.netloc + parse.path

    try:
        if not is_bitlink(formatted_url, autorization_data):
            return f'Битлинк {shorten_url(input_url, autorization_data)}'
        else:
            return f'По вашей ссылке перешли {count_clicks(formatted_url, autorization_data)} раз(а).'
    except requests.exceptions.HTTPError:
        return f'Сссылка {input_url} не может быть обработана, проверьте ввод!'


if __name__ == '__main__':
    load_dotenv()
    print(main())
