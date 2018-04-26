#TornadoWeb Framework
from handllers import *

#MongoDB create collection
client = MongoClient('35.227.115.20')
db = client.userdb
col = db.users

#path to files
settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "static"),
    debug = True
)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/add", AddUser),
        (r"/delete", DeleteUser),
        (r"/update", UpdateUser),
        (r"/list", GetList)
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server running....")
    tornado.ioloop.IOLoop.current().start()