# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.codespaces_list_repo_secrets200_response import CodespacesListRepoSecrets200Response

class TestCodespacesListRepoSecrets200Response(unittest.TestCase):
    """CodespacesListRepoSecrets200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CodespacesListRepoSecrets200Response:
        """Test CodespacesListRepoSecrets200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CodespacesListRepoSecrets200Response`
        """
        model = CodespacesListRepoSecrets200Response()
        if include_optional:
            return CodespacesListRepoSecrets200Response(
                total_count = 56,
                secrets = [
                    github_openapi.models.codespaces_secret.Codespaces Secret(
                        name = 'SECRET_TOKEN', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return CodespacesListRepoSecrets200Response(
                total_count = 56,
                secrets = [
                    github_openapi.models.codespaces_secret.Codespaces Secret(
                        name = 'SECRET_TOKEN', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testCodespacesListRepoSecrets200Response(self):
        """Test CodespacesListRepoSecrets200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
