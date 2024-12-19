# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.create_pull_request_option import CreatePullRequestOption

class TestCreatePullRequestOption(unittest.TestCase):
    """CreatePullRequestOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePullRequestOption:
        """Test CreatePullRequestOption
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePullRequestOption`
        """
        model = CreatePullRequestOption()
        if include_optional:
            return CreatePullRequestOption(
                assignee = '',
                assignees = [
                    ''
                    ],
                base = '',
                body = '',
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                head = '',
                labels = [
                    56
                    ],
                milestone = 56,
                title = ''
            )
        else:
            return CreatePullRequestOption(
        )
        """

    def testCreatePullRequestOption(self):
        """Test CreatePullRequestOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
