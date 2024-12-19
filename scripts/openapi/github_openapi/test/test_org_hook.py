# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.org_hook import OrgHook

class TestOrgHook(unittest.TestCase):
    """OrgHook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrgHook:
        """Test OrgHook
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrgHook`
        """
        model = OrgHook()
        if include_optional:
            return OrgHook(
                id = 1,
                url = 'https://api.github.com/orgs/octocat/hooks/1',
                ping_url = 'https://api.github.com/orgs/octocat/hooks/1/pings',
                deliveries_url = 'https://api.github.com/orgs/octocat/hooks/1/deliveries',
                name = 'web',
                events = ["push","pull_request"],
                active = True,
                config = github_openapi.models.org_hook_config.org_hook_config(
                    url = '"http://example.com/2"', 
                    insecure_ssl = '"0"', 
                    content_type = '"form"', 
                    secret = '"********"', ),
                updated_at = '2011-09-06T20:39:23Z',
                created_at = '2011-09-06T17:26:27Z',
                type = ''
            )
        else:
            return OrgHook(
                id = 1,
                url = 'https://api.github.com/orgs/octocat/hooks/1',
                ping_url = 'https://api.github.com/orgs/octocat/hooks/1/pings',
                name = 'web',
                events = ["push","pull_request"],
                active = True,
                config = github_openapi.models.org_hook_config.org_hook_config(
                    url = '"http://example.com/2"', 
                    insecure_ssl = '"0"', 
                    content_type = '"form"', 
                    secret = '"********"', ),
                updated_at = '2011-09-06T20:39:23Z',
                created_at = '2011-09-06T17:26:27Z',
                type = '',
        )
        """

    def testOrgHook(self):
        """Test OrgHook"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
