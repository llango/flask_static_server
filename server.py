from flask import Flask
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root='docs/')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)
