def get_blog_header_markdown():
    with open('blog/blog_header.md') as blog_header:
        return blog_header.read()

def get_blog_home_markdown():
    with open('blog/blog_home.md') as blog_home:
        return blog_home.read()
