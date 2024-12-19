# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2024.6.4
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from authentik_openapi.models.paginated_user_o_auth_source_connection_list import PaginatedUserOAuthSourceConnectionList

class TestPaginatedUserOAuthSourceConnectionList(unittest.TestCase):
    """PaginatedUserOAuthSourceConnectionList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedUserOAuthSourceConnectionList:
        """Test PaginatedUserOAuthSourceConnectionList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedUserOAuthSourceConnectionList`
        """
        model = PaginatedUserOAuthSourceConnectionList()
        if include_optional:
            return PaginatedUserOAuthSourceConnectionList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.user_o_auth_source_connection.UserOAuthSourceConnection(
                        pk = 56, 
                        user = 56, 
                        source = null, 
                        identifier = '', )
                    ]
            )
        else:
            return PaginatedUserOAuthSourceConnectionList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.user_o_auth_source_connection.UserOAuthSourceConnection(
                        pk = 56, 
                        user = 56, 
                        source = null, 
                        identifier = '', )
                    ],
        )
        """

    def testPaginatedUserOAuthSourceConnectionList(self):
        """Test PaginatedUserOAuthSourceConnectionList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
