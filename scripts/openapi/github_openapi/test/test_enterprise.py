# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.enterprise import Enterprise

class TestEnterprise(unittest.TestCase):
    """Enterprise unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Enterprise:
        """Test Enterprise
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Enterprise`
        """
        model = Enterprise()
        if include_optional:
            return Enterprise(
                description = '',
                html_url = 'https://github.com/enterprises/octo-business',
                website_url = '',
                id = 42,
                node_id = 'MDEwOlJlcG9zaXRvcnkxMjk2MjY5',
                name = 'Octo Business',
                slug = 'octo-business',
                created_at = '2019-01-26T19:01:12Z',
                updated_at = '2019-01-26T19:14:43Z',
                avatar_url = ''
            )
        else:
            return Enterprise(
                html_url = 'https://github.com/enterprises/octo-business',
                id = 42,
                node_id = 'MDEwOlJlcG9zaXRvcnkxMjk2MjY5',
                name = 'Octo Business',
                slug = 'octo-business',
                created_at = '2019-01-26T19:01:12Z',
                updated_at = '2019-01-26T19:14:43Z',
                avatar_url = '',
        )
        """

    def testEnterprise(self):
        """Test Enterprise"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
