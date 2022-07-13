import os
from dotenv import load_dotenv
from urllib.parse import urlparse
import requests


def is_bitlink(url, token):
    tool_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(url)
    print(f'is bitlink: {tool_url}')
    try:
        response = requests.get(tool_url, headers=token)
        response.raise_for_status()
    except:
        return False
    return True


def shorten_url(url, token):
    tool_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    payload = {"long_url": "{}".format(url)}
    print(f'shorten: {tool_url}')

    response = requests.post(tool_url, headers=token, json=payload)
    response.raise_for_status()
    return response.json()["id"]


def count_clicks(url, token):
    tool_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(url)
    print(f'count: {tool_url}')

    response = requests.get(tool_url, headers=token)
    response.raise_for_status()
    return response.json()["total_clicks"]


def main():
    token = {"Authorization": "Bearer {}".format(os.getenv("TOKEN"))}
    input_url = input('Input your URL: ')
    parse = urlparse(input_url)
    formated_url = parse.netloc + parse.path
    url_is_bitlink = is_bitlink(formated_url, token)

    try:
        if not url_is_bitlink:
            bitlink = shorten_url(input_url, token)
            return f'Битлинк {bitlink}'
        else:
            clicks = count_clicks(formated_url, token)
            return f'По вашей ссылке перешли {clicks} раз(а).'
    except requests.exceptions.HTTPError:
        return f'Сссылка {input_url} не может быть обработана, проверьте ввод!'


if __name__ == '__main__':
    load_dotenv()
    print(main())
