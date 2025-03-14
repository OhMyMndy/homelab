# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.projects_move_card403_response import ProjectsMoveCard403Response

class TestProjectsMoveCard403Response(unittest.TestCase):
    """ProjectsMoveCard403Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectsMoveCard403Response:
        """Test ProjectsMoveCard403Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectsMoveCard403Response`
        """
        model = ProjectsMoveCard403Response()
        if include_optional:
            return ProjectsMoveCard403Response(
                message = '',
                documentation_url = '',
                errors = [
                    github_openapi.models.projects_move_card_403_response_errors_inner.projects_move_card_403_response_errors_inner(
                        code = '', 
                        message = '', 
                        resource = '', 
                        field = '', )
                    ]
            )
        else:
            return ProjectsMoveCard403Response(
        )
        """

    def testProjectsMoveCard403Response(self):
        """Test ProjectsMoveCard403Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
