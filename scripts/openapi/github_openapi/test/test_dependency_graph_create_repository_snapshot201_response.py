# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.dependency_graph_create_repository_snapshot201_response import DependencyGraphCreateRepositorySnapshot201Response

class TestDependencyGraphCreateRepositorySnapshot201Response(unittest.TestCase):
    """DependencyGraphCreateRepositorySnapshot201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DependencyGraphCreateRepositorySnapshot201Response:
        """Test DependencyGraphCreateRepositorySnapshot201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DependencyGraphCreateRepositorySnapshot201Response`
        """
        model = DependencyGraphCreateRepositorySnapshot201Response()
        if include_optional:
            return DependencyGraphCreateRepositorySnapshot201Response(
                id = 56,
                created_at = '',
                result = '',
                message = ''
            )
        else:
            return DependencyGraphCreateRepositorySnapshot201Response(
                id = 56,
                created_at = '',
                result = '',
                message = '',
        )
        """

    def testDependencyGraphCreateRepositorySnapshot201Response(self):
        """Test DependencyGraphCreateRepositorySnapshot201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
