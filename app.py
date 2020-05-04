
from opentok import OpenTok
from flask import Flask, request
app = Flask(__name__)
app.config.from_pyfile('.env')

opentok = OpenTok(app.config.get('OPENTOK_API_KEY'), app.config.get('OPENTOK_API_SECRET'))


@app.route('/')
def index():
    return "Success! Endpoints available: /session."


@app.route('/session', methods=['POST'])
def session():
    # return "Success! Endpoints available: /session."
    error = None
    args = []
    if request.method == 'POST':
        if request.form['location']:
            args.append("location=u'" + request.form['location'] + "'")

        if request.form['media_mode']:
            args.append("media_mode=" + request.form['media_mode'])

        if request.form['archive_mode']:
            args.append("archive_mode=" + request.form['archive_mode'])

    otsession = opentok.create_session(','.join(args))
    session_id = otsession.session_id

    return "Request_id is: " + session_id


@app.route('/token/<session_id>')
def token(session_id):
    error = None

    return opentok.generate_token(session_id)
