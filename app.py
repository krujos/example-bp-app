#!/usr/bin/env python
from flask import Flask
import os

if 'PORT' in os.environ:
    port = int(os.getenv("PORT"))

app = Flask(__name__)

@app.route('/')
def root():
    with open ("hello.txt", "r") as myfile:
        data=myfile.read().replace('\n','')
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)
