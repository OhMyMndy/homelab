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

from authentik_openapi.models.paginated_policy_binding_list import PaginatedPolicyBindingList

class TestPaginatedPolicyBindingList(unittest.TestCase):
    """PaginatedPolicyBindingList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedPolicyBindingList:
        """Test PaginatedPolicyBindingList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedPolicyBindingList`
        """
        model = PaginatedPolicyBindingList()
        if include_optional:
            return PaginatedPolicyBindingList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.policy_binding.PolicyBinding(
                        pk = '', 
                        policy = '', 
                        group = '', 
                        user = 56, 
                        policy_obj = null, 
                        group_obj = null, 
                        user_obj = null, 
                        target = '', 
                        negate = True, 
                        enabled = True, 
                        order = -2147483648, 
                        timeout = 0, 
                        failure_result = True, )
                    ]
            )
        else:
            return PaginatedPolicyBindingList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.policy_binding.PolicyBinding(
                        pk = '', 
                        policy = '', 
                        group = '', 
                        user = 56, 
                        policy_obj = null, 
                        group_obj = null, 
                        user_obj = null, 
                        target = '', 
                        negate = True, 
                        enabled = True, 
                        order = -2147483648, 
                        timeout = 0, 
                        failure_result = True, )
                    ],
        )
        """

    def testPaginatedPolicyBindingList(self):
        """Test PaginatedPolicyBindingList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
