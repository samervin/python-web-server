import markdown2

# Metadata extension allows for metadata definitions in Markdown files
md = markdown2.Markdown(extras=['metadata', 'markdown-in-html'])


def md_to_html(md_content: str):
    return md.convert(md_content)

def get_site_html_header():
    with open('meta/site_header.md') as header:
        content = header.read()
        return md_to_html(content)

def get_site_css_header():
    with open('meta/site.css') as css_file:
        css_content = css_file.read()
    css_header = '<head><style>{}</style></head>'.format(css_content)
    return css_header
