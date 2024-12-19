# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.content_tree_entries_inner_links import ContentTreeEntriesInnerLinks

class TestContentTreeEntriesInnerLinks(unittest.TestCase):
    """ContentTreeEntriesInnerLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentTreeEntriesInnerLinks:
        """Test ContentTreeEntriesInnerLinks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentTreeEntriesInnerLinks`
        """
        model = ContentTreeEntriesInnerLinks()
        if include_optional:
            return ContentTreeEntriesInnerLinks(
                git = '',
                html = '',
                var_self = ''
            )
        else:
            return ContentTreeEntriesInnerLinks(
                git = '',
                html = '',
                var_self = '',
        )
        """

    def testContentTreeEntriesInnerLinks(self):
        """Test ContentTreeEntriesInnerLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
