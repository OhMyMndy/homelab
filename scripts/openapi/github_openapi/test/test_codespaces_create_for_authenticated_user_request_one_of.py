# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.codespaces_create_for_authenticated_user_request_one_of import CodespacesCreateForAuthenticatedUserRequestOneOf

class TestCodespacesCreateForAuthenticatedUserRequestOneOf(unittest.TestCase):
    """CodespacesCreateForAuthenticatedUserRequestOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CodespacesCreateForAuthenticatedUserRequestOneOf:
        """Test CodespacesCreateForAuthenticatedUserRequestOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CodespacesCreateForAuthenticatedUserRequestOneOf`
        """
        model = CodespacesCreateForAuthenticatedUserRequestOneOf()
        if include_optional:
            return CodespacesCreateForAuthenticatedUserRequestOneOf(
                repository_id = 56,
                ref = '',
                location = '',
                geo = 'EuropeWest',
                client_ip = '',
                machine = '',
                devcontainer_path = '',
                multi_repo_permissions_opt_out = True,
                working_directory = '',
                idle_timeout_minutes = 56,
                display_name = '',
                retention_period_minutes = 56
            )
        else:
            return CodespacesCreateForAuthenticatedUserRequestOneOf(
                repository_id = 56,
        )
        """

    def testCodespacesCreateForAuthenticatedUserRequestOneOf(self):
        """Test CodespacesCreateForAuthenticatedUserRequestOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
