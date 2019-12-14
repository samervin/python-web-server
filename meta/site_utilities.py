import csscompressor
import markdown2

# Extensions:
#
# 'metadata' allows for metadata definitions in Markdown files,
# however it can cause issues with parsing certain kinds of content and so is used only when necessary
#
# 'markdown-in-html' allows mixing of HTML and Markdown using markdown="1"
#
# 'tables' allows tables to be defined as in this example:
# header 1     | header 2 | header 3
# :----------- | :------: | -------:
# left-aligned | centered | right-aligned
#
# 'strike' allows strikethrough text like so: ~~strikethrough~~
#
# 'fenced-code-blocks` allows for unformatted text/code inside of ```triple backticks```

md = markdown2.Markdown(
    extras=["markdown-in-html", "tables", "strike", "fenced-code-blocks"]
)
md_with_metadata = markdown2.Markdown(
    extras=["metadata", "markdown-in-html", "tables", "strike", "fenced-code-blocks"]
)


def md_to_html(md_content: str, md_extras=None):
    return md.convert(md_content)


def md_with_metadata_to_html(md_content: str):
    return md_with_metadata.convert(md_content)


def get_site_html_header():
    with open("meta/site-header.md") as header:
        content = header.read()
    return md_to_html(content)


def get_site_html_footer():
    with open("meta/site-footer.md") as footer:
        content = footer.read()
    return md_to_html(content)


def get_site_css_header():
    with open("meta/site.css") as css_file:
        css_content = css_file.read()
    css_content = csscompressor.compress(css_content)
    css_header = "<head><style>{}</style></head>".format(css_content)
    return css_header
