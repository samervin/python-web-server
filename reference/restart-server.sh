# Restarts the server according to the set up directions in the README.
# Copy this file to the home directory of your server.
cd python-web-server/
source venv/bin/activate
git pull
kill `cat server.pid`
gunicorn --bind 127.0.0.1:8000 server:server -D -p server.pid
