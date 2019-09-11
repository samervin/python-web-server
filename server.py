import flask
import meta
from meta import site_utilities
from home import home
from blog import blog
from resume import resume

server = flask.Flask(__name__)
# Signal that static files like favicon.ico can be cached for 1 week
server.config["SEND_FILE_MAX_AGE_DEFAULT"] = 604800

# Note on routes:
# use /path/ for folders, places in the hierarchy with children
# use /path for files or other terminating hierarchies


@server.route("/")
def route_home():
    home_content = home.get_home_html()
    home_page = _create_html_page(home_content)
    return home_page


@server.route("/blog/")
def route_blog():
    blog_home = blog.get_blog_home_html()
    blog_page = _create_html_page(blog_home)
    return blog_page


@server.route("/blog/<post_name>")
def route_blog_post(post_name):
    try:
        blog_post = blog.get_blog_post_html(post_name)
        blog_post_page = _create_html_page(blog_post)
        return blog_post_page
    except FileNotFoundError as e:
        return error_404(e)


@server.route("/resume")
def route_resume():
    resume_html = resume.get_resume_html()
    resume_page = _create_html_page(resume_html)
    return resume_page


@server.route("/favicon.ico")
def route_favicon():
    return flask.send_from_directory(meta.__name__, "favicon.ico")


@server.errorhandler(404)
def error_404(e):
    with open("meta/404.md") as file_404:
        md_404 = file_404.read()
    html_404 = site_utilities.md_to_html(md_404)
    return _create_html_page(html_404), 404


@server.errorhandler(500)
def error_500(e):
    with open("meta/500.md") as file_500:
        md_500 = file_500.read()
    html_500 = site_utilities.md_to_html(md_500)
    return _create_html_page(html_500), 500


# Block of error server routes for testing
@server.route("/200")
def route_200():
    return _create_html_page("200 OK"), 200


@server.route("/400")
def route_400():
    return _create_html_page("400 Bad Request"), 400


@server.route("/404")
def route_404():
    return _create_html_page("404 Not Found"), 404


@server.route("/418")
def route_418():
    return _create_html_page("418 I'm a teapot"), 418


@server.route("/420")
def route_420():
    return _create_html_page("420 Enhance Your Calm"), 420


@server.route("/500")
def route_500():
    return _create_html_page("500 Internal Server Error"), 500


@server.route("/503")
def route_503():
    return _create_html_page("503 Service Unavailable"), 503


def _create_html_page(*contents):
    css_header = site_utilities.get_site_css_header()
    site_header = site_utilities.get_site_html_header()
    site_footer = site_utilities.get_site_html_footer()
    page = css_header + site_header
    for content in contents:
        page += content
    page += site_footer
    return page


if __name__ == "__main__":
    server.run()
