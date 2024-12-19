# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.file_commit_commit import FileCommitCommit

class TestFileCommitCommit(unittest.TestCase):
    """FileCommitCommit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileCommitCommit:
        """Test FileCommitCommit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileCommitCommit`
        """
        model = FileCommitCommit()
        if include_optional:
            return FileCommitCommit(
                sha = '',
                node_id = '',
                url = '',
                html_url = '',
                author = github_openapi.models.file_commit_commit_author.file_commit_commit_author(
                    date = '', 
                    name = '', 
                    email = '', ),
                committer = github_openapi.models.file_commit_commit_author.file_commit_commit_author(
                    date = '', 
                    name = '', 
                    email = '', ),
                message = '',
                tree = github_openapi.models.file_commit_commit_tree.file_commit_commit_tree(
                    url = '', 
                    sha = '', ),
                parents = [
                    github_openapi.models.file_commit_commit_parents_inner.file_commit_commit_parents_inner(
                        url = '', 
                        html_url = '', 
                        sha = '', )
                    ],
                verification = github_openapi.models.file_commit_commit_verification.file_commit_commit_verification(
                    verified = True, 
                    reason = '', 
                    signature = '', 
                    payload = '', 
                    verified_at = '', )
            )
        else:
            return FileCommitCommit(
        )
        """

    def testFileCommitCommit(self):
        """Test FileCommitCommit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
