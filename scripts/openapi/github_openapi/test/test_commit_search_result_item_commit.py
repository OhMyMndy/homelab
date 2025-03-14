# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.commit_search_result_item_commit import CommitSearchResultItemCommit

class TestCommitSearchResultItemCommit(unittest.TestCase):
    """CommitSearchResultItemCommit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommitSearchResultItemCommit:
        """Test CommitSearchResultItemCommit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommitSearchResultItemCommit`
        """
        model = CommitSearchResultItemCommit()
        if include_optional:
            return CommitSearchResultItemCommit(
                author = github_openapi.models.commit_search_result_item_commit_author.commit_search_result_item_commit_author(
                    name = '', 
                    email = '', 
                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                committer = github_openapi.models.git_user.Git User(
                    name = '"Chris Wanstrath"', 
                    email = '"chris@ozmm.org"', 
                    date = '"2007-10-29T02:42:39.000-07:00"', ),
                comment_count = 56,
                message = '',
                tree = github_openapi.models.short_branch_commit.short_branch_commit(
                    sha = '', 
                    url = '', ),
                url = '',
                verification = github_openapi.models.verification.Verification(
                    verified = True, 
                    reason = '', 
                    payload = '', 
                    signature = '', 
                    verified_at = '', )
            )
        else:
            return CommitSearchResultItemCommit(
                author = github_openapi.models.commit_search_result_item_commit_author.commit_search_result_item_commit_author(
                    name = '', 
                    email = '', 
                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                committer = github_openapi.models.git_user.Git User(
                    name = '"Chris Wanstrath"', 
                    email = '"chris@ozmm.org"', 
                    date = '"2007-10-29T02:42:39.000-07:00"', ),
                comment_count = 56,
                message = '',
                tree = github_openapi.models.short_branch_commit.short_branch_commit(
                    sha = '', 
                    url = '', ),
                url = '',
        )
        """

    def testCommitSearchResultItemCommit(self):
        """Test CommitSearchResultItemCommit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
