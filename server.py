import flask
import meta
from meta import site_utilities
from home import home
from blog import blog

server = flask.Flask(__name__)


@server.route('/')
def route_home():
    home_header = site_utilities.md_to_html(home.get_home_header_markdown())
    body = site_utilities.md_to_html(home.get_home_markdown())
    home_page = _create_html_page(home_header, body)
    return home_page

# Brief note on routes: /route/ should be used for "folders", /route should be used for "files"
@server.route('/blog/')
def route_blog():
    blog_header = site_utilities.md_to_html(blog.get_blog_header_markdown())
    blog_home = site_utilities.md_to_html(blog.get_blog_home_markdown())
    blog_page = _create_html_page(blog_header, blog_home)
    return blog_page

@server.route('/blog/<post_name>')
def route_blog_post(post_name):
    blog_header = site_utilities.md_to_html(blog.get_blog_header_markdown())
    blog_post = blog.get_blog_post_html(post_name)
    blog_post_page = _create_html_page(blog_header, blog_post)
    return blog_post_page

@server.route('/favicon.ico')
def route_favicon():
    return flask.send_from_directory(meta.__name__, 'favicon.ico')

def _create_html_page(*contents):
    css_header = site_utilities.get_site_css_header()
    site_header = site_utilities.get_site_html_header()
    page = css_header + site_header
    for content in contents:
        page += content
    return page


if __name__ == '__main__':
    server.run()
