# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.models.issue_form_field import IssueFormField

class TestIssueFormField(unittest.TestCase):
    """IssueFormField unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IssueFormField:
        """Test IssueFormField
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IssueFormField`
        """
        model = IssueFormField()
        if include_optional:
            return IssueFormField(
                attributes = {
                    'key' : None
                    },
                id = '',
                type = '',
                validations = {
                    'key' : None
                    },
                visible = [
                    ''
                    ]
            )
        else:
            return IssueFormField(
        )
        """

    def testIssueFormField(self):
        """Test IssueFormField"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
