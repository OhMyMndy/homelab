# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.commit_status import CommitStatus

class TestCommitStatus(unittest.TestCase):
    """CommitStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommitStatus:
        """Test CommitStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommitStatus`
        """
        model = CommitStatus()
        if include_optional:
            return CommitStatus(
                context = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                creator = gitea_openapi.models.user.User(
                    active = True, 
                    avatar_url = '', 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    description = '', 
                    email = '', 
                    followers_count = 56, 
                    following_count = 56, 
                    full_name = '', 
                    id = 56, 
                    is_admin = True, 
                    language = '', 
                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    location = '', 
                    login = '', 
                    login_name = 'empty', 
                    prohibit_login = True, 
                    restricted = True, 
                    source_id = 56, 
                    starred_repos_count = 56, 
                    visibility = '', 
                    website = '', ),
                description = '',
                id = 56,
                status = '',
                target_url = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = ''
            )
        else:
            return CommitStatus(
        )
        """

    def testCommitStatus(self):
        """Test CommitStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
