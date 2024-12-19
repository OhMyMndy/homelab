# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.cvss_severities_cvss_v3 import CvssSeveritiesCvssV3

class TestCvssSeveritiesCvssV3(unittest.TestCase):
    """CvssSeveritiesCvssV3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CvssSeveritiesCvssV3:
        """Test CvssSeveritiesCvssV3
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CvssSeveritiesCvssV3`
        """
        model = CvssSeveritiesCvssV3()
        if include_optional:
            return CvssSeveritiesCvssV3(
                vector_string = '',
                score = 0
            )
        else:
            return CvssSeveritiesCvssV3(
                vector_string = '',
                score = 0,
        )
        """

    def testCvssSeveritiesCvssV3(self):
        """Test CvssSeveritiesCvssV3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
