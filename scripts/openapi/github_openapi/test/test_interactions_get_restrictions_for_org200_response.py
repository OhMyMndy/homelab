# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.interactions_get_restrictions_for_org200_response import InteractionsGetRestrictionsForOrg200Response

class TestInteractionsGetRestrictionsForOrg200Response(unittest.TestCase):
    """InteractionsGetRestrictionsForOrg200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InteractionsGetRestrictionsForOrg200Response:
        """Test InteractionsGetRestrictionsForOrg200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InteractionsGetRestrictionsForOrg200Response`
        """
        model = InteractionsGetRestrictionsForOrg200Response()
        if include_optional:
            return InteractionsGetRestrictionsForOrg200Response(
                limit = 'collaborators_only',
                origin = 'repository',
                expires_at = '2018-08-17T04:18:39Z'
            )
        else:
            return InteractionsGetRestrictionsForOrg200Response(
                limit = 'collaborators_only',
                origin = 'repository',
                expires_at = '2018-08-17T04:18:39Z',
        )
        """

    def testInteractionsGetRestrictionsForOrg200Response(self):
        """Test InteractionsGetRestrictionsForOrg200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
