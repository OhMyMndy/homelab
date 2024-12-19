# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.rate_limit import RateLimit

class TestRateLimit(unittest.TestCase):
    """RateLimit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RateLimit:
        """Test RateLimit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RateLimit`
        """
        model = RateLimit()
        if include_optional:
            return RateLimit(
                limit = 56,
                remaining = 56,
                reset = 56,
                used = 56
            )
        else:
            return RateLimit(
                limit = 56,
                remaining = 56,
                reset = 56,
                used = 56,
        )
        """

    def testRateLimit(self):
        """Test RateLimit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
