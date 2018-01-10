from flask import Flask
import site_functions

server = Flask(__name__)


@server.route('/')
def root():
    # TODO: make this logic generic
    header = site_functions.get_header()
    return header + 'root'


# Brief note on routes: /route/ should be used for "folders", /route should be used for "files"
@server.route('/blog/')
def blog():
    return 'blog'


@server.route('/podcast/')
def podcast():
    return 'podcast'


@server.route('/reading-list/')
def reading_list():
    return 'reading list'


@server.route('/resume')
def resume():
    return 'resume'


if __name__ == '__main__':
    server.run()
