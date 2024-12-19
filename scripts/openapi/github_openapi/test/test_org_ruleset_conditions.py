# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.org_ruleset_conditions import OrgRulesetConditions

class TestOrgRulesetConditions(unittest.TestCase):
    """OrgRulesetConditions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrgRulesetConditions:
        """Test OrgRulesetConditions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrgRulesetConditions`
        """
        model = OrgRulesetConditions()
        if include_optional:
            return OrgRulesetConditions(
                ref_name = github_openapi.models.repository_ruleset_conditions_ref_name.repository_ruleset_conditions_ref_name(
                    include = [
                        ''
                        ], 
                    exclude = [
                        ''
                        ], ),
                repository_name = github_openapi.models.repository_ruleset_conditions_repository_name_target_repository_name.repository_ruleset_conditions_repository_name_target_repository_name(
                    include = [
                        ''
                        ], 
                    exclude = [
                        ''
                        ], 
                    protected = True, ),
                repository_id = github_openapi.models.repository_ruleset_conditions_repository_id_target_repository_id.repository_ruleset_conditions_repository_id_target_repository_id(
                    repository_ids = [
                        56
                        ], ),
                repository_property = github_openapi.models.repository_ruleset_conditions_repository_property_target_repository_property.repository_ruleset_conditions_repository_property_target_repository_property(
                    include = [
                        github_openapi.models.repository_ruleset_property_targeting_definition.Repository ruleset property targeting definition(
                            name = '', 
                            property_values = [
                                ''
                                ], 
                            source = 'custom', )
                        ], 
                    exclude = [
                        github_openapi.models.repository_ruleset_property_targeting_definition.Repository ruleset property targeting definition(
                            name = '', 
                            property_values = [
                                ''
                                ], 
                            source = 'custom', )
                        ], )
            )
        else:
            return OrgRulesetConditions(
                repository_name = github_openapi.models.repository_ruleset_conditions_repository_name_target_repository_name.repository_ruleset_conditions_repository_name_target_repository_name(
                    include = [
                        ''
                        ], 
                    exclude = [
                        ''
                        ], 
                    protected = True, ),
                repository_id = github_openapi.models.repository_ruleset_conditions_repository_id_target_repository_id.repository_ruleset_conditions_repository_id_target_repository_id(
                    repository_ids = [
                        56
                        ], ),
                repository_property = github_openapi.models.repository_ruleset_conditions_repository_property_target_repository_property.repository_ruleset_conditions_repository_property_target_repository_property(
                    include = [
                        github_openapi.models.repository_ruleset_property_targeting_definition.Repository ruleset property targeting definition(
                            name = '', 
                            property_values = [
                                ''
                                ], 
                            source = 'custom', )
                        ], 
                    exclude = [
                        github_openapi.models.repository_ruleset_property_targeting_definition.Repository ruleset property targeting definition(
                            name = '', 
                            property_values = [
                                ''
                                ], 
                            source = 'custom', )
                        ], ),
        )
        """

    def testOrgRulesetConditions(self):
        """Test OrgRulesetConditions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
