from flask import Flask
import site_functions
from root import root
from blog import blog

server = Flask(__name__)


@server.route('/')
def route_root():
    site_header = site_functions.get_site_header()
    root_header = site_functions.md_to_html(root.get_root_header_markdown())
    body = site_functions.md_to_html(root.get_root_markdown())
    return site_header + root_header + body


# Brief note on routes: /route/ should be used for "folders", /route should be used for "files"
@server.route('/blog/')
def route_blog():
    site_header = site_functions.get_site_header()
    blog_header = site_functions.md_to_html(blog.get_blog_header_markdown())
    blog_home = site_functions.md_to_html(blog.get_blog_home_markdown())
    return site_header + blog_header + blog_home

@server.route('/blog/<post_name>')
def route_blog_post(post_name):
    site_header = site_functions.get_site_header()
    blog_header = site_functions.md_to_html(blog.get_blog_header_markdown())
    blog_post = site_functions.md_to_html(blog.get_blog_post_html(post_name))
    return site_header + blog_header + blog_post


@server.route('/podcast/')
def route_podcast():
    return 'podcast'


@server.route('/reading-list/')
def route_reading_list():
    return 'reading list'


@server.route('/resume')
def route_resume():
    return 'resume'


if __name__ == '__main__':
    server.run()
