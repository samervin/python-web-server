import unittest
import meta.site_utilities

class TestSiteUtilities(unittest.TestCase):

    def test_md_to_html(self):
        test_cases = [
            # Markdown input, expected HTML output
            ('text', '<p>text</p>\n'),
            ('- list\n- list', '<ul>\n<li>list</li>\n<li>list</li>\n</ul>\n')
        ]
        for test_case in test_cases:
            md = test_case[0]
            with self.subTest(md=md):
                output = meta.site_utilities.md_to_html(md)
                self.assertEqual(output, test_case[1])
    
    def test_md_with_metadata_to_html(self):
        test_cases = [
            # Markdown input, expected HTML output, expected key, expected value
            ('---\nkey: value\n---\ntext', '<p>text</p>\n', 'key', 'value')
        ]
        for test_case in test_cases:
            md = test_case[0]
            with self.subTest(md=md):
                output = meta.site_utilities.md_with_metadata_to_html(md)
                self.assertEqual(output, test_case[1])
                self.assertEqual(output.metadata[test_case[2]], test_case[3])
    
    def test_minify_css(self):
        test_cases = [
            # Raw CSS input, expected minified output
            ('p, ul {\n\tline-height: 1.3\n}', 'p,ul{line-height:1.3}')
        ]
        for test_case in test_cases:
            minified_css = meta.site_utilities._minify_css(test_case[0])
            self.assertEqual(minified_css, test_case[1])

if __name__ == '__main__':
    unittest.main()
