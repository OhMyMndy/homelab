# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.git_commit_parents_inner import GitCommitParentsInner

class TestGitCommitParentsInner(unittest.TestCase):
    """GitCommitParentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GitCommitParentsInner:
        """Test GitCommitParentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GitCommitParentsInner`
        """
        model = GitCommitParentsInner()
        if include_optional:
            return GitCommitParentsInner(
                sha = '7638417db6d59f3c431d3e1f261cc637155684cd',
                url = '',
                html_url = ''
            )
        else:
            return GitCommitParentsInner(
                sha = '7638417db6d59f3c431d3e1f261cc637155684cd',
                url = '',
                html_url = '',
        )
        """

    def testGitCommitParentsInner(self):
        """Test GitCommitParentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
