import tornado.ioloop
import tornado.web
import json
from UserManage import
from bson import ObjectId
import os.path

users = db.users

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class AddUser(tornado.web.RequestHandler):
    def post(self):
        users.insert(json.loads(self.requst.body))


class RemoveUser(tornado.web.RequestHandler):
    def post(self):
        users.remove(json.loads(self.requst.body))


class UpdateUser(tornado.web.RequestHandler):
    def post(self):
        body_args = json.loads(self.request.body)
        users.update({'_id': body_args['_id']}, {$set:{body_args}})


class List(tornado.web.RequestHandler):
    def get(self):
        result=list()
        for doc in users.find():
            result.append(json.dumps(doc,cls=ComplexEncoder))
        self.write(result)
