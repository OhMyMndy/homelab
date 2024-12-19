# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.codespaces_pre_flight_with_repo_for_authenticated_user200_response_defaults import CodespacesPreFlightWithRepoForAuthenticatedUser200ResponseDefaults

class TestCodespacesPreFlightWithRepoForAuthenticatedUser200ResponseDefaults(unittest.TestCase):
    """CodespacesPreFlightWithRepoForAuthenticatedUser200ResponseDefaults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CodespacesPreFlightWithRepoForAuthenticatedUser200ResponseDefaults:
        """Test CodespacesPreFlightWithRepoForAuthenticatedUser200ResponseDefaults
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CodespacesPreFlightWithRepoForAuthenticatedUser200ResponseDefaults`
        """
        model = CodespacesPreFlightWithRepoForAuthenticatedUser200ResponseDefaults()
        if include_optional:
            return CodespacesPreFlightWithRepoForAuthenticatedUser200ResponseDefaults(
                location = '',
                devcontainer_path = ''
            )
        else:
            return CodespacesPreFlightWithRepoForAuthenticatedUser200ResponseDefaults(
                location = '',
                devcontainer_path = '',
        )
        """

    def testCodespacesPreFlightWithRepoForAuthenticatedUser200ResponseDefaults(self):
        """Test CodespacesPreFlightWithRepoForAuthenticatedUser200ResponseDefaults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
