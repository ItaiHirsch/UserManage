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
        #import ipdb; ipdb.set_trace()
        body_args = json.loads(self.request.body)
        users.insert(body_args)


class RemoveUser(tornado.web.RequestHandler):
    def post(self):
        users.remove(json.loads(self.request.body))


class UpdateUser(tornado.web.RequestHandler):
    def post(self):
        body_args = json.loads(self.request.body)
        #r = users.find({"_id":ObjectId(body_args["_id"])})
        #bbb = list(r)
        #import ipdb; ipdb.set_trace()
        users.update({"_id":ObjectId(body_args["_id"])}, {'$set':{'mobile':body_args['mobile']}})


class List(tornado.web.RequestHandler):
    def get(self):
        result=dict()
        result['data']=list()
        for doc in users.find():
            new_doc = json.loads(json.dumps(doc,cls=MongoEncoder))
            result['data'].append(new_doc)
        self.write(result)
