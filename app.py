
from opentok import OpenTok, MediaModes, ArchiveModes
from flask import Flask, request
app = Flask(__name__)
app.config.from_pyfile('.env')

opentok = OpenTok(app.config.get('OPENTOK_API_KEY'), app.config.get('OPENTOK_API_SECRET'))


@app.route('/')
def index():
    return "Success! Endpoints available: /session."


@app.route('/session', methods=['POST'])
def session():
    error = None
    args_dict = {}
    if request.method == 'POST':
        if request.form.get("location", None):
            args_dict["location"] = "u'" + request.form['location'] + "'"

        if request.form.get("media_mode", None):
            args_dict["media_mode"] = request.form['media_mode']

        if request.form.get("archive_mode", None):
            args_dict["archive_mode"] = request.form['archive_mode']

        if args_dict:
            args = {', '.join(args_dict)}

    otsession = opentok.create_session(**args)

    session_id = otsession.session_id

    return "Request_id is: " + session_id


@app.route('/token/<session_id>')
def token(session_id):
    error = None

    return opentok.generate_token(session_id)
