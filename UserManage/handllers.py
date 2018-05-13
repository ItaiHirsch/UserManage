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
        #import ipdb;ipdb.set_trace()
        data = json.loads(self.request.body)
        doc = {
            'first': data['first'],
            'last': data['last'],
            'mobile': data['mobile']
        }
        users.insert(doc)
        self.write({'status': 'ok'})


class RemoveUser(tornado.web.RequestHandler):
    '''
    this handler removing a user
    '''
    def post(self):
        #import ipdb;ipdb.set_trace()
        users.remove({'_id':ObjectId((json.loads(self.request.body))['id'])})
        self.write({'status': 'OK'})

class UpdateUser(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        #import ipdb;ipdb.set_trace()
        users.update({"_id":ObjectId(data['id'])}, {'$set':{'mobile':data['mobile'],'first':data['first'],'last':data['last']}})
        self.write({'status': 'OK'})


class List(tornado.web.RequestHandler):
    def get(self):
        #import ipdb;ipdb.set_trace()
        response = json.dumps(list(users.find()), cls=MongoEncoder)
        self.write({'status': 'ok', 'data': response})






