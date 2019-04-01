import os
import sys
import tornado
from clients import WSClient

DEFAULT_HOST = 'localhost:8000'
DEFAULT_PASS = 'dev_pass'
DEFAULT_SEND_RATE = 1000
DEFAULT_RECONNECTION_RATE = 1000  # One second to evaluate reconnection


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

    if password and password != '':
        return 'ws://{}/stream/?password={}'.format(host, password)
    else:
        return 'ws://{}/stream/'.format(host)


def main(**kwargs):
    url = get_websocket_url(kwargs)
    print('Going to send messages to: ', url)

    ws_client = WSClient(url, kwargs)

    def send_alarm():
        if ws_client.is_connected():
            msg = {
                'stream': 'broadcast',
                'payload': {
                    'action': 'list'
                }
            }
            print('Sending message: ', msg)
            ws_client.send_message(msg)

    send_rate = DEFAULT_SEND_RATE
    reconnection_rate = DEFAULT_RECONNECTION_RATE

    def ws_reconnection():
        if not ws_client.is_connected():
            ws_client.reconnect()

    broadcast_task = tornado.ioloop.PeriodicCallback(
        send_alarm,
        send_rate
    )

    reconnection_task = tornado.ioloop.PeriodicCallback(
        ws_reconnection,
        reconnection_rate
    )
    tasks = [broadcast_task, reconnection_task]

    for task in tasks:
        task.start()

    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = DEFAULT_HOST
    password = os.getenv('WEBSOCKET_PASS', DEFAULT_PASS)
    main(host=host, password=password, verbosity=1)
