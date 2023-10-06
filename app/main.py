from flask import Flask, request, jsonify
import redis
import psycopg2

app = Flask(__name__)
cache = redis.Redis(host='cache', port=6379)
conn = psycopg2.connect(database="mydatabase", user="user", password="password", host="database", port="5432")

@app.route('/')
def hello():
    cache.incr('hits')
    return 'Hello from Flask! This page has been viewed %s times.' % cache.get('hits').decode('utf-8')

@app.route('/data', methods=['POST'])
def add_data():
    data = request.json.get('data')
    cur = conn.cursor()
    cur.execute("INSERT INTO data (info) VALUES (%s)", (data,))
    conn.commit()
    return jsonify({"message": "Data added successfully!"})

@app.route('/data', methods=['GET'])
def get_data():
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    results = cur.fetchall()
    return jsonify({"data": results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9800)
