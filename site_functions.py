import markdown2

# Metadata extension allows for metadata definitions in Markdown files
md = markdown2.Markdown(extras=['metadata', 'markdown-in-html'])


def get_site_header():
    with open('site_pages\header.md') as header:
        content = header.read()
        return md_to_html(content)

def md_to_html(md_content: str):
    return md.convert(md_content)

def get_site_css():
    with open('site.css') as css_file:
        css_content = css_file.read()
        return css_content
