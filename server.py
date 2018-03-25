import flask
import meta
from meta import site_utilities
from home import home
from blog import blog

server = flask.Flask(__name__)
# Note on routes:
# use /path/ for folders, places in the hierarchy with children
# use /path for files or other terminating hierarchies

@server.route('/')
def route_home():
    home_content = home.get_home_html()
    home_page = _create_html_page(home_content)
    return home_page

@server.route('/blog/')
def route_blog():
    blog_home = blog.get_blog_home_html()
    blog_page = _create_html_page(blog_home)
    return blog_page

@server.route('/blog/<post_name>')
def route_blog_post(post_name):
    blog_post = blog.get_blog_post_html(post_name)
    blog_post_page = _create_html_page(blog_post)
    return blog_post_page

@server.route('/favicon.ico')
def route_favicon():
    return flask.send_from_directory(meta.__name__, 'favicon.ico')

def _create_html_page(*contents):
    css_header = site_utilities.get_site_css_header()
    site_header = site_utilities.get_site_html_header()
    site_footer = site_utilities.get_site_html_footer()
    page = css_header + site_header
    for content in contents:
        page += content
    page += site_footer
    return page


if __name__ == '__main__':
    server.run()
