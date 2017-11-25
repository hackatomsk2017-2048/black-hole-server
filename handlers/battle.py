import random

from tornado.web import RequestHandler


class RandomCardsHandler(RequestHandler):
    def get(self):
        # ToDo: This is legacy endpoint. Delete me
        self.write("{}".format(random.randint(0, 5)))
