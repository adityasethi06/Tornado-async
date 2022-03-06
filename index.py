import asyncio
import tornado
import tornado.web
import tornado.ioloop
import datetime

PORT=8888


class First(tornado.web.RequestHandler):
    async def get(self):
        print("First request: " + str(datetime.datetime.now()))
        await tornado.gen.sleep(15)
        # for _ in range(1000000000):
        #     pass
        self.set_status(200)
        self.write("First task")
        self.finish()
        print("First answer: " + str(datetime.datetime.now()))


class Second(tornado.web.RequestHandler):
    def get(self):
        print("Second request: " + str(datetime.datetime.now()))
        self.set_status(200)
        self.write("Second task")
        self.finish()
        print("Second answer: " + str(datetime.datetime.now()))


class Application(tornado.web.Application):
    def __init__(self):
        ENDPOINTS = [
            # USERS #
            (r"/test-first", First),
            (r"/test-second", Second)
        ]

        SETTINGS = {
            "debug": True,
            "autoreload": True,
            "serve_traceback": True,
            "compress_response": True
        }

        tornado.web.Application.__init__(self, ENDPOINTS, SETTINGS)


if __name__ == "__main__":
    Application().listen(PORT)
    print(f"Server listening on PORT: {PORT}")
    tornado.ioloop.IOLoop.instance().start()