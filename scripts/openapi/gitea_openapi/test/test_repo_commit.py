# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.repo_commit import RepoCommit

class TestRepoCommit(unittest.TestCase):
    """RepoCommit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepoCommit:
        """Test RepoCommit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepoCommit`
        """
        model = RepoCommit()
        if include_optional:
            return RepoCommit(
                author = gitea_openapi.models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit/.CommitUser contains information of a user in the context of a commit.(
                    date = '', 
                    email = '', 
                    name = '', ),
                committer = gitea_openapi.models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit/.CommitUser contains information of a user in the context of a commit.(
                    date = '', 
                    email = '', 
                    name = '', ),
                message = '',
                tree = gitea_openapi.models.commit_meta_contains_meta_information_of_a_commit_in_terms_of_api/.CommitMeta contains meta information of a commit in terms of API.(
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    sha = '', 
                    url = '', ),
                url = '',
                verification = gitea_openapi.models.payload_commit_verification.PayloadCommitVerification(
                    payload = '', 
                    reason = '', 
                    signature = '', 
                    signer = gitea_openapi.models.payload_user.PayloadUser(
                        email = '', 
                        name = '', 
                        username = '', ), 
                    verified = True, )
            )
        else:
            return RepoCommit(
        )
        """

    def testRepoCommit(self):
        """Test RepoCommit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
