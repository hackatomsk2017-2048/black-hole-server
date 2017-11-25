import random

import tornado.ioloop
import tornado.web
import tornado.websocket


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

    def check_origin(self, origin):
        # enable support for allowing alternate origins.
        return True


class RandomCardsHandler(tornado.web.RequestHandler):
    def get(self):
        # ToDo: This is legacy endpoint. Delete me
        self.write("{}".format(random.randint(0, 5)))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/cards", RandomCardsHandler),
        (r"/websocket", EchoWebSocket),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
