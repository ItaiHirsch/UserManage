import tornado.ioloop
import tornado.web
import json
from UserManage import client
import pymongo
from utils import MongoEncoder
from bson import ObjectId
import os.path

db = client.userdb
users = db.users

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
        users.update({'_id': body_args['_id']}, {'$set':{body_args}})


class List(tornado.web.RequestHandler):
    def get(self):
       # import ipdb; ipdb.set_trace()
        #for doc in users.find():
        #    #import ipdb; ipdb.set_trace()
        #    new_doc = json.loads(json.dumps(doc,cls=MongoEncoder))
        #    self.write(new_doc)
        #import ipdb; ipdb.set_trace()
        result=dict()
        result['data']=list()
        for doc in users.find():
            new_doc = json.loads(json.dumps(doc,cls=MongoEncoder))
            result['data'].append(new_doc)
        self.write(result)
