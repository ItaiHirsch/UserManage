import tornado.ioloop
import tornado.web
import json
from UserManage import db

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class AddUser(tornado.web.RequestHandler):
    def post(self):
        body_args = json.loads(self.requst.body)
        pass


class RemoveUser(tornado.web.RequestHandler):
    def post(self):
        pass


class UpdateUser(tornado.web.RequestHandler):
    def post(self):
        pass


class List(tornado.web.RequestHandler):
    def get(self):
        pass