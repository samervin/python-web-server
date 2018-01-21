import markdown

# Meta extension used for metadata on markdown files
md = markdown.Markdown(extensions=['markdown.extensions.meta'])


def get_site_header():
    with open('site_pages\header.md') as header:
        content = header.read()
        return md_to_html(content)

def md_to_html(md_content: str):
    return md.convert(md_content)
