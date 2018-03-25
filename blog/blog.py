import os
from meta import site_utilities
from collections import namedtuple

Post = namedtuple('Post', ['filename', 'url_slug', 'markdown', 'html', 'datetime', 'title'])


def get_blog_post_html(post_name):
    with open('blog/posts/{}.md'.format(post_name)) as post_file:
        post_md = post_file.read()
    post_html = site_utilities.md_with_metadata_to_html(post_md)
    post_title = post_html.metadata.get('title')
    browser_title_html = '<title>{}</title>'.format(post_title)
    blog_title_html = site_utilities.md_to_html('### {}'.format(post_title))
    footer_md = _get_blog_post_footer_markdown(post_name)
    footer_html = site_utilities.md_to_html(footer_md)
    header = _get_blog_header_html()
    return header + browser_title_html + blog_title_html + post_html + footer_html


def _get_blog_header_html():
    with open('blog/blog_header.md') as blog_header:
        content = blog_header.read()
    return site_utilities.md_to_html(content)


def get_blog_home_html():
    with open('blog/blog_home.md') as blog_home:
        blog_opener = blog_home.read()
    post_list = _get_blog_posts_list()
    post_list.reverse()
    post_list_str = ''
    for post in post_list:
        post_list_str += '\n- [{}]({})'.format(post.title, post.url_slug)
    header = _get_blog_header_html()
    content = site_utilities.md_to_html(blog_opener + post_list_str)
    return header + content


def _get_blog_posts_list():
    post_list = []
    for _, _, files in os.walk('blog/posts'):
        for filename in files:
            with open('blog/posts/{}'.format(filename)) as post_file:
                post_md = post_file.read()
            post_html = site_utilities.md_with_metadata_to_html(post_md)
            post_datetime = post_html.metadata.get('datetime')
            post_title = post_html.metadata.get('title')
            url_slug = filename.replace('.md', '')
            post_list.append(Post(filename, url_slug, post_md, post_html, post_datetime, post_title))
    post_list = sorted(post_list, key=lambda p: p.datetime)
    return post_list


def _get_blog_post_footer_markdown(post_name):
    with open('blog/blog_post_footer.md') as footer_file:
        footer_md = footer_file.read()
    post_list = _get_blog_posts_list()

    for index, post in enumerate(post_list):
        if post.url_slug == post_name:
            break

    previous_post_link = '←'
    next_post_link = '→'
    if index > 0:
        previous_post = post_list[index - 1]
        previous_post_link = '[← {}]({})'.format(previous_post.title, previous_post.url_slug)
    if index < len(post_list) - 1:
        next_post = post_list[index + 1]
        next_post_link = '[{} →]({})'.format(next_post.title, next_post.url_slug)
    footer_md = footer_md.replace('{previous-post-link}', previous_post_link)
    footer_md = footer_md.replace('{next-post-link}', next_post_link)
    return footer_md
