from flask import Flask
import parser

app = Flask(__name__)

parser.pars()

if __name__ == "__main__":
    app.run()