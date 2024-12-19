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

from authentik_openapi.models.paginated_identification_stage_list import PaginatedIdentificationStageList

class TestPaginatedIdentificationStageList(unittest.TestCase):
    """PaginatedIdentificationStageList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedIdentificationStageList:
        """Test PaginatedIdentificationStageList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedIdentificationStageList`
        """
        model = PaginatedIdentificationStageList()
        if include_optional:
            return PaginatedIdentificationStageList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.identification_stage.IdentificationStage(
                        pk = '', 
                        name = '', 
                        component = '', 
                        verbose_name = '', 
                        verbose_name_plural = '', 
                        meta_model_name = '', 
                        flow_set = [
                            authentik_openapi.models.flow_set.FlowSet(
                                pk = '', 
                                policybindingmodel_ptr_id = '', 
                                name = '', 
                                slug = 'z', 
                                title = '', 
                                designation = null, 
                                background = '', 
                                policy_engine_mode = 'all', 
                                compatibility_mode = True, 
                                export_url = '', 
                                layout = 'stacked', 
                                denied_action = null, )
                            ], 
                        user_fields = [
                            'email'
                            ], 
                        password_stage = '', 
                        case_insensitive_matching = True, 
                        show_matched_user = True, 
                        enrollment_flow = '', 
                        recovery_flow = '', 
                        passwordless_flow = '', 
                        sources = [
                            ''
                            ], 
                        show_source_labels = True, 
                        pretend_user_exists = True, )
                    ]
            )
        else:
            return PaginatedIdentificationStageList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.identification_stage.IdentificationStage(
                        pk = '', 
                        name = '', 
                        component = '', 
                        verbose_name = '', 
                        verbose_name_plural = '', 
                        meta_model_name = '', 
                        flow_set = [
                            authentik_openapi.models.flow_set.FlowSet(
                                pk = '', 
                                policybindingmodel_ptr_id = '', 
                                name = '', 
                                slug = 'z', 
                                title = '', 
                                designation = null, 
                                background = '', 
                                policy_engine_mode = 'all', 
                                compatibility_mode = True, 
                                export_url = '', 
                                layout = 'stacked', 
                                denied_action = null, )
                            ], 
                        user_fields = [
                            'email'
                            ], 
                        password_stage = '', 
                        case_insensitive_matching = True, 
                        show_matched_user = True, 
                        enrollment_flow = '', 
                        recovery_flow = '', 
                        passwordless_flow = '', 
                        sources = [
                            ''
                            ], 
                        show_source_labels = True, 
                        pretend_user_exists = True, )
                    ],
        )
        """

    def testPaginatedIdentificationStageList(self):
        """Test PaginatedIdentificationStageList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
