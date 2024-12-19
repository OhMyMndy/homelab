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

from authentik_openapi.models.identification_stage import IdentificationStage

class TestIdentificationStage(unittest.TestCase):
    """IdentificationStage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentificationStage:
        """Test IdentificationStage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentificationStage`
        """
        model = IdentificationStage()
        if include_optional:
            return IdentificationStage(
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
                pretend_user_exists = True
            )
        else:
            return IdentificationStage(
                pk = '',
                name = '',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
        )
        """

    def testIdentificationStage(self):
        """Test IdentificationStage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
