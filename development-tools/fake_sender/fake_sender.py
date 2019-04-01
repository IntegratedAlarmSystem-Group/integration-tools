import os
import sys
import tornado

DEFAULT_HOST = 'localhost:8000'
DEFAULT_PASS = ''


def get_websocket_url(kwargs):
    """
    Returns the url to send websocket messages

    Args:
        kwargs (dict): optional arguments passed to the command

    Returns:
        string: the url
    """

    if kwargs['host'] is not None:
        host = kwargs['host']

    if kwargs['password'] is not None:
        password = kwargs['password']

    return 'ws://{}/stream/?password={}'.format(host, password)


def main(**kwargs):
    print('kwargs: ', kwargs)
    url = get_websocket_url(kwargs)
    print('url: ', url)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = DEFAULT_HOST
    password = os.getenv('WEBSOCKET_PASS', DEFAULT_PASS)
    main(host=host, password=password)
