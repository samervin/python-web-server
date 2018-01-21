def get_podcast_header_markdown():
    with open('podcast/podcast_header.md') as blog_header:
        return blog_header.read()
