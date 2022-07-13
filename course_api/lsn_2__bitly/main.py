import os
from dotenv import load_dotenv
from urllib.parse import urlparse
import requests


def is_bitlink(url, header):
    request_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(url)
    try:
        response = requests.get(request_url, headers=header)
        response.raise_for_status()
    except:
        return False
    return True


def shorten_url(url, header):
    request_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    payload = {"long_url": "{}".format(url)}

    response = requests.post(request_url, headers=header, json=payload)
    response.raise_for_status()
    return response.json()["id"]


def count_clicks(url, header):
    request_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(url)

    response = requests.get(request_url, headers=header)
    response.raise_for_status()
    return response.json()["total_clicks"]


def main():
    autorization_data = {"Authorization": "Bearer {}".format(os.getenv("TOKEN"))}
    input_url = input('Input your URL: ')
    parse = urlparse(input_url)
    formatted_url = parse.netloc + parse.path
    url_is_bitlink = is_bitlink(formatted_url, autorization_data)

    try:
        if not url_is_bitlink:
            bitlink = shorten_url(input_url, autorization_data)
            return f'Битлинк {bitlink}'
        else:
            clicks = count_clicks(formatted_url, autorization_data)
            return f'По вашей ссылке перешли {clicks} раз(а).'
    except requests.exceptions.HTTPError:
        return f'Сссылка {input_url} не может быть обработана, проверьте ввод!'


if __name__ == '__main__':
    load_dotenv()
    print(main())
