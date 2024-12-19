# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.content_symlink import ContentSymlink

class TestContentSymlink(unittest.TestCase):
    """ContentSymlink unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentSymlink:
        """Test ContentSymlink
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentSymlink`
        """
        model = ContentSymlink()
        if include_optional:
            return ContentSymlink(
                type = 'symlink',
                target = '',
                size = 56,
                name = '',
                path = '',
                sha = '',
                url = '',
                git_url = '',
                html_url = '',
                download_url = '',
                links = github_openapi.models.content_tree_entries_inner__links.content_tree_entries_inner__links(
                    git = '', 
                    html = '', 
                    self = '', )
            )
        else:
            return ContentSymlink(
                type = 'symlink',
                target = '',
                size = 56,
                name = '',
                path = '',
                sha = '',
                url = '',
                git_url = '',
                html_url = '',
                download_url = '',
                links = github_openapi.models.content_tree_entries_inner__links.content_tree_entries_inner__links(
                    git = '', 
                    html = '', 
                    self = '', ),
        )
        """

    def testContentSymlink(self):
        """Test ContentSymlink"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()