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

from authentik_openapi.models.paginated_google_workspace_provider_list import PaginatedGoogleWorkspaceProviderList

class TestPaginatedGoogleWorkspaceProviderList(unittest.TestCase):
    """PaginatedGoogleWorkspaceProviderList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedGoogleWorkspaceProviderList:
        """Test PaginatedGoogleWorkspaceProviderList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedGoogleWorkspaceProviderList`
        """
        model = PaginatedGoogleWorkspaceProviderList()
        if include_optional:
            return PaginatedGoogleWorkspaceProviderList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.google_workspace_provider.GoogleWorkspaceProvider(
                        pk = 56, 
                        name = '', 
                        property_mappings = [
                            ''
                            ], 
                        property_mappings_group = [
                            ''
                            ], 
                        component = '', 
                        assigned_backchannel_application_slug = '', 
                        assigned_backchannel_application_name = '', 
                        verbose_name = '', 
                        verbose_name_plural = '', 
                        meta_model_name = '', 
                        delegated_subject = '', 
                        credentials = null, 
                        scopes = '', 
                        exclude_users_service_account = True, 
                        filter_group = '', 
                        user_delete_action = 'do_nothing', 
                        group_delete_action = 'do_nothing', 
                        default_group_email_domain = '', )
                    ]
            )
        else:
            return PaginatedGoogleWorkspaceProviderList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.google_workspace_provider.GoogleWorkspaceProvider(
                        pk = 56, 
                        name = '', 
                        property_mappings = [
                            ''
                            ], 
                        property_mappings_group = [
                            ''
                            ], 
                        component = '', 
                        assigned_backchannel_application_slug = '', 
                        assigned_backchannel_application_name = '', 
                        verbose_name = '', 
                        verbose_name_plural = '', 
                        meta_model_name = '', 
                        delegated_subject = '', 
                        credentials = null, 
                        scopes = '', 
                        exclude_users_service_account = True, 
                        filter_group = '', 
                        user_delete_action = 'do_nothing', 
                        group_delete_action = 'do_nothing', 
                        default_group_email_domain = '', )
                    ],
        )
        """

    def testPaginatedGoogleWorkspaceProviderList(self):
        """Test PaginatedGoogleWorkspaceProviderList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
