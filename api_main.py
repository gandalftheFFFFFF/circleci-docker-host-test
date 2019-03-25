import requests
import os

environment = os.getenv('CIRCLE_SHA1', 'offline')

if environment == 'offline':
    host = 'localhost'
else:
    host = 'web'


def main():
    r = requests.get(f'http://{host}:8080/')
    assert r.status_code == 200


if __name__ == '__main__':
    main()

