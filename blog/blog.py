import os

def get_blog_header_markdown():
    with open('blog/blog_header.md') as blog_header:
        return blog_header.read()

def get_blog_home_markdown():
    with open('blog/blog_home.md') as blog_home:
        blog_opener = blog_home.read()
    post_list = ''
    for root, directories, files in os.walk('blog/posts'):
        for filename in files:
            no_extension = filename.replace('.md', '')  # Remove .md extension
            post_list += '\n- [{}]({})'.format(no_extension, no_extension)
    return blog_opener + post_list

def get_blog_post_markdown(post_name):
    with open('blog/posts/{}.md'.format(post_name)) as post:
        return post.read()
