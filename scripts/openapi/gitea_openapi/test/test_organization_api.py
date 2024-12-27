# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_openapi.api.organization_api import OrganizationApi


class TestOrganizationApi(unittest.TestCase):
    """OrganizationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrganizationApi()

    def tearDown(self) -> None:
        pass

    def test_create_org_repo(self) -> None:
        """Test case for create_org_repo

        Create a repository in an organization
        """
        pass

    def test_create_org_repo_deprecated(self) -> None:
        """Test case for create_org_repo_deprecated

        Create a repository in an organization
        """
        pass

    def test_create_org_variable(self) -> None:
        """Test case for create_org_variable

        Create an org-level variable
        """
        pass

    def test_delete_org_secret(self) -> None:
        """Test case for delete_org_secret

        Delete a secret in an organization
        """
        pass

    def test_delete_org_variable(self) -> None:
        """Test case for delete_org_variable

        Delete an org-level variable
        """
        pass

    def test_get_org_variable(self) -> None:
        """Test case for get_org_variable

        Get an org-level variable
        """
        pass

    def test_get_org_variables_list(self) -> None:
        """Test case for get_org_variables_list

        Get an org-level variables list
        """
        pass

    def test_org_add_team_member(self) -> None:
        """Test case for org_add_team_member

        Add a team member
        """
        pass

    def test_org_add_team_repository(self) -> None:
        """Test case for org_add_team_repository

        Add a repository to a team
        """
        pass

    def test_org_conceal_member(self) -> None:
        """Test case for org_conceal_member

        Conceal a user's membership
        """
        pass

    def test_org_create(self) -> None:
        """Test case for org_create

        Create an organization
        """
        pass

    def test_org_create_hook(self) -> None:
        """Test case for org_create_hook

        Create a hook
        """
        pass

    def test_org_create_label(self) -> None:
        """Test case for org_create_label

        Create a label for an organization
        """
        pass

    def test_org_create_team(self) -> None:
        """Test case for org_create_team

        Create a team
        """
        pass

    def test_org_delete(self) -> None:
        """Test case for org_delete

        Delete an organization
        """
        pass

    def test_org_delete_avatar(self) -> None:
        """Test case for org_delete_avatar

        Delete Avatar
        """
        pass

    def test_org_delete_hook(self) -> None:
        """Test case for org_delete_hook

        Delete a hook
        """
        pass

    def test_org_delete_label(self) -> None:
        """Test case for org_delete_label

        Delete a label
        """
        pass

    def test_org_delete_member(self) -> None:
        """Test case for org_delete_member

        Remove a member from an organization
        """
        pass

    def test_org_delete_team(self) -> None:
        """Test case for org_delete_team

        Delete a team
        """
        pass

    def test_org_edit(self) -> None:
        """Test case for org_edit

        Edit an organization
        """
        pass

    def test_org_edit_hook(self) -> None:
        """Test case for org_edit_hook

        Update a hook
        """
        pass

    def test_org_edit_label(self) -> None:
        """Test case for org_edit_label

        Update a label
        """
        pass

    def test_org_edit_team(self) -> None:
        """Test case for org_edit_team

        Edit a team
        """
        pass

    def test_org_get(self) -> None:
        """Test case for org_get

        Get an organization
        """
        pass

    def test_org_get_all(self) -> None:
        """Test case for org_get_all

        Get list of organizations
        """
        pass

    def test_org_get_hook(self) -> None:
        """Test case for org_get_hook

        Get a hook
        """
        pass

    def test_org_get_label(self) -> None:
        """Test case for org_get_label

        Get a single label
        """
        pass

    def test_org_get_runner_registration_token(self) -> None:
        """Test case for org_get_runner_registration_token

        Get an organization's actions runner registration token
        """
        pass

    def test_org_get_team(self) -> None:
        """Test case for org_get_team

        Get a team
        """
        pass

    def test_org_get_user_permissions(self) -> None:
        """Test case for org_get_user_permissions

        Get user permissions in organization
        """
        pass

    def test_org_is_member(self) -> None:
        """Test case for org_is_member

        Check if a user is a member of an organization
        """
        pass

    def test_org_is_public_member(self) -> None:
        """Test case for org_is_public_member

        Check if a user is a public member of an organization
        """
        pass

    def test_org_list_actions_secrets(self) -> None:
        """Test case for org_list_actions_secrets

        List an organization's actions secrets
        """
        pass

    def test_org_list_activity_feeds(self) -> None:
        """Test case for org_list_activity_feeds

        List an organization's activity feeds
        """
        pass

    def test_org_list_current_user_orgs(self) -> None:
        """Test case for org_list_current_user_orgs

        List the current user's organizations
        """
        pass

    def test_org_list_hooks(self) -> None:
        """Test case for org_list_hooks

        List an organization's webhooks
        """
        pass

    def test_org_list_labels(self) -> None:
        """Test case for org_list_labels

        List an organization's labels
        """
        pass

    def test_org_list_members(self) -> None:
        """Test case for org_list_members

        List an organization's members
        """
        pass

    def test_org_list_public_members(self) -> None:
        """Test case for org_list_public_members

        List an organization's public members
        """
        pass

    def test_org_list_repos(self) -> None:
        """Test case for org_list_repos

        List an organization's repos
        """
        pass

    def test_org_list_team_activity_feeds(self) -> None:
        """Test case for org_list_team_activity_feeds

        List a team's activity feeds
        """
        pass

    def test_org_list_team_member(self) -> None:
        """Test case for org_list_team_member

        List a particular member of team
        """
        pass

    def test_org_list_team_members(self) -> None:
        """Test case for org_list_team_members

        List a team's members
        """
        pass

    def test_org_list_team_repo(self) -> None:
        """Test case for org_list_team_repo

        List a particular repo of team
        """
        pass

    def test_org_list_team_repos(self) -> None:
        """Test case for org_list_team_repos

        List a team's repos
        """
        pass

    def test_org_list_teams(self) -> None:
        """Test case for org_list_teams

        List an organization's teams
        """
        pass

    def test_org_list_user_orgs(self) -> None:
        """Test case for org_list_user_orgs

        List a user's organizations
        """
        pass

    def test_org_publicize_member(self) -> None:
        """Test case for org_publicize_member

        Publicize a user's membership
        """
        pass

    def test_org_remove_team_member(self) -> None:
        """Test case for org_remove_team_member

        Remove a team member
        """
        pass

    def test_org_remove_team_repository(self) -> None:
        """Test case for org_remove_team_repository

        Remove a repository from a team
        """
        pass

    def test_org_update_avatar(self) -> None:
        """Test case for org_update_avatar

        Update Avatar
        """
        pass

    def test_organization_block_user(self) -> None:
        """Test case for organization_block_user

        Block a user
        """
        pass

    def test_organization_check_user_block(self) -> None:
        """Test case for organization_check_user_block

        Check if a user is blocked by the organization
        """
        pass

    def test_organization_list_blocks(self) -> None:
        """Test case for organization_list_blocks

        List users blocked by the organization
        """
        pass

    def test_organization_unblock_user(self) -> None:
        """Test case for organization_unblock_user

        Unblock a user
        """
        pass

    def test_team_search(self) -> None:
        """Test case for team_search

        Search for teams within an organization
        """
        pass

    def test_update_org_secret(self) -> None:
        """Test case for update_org_secret

        Create or Update a secret value in an organization
        """
        pass

    def test_update_org_variable(self) -> None:
        """Test case for update_org_variable

        Update an org-level variable
        """
        pass


if __name__ == '__main__':
    unittest.main()