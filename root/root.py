def get_root_header_markdown():
    with open('root/root_header.md') as root_header:
        return root_header.read()

def get_root_markdown():
    with open('root/root.md') as root:
        return root.read()
