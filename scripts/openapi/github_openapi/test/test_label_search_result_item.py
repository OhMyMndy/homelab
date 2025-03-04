# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.label_search_result_item import LabelSearchResultItem

class TestLabelSearchResultItem(unittest.TestCase):
    """LabelSearchResultItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LabelSearchResultItem:
        """Test LabelSearchResultItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LabelSearchResultItem`
        """
        model = LabelSearchResultItem()
        if include_optional:
            return LabelSearchResultItem(
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
                    ]
            )
        else:
            return LabelSearchResultItem(
                id = 56,
                node_id = '',
                url = '',
                name = '',
                color = '',
                default = True,
                description = '',
                score = 1.337,
        )
        """

    def testLabelSearchResultItem(self):
        """Test LabelSearchResultItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
