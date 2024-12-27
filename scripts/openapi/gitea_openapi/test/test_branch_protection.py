# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.branch_protection import BranchProtection

class TestBranchProtection(unittest.TestCase):
    """BranchProtection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BranchProtection:
        """Test BranchProtection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BranchProtection`
        """
        model = BranchProtection()
        if include_optional:
            return BranchProtection(
                approvals_whitelist_teams = [
                    ''
                    ],
                approvals_whitelist_username = [
                    ''
                    ],
                block_on_official_review_requests = True,
                block_on_outdated_branch = True,
                block_on_rejected_reviews = True,
                branch_name = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                dismiss_stale_approvals = True,
                enable_approvals_whitelist = True,
                enable_merge_whitelist = True,
                enable_push = True,
                enable_push_whitelist = True,
                enable_status_check = True,
                ignore_stale_approvals = True,
                merge_whitelist_teams = [
                    ''
                    ],
                merge_whitelist_usernames = [
                    ''
                    ],
                protected_file_patterns = '',
                push_whitelist_deploy_keys = True,
                push_whitelist_teams = [
                    ''
                    ],
                push_whitelist_usernames = [
                    ''
                    ],
                require_signed_commits = True,
                required_approvals = 56,
                rule_name = '',
                status_check_contexts = [
                    ''
                    ],
                unprotected_file_patterns = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return BranchProtection(
        )
        """

    def testBranchProtection(self):
        """Test BranchProtection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()