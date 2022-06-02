from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json



HAZARDS = {'1':'trash', '2':'leafs','3':'pothole'}
PORT = 5001
URL ='10.176.94.15'


app = Flask(__name__)
api = Api(app)

class hazard_classificator(Resource):
    def post(self):
        return 'HI DUDU'
    def get(self):
        return 'HELLO ben '

    def put(self):
        data = json.loads(request.get_json())
        # print(data)
        # print(type(data))
        # data_j = json.loads(data)
        # print(type(data_j))
        if data['hazard_type'] == None:
            return 'OK'
        else:
            return 'off'
        print(data['gps_x'],data['gps_y'])
        return 


api.add_resource(hazard_classificator, '/')

if __name__ == '__main__':
    app.run(host = URL,port=PORT,debug=True)


#TODO:
    '''
    1. get data
    2. clasify for the correct service provider and the eurgency
    3. server sends request to closest client
    4. DB gets a new line with the name of the client that should do the thing and has status unknown
    '''
