# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.projects_move_card_request import ProjectsMoveCardRequest

class TestProjectsMoveCardRequest(unittest.TestCase):
    """ProjectsMoveCardRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectsMoveCardRequest:
        """Test ProjectsMoveCardRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectsMoveCardRequest`
        """
        model = ProjectsMoveCardRequest()
        if include_optional:
            return ProjectsMoveCardRequest(
                position = 'bottom',
                column_id = 42
            )
        else:
            return ProjectsMoveCardRequest(
                position = 'bottom',
        )
        """

    def testProjectsMoveCardRequest(self):
        """Test ProjectsMoveCardRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()