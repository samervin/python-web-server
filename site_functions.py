import markdown

# Meta extension used for metadata on markdown files
md = markdown.Markdown(extensions=['markdown.extensions.meta'])


def get_header():
    # TODO: don't hardcode a path
    with open('site_pages\header.md') as header:
        content = header.read()
        return md.convert(content)
