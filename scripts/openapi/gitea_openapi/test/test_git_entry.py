# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.git_entry import GitEntry

class TestGitEntry(unittest.TestCase):
    """GitEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GitEntry:
        """Test GitEntry
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GitEntry`
        """
        model = GitEntry()
        if include_optional:
            return GitEntry(
                mode = '',
                path = '',
                sha = '',
                size = 56,
                type = '',
                url = ''
            )
        else:
            return GitEntry(
        )
        """

    def testGitEntry(self):
        """Test GitEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
