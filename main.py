from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import TECHSTAR

from TECHSTAR import Date
print(Date)

app = Flask(__name__)
api = Api(app)

data_put_args = reqparse.RequestParser()
data_put_args.add_argument("name", type=str, help="name of data is required", required=True)
data_put_args.add_argument("count", type=int, help="count of data", required=True)
data_put_args.add_argument("popularity", type=int, help="popularity of data", required=True)

#data_put_args.add_argument("Title", "Job", required=True)

DATA = {}

def abort_if_data_id_nonexistant(data_id):
    if data_id not in DATA:
        abort(404, message="TechStar Job Data is not valid 404 error encountered")

def abort_if_data_exists(data_id):
    if data_id in DATA:
        abort(409, messsage="Data already exists with that id")

class rand_data(Resource):
    def get(self, data_id):
        abort_if_data_id_nonexistant(data_id)
        return DATA[data_id]

    def put(self, data_id):
        abort_if_data_exists(data_id)
        args = data_put_args.parse_args()
        DATA[data_id] = args
        #print(request.form['data'])
        return DATA[data_id], 201

    def delete(self, data_id):
        abort_if_data_id_nonexistant(data_id)
        del DATA[data_id]
        return '', 204



api.add_resource(rand_data, "/rand_data/<int:data_id>")


#api.add_resource(techdata_one, "/hellotech/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)


'''

class techdata_one(Resource):
    def get(self, name):
        return names[name]

    def post(self):
        return {"data": name, "tester": tester}
'''

