import tornado.web
from views.user import UserHandler

def make_app():
    return tornado.web.Application([
        (r"/user", UserHandler),
        (r"/user/([0-9]+)", UserHandler),  # Handling user_id in the URL
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()