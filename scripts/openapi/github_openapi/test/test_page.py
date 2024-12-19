# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.page import Page

class TestPage(unittest.TestCase):
    """Page unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Page:
        """Test Page
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Page`
        """
        model = Page()
        if include_optional:
            return Page(
                url = 'https://api.github.com/repos/github/hello-world/pages',
                status = 'built',
                cname = 'example.com',
                protected_domain_state = 'pending',
                pending_domain_unverified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                custom_404 = False,
                html_url = 'https://example.com',
                build_type = 'legacy',
                source = github_openapi.models.pages_source_hash.Pages Source Hash(
                    branch = '', 
                    path = '', ),
                public = True,
                https_certificate = github_openapi.models.pages_https_certificate.Pages Https Certificate(
                    state = 'approved', 
                    description = 'Certificate is approved', 
                    domains = ["example.com","www.example.com"], 
                    expires_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), ),
                https_enforced = True
            )
        else:
            return Page(
                url = 'https://api.github.com/repos/github/hello-world/pages',
                status = 'built',
                cname = 'example.com',
                custom_404 = False,
                public = True,
        )
        """

    def testPage(self):
        """Test Page"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
