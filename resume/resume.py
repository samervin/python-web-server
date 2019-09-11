from meta import site_utilities


def get_resume_html():
    with open("resume/resume.md") as resume:
        resume = resume.read()
    resume_html = site_utilities.md_to_html(resume)
    header_html = _get_resume_header_html()
    browser_title_html = "<title>resume | samerv.in</title>"
    return header_html + browser_title_html + resume_html


def _get_resume_header_html():
    with open("resume/resume_header.md") as resume_header:
        content = resume_header.read()
    return site_utilities.md_to_html(content)
