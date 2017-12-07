import falcon, json

class ObjRec:
    def on_get(self, req, response):
        print "hey falcon"
        return""


api = falcon.API()
api.add_route('/app', ObjRec())
