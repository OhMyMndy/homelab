# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.git_tree_tree_inner import GitTreeTreeInner

class TestGitTreeTreeInner(unittest.TestCase):
    """GitTreeTreeInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GitTreeTreeInner:
        """Test GitTreeTreeInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GitTreeTreeInner`
        """
        model = GitTreeTreeInner()
        if include_optional:
            return GitTreeTreeInner(
                path = 'test/file.rb',
                mode = '040000',
                type = 'tree',
                sha = '23f6827669e43831def8a7ad935069c8bd418261',
                size = 12,
                url = 'https://api.github.com/repos/owner-482f3203ecf01f67e9deb18e/BBB_Private_Repo/git/blobs/23f6827669e43831def8a7ad935069c8bd418261'
            )
        else:
            return GitTreeTreeInner(
        )
        """

    def testGitTreeTreeInner(self):
        """Test GitTreeTreeInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
