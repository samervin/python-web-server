from meta import site_utilities


def get_home_html():
    with open('home/home.md') as home:
        home = home.read()
    home_html = site_utilities.md_to_html(home)
    header_html = _get_home_header_html()
    browser_title_html = '<title>samerv.in</title>'
    return header_html + browser_title_html + home_html


def _get_home_header_html():
    with open('home/home_header.md') as home_header:
        content = home_header.read()
    return site_utilities.md_to_html(content)
