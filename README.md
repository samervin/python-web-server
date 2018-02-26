# python-web-server

A personal web server, written in Python.

To start the server locally ([ref](http://flask.pocoo.org/docs/0.12/quickstart/)):

- Install Python 3. I'm using Python 3.6 locally.
- `python -m venv venv`
- `venv\Scripts\activate` on Windows
    - `source venv/bin/activate` on Unix
- `pip install -r requirements.txt`
- `set FLASK_APP=server.py` on Windows
    - `export FLASK_APP=server.py` on Unix
- `set FLASK_DEBUG=1` on Windows to enable live reloading and verbose debugging
    - `export FLASK_DEBUG=1` on Unix
- `flask run`
- Open either `localhost:5000` or `127.0.0.1:5000` to browse and generate logs

---

## AWS set up

Note: these directions are not complete and are specific to my requirements. Follow at your own risk.

To set up an EC2 instance:

- Click "Launch Instance" in the EC2 console.
- Choose your favorite Linux flavor. I've chosen one of the Amazon Linux AMIs (eligible for free tier usage).
- Choose an instance type. `t2.micro` is eligible for free tier usage.
- Double-check the instance details; the defaults are probably OK.
- Confirm the storage settings; again, the default of an 8 GB root SSD is probably fine.
- If you haven't created a security group, create one now.
    - Allow SSH access from your IP.
    - Allow HTTP access from your IP. (You'll change this later.)
    - For convenience, you can also allow port 5000 (Flask's default dev port) from your IP.
- If you don't have a key pair, create one now.
    - Save the `.pem` file in a safe location. This repository's `.gitignore` will ignore `ssh-key.pem` if you want to keep it in the same place.

To set up DNS using Route53:

- Register a domain. I've registered samerv.in for personal use.
- Created a Hosted Zone in Route53 for your domain.
- AWS should populate the NS and SOA record sets.
    - Make sure the values of NS match the list of Name servers in your registered domain!
- Copy the public IPv4 address from the EC2 console for the instance you launched earlier.
- Create a new record set.
    - Leave name blank.
    - Type `A`.
    - Paste the IP address into the Value field.
- Test by accessing the domain name (samerv.in in my case). You should see "refused to connect" (and not any other DNS errors).
    - Remember DNS changes can take minutes to propogate, and name server changes can take hours.
- Side note: you can choose to add a CNAME for www.(your domain) with a value of (your domain) as well.

To set up the Python web server on the EC2 instance ([ref](http://exploreflask.com/en/latest/deployment.html)):

- SSH on to the instance, using your `.pem` file and the public DNS of the instance.
    - `ssh -i <key-pair>.pem ec2-user@<public-dns>`
- `sudo yum install python36 git` (or your preferred package manager + Python version)
- `git clone https://github.com/samervin/python-web-server`
- `cd python-web-server`
- `python3 -m venv venv`
    - If this throws an error, try `python3 -m venv venv --without-pip` ([ref](https://stackoverflow.com/questions/26215790/venv-doesnt-create-activate-script-python3))
- `source venv/bin/activate`
    - If venv threw an error above, run `curl https://bootstrap.pypa.io/get-pip.py | python3`
- `pip3 install -r requirements.txt`
- `gunicorn --bind 0.0.0.0:5000 server:server`
    - You can add `-D` to run as a daemon and `-p server.pid` to save the process ID to a file.

To set up Nginx:

- `sudo yum install nginx`
- Copy and paste the relevant parts of `nginx.conf` into `/etc/nginx/nginx.conf`
- `sudo service nginx reload`
- Now, instead of the previous gunicorn command, run `gunicorn --bind 127.0.0.1:8000 server:server -D -p server.pid`

To update the site after pushing to `master`:

- SSH on to the instance.
- `cd python-web-server`
- `git pull`. That's it!
