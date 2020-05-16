
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
    kwargs = {}
    if request.method == 'POST':
        if request.form.get("location", None):
            kwargs["location"] = request.form['location']

        if request.form.get("media_mode", None):
            kwargs["media_mode"] = request.form['media_mode']

        if request.form.get("archive_mode", None):
            kwargs["archive_mode"] = request.form['archive_mode']

    # otsession = opentok.create_session(location='12.34.56.78', media_mode=MediaModes.routed, archive_mode=ArchiveModes.always)
    otsession = opentok.create_session(**kwargs)

    session_id = otsession.session_id

    return "Request_id is: " + session_id


@app.route('/token/<session_id>')
def token(session_id):
    error = None

    return opentok.generate_token(session_id)
