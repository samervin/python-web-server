import os
import site_functions
from collections import namedtuple

Post = namedtuple('Post', ['filename', 'title', 'markdown', 'html', 'datetime'])

def get_blog_header_markdown():
    with open('blog/blog_header.md') as blog_header:
        return blog_header.read()

def get_blog_home_markdown():
    with open('blog/blog_home.md') as blog_home:
        blog_opener = blog_home.read()

    post_list = []
    for root, directories, files in os.walk('blog/posts'):
        for filename in files:
            title = filename.replace('.md', '')
            with open('blog/posts/{}'.format(filename)) as post_file:
                post_md = post_file.read()
            post_html = site_functions.md_to_html(post_md)
            post_datetime = post_html.metadata.get('datetime')
            post_list.append(Post(filename, title, post_md, post_html, post_datetime))
    
    post_list = sorted(post_list, key=lambda p: p.datetime)
    post_list_str = ''
    for post in post_list:
        post_list_str += '\n- [{}]({})'.format(post.title, post.title)
    return post_list_str


def get_blog_post_markdown(post_name):
    with open('blog/posts/{}.md'.format(post_name)) as post:
        return post.read()
