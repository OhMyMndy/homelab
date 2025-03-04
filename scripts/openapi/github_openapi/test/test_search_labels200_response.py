# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.search_labels200_response import SearchLabels200Response

class TestSearchLabels200Response(unittest.TestCase):
    """SearchLabels200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchLabels200Response:
        """Test SearchLabels200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchLabels200Response`
        """
        model = SearchLabels200Response()
        if include_optional:
            return SearchLabels200Response(
                total_count = 56,
                incomplete_results = True,
                items = [
                    github_openapi.models.label_search_result_item.Label Search Result Item(
                        id = 56, 
                        node_id = '', 
                        url = '', 
                        name = '', 
                        color = '', 
                        default = True, 
                        description = '', 
                        score = 1.337, 
                        text_matches = [
                            github_openapi.models.search_result_text_matches_inner.search_result_text_matches_inner(
                                object_url = '', 
                                object_type = '', 
                                property = '', 
                                fragment = '', 
                                matches = [
                                    github_openapi.models.search_result_text_matches_inner_matches_inner.search_result_text_matches_inner_matches_inner(
                                        text = '', 
                                        indices = [
                                            56
                                            ], )
                                    ], )
                            ], )
                    ]
            )
        else:
            return SearchLabels200Response(
                total_count = 56,
                incomplete_results = True,
                items = [
                    github_openapi.models.label_search_result_item.Label Search Result Item(
                        id = 56, 
                        node_id = '', 
                        url = '', 
                        name = '', 
                        color = '', 
                        default = True, 
                        description = '', 
                        score = 1.337, 
                        text_matches = [
                            github_openapi.models.search_result_text_matches_inner.search_result_text_matches_inner(
                                object_url = '', 
                                object_type = '', 
                                property = '', 
                                fragment = '', 
                                matches = [
                                    github_openapi.models.search_result_text_matches_inner_matches_inner.search_result_text_matches_inner_matches_inner(
                                        text = '', 
                                        indices = [
                                            56
                                            ], )
                                    ], )
                            ], )
                    ],
        )
        """

    def testSearchLabels200Response(self):
        """Test SearchLabels200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
