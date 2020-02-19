import os
from collections import namedtuple
from datetime import datetime as dt

from meta import site_utilities

Post = namedtuple(
    "Post", ["filename", "url_slug", "markdown", "html", "datetime", "title"]
)


def get_blog_post_html(post_name):
    with open("blog/posts/{}.md".format(post_name)) as post_file:
        post_md = post_file.read()
    post_html = site_utilities.md_with_metadata_to_html(post_md)
    post_title = post_html.metadata.get("title")
    raw_datetime = dt.strptime(post_html.metadata.get("datetime"), "%Y-%m-%d %H:%M")
    browser_title_html = "<title>{} | samerv.in</title>".format(post_title)
    blog_title_html = site_utilities.md_to_html("## {}".format(post_title))
    blog_date = raw_datetime.strftime("<i>%b %d %Y</i>")
    footer_html = _get_blog_post_footer_html(post_name)
    header = _get_blog_header_html()
    return (
        header
        + browser_title_html
        + blog_title_html
        + blog_date
        + post_html
        + footer_html
    )


def _get_blog_header_html():
    with open("blog/blog_header.md") as blog_header:
        content = blog_header.read()
    return site_utilities.md_to_html(content)


def get_blog_home_html():
    with open("blog/blog_home.md") as blog_home:
        blog_opener = blog_home.read()
    post_list = _get_blog_posts_list()
    post_list.reverse()
    post_list_str = ""
    for post in post_list:
        raw_datetime = dt.strptime(post.datetime, "%Y-%m-%d %H:%M")
        pretty_datetime = raw_datetime.strftime("<i>%b %d %Y</i>")
        post_list_str += "\n- [{}]({}) ({})".format(
            post.title, post.url_slug, pretty_datetime
        )
    header = _get_blog_header_html()
    browser_title_html = "<title>blog | samerv.in</title>"
    content = site_utilities.md_to_html(blog_opener + post_list_str)
    return header + browser_title_html + content


def _get_blog_posts_list():
    post_list = []
    for _, _, files in os.walk("blog/posts"):
        for filename in files:
            with open("blog/posts/{}".format(filename)) as post_file:
                post_md = post_file.read()
            post_html = site_utilities.md_with_metadata_to_html(post_md)
            post_datetime = post_html.metadata.get("datetime")
            post_title = post_html.metadata.get("title")
            url_slug = filename.replace(".md", "")
            post_list.append(
                Post(filename, url_slug, post_md, post_html, post_datetime, post_title)
            )
    post_list = sorted(post_list, key=lambda p: p.datetime)
    return post_list


def _get_blog_post_footer_html(post_name):
    with open("blog/blog_post_footer.html") as footer_file:
        footer_html = footer_file.read()
    post_list = _get_blog_posts_list()

    for index, post in enumerate(post_list):
        if post.url_slug == post_name:
            break

    previous_post_link = "←"
    next_post_link = "→"
    if index > 0:
        previous_post = post_list[index - 1]
        previous_post_link = '<a href="{}">← {}</a>'.format(
            previous_post.url_slug, previous_post.title
        )
    if index < len(post_list) - 1:
        next_post = post_list[index + 1]
        next_post_link = '<a href="{}">{} →</a>'.format(
            next_post.url_slug, next_post.title
        )
    footer_html = footer_html.replace("{previous-post-link}", previous_post_link)
    footer_html = footer_html.replace("{next-post-link}", next_post_link)
    return footer_html


def get_rss_feed():
    with open("blog/feed_template.xml") as feed_file:
        feed_template = feed_file.read()
    post_list = _get_blog_posts_list()
    post_list.reverse()
    item_format = (
        "<item><title>{}</title><link>{}</link>"
        "<description>{}</description><pubDate>{}</pubDate></item>"
    )
    all_items = ""
    for post in post_list:
        formatted_url = "https://samerv.in/blog/{}".format(post.url_slug)
        truncated_content = "\n".join(post.markdown.splitlines()[5:10])
        item = item_format.format(
            post.title, formatted_url, truncated_content, post.datetime
        )
        all_items += item
    feed_template = feed_template.replace("{item-list}", all_items)
    return feed_template
