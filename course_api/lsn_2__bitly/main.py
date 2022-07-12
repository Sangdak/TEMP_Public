import os
from dotenv import load_dotenv
import requests


def is_bitlink(url):
    if 'bit.ly' in url:
        return True
    else:
        return False


def shorten_url(token, url):
    tool_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    payload = {"long_url": "{}".format(url)}

    response = requests.post(tool_url, headers=token, json=payload)
    response.raise_for_status()
    return response.json()["id"]


def count_clicks(bitlink, token):
    tool_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(bitlink)

    response = requests.get(tool_url, headers=token)
    response.raise_for_status()
    return response.json()["total_clicks"]


def main():
    token = {"Authorization": "Bearer {}".format(os.getenv("TOKEN"))}
    input_url = input('Input your URL: ')
    url_is_bitlink = is_bitlink(input_url)

    try:
        if not url_is_bitlink:
            bitlink = shorten_url(token, input_url)
            return f'Битлинк {bitlink}'
        else:
            clicks = count_clicks(input_url, token)
            return f'По вашей ссылке перешли {clicks} раз(а).'
    except requests.exceptions.HTTPError:
        return f'Сссылка {input_url} не может быть обработана, проверьте ввод!'


if __name__ == '__main__':
    load_dotenv()
    print(main())
