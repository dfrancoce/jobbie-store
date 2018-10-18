import json

from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'jobbie-store'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/jobbie-store'

mongo = PyMongo(app)

@app.route('/jobs', methods=['POST'])
def jobs():
    jobs_json = request.json
    data = json.loads(jobs_json)
    jobs = mongo.db.jobs
    jobs.insert_one(data)
    
    return Response(None, 201)

if __name__ == '__main__':
    app.run(debug=True)