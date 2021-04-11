from bottle import Bottle, run, template, request
import http
import json
import urllib

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/')
@app.route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

@app.route('/')
def load_start_page():
    people = load_people()
    venues = load_venues()
    return template('start', people=people, venues=venues)

@app.route("/add_venue", "GET")
def load_add_venue_page():
    return template('add_venue')

@app.route("/add_venue", method="POST")
def add_venue():
    name = request.forms.get("name")
    website = request.forms.get("website")
    print(f"name={name} website={website}")
    put_venue(name, website)

def load_people():
    conn = http.client.HTTPConnection("192.168.3.6:8081")
    conn.request(method="GET", url="/v1/people")
    resp = conn.getresponse()
    data = resp.read()
    people = json.loads(data)
    conn.close()
    return people

def load_venues():
    conn = http.client.HTTPConnection("192.168.3.6:8081")
    conn.request(method="GET", url="/v1/venues")
    resp = conn.getresponse()
    data = resp.read()
    venues = json.loads(data)
    conn.close()
    return venues

def put_venue(name, website):
    conn = http.client.HTTPConnection("192.168.3.6:8081")
    conn.request(
        method="POST", 
        url="/v1/addVenue", 
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        body=urllib.parse.urlencode({"name": name, "website": website}),
    )
    resp = conn.getresponse()
    print(f"status: {resp.status}")
    conn.close()

run(app, host='0.0.0.0', port=8080)
