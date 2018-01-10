# python-web-server

A personal web server, written in Python.

To start the server:

- Install Python 3 (personally using Python 3.6)
- `python -m venv venv`
- `venv\Scripts\activate` on Windows or `. venv/bin/activate` on Unix
- `pip install -r requirements.txt`
- `set FLASK_APP=server.py` on Windows or `export FLASK_APP=server.py` on Unix
- `flask run`
- Open either `localhost:5000` or `127.0.0.1:5000` to browse and generate logs

To enable debug mode, which enables live reloading and more debugging help:

- `set FLASK_DEBUG=1` on Windows or `export FLASK_DEBUG=1` on Unix
