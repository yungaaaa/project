from flask import Flask, render_template, Response
import argparse
from flask import url_for
from flask import request

ap = argparse.ArgumentParser()
ap.add_argument("-d","--data", required = True,
    help = "Data to send")
args = vars(ap.parse_args())
data=args['data']

app = Flask(__name__)


@app.route('/')
def index():
    return data


	

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['GET','POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
	
if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
