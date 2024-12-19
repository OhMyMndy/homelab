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

from authentik_openapi.models.paginated_plex_source_list import PaginatedPlexSourceList

class TestPaginatedPlexSourceList(unittest.TestCase):
    """PaginatedPlexSourceList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedPlexSourceList:
        """Test PaginatedPlexSourceList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedPlexSourceList`
        """
        model = PaginatedPlexSourceList()
        if include_optional:
            return PaginatedPlexSourceList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.plex_source.PlexSource(
                        pk = '', 
                        name = '', 
                        slug = 'z', 
                        enabled = True, 
                        authentication_flow = '', 
                        enrollment_flow = '', 
                        component = '', 
                        verbose_name = '', 
                        verbose_name_plural = '', 
                        meta_model_name = '', 
                        policy_engine_mode = 'all', 
                        user_matching_mode = null, 
                        managed = '', 
                        user_path_template = '', 
                        icon = '', 
                        client_id = '', 
                        allowed_servers = [
                            ''
                            ], 
                        allow_friends = True, 
                        plex_token = '', )
                    ]
            )
        else:
            return PaginatedPlexSourceList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.plex_source.PlexSource(
                        pk = '', 
                        name = '', 
                        slug = 'z', 
                        enabled = True, 
                        authentication_flow = '', 
                        enrollment_flow = '', 
                        component = '', 
                        verbose_name = '', 
                        verbose_name_plural = '', 
                        meta_model_name = '', 
                        policy_engine_mode = 'all', 
                        user_matching_mode = null, 
                        managed = '', 
                        user_path_template = '', 
                        icon = '', 
                        client_id = '', 
                        allowed_servers = [
                            ''
                            ], 
                        allow_friends = True, 
                        plex_token = '', )
                    ],
        )
        """

    def testPaginatedPlexSourceList(self):
        """Test PaginatedPlexSourceList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
