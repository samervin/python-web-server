# Restarts the server according to the set up directions in the README.
# Copy this file to the home directory of your server.
function echo_green {
    echo -e "\e[32m$1\e[0m"
}

cd python-web-server/
source venv/bin/activate

echo_green "Updating source from Git"
git pull

echo_green "Stopping server and installing packages"
kill `cat server.pid`
python -m pip install --upgrade pip
pip install -r requirements.txt

echo_green "Starting server"
gunicorn --bind 127.0.0.1:8000 server:server -D -p server.pid
