def get_home_header_markdown():
    with open('home/home_header.md') as home_header:
        return home_header.read()

def get_home_markdown():
    with open('home/home.md') as home:
        return home.read()
