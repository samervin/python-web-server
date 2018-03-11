import flask
import site_functions
from home import home
from blog import blog
from podcast import podcast

server = flask.Flask(__name__)


@server.route('/')
def route_home():
    css_header = '<head><style>{}</style></head>'.format(site_functions.get_site_css())
    site_header = site_functions.get_site_header()
    home_header = site_functions.md_to_html(home.get_home_header_markdown())
    body = site_functions.md_to_html(home.get_home_markdown())
    return css_header + site_header + home_header + body


# Brief note on routes: /route/ should be used for "folders", /route should be used for "files"
@server.route('/blog/')
def route_blog():
    css_header = '<head><style>{}</style></head>'.format(site_functions.get_site_css())
    site_header = site_functions.get_site_header()
    blog_header = site_functions.md_to_html(blog.get_blog_header_markdown())
    blog_home = site_functions.md_to_html(blog.get_blog_home_markdown())
    return css_header + site_header + blog_header + blog_home

@server.route('/blog/<post_name>')
def route_blog_post(post_name):
    css_header = '<head><style>{}</style></head>'.format(site_functions.get_site_css())
    site_header = site_functions.get_site_header()
    blog_header = site_functions.md_to_html(blog.get_blog_header_markdown())
    blog_post = blog.get_blog_post_html(post_name)
    return css_header + site_header + blog_header + blog_post


@server.route('/podcast/')
def route_podcast():
    css_header = '<head><style>{}</style></head>'.format(site_functions.get_site_css())
    site_header = site_functions.get_site_header()
    podcast_header = site_functions.md_to_html(podcast.get_podcast_header_markdown())
    return css_header + site_header + podcast_header + 'podcast home'


@server.route('/reading-list/')
def route_reading_list():
    css_header = '<head><style>{}</style></head>'.format(site_functions.get_site_css())
    site_header = site_functions.get_site_header()
    return css_header + site_header + 'reading list home'


@server.route('/resume')
def route_resume():
    css_header = '<head><style>{}</style></head>'.format(site_functions.get_site_css())
    site_header = site_functions.get_site_header()
    return css_header + site_header + 'resume'


@server.route('/favicon.ico')
def route_favicon():
    return flask.send_from_directory(server.home_path, 'favicon.ico')


if __name__ == '__main__':
    server.run()
