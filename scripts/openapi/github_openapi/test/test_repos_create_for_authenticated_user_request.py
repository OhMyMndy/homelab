# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repos_create_for_authenticated_user_request import ReposCreateForAuthenticatedUserRequest

class TestReposCreateForAuthenticatedUserRequest(unittest.TestCase):
    """ReposCreateForAuthenticatedUserRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReposCreateForAuthenticatedUserRequest:
        """Test ReposCreateForAuthenticatedUserRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReposCreateForAuthenticatedUserRequest`
        """
        model = ReposCreateForAuthenticatedUserRequest()
        if include_optional:
            return ReposCreateForAuthenticatedUserRequest(
                name = 'Team Environment',
                description = '',
                homepage = '',
                private = True,
                has_issues = True,
                has_projects = True,
                has_wiki = True,
                has_discussions = True,
                team_id = 56,
                auto_init = True,
                gitignore_template = 'Haskell',
                license_template = 'mit',
                allow_squash_merge = True,
                allow_merge_commit = True,
                allow_rebase_merge = True,
                allow_auto_merge = False,
                delete_branch_on_merge = False,
                squash_merge_commit_title = 'PR_TITLE',
                squash_merge_commit_message = 'PR_BODY',
                merge_commit_title = 'PR_TITLE',
                merge_commit_message = 'PR_BODY',
                has_downloads = True,
                is_template = True
            )
        else:
            return ReposCreateForAuthenticatedUserRequest(
                name = 'Team Environment',
        )
        """

    def testReposCreateForAuthenticatedUserRequest(self):
        """Test ReposCreateForAuthenticatedUserRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
