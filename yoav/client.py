import requests
import time
import numpy as np
import json



URL = '10.176.94.15'
SERVER = f'http://{URL}:5001'

def gps_mock():
    return int(np.random.randint(0,100)),int(np.random.randint(0,100))

HAZARDS = {'1':'trash', '2':'leafs','3':'pothole'}

class car():
    def __init__(self,name='car_name'):
        self.status = False
        self.name = name
        self.gps_x,self.gps_y = gps_mock()
        self.req = {"user": self.name, "gps_x":self.gps_x,"gps_y":self.gps_y , "hazard_type": None, "taken_by_me": None}
        self.i = 0
    def start(self):
        self.status = True
    
    def stream(self):
        time.sleep(1)
        if self.i == 4:
            self.req["hazard_type"] = 1
            self.req["user"]='Ben'
        if self.i == 3:
            self.req["hazard_type"] = 3
            self.req['user'] = 'Yoav'
        if self.i == 2:
            self.req["hazard_type"] = 2
            self.req['user'] = 'Netanel'
        if self.i == 1:
            self.req["hazard_type"] = 2
            self.req['user'] = 'DUDI'
        response = requests.put(url=SERVER,json=json.dumps(self.req))
        print(response.json())
        self.i +=1
        # if response.json() == 'Hazard added':
        #     self.status = False


if __name__ == "__main__":
    p = car(name = 'yoav')
    p.start()

    while p.status:
        p.stream()
