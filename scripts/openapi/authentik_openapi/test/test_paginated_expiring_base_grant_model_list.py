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

from authentik_openapi.models.paginated_expiring_base_grant_model_list import PaginatedExpiringBaseGrantModelList

class TestPaginatedExpiringBaseGrantModelList(unittest.TestCase):
    """PaginatedExpiringBaseGrantModelList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedExpiringBaseGrantModelList:
        """Test PaginatedExpiringBaseGrantModelList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedExpiringBaseGrantModelList`
        """
        model = PaginatedExpiringBaseGrantModelList()
        if include_optional:
            return PaginatedExpiringBaseGrantModelList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.expiring_base_grant_model.ExpiringBaseGrantModel(
                        pk = 56, 
                        provider = authentik_openapi.models.o_auth2_provider.OAuth2Provider(
                            pk = 56, 
                            name = '', 
                            authentication_flow = '', 
                            authorization_flow = '', 
                            property_mappings = [
                                ''
                                ], 
                            component = '', 
                            assigned_application_slug = '', 
                            assigned_application_name = '', 
                            assigned_backchannel_application_slug = '', 
                            assigned_backchannel_application_name = '', 
                            verbose_name = '', 
                            verbose_name_plural = '', 
                            meta_model_name = '', 
                            client_type = null, 
                            client_id = '', 
                            client_secret = '', 
                            access_code_validity = '', 
                            access_token_validity = '', 
                            refresh_token_validity = '', 
                            include_claims_in_id_token = True, 
                            signing_key = '', 
                            redirect_uris = '', 
                            sub_mode = null, 
                            issuer_mode = null, 
                            jwks_sources = [
                                ''
                                ], ), 
                        user = authentik_openapi.models.user.User(
                            pk = 56, 
                            username = '', 
                            name = '', 
                            is_active = True, 
                            last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            is_superuser = True, 
                            groups = [
                                ''
                                ], 
                            groups_obj = [
                                authentik_openapi.models.user_group.UserGroup(
                                    pk = '', 
                                    num_pk = 56, 
                                    name = '', 
                                    is_superuser = True, 
                                    parent = '', 
                                    parent_name = '', 
                                    attributes = {
                                        'key' : null
                                        }, )
                                ], 
                            email = '', 
                            avatar = '', 
                            attributes = {
                                'key' : null
                                }, 
                            uid = '', 
                            path = '', 
                            type = 'internal', 
                            uuid = '', ), 
                        is_expired = True, 
                        expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        scope = [
                            ''
                            ], )
                    ]
            )
        else:
            return PaginatedExpiringBaseGrantModelList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.expiring_base_grant_model.ExpiringBaseGrantModel(
                        pk = 56, 
                        provider = authentik_openapi.models.o_auth2_provider.OAuth2Provider(
                            pk = 56, 
                            name = '', 
                            authentication_flow = '', 
                            authorization_flow = '', 
                            property_mappings = [
                                ''
                                ], 
                            component = '', 
                            assigned_application_slug = '', 
                            assigned_application_name = '', 
                            assigned_backchannel_application_slug = '', 
                            assigned_backchannel_application_name = '', 
                            verbose_name = '', 
                            verbose_name_plural = '', 
                            meta_model_name = '', 
                            client_type = null, 
                            client_id = '', 
                            client_secret = '', 
                            access_code_validity = '', 
                            access_token_validity = '', 
                            refresh_token_validity = '', 
                            include_claims_in_id_token = True, 
                            signing_key = '', 
                            redirect_uris = '', 
                            sub_mode = null, 
                            issuer_mode = null, 
                            jwks_sources = [
                                ''
                                ], ), 
                        user = authentik_openapi.models.user.User(
                            pk = 56, 
                            username = '', 
                            name = '', 
                            is_active = True, 
                            last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            is_superuser = True, 
                            groups = [
                                ''
                                ], 
                            groups_obj = [
                                authentik_openapi.models.user_group.UserGroup(
                                    pk = '', 
                                    num_pk = 56, 
                                    name = '', 
                                    is_superuser = True, 
                                    parent = '', 
                                    parent_name = '', 
                                    attributes = {
                                        'key' : null
                                        }, )
                                ], 
                            email = '', 
                            avatar = '', 
                            attributes = {
                                'key' : null
                                }, 
                            uid = '', 
                            path = '', 
                            type = 'internal', 
                            uuid = '', ), 
                        is_expired = True, 
                        expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        scope = [
                            ''
                            ], )
                    ],
        )
        """

    def testPaginatedExpiringBaseGrantModelList(self):
        """Test PaginatedExpiringBaseGrantModelList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
