# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.api.projects_api import ProjectsApi


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectsApi()

    def tearDown(self) -> None:
        pass

    def test_projects_add_collaborator(self) -> None:
        """Test case for projects_add_collaborator

        Add project collaborator
        """
        pass

    def test_projects_create_card(self) -> None:
        """Test case for projects_create_card

        Create a project card
        """
        pass

    def test_projects_create_column(self) -> None:
        """Test case for projects_create_column

        Create a project column
        """
        pass

    def test_projects_create_for_authenticated_user(self) -> None:
        """Test case for projects_create_for_authenticated_user

        Create a user project
        """
        pass

    def test_projects_create_for_org(self) -> None:
        """Test case for projects_create_for_org

        Create an organization project
        """
        pass

    def test_projects_create_for_repo(self) -> None:
        """Test case for projects_create_for_repo

        Create a repository project
        """
        pass

    def test_projects_delete(self) -> None:
        """Test case for projects_delete

        Delete a project
        """
        pass

    def test_projects_delete_card(self) -> None:
        """Test case for projects_delete_card

        Delete a project card
        """
        pass

    def test_projects_delete_column(self) -> None:
        """Test case for projects_delete_column

        Delete a project column
        """
        pass

    def test_projects_get(self) -> None:
        """Test case for projects_get

        Get a project
        """
        pass

    def test_projects_get_card(self) -> None:
        """Test case for projects_get_card

        Get a project card
        """
        pass

    def test_projects_get_column(self) -> None:
        """Test case for projects_get_column

        Get a project column
        """
        pass

    def test_projects_get_permission_for_user(self) -> None:
        """Test case for projects_get_permission_for_user

        Get project permission for a user
        """
        pass

    def test_projects_list_cards(self) -> None:
        """Test case for projects_list_cards

        List project cards
        """
        pass

    def test_projects_list_collaborators(self) -> None:
        """Test case for projects_list_collaborators

        List project collaborators
        """
        pass

    def test_projects_list_columns(self) -> None:
        """Test case for projects_list_columns

        List project columns
        """
        pass

    def test_projects_list_for_org(self) -> None:
        """Test case for projects_list_for_org

        List organization projects
        """
        pass

    def test_projects_list_for_repo(self) -> None:
        """Test case for projects_list_for_repo

        List repository projects
        """
        pass

    def test_projects_list_for_user(self) -> None:
        """Test case for projects_list_for_user

        List user projects
        """
        pass

    def test_projects_move_card(self) -> None:
        """Test case for projects_move_card

        Move a project card
        """
        pass

    def test_projects_move_column(self) -> None:
        """Test case for projects_move_column

        Move a project column
        """
        pass

    def test_projects_remove_collaborator(self) -> None:
        """Test case for projects_remove_collaborator

        Remove user as a collaborator
        """
        pass

    def test_projects_update(self) -> None:
        """Test case for projects_update

        Update a project
        """
        pass

    def test_projects_update_card(self) -> None:
        """Test case for projects_update_card

        Update an existing project card
        """
        pass

    def test_projects_update_column(self) -> None:
        """Test case for projects_update_column

        Update an existing project column
        """
        pass


if __name__ == '__main__':
    unittest.main()
