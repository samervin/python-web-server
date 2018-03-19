import markdown2

# Markdown in HTML extension allows mixing of HTML and Markdown using markdown="1"
# Metadata extension allows for metadata definitions in Markdown files,
# however it can cause issues with parsing certain kinds of content and so is used only when necessary
md = markdown2.Markdown(extras=['markdown-in-html'])
md_with_metadata = markdown2.Markdown(extras=['metadata', 'markdown-in-html'])


def md_to_html(md_content: str, md_extras=None):
    return md.convert(md_content)

def md_with_metadata_to_html(md_content: str):
    return md_with_metadata.convert(md_content)

def get_site_html_header():
    with open('meta/site-header.md') as header:
        content = header.read()
        return md_to_html(content)

def get_site_html_footer():
    with open('meta/site-footer.md') as footer:
        content = footer.read()
        # import pdb; pdb.set_trace()
        print(md_to_html(content))
        return md_to_html(content)

def get_site_css_header():
    with open('meta/site.css') as css_file:
        css_content = css_file.read()
    css_header = '<head><style>{}</style></head>'.format(css_content)
    return css_header
