# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.api.orgs_api import OrgsApi


class TestOrgsApi(unittest.TestCase):
    """OrgsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrgsApi()

    def tearDown(self) -> None:
        pass

    def test_api_insights_get_route_stats_by_actor(self) -> None:
        """Test case for api_insights_get_route_stats_by_actor

        Get route stats by actor
        """
        pass

    def test_api_insights_get_subject_stats(self) -> None:
        """Test case for api_insights_get_subject_stats

        Get subject stats
        """
        pass

    def test_api_insights_get_summary_stats(self) -> None:
        """Test case for api_insights_get_summary_stats

        Get summary stats
        """
        pass

    def test_api_insights_get_summary_stats_by_actor(self) -> None:
        """Test case for api_insights_get_summary_stats_by_actor

        Get summary stats by actor
        """
        pass

    def test_api_insights_get_summary_stats_by_user(self) -> None:
        """Test case for api_insights_get_summary_stats_by_user

        Get summary stats by user
        """
        pass

    def test_api_insights_get_time_stats(self) -> None:
        """Test case for api_insights_get_time_stats

        Get time stats
        """
        pass

    def test_api_insights_get_time_stats_by_actor(self) -> None:
        """Test case for api_insights_get_time_stats_by_actor

        Get time stats by actor
        """
        pass

    def test_api_insights_get_time_stats_by_user(self) -> None:
        """Test case for api_insights_get_time_stats_by_user

        Get time stats by user
        """
        pass

    def test_api_insights_get_user_stats(self) -> None:
        """Test case for api_insights_get_user_stats

        Get user stats
        """
        pass

    def test_orgs_add_security_manager_team(self) -> None:
        """Test case for orgs_add_security_manager_team

        Add a security manager team
        """
        pass

    def test_orgs_assign_team_to_org_role(self) -> None:
        """Test case for orgs_assign_team_to_org_role

        Assign an organization role to a team
        """
        pass

    def test_orgs_assign_user_to_org_role(self) -> None:
        """Test case for orgs_assign_user_to_org_role

        Assign an organization role to a user
        """
        pass

    def test_orgs_block_user(self) -> None:
        """Test case for orgs_block_user

        Block a user from an organization
        """
        pass

    def test_orgs_cancel_invitation(self) -> None:
        """Test case for orgs_cancel_invitation

        Cancel an organization invitation
        """
        pass

    def test_orgs_check_blocked_user(self) -> None:
        """Test case for orgs_check_blocked_user

        Check if a user is blocked by an organization
        """
        pass

    def test_orgs_check_membership_for_user(self) -> None:
        """Test case for orgs_check_membership_for_user

        Check organization membership for a user
        """
        pass

    def test_orgs_check_public_membership_for_user(self) -> None:
        """Test case for orgs_check_public_membership_for_user

        Check public organization membership for a user
        """
        pass

    def test_orgs_convert_member_to_outside_collaborator(self) -> None:
        """Test case for orgs_convert_member_to_outside_collaborator

        Convert an organization member to outside collaborator
        """
        pass

    def test_orgs_create_invitation(self) -> None:
        """Test case for orgs_create_invitation

        Create an organization invitation
        """
        pass

    def test_orgs_create_or_update_custom_properties(self) -> None:
        """Test case for orgs_create_or_update_custom_properties

        Create or update custom properties for an organization
        """
        pass

    def test_orgs_create_or_update_custom_properties_values_for_repos(self) -> None:
        """Test case for orgs_create_or_update_custom_properties_values_for_repos

        Create or update custom property values for organization repositories
        """
        pass

    def test_orgs_create_or_update_custom_property(self) -> None:
        """Test case for orgs_create_or_update_custom_property

        Create or update a custom property for an organization
        """
        pass

    def test_orgs_create_webhook(self) -> None:
        """Test case for orgs_create_webhook

        Create an organization webhook
        """
        pass

    def test_orgs_delete(self) -> None:
        """Test case for orgs_delete

        Delete an organization
        """
        pass

    def test_orgs_delete_webhook(self) -> None:
        """Test case for orgs_delete_webhook

        Delete an organization webhook
        """
        pass

    def test_orgs_enable_or_disable_security_product_on_all_org_repos(self) -> None:
        """Test case for orgs_enable_or_disable_security_product_on_all_org_repos

        Enable or disable a security feature for an organization
        """
        pass

    def test_orgs_get(self) -> None:
        """Test case for orgs_get

        Get an organization
        """
        pass

    def test_orgs_get_all_custom_properties(self) -> None:
        """Test case for orgs_get_all_custom_properties

        Get all custom properties for an organization
        """
        pass

    def test_orgs_get_custom_property(self) -> None:
        """Test case for orgs_get_custom_property

        Get a custom property for an organization
        """
        pass

    def test_orgs_get_membership_for_authenticated_user(self) -> None:
        """Test case for orgs_get_membership_for_authenticated_user

        Get an organization membership for the authenticated user
        """
        pass

    def test_orgs_get_membership_for_user(self) -> None:
        """Test case for orgs_get_membership_for_user

        Get organization membership for a user
        """
        pass

    def test_orgs_get_org_role(self) -> None:
        """Test case for orgs_get_org_role

        Get an organization role
        """
        pass

    def test_orgs_get_webhook(self) -> None:
        """Test case for orgs_get_webhook

        Get an organization webhook
        """
        pass

    def test_orgs_get_webhook_config_for_org(self) -> None:
        """Test case for orgs_get_webhook_config_for_org

        Get a webhook configuration for an organization
        """
        pass

    def test_orgs_get_webhook_delivery(self) -> None:
        """Test case for orgs_get_webhook_delivery

        Get a webhook delivery for an organization webhook
        """
        pass

    def test_orgs_list(self) -> None:
        """Test case for orgs_list

        List organizations
        """
        pass

    def test_orgs_list_app_installations(self) -> None:
        """Test case for orgs_list_app_installations

        List app installations for an organization
        """
        pass

    def test_orgs_list_attestations(self) -> None:
        """Test case for orgs_list_attestations

        List attestations
        """
        pass

    def test_orgs_list_blocked_users(self) -> None:
        """Test case for orgs_list_blocked_users

        List users blocked by an organization
        """
        pass

    def test_orgs_list_custom_properties_values_for_repos(self) -> None:
        """Test case for orgs_list_custom_properties_values_for_repos

        List custom property values for organization repositories
        """
        pass

    def test_orgs_list_failed_invitations(self) -> None:
        """Test case for orgs_list_failed_invitations

        List failed organization invitations
        """
        pass

    def test_orgs_list_for_authenticated_user(self) -> None:
        """Test case for orgs_list_for_authenticated_user

        List organizations for the authenticated user
        """
        pass

    def test_orgs_list_for_user(self) -> None:
        """Test case for orgs_list_for_user

        List organizations for a user
        """
        pass

    def test_orgs_list_invitation_teams(self) -> None:
        """Test case for orgs_list_invitation_teams

        List organization invitation teams
        """
        pass

    def test_orgs_list_members(self) -> None:
        """Test case for orgs_list_members

        List organization members
        """
        pass

    def test_orgs_list_memberships_for_authenticated_user(self) -> None:
        """Test case for orgs_list_memberships_for_authenticated_user

        List organization memberships for the authenticated user
        """
        pass

    def test_orgs_list_org_role_teams(self) -> None:
        """Test case for orgs_list_org_role_teams

        List teams that are assigned to an organization role
        """
        pass

    def test_orgs_list_org_role_users(self) -> None:
        """Test case for orgs_list_org_role_users

        List users that are assigned to an organization role
        """
        pass

    def test_orgs_list_org_roles(self) -> None:
        """Test case for orgs_list_org_roles

        Get all organization roles for an organization
        """
        pass

    def test_orgs_list_outside_collaborators(self) -> None:
        """Test case for orgs_list_outside_collaborators

        List outside collaborators for an organization
        """
        pass

    def test_orgs_list_pat_grant_repositories(self) -> None:
        """Test case for orgs_list_pat_grant_repositories

        List repositories a fine-grained personal access token has access to
        """
        pass

    def test_orgs_list_pat_grant_request_repositories(self) -> None:
        """Test case for orgs_list_pat_grant_request_repositories

        List repositories requested to be accessed by a fine-grained personal access token
        """
        pass

    def test_orgs_list_pat_grant_requests(self) -> None:
        """Test case for orgs_list_pat_grant_requests

        List requests to access organization resources with fine-grained personal access tokens
        """
        pass

    def test_orgs_list_pat_grants(self) -> None:
        """Test case for orgs_list_pat_grants

        List fine-grained personal access tokens with access to organization resources
        """
        pass

    def test_orgs_list_pending_invitations(self) -> None:
        """Test case for orgs_list_pending_invitations

        List pending organization invitations
        """
        pass

    def test_orgs_list_public_members(self) -> None:
        """Test case for orgs_list_public_members

        List public organization members
        """
        pass

    def test_orgs_list_security_manager_teams(self) -> None:
        """Test case for orgs_list_security_manager_teams

        List security manager teams
        """
        pass

    def test_orgs_list_webhook_deliveries(self) -> None:
        """Test case for orgs_list_webhook_deliveries

        List deliveries for an organization webhook
        """
        pass

    def test_orgs_list_webhooks(self) -> None:
        """Test case for orgs_list_webhooks

        List organization webhooks
        """
        pass

    def test_orgs_ping_webhook(self) -> None:
        """Test case for orgs_ping_webhook

        Ping an organization webhook
        """
        pass

    def test_orgs_redeliver_webhook_delivery(self) -> None:
        """Test case for orgs_redeliver_webhook_delivery

        Redeliver a delivery for an organization webhook
        """
        pass

    def test_orgs_remove_custom_property(self) -> None:
        """Test case for orgs_remove_custom_property

        Remove a custom property for an organization
        """
        pass

    def test_orgs_remove_member(self) -> None:
        """Test case for orgs_remove_member

        Remove an organization member
        """
        pass

    def test_orgs_remove_membership_for_user(self) -> None:
        """Test case for orgs_remove_membership_for_user

        Remove organization membership for a user
        """
        pass

    def test_orgs_remove_outside_collaborator(self) -> None:
        """Test case for orgs_remove_outside_collaborator

        Remove outside collaborator from an organization
        """
        pass

    def test_orgs_remove_public_membership_for_authenticated_user(self) -> None:
        """Test case for orgs_remove_public_membership_for_authenticated_user

        Remove public organization membership for the authenticated user
        """
        pass

    def test_orgs_remove_security_manager_team(self) -> None:
        """Test case for orgs_remove_security_manager_team

        Remove a security manager team
        """
        pass

    def test_orgs_review_pat_grant_request(self) -> None:
        """Test case for orgs_review_pat_grant_request

        Review a request to access organization resources with a fine-grained personal access token
        """
        pass

    def test_orgs_review_pat_grant_requests_in_bulk(self) -> None:
        """Test case for orgs_review_pat_grant_requests_in_bulk

        Review requests to access organization resources with fine-grained personal access tokens
        """
        pass

    def test_orgs_revoke_all_org_roles_team(self) -> None:
        """Test case for orgs_revoke_all_org_roles_team

        Remove all organization roles for a team
        """
        pass

    def test_orgs_revoke_all_org_roles_user(self) -> None:
        """Test case for orgs_revoke_all_org_roles_user

        Remove all organization roles for a user
        """
        pass

    def test_orgs_revoke_org_role_team(self) -> None:
        """Test case for orgs_revoke_org_role_team

        Remove an organization role from a team
        """
        pass

    def test_orgs_revoke_org_role_user(self) -> None:
        """Test case for orgs_revoke_org_role_user

        Remove an organization role from a user
        """
        pass

    def test_orgs_set_membership_for_user(self) -> None:
        """Test case for orgs_set_membership_for_user

        Set organization membership for a user
        """
        pass

    def test_orgs_set_public_membership_for_authenticated_user(self) -> None:
        """Test case for orgs_set_public_membership_for_authenticated_user

        Set public organization membership for the authenticated user
        """
        pass

    def test_orgs_unblock_user(self) -> None:
        """Test case for orgs_unblock_user

        Unblock a user from an organization
        """
        pass

    def test_orgs_update(self) -> None:
        """Test case for orgs_update

        Update an organization
        """
        pass

    def test_orgs_update_membership_for_authenticated_user(self) -> None:
        """Test case for orgs_update_membership_for_authenticated_user

        Update an organization membership for the authenticated user
        """
        pass

    def test_orgs_update_pat_access(self) -> None:
        """Test case for orgs_update_pat_access

        Update the access a fine-grained personal access token has to organization resources
        """
        pass

    def test_orgs_update_pat_accesses(self) -> None:
        """Test case for orgs_update_pat_accesses

        Update the access to organization resources via fine-grained personal access tokens
        """
        pass

    def test_orgs_update_webhook(self) -> None:
        """Test case for orgs_update_webhook

        Update an organization webhook
        """
        pass

    def test_orgs_update_webhook_config_for_org(self) -> None:
        """Test case for orgs_update_webhook_config_for_org

        Update a webhook configuration for an organization
        """
        pass


if __name__ == '__main__':
    unittest.main()
