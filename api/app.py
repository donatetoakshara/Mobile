from flask import Flask

app = flask.Flask(__name__)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)
app.register_blueprint(google_auth.app)
app.register_blueprint(users.app)



if __name__== '__main__' :
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)