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
    '''
    thid handler is the default one loading thml page
    '''
    def get(self):
        self.render('front.html')

class AddUser(tornado.web.RequestHandler):
    '''
    this handler alowing to add a user
    '''
    def post(self):
        doc = {
            'first': self.get_argument('first'),
            'last': self.get_argument('last'),
            'mobile': self.get_argument('mobile')
        }
        users.insert(doc)
        self.write({'status': 'ok'})


class RemoveUser(tornado.web.RequestHandler):
    '''
    this handler removing a user
    '''
    def post(self):
        users.remove({'_id':ObjectId(self.get_argument('id'))})

class UpdateUser(tornado.web.RequestHandler):
    def post(self):
        users.update({"_id":ObjectId(self.get_argument('id'))}, {'$set':{'mobile':self.get_argument('mobile'),'first':self.get_argument('first'),'last':self.get_argument('last')}})
        self.write({'status': 'OK'})


class List(tornado.web.RequestHandler):
    def get(self):
        response = json.dumps(list(users.find()), cls=MongoEncoder)
        self.write({'status': 'ok', 'data': response})






