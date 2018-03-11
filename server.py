import flask
from meta import site_utilities
from home import home
from blog import blog

server = flask.Flask(__name__)


@server.route('/')
def route_home():
    css_header = '<head><style>{}</style></head>'.format(site_utilities.get_site_css())
    site_header = site_utilities.get_site_header()
    home_header = site_utilities.md_to_html(home.get_home_header_markdown())
    body = site_utilities.md_to_html(home.get_home_markdown())
    return css_header + site_header + home_header + body


# Brief note on routes: /route/ should be used for "folders", /route should be used for "files"
@server.route('/blog/')
def route_blog():
    css_header = '<head><style>{}</style></head>'.format(site_utilities.get_site_css())
    site_header = site_utilities.get_site_header()
    blog_header = site_utilities.md_to_html(blog.get_blog_header_markdown())
    blog_home = site_utilities.md_to_html(blog.get_blog_home_markdown())
    return css_header + site_header + blog_header + blog_home

@server.route('/blog/<post_name>')
def route_blog_post(post_name):
    css_header = '<head><style>{}</style></head>'.format(site_utilities.get_site_css())
    site_header = site_utilities.get_site_header()
    blog_header = site_utilities.md_to_html(blog.get_blog_header_markdown())
    blog_post = blog.get_blog_post_html(post_name)
    return css_header + site_header + blog_header + blog_post


@server.route('/favicon.ico')
def route_favicon():
    return flask.send_from_directory(meta.__name__, 'favicon.ico')


if __name__ == '__main__':
    server.run()
