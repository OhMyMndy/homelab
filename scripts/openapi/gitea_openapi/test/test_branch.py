# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.branch import Branch

class TestBranch(unittest.TestCase):
    """Branch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Branch:
        """Test Branch
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Branch`
        """
        model = Branch()
        if include_optional:
            return Branch(
                commit = gitea_openapi.models.payload_commit.PayloadCommit(
                    added = [
                        ''
                        ], 
                    author = gitea_openapi.models.payload_user.PayloadUser(
                        email = '', 
                        name = '', 
                        username = '', ), 
                    committer = gitea_openapi.models.payload_user.PayloadUser(
                        email = '', 
                        name = '', 
                        username = '', ), 
                    id = '', 
                    message = '', 
                    modified = [
                        ''
                        ], 
                    removed = [
                        ''
                        ], 
                    timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    url = '', 
                    verification = gitea_openapi.models.payload_commit_verification.PayloadCommitVerification(
                        payload = '', 
                        reason = '', 
                        signature = '', 
                        signer = , 
                        verified = True, ), ),
                effective_branch_protection_name = '',
                enable_status_check = True,
                name = '',
                protected = True,
                required_approvals = 56,
                status_check_contexts = [
                    ''
                    ],
                user_can_merge = True,
                user_can_push = True
            )
        else:
            return Branch(
        )
        """

    def testBranch(self):
        """Test Branch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
