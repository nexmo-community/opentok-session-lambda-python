# opentok-session-lambda-python
A Flask based Python Lambda function to provide OpenTok session upon request.

## Prerequisites
* Python 3.7 (update `serverless.yml` if higher version is desired)
* Pip
* [Node.js](https://nodejs.org/en/) and npm
* [Serverless Framework](https://serverless.com/framework/docs/getting-started/)

## Setup Instructions
Clone this repo from GitHub, and navigate into the newly created directory to proceed.

### Environment
Rename `.env.default` to `.env` and add values to `OPENTOK_API_KEY` and `OPENTOK_API_SECRET` provided by your Vonage Video APIs account.

### Usage
To start, create a virtualenv from within the project root to contain the project as you proceed. Then activate it as follows:

```bash
virtualenv venv --python=python3
source venv/bin/activate
```

Next, initialize npm and follow the prompts selecting the defaults. Unless you desire to change any of them. Also, use npm to install needed dependencies for dev to enable Serverless and Lambda to work with the Flask app.

```bash
npm init
npm install --save-dev serverless-wsgi serverless-python-requirements
```

Now you can use pip to install the required Python dependencies. The dependencies are already listed in the requirements.txt, so instruct pip to use it.

```bash
pip install -r requirements.txt
```

#### Running Local
You can run the app locally and test things out, prior to deploying to AWS Lambda, you can serve it with the following command:

```bash
sls wsgi serve
```

By default this will serve the app at http://localhost:5000. Hitting `Ctrl+c` will close it down.

#### Deploy to Lambda
With all the above finished successfully, you can now use Serverless to deploy the app to AWS Lambda.

```bash
sls deploy
```

#### Available Endpoints
There are 4 URL endpoints available with this client:

* GET request to `/`
    - Doesn't perform any actions, but provides a quick way to test

* POST request to `/session`
    - This will provide the session ID.
    - By passing a form POST like the following, you can change default parameters used to create a session: (defaults shown, if you leave the body empty.)
    
```text
location=None, media_mode=MediaModes.relayed, archive_mode=ArchiveModes.manual
```

NOTE: Location expects an IP address.

* `/token/<session_id>`
    - You can then request a new session by passing the `<session_id>` to the `/token` endpoint.

##### Examples:
Go to the URL provided by the deploy process. Below are some examples of what sample requests may look like:

GET `https://7ulasfasdasdfw4.execute-api.us-east-1.amazonaws.com/dev/`

The `/` endpoint returns the generic message.

POST `https://7ulasfasdasdfw4.execute-api.us-east-1.amazonaws.com/dev/session`

The `session` endpoint will return the `session_id` needed to request a token.

GET `https://7ulasfasdasdfw4.execute-api.us-east-1.amazonaws.com/dev/token/9807adsf0sae89fu0se87r0sf`

The `token` endpoing will return the `token` needed to interact with OpenTok.

#### Deactivating Virtualenv
To exit the virtualenv you can deactivate it, when desired.

```bash
deactivate
```

NOTE: Depending on OS, you may need to prepend `virtualenv` to the command above.

## Contributing

We love questions, comments, issues - and especially pull requests. Either open an issue to talk to us, or reach us on twitter: <https://twitter.com/VonageDev>.
