# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.api.migrations_api import MigrationsApi


class TestMigrationsApi(unittest.TestCase):
    """MigrationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MigrationsApi()

    def tearDown(self) -> None:
        pass

    def test_migrations_cancel_import(self) -> None:
        """Test case for migrations_cancel_import

        Cancel an import
        """
        pass

    def test_migrations_delete_archive_for_authenticated_user(self) -> None:
        """Test case for migrations_delete_archive_for_authenticated_user

        Delete a user migration archive
        """
        pass

    def test_migrations_delete_archive_for_org(self) -> None:
        """Test case for migrations_delete_archive_for_org

        Delete an organization migration archive
        """
        pass

    def test_migrations_download_archive_for_org(self) -> None:
        """Test case for migrations_download_archive_for_org

        Download an organization migration archive
        """
        pass

    def test_migrations_get_archive_for_authenticated_user(self) -> None:
        """Test case for migrations_get_archive_for_authenticated_user

        Download a user migration archive
        """
        pass

    def test_migrations_get_commit_authors(self) -> None:
        """Test case for migrations_get_commit_authors

        Get commit authors
        """
        pass

    def test_migrations_get_import_status(self) -> None:
        """Test case for migrations_get_import_status

        Get an import status
        """
        pass

    def test_migrations_get_large_files(self) -> None:
        """Test case for migrations_get_large_files

        Get large files
        """
        pass

    def test_migrations_get_status_for_authenticated_user(self) -> None:
        """Test case for migrations_get_status_for_authenticated_user

        Get a user migration status
        """
        pass

    def test_migrations_get_status_for_org(self) -> None:
        """Test case for migrations_get_status_for_org

        Get an organization migration status
        """
        pass

    def test_migrations_list_for_authenticated_user(self) -> None:
        """Test case for migrations_list_for_authenticated_user

        List user migrations
        """
        pass

    def test_migrations_list_for_org(self) -> None:
        """Test case for migrations_list_for_org

        List organization migrations
        """
        pass

    def test_migrations_list_repos_for_authenticated_user(self) -> None:
        """Test case for migrations_list_repos_for_authenticated_user

        List repositories for a user migration
        """
        pass

    def test_migrations_list_repos_for_org(self) -> None:
        """Test case for migrations_list_repos_for_org

        List repositories in an organization migration
        """
        pass

    def test_migrations_map_commit_author(self) -> None:
        """Test case for migrations_map_commit_author

        Map a commit author
        """
        pass

    def test_migrations_set_lfs_preference(self) -> None:
        """Test case for migrations_set_lfs_preference

        Update Git LFS preference
        """
        pass

    def test_migrations_start_for_authenticated_user(self) -> None:
        """Test case for migrations_start_for_authenticated_user

        Start a user migration
        """
        pass

    def test_migrations_start_for_org(self) -> None:
        """Test case for migrations_start_for_org

        Start an organization migration
        """
        pass

    def test_migrations_start_import(self) -> None:
        """Test case for migrations_start_import

        Start an import
        """
        pass

    def test_migrations_unlock_repo_for_authenticated_user(self) -> None:
        """Test case for migrations_unlock_repo_for_authenticated_user

        Unlock a user repository
        """
        pass

    def test_migrations_unlock_repo_for_org(self) -> None:
        """Test case for migrations_unlock_repo_for_org

        Unlock an organization repository
        """
        pass

    def test_migrations_update_import(self) -> None:
        """Test case for migrations_update_import

        Update an import
        """
        pass


if __name__ == '__main__':
    unittest.main()
