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

from authentik_openapi.models.paginated_reputation_policy_list import PaginatedReputationPolicyList

class TestPaginatedReputationPolicyList(unittest.TestCase):
    """PaginatedReputationPolicyList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedReputationPolicyList:
        """Test PaginatedReputationPolicyList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedReputationPolicyList`
        """
        model = PaginatedReputationPolicyList()
        if include_optional:
            return PaginatedReputationPolicyList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.reputation_policy.ReputationPolicy(
                        pk = '', 
                        name = '', 
                        execution_logging = True, 
                        component = '', 
                        verbose_name = '', 
                        verbose_name_plural = '', 
                        meta_model_name = '', 
                        bound_to = 56, 
                        check_ip = True, 
                        check_username = True, 
                        threshold = -2147483648, )
                    ]
            )
        else:
            return PaginatedReputationPolicyList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.reputation_policy.ReputationPolicy(
                        pk = '', 
                        name = '', 
                        execution_logging = True, 
                        component = '', 
                        verbose_name = '', 
                        verbose_name_plural = '', 
                        meta_model_name = '', 
                        bound_to = 56, 
                        check_ip = True, 
                        check_username = True, 
                        threshold = -2147483648, )
                    ],
        )
        """

    def testPaginatedReputationPolicyList(self):
        """Test PaginatedReputationPolicyList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
