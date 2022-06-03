from pickle import APPEND
from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
from flask_sqlalchemy_report import Reporter



PORT = 5001
URL ='192.168.91.178'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
api = Api(app)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, nullable=False)
    time_posted = db.Column(db.String(40), nullable=False)
    location_X = db.Column(db.Float,nullable = False)
    location_Y = db.Column(db.Float,nullable = False)
    status = db.Column(db.Boolean,unique=False,nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.time_posted}')"


class hazard_classificator(Resource):
    def post(self):
        return 'HI DUDU'
    def get(self):
        return 'HELLO ben '

    def put(self):
        usernames = []
        data = json.loads(request.get_json())
        users = list(User.query.all())
        for u in users:
            usernames.append(u.username)

        if data['user'] not in usernames:
            tmp_usr = User(username = data['user'])
            db.session.add(tmp_usr)
            db.session.commit()

        if data['hazard_type'] == None:
            return 'No Hazard'
        else:
            tmp_post = Post(title = data['hazard_type'],
                            time_posted = str(datetime.utcnow()),
                            location_X = data['gps_x'],
                            location_Y = data['gps_y'],
                            status = data['taken_by_me'],
                            user_id = User.query.filter_by(username = data['user']).first().id)
            db.session.add(tmp_post)
            db.session.commit()
            print(f"hazard added{data['hazard_type']}")
            return 'Hazard added'


api.add_resource(hazard_classificator, '/')

@app.route('/summary') 
def index():
    rows = User.query.all()
    return render_template('main_summary.html',
                            title='Overview',
                            rows=rows)

@app.route('/car1') 
def new_index():
    rows = Post.query.filter_by(user_id=12).all()
    hazards = ['Garbage','Prune','Garbage Bag','Small Trash','Furneture']
    return render_template('car_summary.html',
                            title='Overview',
                            rows=rows,
                            hazards = hazards)
if __name__ == '__main__':
    app.run(host = URL,port=PORT,debug=True)


