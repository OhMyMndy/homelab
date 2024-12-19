# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.cvss_severities_cvss_v4 import CvssSeveritiesCvssV4

class TestCvssSeveritiesCvssV4(unittest.TestCase):
    """CvssSeveritiesCvssV4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CvssSeveritiesCvssV4:
        """Test CvssSeveritiesCvssV4
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CvssSeveritiesCvssV4`
        """
        model = CvssSeveritiesCvssV4()
        if include_optional:
            return CvssSeveritiesCvssV4(
                vector_string = '',
                score = 0
            )
        else:
            return CvssSeveritiesCvssV4(
                vector_string = '',
                score = 0,
        )
        """

    def testCvssSeveritiesCvssV4(self):
        """Test CvssSeveritiesCvssV4"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
