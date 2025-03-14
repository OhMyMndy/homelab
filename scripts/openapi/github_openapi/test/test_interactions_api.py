# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.api.interactions_api import InteractionsApi


class TestInteractionsApi(unittest.TestCase):
    """InteractionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InteractionsApi()

    def tearDown(self) -> None:
        pass

    def test_interactions_get_restrictions_for_authenticated_user(self) -> None:
        """Test case for interactions_get_restrictions_for_authenticated_user

        Get interaction restrictions for your public repositories
        """
        pass

    def test_interactions_get_restrictions_for_org(self) -> None:
        """Test case for interactions_get_restrictions_for_org

        Get interaction restrictions for an organization
        """
        pass

    def test_interactions_get_restrictions_for_repo(self) -> None:
        """Test case for interactions_get_restrictions_for_repo

        Get interaction restrictions for a repository
        """
        pass

    def test_interactions_remove_restrictions_for_authenticated_user(self) -> None:
        """Test case for interactions_remove_restrictions_for_authenticated_user

        Remove interaction restrictions from your public repositories
        """
        pass

    def test_interactions_remove_restrictions_for_org(self) -> None:
        """Test case for interactions_remove_restrictions_for_org

        Remove interaction restrictions for an organization
        """
        pass

    def test_interactions_remove_restrictions_for_repo(self) -> None:
        """Test case for interactions_remove_restrictions_for_repo

        Remove interaction restrictions for a repository
        """
        pass

    def test_interactions_set_restrictions_for_authenticated_user(self) -> None:
        """Test case for interactions_set_restrictions_for_authenticated_user

        Set interaction restrictions for your public repositories
        """
        pass

    def test_interactions_set_restrictions_for_org(self) -> None:
        """Test case for interactions_set_restrictions_for_org

        Set interaction restrictions for an organization
        """
        pass

    def test_interactions_set_restrictions_for_repo(self) -> None:
        """Test case for interactions_set_restrictions_for_repo

        Set interaction restrictions for a repository
        """
        pass


if __name__ == '__main__':
    unittest.main()
