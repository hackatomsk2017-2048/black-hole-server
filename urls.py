from handlers.base import MainHandler, EchoWebSocket
from handlers.battle import RandomCardsHandler

url_patterns = [
    (r"/", MainHandler),
    (r"/cards", RandomCardsHandler),
    (r"/websocket", EchoWebSocket),
]
