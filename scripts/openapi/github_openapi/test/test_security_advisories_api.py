# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.api.security_advisories_api import SecurityAdvisoriesApi


class TestSecurityAdvisoriesApi(unittest.TestCase):
    """SecurityAdvisoriesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SecurityAdvisoriesApi()

    def tearDown(self) -> None:
        pass

    def test_security_advisories_create_fork(self) -> None:
        """Test case for security_advisories_create_fork

        Create a temporary private fork
        """
        pass

    def test_security_advisories_create_private_vulnerability_report(self) -> None:
        """Test case for security_advisories_create_private_vulnerability_report

        Privately report a security vulnerability
        """
        pass

    def test_security_advisories_create_repository_advisory(self) -> None:
        """Test case for security_advisories_create_repository_advisory

        Create a repository security advisory
        """
        pass

    def test_security_advisories_create_repository_advisory_cve_request(self) -> None:
        """Test case for security_advisories_create_repository_advisory_cve_request

        Request a CVE for a repository security advisory
        """
        pass

    def test_security_advisories_get_global_advisory(self) -> None:
        """Test case for security_advisories_get_global_advisory

        Get a global security advisory
        """
        pass

    def test_security_advisories_get_repository_advisory(self) -> None:
        """Test case for security_advisories_get_repository_advisory

        Get a repository security advisory
        """
        pass

    def test_security_advisories_list_global_advisories(self) -> None:
        """Test case for security_advisories_list_global_advisories

        List global security advisories
        """
        pass

    def test_security_advisories_list_org_repository_advisories(self) -> None:
        """Test case for security_advisories_list_org_repository_advisories

        List repository security advisories for an organization
        """
        pass

    def test_security_advisories_list_repository_advisories(self) -> None:
        """Test case for security_advisories_list_repository_advisories

        List repository security advisories
        """
        pass

    def test_security_advisories_update_repository_advisory(self) -> None:
        """Test case for security_advisories_update_repository_advisory

        Update a repository security advisory
        """
        pass


if __name__ == '__main__':
    unittest.main()
