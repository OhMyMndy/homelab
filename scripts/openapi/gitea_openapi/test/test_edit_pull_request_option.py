# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.edit_pull_request_option import EditPullRequestOption

class TestEditPullRequestOption(unittest.TestCase):
    """EditPullRequestOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditPullRequestOption:
        """Test EditPullRequestOption
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditPullRequestOption`
        """
        model = EditPullRequestOption()
        if include_optional:
            return EditPullRequestOption(
                allow_maintainer_edit = True,
                assignee = '',
                assignees = [
                    ''
                    ],
                base = '',
                body = '',
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                labels = [
                    56
                    ],
                milestone = 56,
                state = '',
                title = '',
                unset_due_date = True
            )
        else:
            return EditPullRequestOption(
        )
        """

    def testEditPullRequestOption(self):
        """Test EditPullRequestOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
