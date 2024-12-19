# github_openapi.ReposApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repos_accept_invitation_for_authenticated_user**](ReposApi.md#repos_accept_invitation_for_authenticated_user) | **PATCH** /user/repository_invitations/{invitation_id} | Accept a repository invitation
[**repos_add_app_access_restrictions**](ReposApi.md#repos_add_app_access_restrictions) | **POST** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | Add app access restrictions
[**repos_add_collaborator**](ReposApi.md#repos_add_collaborator) | **PUT** /repos/{owner}/{repo}/collaborators/{username} | Add a repository collaborator
[**repos_add_status_check_contexts**](ReposApi.md#repos_add_status_check_contexts) | **POST** /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | Add status check contexts
[**repos_add_team_access_restrictions**](ReposApi.md#repos_add_team_access_restrictions) | **POST** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | Add team access restrictions
[**repos_add_user_access_restrictions**](ReposApi.md#repos_add_user_access_restrictions) | **POST** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | Add user access restrictions
[**repos_cancel_pages_deployment**](ReposApi.md#repos_cancel_pages_deployment) | **POST** /repos/{owner}/{repo}/pages/deployments/{pages_deployment_id}/cancel | Cancel a GitHub Pages deployment
[**repos_check_automated_security_fixes**](ReposApi.md#repos_check_automated_security_fixes) | **GET** /repos/{owner}/{repo}/automated-security-fixes | Check if automated security fixes are enabled for a repository
[**repos_check_collaborator**](ReposApi.md#repos_check_collaborator) | **GET** /repos/{owner}/{repo}/collaborators/{username} | Check if a user is a repository collaborator
[**repos_check_private_vulnerability_reporting**](ReposApi.md#repos_check_private_vulnerability_reporting) | **GET** /repos/{owner}/{repo}/private-vulnerability-reporting | Check if private vulnerability reporting is enabled for a repository
[**repos_check_vulnerability_alerts**](ReposApi.md#repos_check_vulnerability_alerts) | **GET** /repos/{owner}/{repo}/vulnerability-alerts | Check if vulnerability alerts are enabled for a repository
[**repos_codeowners_errors**](ReposApi.md#repos_codeowners_errors) | **GET** /repos/{owner}/{repo}/codeowners/errors | List CODEOWNERS errors
[**repos_compare_commits**](ReposApi.md#repos_compare_commits) | **GET** /repos/{owner}/{repo}/compare/{basehead} | Compare two commits
[**repos_create_attestation**](ReposApi.md#repos_create_attestation) | **POST** /repos/{owner}/{repo}/attestations | Create an attestation
[**repos_create_autolink**](ReposApi.md#repos_create_autolink) | **POST** /repos/{owner}/{repo}/autolinks | Create an autolink reference for a repository
[**repos_create_commit_comment**](ReposApi.md#repos_create_commit_comment) | **POST** /repos/{owner}/{repo}/commits/{commit_sha}/comments | Create a commit comment
[**repos_create_commit_signature_protection**](ReposApi.md#repos_create_commit_signature_protection) | **POST** /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures | Create commit signature protection
[**repos_create_commit_status**](ReposApi.md#repos_create_commit_status) | **POST** /repos/{owner}/{repo}/statuses/{sha} | Create a commit status
[**repos_create_deploy_key**](ReposApi.md#repos_create_deploy_key) | **POST** /repos/{owner}/{repo}/keys | Create a deploy key
[**repos_create_deployment**](ReposApi.md#repos_create_deployment) | **POST** /repos/{owner}/{repo}/deployments | Create a deployment
[**repos_create_deployment_branch_policy**](ReposApi.md#repos_create_deployment_branch_policy) | **POST** /repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies | Create a deployment branch policy
[**repos_create_deployment_protection_rule**](ReposApi.md#repos_create_deployment_protection_rule) | **POST** /repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules | Create a custom deployment protection rule on an environment
[**repos_create_deployment_status**](ReposApi.md#repos_create_deployment_status) | **POST** /repos/{owner}/{repo}/deployments/{deployment_id}/statuses | Create a deployment status
[**repos_create_dispatch_event**](ReposApi.md#repos_create_dispatch_event) | **POST** /repos/{owner}/{repo}/dispatches | Create a repository dispatch event
[**repos_create_for_authenticated_user**](ReposApi.md#repos_create_for_authenticated_user) | **POST** /user/repos | Create a repository for the authenticated user
[**repos_create_fork**](ReposApi.md#repos_create_fork) | **POST** /repos/{owner}/{repo}/forks | Create a fork
[**repos_create_in_org**](ReposApi.md#repos_create_in_org) | **POST** /orgs/{org}/repos | Create an organization repository
[**repos_create_or_update_custom_properties_values**](ReposApi.md#repos_create_or_update_custom_properties_values) | **PATCH** /repos/{owner}/{repo}/properties/values | Create or update custom property values for a repository
[**repos_create_or_update_environment**](ReposApi.md#repos_create_or_update_environment) | **PUT** /repos/{owner}/{repo}/environments/{environment_name} | Create or update an environment
[**repos_create_or_update_file_contents**](ReposApi.md#repos_create_or_update_file_contents) | **PUT** /repos/{owner}/{repo}/contents/{path} | Create or update file contents
[**repos_create_org_ruleset**](ReposApi.md#repos_create_org_ruleset) | **POST** /orgs/{org}/rulesets | Create an organization repository ruleset
[**repos_create_pages_deployment**](ReposApi.md#repos_create_pages_deployment) | **POST** /repos/{owner}/{repo}/pages/deployments | Create a GitHub Pages deployment
[**repos_create_pages_site**](ReposApi.md#repos_create_pages_site) | **POST** /repos/{owner}/{repo}/pages | Create a GitHub Pages site
[**repos_create_release**](ReposApi.md#repos_create_release) | **POST** /repos/{owner}/{repo}/releases | Create a release
[**repos_create_repo_ruleset**](ReposApi.md#repos_create_repo_ruleset) | **POST** /repos/{owner}/{repo}/rulesets | Create a repository ruleset
[**repos_create_tag_protection**](ReposApi.md#repos_create_tag_protection) | **POST** /repos/{owner}/{repo}/tags/protection | Closing down - Create a tag protection state for a repository
[**repos_create_using_template**](ReposApi.md#repos_create_using_template) | **POST** /repos/{template_owner}/{template_repo}/generate | Create a repository using a template
[**repos_create_webhook**](ReposApi.md#repos_create_webhook) | **POST** /repos/{owner}/{repo}/hooks | Create a repository webhook
[**repos_decline_invitation_for_authenticated_user**](ReposApi.md#repos_decline_invitation_for_authenticated_user) | **DELETE** /user/repository_invitations/{invitation_id} | Decline a repository invitation
[**repos_delete**](ReposApi.md#repos_delete) | **DELETE** /repos/{owner}/{repo} | Delete a repository
[**repos_delete_access_restrictions**](ReposApi.md#repos_delete_access_restrictions) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions | Delete access restrictions
[**repos_delete_admin_branch_protection**](ReposApi.md#repos_delete_admin_branch_protection) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins | Delete admin branch protection
[**repos_delete_an_environment**](ReposApi.md#repos_delete_an_environment) | **DELETE** /repos/{owner}/{repo}/environments/{environment_name} | Delete an environment
[**repos_delete_autolink**](ReposApi.md#repos_delete_autolink) | **DELETE** /repos/{owner}/{repo}/autolinks/{autolink_id} | Delete an autolink reference from a repository
[**repos_delete_branch_protection**](ReposApi.md#repos_delete_branch_protection) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection | Delete branch protection
[**repos_delete_commit_comment**](ReposApi.md#repos_delete_commit_comment) | **DELETE** /repos/{owner}/{repo}/comments/{comment_id} | Delete a commit comment
[**repos_delete_commit_signature_protection**](ReposApi.md#repos_delete_commit_signature_protection) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures | Delete commit signature protection
[**repos_delete_deploy_key**](ReposApi.md#repos_delete_deploy_key) | **DELETE** /repos/{owner}/{repo}/keys/{key_id} | Delete a deploy key
[**repos_delete_deployment**](ReposApi.md#repos_delete_deployment) | **DELETE** /repos/{owner}/{repo}/deployments/{deployment_id} | Delete a deployment
[**repos_delete_deployment_branch_policy**](ReposApi.md#repos_delete_deployment_branch_policy) | **DELETE** /repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id} | Delete a deployment branch policy
[**repos_delete_file**](ReposApi.md#repos_delete_file) | **DELETE** /repos/{owner}/{repo}/contents/{path} | Delete a file
[**repos_delete_invitation**](ReposApi.md#repos_delete_invitation) | **DELETE** /repos/{owner}/{repo}/invitations/{invitation_id} | Delete a repository invitation
[**repos_delete_org_ruleset**](ReposApi.md#repos_delete_org_ruleset) | **DELETE** /orgs/{org}/rulesets/{ruleset_id} | Delete an organization repository ruleset
[**repos_delete_pages_site**](ReposApi.md#repos_delete_pages_site) | **DELETE** /repos/{owner}/{repo}/pages | Delete a GitHub Pages site
[**repos_delete_pull_request_review_protection**](ReposApi.md#repos_delete_pull_request_review_protection) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews | Delete pull request review protection
[**repos_delete_release**](ReposApi.md#repos_delete_release) | **DELETE** /repos/{owner}/{repo}/releases/{release_id} | Delete a release
[**repos_delete_release_asset**](ReposApi.md#repos_delete_release_asset) | **DELETE** /repos/{owner}/{repo}/releases/assets/{asset_id} | Delete a release asset
[**repos_delete_repo_ruleset**](ReposApi.md#repos_delete_repo_ruleset) | **DELETE** /repos/{owner}/{repo}/rulesets/{ruleset_id} | Delete a repository ruleset
[**repos_delete_tag_protection**](ReposApi.md#repos_delete_tag_protection) | **DELETE** /repos/{owner}/{repo}/tags/protection/{tag_protection_id} | Closing down - Delete a tag protection state for a repository
[**repos_delete_webhook**](ReposApi.md#repos_delete_webhook) | **DELETE** /repos/{owner}/{repo}/hooks/{hook_id} | Delete a repository webhook
[**repos_disable_automated_security_fixes**](ReposApi.md#repos_disable_automated_security_fixes) | **DELETE** /repos/{owner}/{repo}/automated-security-fixes | Disable automated security fixes
[**repos_disable_deployment_protection_rule**](ReposApi.md#repos_disable_deployment_protection_rule) | **DELETE** /repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/{protection_rule_id} | Disable a custom protection rule for an environment
[**repos_disable_private_vulnerability_reporting**](ReposApi.md#repos_disable_private_vulnerability_reporting) | **DELETE** /repos/{owner}/{repo}/private-vulnerability-reporting | Disable private vulnerability reporting for a repository
[**repos_disable_vulnerability_alerts**](ReposApi.md#repos_disable_vulnerability_alerts) | **DELETE** /repos/{owner}/{repo}/vulnerability-alerts | Disable vulnerability alerts
[**repos_download_tarball_archive**](ReposApi.md#repos_download_tarball_archive) | **GET** /repos/{owner}/{repo}/tarball/{ref} | Download a repository archive (tar)
[**repos_download_zipball_archive**](ReposApi.md#repos_download_zipball_archive) | **GET** /repos/{owner}/{repo}/zipball/{ref} | Download a repository archive (zip)
[**repos_enable_automated_security_fixes**](ReposApi.md#repos_enable_automated_security_fixes) | **PUT** /repos/{owner}/{repo}/automated-security-fixes | Enable automated security fixes
[**repos_enable_private_vulnerability_reporting**](ReposApi.md#repos_enable_private_vulnerability_reporting) | **PUT** /repos/{owner}/{repo}/private-vulnerability-reporting | Enable private vulnerability reporting for a repository
[**repos_enable_vulnerability_alerts**](ReposApi.md#repos_enable_vulnerability_alerts) | **PUT** /repos/{owner}/{repo}/vulnerability-alerts | Enable vulnerability alerts
[**repos_generate_release_notes**](ReposApi.md#repos_generate_release_notes) | **POST** /repos/{owner}/{repo}/releases/generate-notes | Generate release notes content for a release
[**repos_get**](ReposApi.md#repos_get) | **GET** /repos/{owner}/{repo} | Get a repository
[**repos_get_access_restrictions**](ReposApi.md#repos_get_access_restrictions) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions | Get access restrictions
[**repos_get_admin_branch_protection**](ReposApi.md#repos_get_admin_branch_protection) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins | Get admin branch protection
[**repos_get_all_deployment_protection_rules**](ReposApi.md#repos_get_all_deployment_protection_rules) | **GET** /repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules | Get all deployment protection rules for an environment
[**repos_get_all_environments**](ReposApi.md#repos_get_all_environments) | **GET** /repos/{owner}/{repo}/environments | List environments
[**repos_get_all_status_check_contexts**](ReposApi.md#repos_get_all_status_check_contexts) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | Get all status check contexts
[**repos_get_all_topics**](ReposApi.md#repos_get_all_topics) | **GET** /repos/{owner}/{repo}/topics | Get all repository topics
[**repos_get_apps_with_access_to_protected_branch**](ReposApi.md#repos_get_apps_with_access_to_protected_branch) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | Get apps with access to the protected branch
[**repos_get_autolink**](ReposApi.md#repos_get_autolink) | **GET** /repos/{owner}/{repo}/autolinks/{autolink_id} | Get an autolink reference of a repository
[**repos_get_branch**](ReposApi.md#repos_get_branch) | **GET** /repos/{owner}/{repo}/branches/{branch} | Get a branch
[**repos_get_branch_protection**](ReposApi.md#repos_get_branch_protection) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection | Get branch protection
[**repos_get_branch_rules**](ReposApi.md#repos_get_branch_rules) | **GET** /repos/{owner}/{repo}/rules/branches/{branch} | Get rules for a branch
[**repos_get_clones**](ReposApi.md#repos_get_clones) | **GET** /repos/{owner}/{repo}/traffic/clones | Get repository clones
[**repos_get_code_frequency_stats**](ReposApi.md#repos_get_code_frequency_stats) | **GET** /repos/{owner}/{repo}/stats/code_frequency | Get the weekly commit activity
[**repos_get_collaborator_permission_level**](ReposApi.md#repos_get_collaborator_permission_level) | **GET** /repos/{owner}/{repo}/collaborators/{username}/permission | Get repository permissions for a user
[**repos_get_combined_status_for_ref**](ReposApi.md#repos_get_combined_status_for_ref) | **GET** /repos/{owner}/{repo}/commits/{ref}/status | Get the combined status for a specific reference
[**repos_get_commit**](ReposApi.md#repos_get_commit) | **GET** /repos/{owner}/{repo}/commits/{ref} | Get a commit
[**repos_get_commit_activity_stats**](ReposApi.md#repos_get_commit_activity_stats) | **GET** /repos/{owner}/{repo}/stats/commit_activity | Get the last year of commit activity
[**repos_get_commit_comment**](ReposApi.md#repos_get_commit_comment) | **GET** /repos/{owner}/{repo}/comments/{comment_id} | Get a commit comment
[**repos_get_commit_signature_protection**](ReposApi.md#repos_get_commit_signature_protection) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures | Get commit signature protection
[**repos_get_community_profile_metrics**](ReposApi.md#repos_get_community_profile_metrics) | **GET** /repos/{owner}/{repo}/community/profile | Get community profile metrics
[**repos_get_content**](ReposApi.md#repos_get_content) | **GET** /repos/{owner}/{repo}/contents/{path} | Get repository content
[**repos_get_contributors_stats**](ReposApi.md#repos_get_contributors_stats) | **GET** /repos/{owner}/{repo}/stats/contributors | Get all contributor commit activity
[**repos_get_custom_deployment_protection_rule**](ReposApi.md#repos_get_custom_deployment_protection_rule) | **GET** /repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/{protection_rule_id} | Get a custom deployment protection rule
[**repos_get_custom_properties_values**](ReposApi.md#repos_get_custom_properties_values) | **GET** /repos/{owner}/{repo}/properties/values | Get all custom property values for a repository
[**repos_get_deploy_key**](ReposApi.md#repos_get_deploy_key) | **GET** /repos/{owner}/{repo}/keys/{key_id} | Get a deploy key
[**repos_get_deployment**](ReposApi.md#repos_get_deployment) | **GET** /repos/{owner}/{repo}/deployments/{deployment_id} | Get a deployment
[**repos_get_deployment_branch_policy**](ReposApi.md#repos_get_deployment_branch_policy) | **GET** /repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id} | Get a deployment branch policy
[**repos_get_deployment_status**](ReposApi.md#repos_get_deployment_status) | **GET** /repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id} | Get a deployment status
[**repos_get_environment**](ReposApi.md#repos_get_environment) | **GET** /repos/{owner}/{repo}/environments/{environment_name} | Get an environment
[**repos_get_latest_pages_build**](ReposApi.md#repos_get_latest_pages_build) | **GET** /repos/{owner}/{repo}/pages/builds/latest | Get latest Pages build
[**repos_get_latest_release**](ReposApi.md#repos_get_latest_release) | **GET** /repos/{owner}/{repo}/releases/latest | Get the latest release
[**repos_get_org_rule_suite**](ReposApi.md#repos_get_org_rule_suite) | **GET** /orgs/{org}/rulesets/rule-suites/{rule_suite_id} | Get an organization rule suite
[**repos_get_org_rule_suites**](ReposApi.md#repos_get_org_rule_suites) | **GET** /orgs/{org}/rulesets/rule-suites | List organization rule suites
[**repos_get_org_ruleset**](ReposApi.md#repos_get_org_ruleset) | **GET** /orgs/{org}/rulesets/{ruleset_id} | Get an organization repository ruleset
[**repos_get_org_rulesets**](ReposApi.md#repos_get_org_rulesets) | **GET** /orgs/{org}/rulesets | Get all organization repository rulesets
[**repos_get_pages**](ReposApi.md#repos_get_pages) | **GET** /repos/{owner}/{repo}/pages | Get a GitHub Pages site
[**repos_get_pages_build**](ReposApi.md#repos_get_pages_build) | **GET** /repos/{owner}/{repo}/pages/builds/{build_id} | Get GitHub Pages build
[**repos_get_pages_deployment**](ReposApi.md#repos_get_pages_deployment) | **GET** /repos/{owner}/{repo}/pages/deployments/{pages_deployment_id} | Get the status of a GitHub Pages deployment
[**repos_get_pages_health_check**](ReposApi.md#repos_get_pages_health_check) | **GET** /repos/{owner}/{repo}/pages/health | Get a DNS health check for GitHub Pages
[**repos_get_participation_stats**](ReposApi.md#repos_get_participation_stats) | **GET** /repos/{owner}/{repo}/stats/participation | Get the weekly commit count
[**repos_get_pull_request_review_protection**](ReposApi.md#repos_get_pull_request_review_protection) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews | Get pull request review protection
[**repos_get_punch_card_stats**](ReposApi.md#repos_get_punch_card_stats) | **GET** /repos/{owner}/{repo}/stats/punch_card | Get the hourly commit count for each day
[**repos_get_readme**](ReposApi.md#repos_get_readme) | **GET** /repos/{owner}/{repo}/readme | Get a repository README
[**repos_get_readme_in_directory**](ReposApi.md#repos_get_readme_in_directory) | **GET** /repos/{owner}/{repo}/readme/{dir} | Get a repository README for a directory
[**repos_get_release**](ReposApi.md#repos_get_release) | **GET** /repos/{owner}/{repo}/releases/{release_id} | Get a release
[**repos_get_release_asset**](ReposApi.md#repos_get_release_asset) | **GET** /repos/{owner}/{repo}/releases/assets/{asset_id} | Get a release asset
[**repos_get_release_by_tag**](ReposApi.md#repos_get_release_by_tag) | **GET** /repos/{owner}/{repo}/releases/tags/{tag} | Get a release by tag name
[**repos_get_repo_rule_suite**](ReposApi.md#repos_get_repo_rule_suite) | **GET** /repos/{owner}/{repo}/rulesets/rule-suites/{rule_suite_id} | Get a repository rule suite
[**repos_get_repo_rule_suites**](ReposApi.md#repos_get_repo_rule_suites) | **GET** /repos/{owner}/{repo}/rulesets/rule-suites | List repository rule suites
[**repos_get_repo_ruleset**](ReposApi.md#repos_get_repo_ruleset) | **GET** /repos/{owner}/{repo}/rulesets/{ruleset_id} | Get a repository ruleset
[**repos_get_repo_rulesets**](ReposApi.md#repos_get_repo_rulesets) | **GET** /repos/{owner}/{repo}/rulesets | Get all repository rulesets
[**repos_get_status_checks_protection**](ReposApi.md#repos_get_status_checks_protection) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks | Get status checks protection
[**repos_get_teams_with_access_to_protected_branch**](ReposApi.md#repos_get_teams_with_access_to_protected_branch) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | Get teams with access to the protected branch
[**repos_get_top_paths**](ReposApi.md#repos_get_top_paths) | **GET** /repos/{owner}/{repo}/traffic/popular/paths | Get top referral paths
[**repos_get_top_referrers**](ReposApi.md#repos_get_top_referrers) | **GET** /repos/{owner}/{repo}/traffic/popular/referrers | Get top referral sources
[**repos_get_users_with_access_to_protected_branch**](ReposApi.md#repos_get_users_with_access_to_protected_branch) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | Get users with access to the protected branch
[**repos_get_views**](ReposApi.md#repos_get_views) | **GET** /repos/{owner}/{repo}/traffic/views | Get page views
[**repos_get_webhook**](ReposApi.md#repos_get_webhook) | **GET** /repos/{owner}/{repo}/hooks/{hook_id} | Get a repository webhook
[**repos_get_webhook_config_for_repo**](ReposApi.md#repos_get_webhook_config_for_repo) | **GET** /repos/{owner}/{repo}/hooks/{hook_id}/config | Get a webhook configuration for a repository
[**repos_get_webhook_delivery**](ReposApi.md#repos_get_webhook_delivery) | **GET** /repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id} | Get a delivery for a repository webhook
[**repos_list_activities**](ReposApi.md#repos_list_activities) | **GET** /repos/{owner}/{repo}/activity | List repository activities
[**repos_list_attestations**](ReposApi.md#repos_list_attestations) | **GET** /repos/{owner}/{repo}/attestations/{subject_digest} | List attestations
[**repos_list_autolinks**](ReposApi.md#repos_list_autolinks) | **GET** /repos/{owner}/{repo}/autolinks | Get all autolinks of a repository
[**repos_list_branches**](ReposApi.md#repos_list_branches) | **GET** /repos/{owner}/{repo}/branches | List branches
[**repos_list_branches_for_head_commit**](ReposApi.md#repos_list_branches_for_head_commit) | **GET** /repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head | List branches for HEAD commit
[**repos_list_collaborators**](ReposApi.md#repos_list_collaborators) | **GET** /repos/{owner}/{repo}/collaborators | List repository collaborators
[**repos_list_comments_for_commit**](ReposApi.md#repos_list_comments_for_commit) | **GET** /repos/{owner}/{repo}/commits/{commit_sha}/comments | List commit comments
[**repos_list_commit_comments_for_repo**](ReposApi.md#repos_list_commit_comments_for_repo) | **GET** /repos/{owner}/{repo}/comments | List commit comments for a repository
[**repos_list_commit_statuses_for_ref**](ReposApi.md#repos_list_commit_statuses_for_ref) | **GET** /repos/{owner}/{repo}/commits/{ref}/statuses | List commit statuses for a reference
[**repos_list_commits**](ReposApi.md#repos_list_commits) | **GET** /repos/{owner}/{repo}/commits | List commits
[**repos_list_contributors**](ReposApi.md#repos_list_contributors) | **GET** /repos/{owner}/{repo}/contributors | List repository contributors
[**repos_list_custom_deployment_rule_integrations**](ReposApi.md#repos_list_custom_deployment_rule_integrations) | **GET** /repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/apps | List custom deployment rule integrations available for an environment
[**repos_list_deploy_keys**](ReposApi.md#repos_list_deploy_keys) | **GET** /repos/{owner}/{repo}/keys | List deploy keys
[**repos_list_deployment_branch_policies**](ReposApi.md#repos_list_deployment_branch_policies) | **GET** /repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies | List deployment branch policies
[**repos_list_deployment_statuses**](ReposApi.md#repos_list_deployment_statuses) | **GET** /repos/{owner}/{repo}/deployments/{deployment_id}/statuses | List deployment statuses
[**repos_list_deployments**](ReposApi.md#repos_list_deployments) | **GET** /repos/{owner}/{repo}/deployments | List deployments
[**repos_list_for_authenticated_user**](ReposApi.md#repos_list_for_authenticated_user) | **GET** /user/repos | List repositories for the authenticated user
[**repos_list_for_org**](ReposApi.md#repos_list_for_org) | **GET** /orgs/{org}/repos | List organization repositories
[**repos_list_for_user**](ReposApi.md#repos_list_for_user) | **GET** /users/{username}/repos | List repositories for a user
[**repos_list_forks**](ReposApi.md#repos_list_forks) | **GET** /repos/{owner}/{repo}/forks | List forks
[**repos_list_invitations**](ReposApi.md#repos_list_invitations) | **GET** /repos/{owner}/{repo}/invitations | List repository invitations
[**repos_list_invitations_for_authenticated_user**](ReposApi.md#repos_list_invitations_for_authenticated_user) | **GET** /user/repository_invitations | List repository invitations for the authenticated user
[**repos_list_languages**](ReposApi.md#repos_list_languages) | **GET** /repos/{owner}/{repo}/languages | List repository languages
[**repos_list_pages_builds**](ReposApi.md#repos_list_pages_builds) | **GET** /repos/{owner}/{repo}/pages/builds | List GitHub Pages builds
[**repos_list_public**](ReposApi.md#repos_list_public) | **GET** /repositories | List public repositories
[**repos_list_pull_requests_associated_with_commit**](ReposApi.md#repos_list_pull_requests_associated_with_commit) | **GET** /repos/{owner}/{repo}/commits/{commit_sha}/pulls | List pull requests associated with a commit
[**repos_list_release_assets**](ReposApi.md#repos_list_release_assets) | **GET** /repos/{owner}/{repo}/releases/{release_id}/assets | List release assets
[**repos_list_releases**](ReposApi.md#repos_list_releases) | **GET** /repos/{owner}/{repo}/releases | List releases
[**repos_list_tag_protection**](ReposApi.md#repos_list_tag_protection) | **GET** /repos/{owner}/{repo}/tags/protection | Closing down - List tag protection states for a repository
[**repos_list_tags**](ReposApi.md#repos_list_tags) | **GET** /repos/{owner}/{repo}/tags | List repository tags
[**repos_list_teams**](ReposApi.md#repos_list_teams) | **GET** /repos/{owner}/{repo}/teams | List repository teams
[**repos_list_webhook_deliveries**](ReposApi.md#repos_list_webhook_deliveries) | **GET** /repos/{owner}/{repo}/hooks/{hook_id}/deliveries | List deliveries for a repository webhook
[**repos_list_webhooks**](ReposApi.md#repos_list_webhooks) | **GET** /repos/{owner}/{repo}/hooks | List repository webhooks
[**repos_merge**](ReposApi.md#repos_merge) | **POST** /repos/{owner}/{repo}/merges | Merge a branch
[**repos_merge_upstream**](ReposApi.md#repos_merge_upstream) | **POST** /repos/{owner}/{repo}/merge-upstream | Sync a fork branch with the upstream repository
[**repos_ping_webhook**](ReposApi.md#repos_ping_webhook) | **POST** /repos/{owner}/{repo}/hooks/{hook_id}/pings | Ping a repository webhook
[**repos_redeliver_webhook_delivery**](ReposApi.md#repos_redeliver_webhook_delivery) | **POST** /repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}/attempts | Redeliver a delivery for a repository webhook
[**repos_remove_app_access_restrictions**](ReposApi.md#repos_remove_app_access_restrictions) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | Remove app access restrictions
[**repos_remove_collaborator**](ReposApi.md#repos_remove_collaborator) | **DELETE** /repos/{owner}/{repo}/collaborators/{username} | Remove a repository collaborator
[**repos_remove_status_check_contexts**](ReposApi.md#repos_remove_status_check_contexts) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | Remove status check contexts
[**repos_remove_status_check_protection**](ReposApi.md#repos_remove_status_check_protection) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks | Remove status check protection
[**repos_remove_team_access_restrictions**](ReposApi.md#repos_remove_team_access_restrictions) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | Remove team access restrictions
[**repos_remove_user_access_restrictions**](ReposApi.md#repos_remove_user_access_restrictions) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | Remove user access restrictions
[**repos_rename_branch**](ReposApi.md#repos_rename_branch) | **POST** /repos/{owner}/{repo}/branches/{branch}/rename | Rename a branch
[**repos_replace_all_topics**](ReposApi.md#repos_replace_all_topics) | **PUT** /repos/{owner}/{repo}/topics | Replace all repository topics
[**repos_request_pages_build**](ReposApi.md#repos_request_pages_build) | **POST** /repos/{owner}/{repo}/pages/builds | Request a GitHub Pages build
[**repos_set_admin_branch_protection**](ReposApi.md#repos_set_admin_branch_protection) | **POST** /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins | Set admin branch protection
[**repos_set_app_access_restrictions**](ReposApi.md#repos_set_app_access_restrictions) | **PUT** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | Set app access restrictions
[**repos_set_status_check_contexts**](ReposApi.md#repos_set_status_check_contexts) | **PUT** /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | Set status check contexts
[**repos_set_team_access_restrictions**](ReposApi.md#repos_set_team_access_restrictions) | **PUT** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | Set team access restrictions
[**repos_set_user_access_restrictions**](ReposApi.md#repos_set_user_access_restrictions) | **PUT** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | Set user access restrictions
[**repos_test_push_webhook**](ReposApi.md#repos_test_push_webhook) | **POST** /repos/{owner}/{repo}/hooks/{hook_id}/tests | Test the push repository webhook
[**repos_transfer**](ReposApi.md#repos_transfer) | **POST** /repos/{owner}/{repo}/transfer | Transfer a repository
[**repos_update**](ReposApi.md#repos_update) | **PATCH** /repos/{owner}/{repo} | Update a repository
[**repos_update_branch_protection**](ReposApi.md#repos_update_branch_protection) | **PUT** /repos/{owner}/{repo}/branches/{branch}/protection | Update branch protection
[**repos_update_commit_comment**](ReposApi.md#repos_update_commit_comment) | **PATCH** /repos/{owner}/{repo}/comments/{comment_id} | Update a commit comment
[**repos_update_deployment_branch_policy**](ReposApi.md#repos_update_deployment_branch_policy) | **PUT** /repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id} | Update a deployment branch policy
[**repos_update_information_about_pages_site**](ReposApi.md#repos_update_information_about_pages_site) | **PUT** /repos/{owner}/{repo}/pages | Update information about a GitHub Pages site
[**repos_update_invitation**](ReposApi.md#repos_update_invitation) | **PATCH** /repos/{owner}/{repo}/invitations/{invitation_id} | Update a repository invitation
[**repos_update_org_ruleset**](ReposApi.md#repos_update_org_ruleset) | **PUT** /orgs/{org}/rulesets/{ruleset_id} | Update an organization repository ruleset
[**repos_update_pull_request_review_protection**](ReposApi.md#repos_update_pull_request_review_protection) | **PATCH** /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews | Update pull request review protection
[**repos_update_release**](ReposApi.md#repos_update_release) | **PATCH** /repos/{owner}/{repo}/releases/{release_id} | Update a release
[**repos_update_release_asset**](ReposApi.md#repos_update_release_asset) | **PATCH** /repos/{owner}/{repo}/releases/assets/{asset_id} | Update a release asset
[**repos_update_repo_ruleset**](ReposApi.md#repos_update_repo_ruleset) | **PUT** /repos/{owner}/{repo}/rulesets/{ruleset_id} | Update a repository ruleset
[**repos_update_status_check_protection**](ReposApi.md#repos_update_status_check_protection) | **PATCH** /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks | Update status check protection
[**repos_update_webhook**](ReposApi.md#repos_update_webhook) | **PATCH** /repos/{owner}/{repo}/hooks/{hook_id} | Update a repository webhook
[**repos_update_webhook_config_for_repo**](ReposApi.md#repos_update_webhook_config_for_repo) | **PATCH** /repos/{owner}/{repo}/hooks/{hook_id}/config | Update a webhook configuration for a repository
[**repos_upload_release_asset**](ReposApi.md#repos_upload_release_asset) | **POST** /repos/{owner}/{repo}/releases/{release_id}/assets | Upload a release asset


# **repos_accept_invitation_for_authenticated_user**
> repos_accept_invitation_for_authenticated_user(invitation_id)

Accept a repository invitation



### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    invitation_id = 56 # int | The unique identifier of the invitation.

    try:
        # Accept a repository invitation
        api_instance.repos_accept_invitation_for_authenticated_user(invitation_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_accept_invitation_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **int**| The unique identifier of the invitation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**404** | Resource not found |  -  |
**304** | Not modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_add_app_access_restrictions**
> List[Integration] repos_add_app_access_restrictions(owner, repo, branch, repos_set_app_access_restrictions_request)

Add app access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Grants the specified apps push access for this branch. Only GitHub Apps that are installed on the repository and that have been granted write access to the repository contents can be added as authorized actors on a protected branch.

### Example


```python
import github_openapi
from github_openapi.models.integration import Integration
from github_openapi.models.repos_set_app_access_restrictions_request import ReposSetAppAccessRestrictionsRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    repos_set_app_access_restrictions_request = {"apps":["octoapp"]} # ReposSetAppAccessRestrictionsRequest | 

    try:
        # Add app access restrictions
        api_response = api_instance.repos_add_app_access_restrictions(owner, repo, branch, repos_set_app_access_restrictions_request)
        print("The response of ReposApi->repos_add_app_access_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_add_app_access_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **repos_set_app_access_restrictions_request** | [**ReposSetAppAccessRestrictionsRequest**](ReposSetAppAccessRestrictionsRequest.md)|  | 

### Return type

[**List[Integration]**](Integration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_add_collaborator**
> RepositoryInvitation repos_add_collaborator(owner, repo, username, repos_add_collaborator_request=repos_add_collaborator_request)

Add a repository collaborator

This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. For more information, see \"[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)\" and \"[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api).\"  Adding an outside collaborator may be restricted by enterprise administrators. For more information, see \"[Enforcing repository management policies in your enterprise](https://docs.github.com/admin/policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise#enforcing-a-policy-for-inviting-outside-collaborators-to-repositories).\"  For more information on permission levels, see \"[Repository permission levels for an organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)\". There are restrictions on which permissions can be granted to organization members when an organization base role is in place. In this case, the permission being given must be equal to or higher than the org base permission. Otherwise, the request will fail with:  ``` Cannot assign {member} permission of {role name} ```  Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see \"[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method).\"  The invitee will receive a notification that they have been invited to the repository, which they must accept or decline. They may do this via the notifications page, the email they receive, or by using the [API](https://docs.github.com/rest/collaborators/invitations).  **Updating an existing collaborator's permission level**  The endpoint can also be used to change the permissions of an existing collaborator without first removing and re-adding the collaborator. To change the permissions, use the same endpoint and pass a different `permission` parameter. The response will be a `204`, with no other indication that the permission level changed.  **Rate limits**  You are limited to sending 50 invitations to a repository per 24 hour period. Note there is no limit if you are inviting organization members to an organization repository.

### Example


```python
import github_openapi
from github_openapi.models.repos_add_collaborator_request import ReposAddCollaboratorRequest
from github_openapi.models.repository_invitation import RepositoryInvitation
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.
    repos_add_collaborator_request = {"permission":"triage"} # ReposAddCollaboratorRequest |  (optional)

    try:
        # Add a repository collaborator
        api_response = api_instance.repos_add_collaborator(owner, repo, username, repos_add_collaborator_request=repos_add_collaborator_request)
        print("The response of ReposApi->repos_add_collaborator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_add_collaborator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 
 **repos_add_collaborator_request** | [**ReposAddCollaboratorRequest**](ReposAddCollaboratorRequest.md)|  | [optional] 

### Return type

[**RepositoryInvitation**](RepositoryInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response when a new invitation is created |  -  |
**204** | Response when: - an existing collaborator is added as a collaborator - an organization member is added as an individual collaborator - an existing team member (whose team is also a repository collaborator) is added as an individual collaborator |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_add_status_check_contexts**
> List[str] repos_add_status_check_contexts(owner, repo, branch, repos_set_status_check_contexts_request=repos_set_status_check_contexts_request)

Add status check contexts

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example


```python
import github_openapi
from github_openapi.models.repos_set_status_check_contexts_request import ReposSetStatusCheckContextsRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    repos_set_status_check_contexts_request = {"contexts":["continuous-integration/travis-ci","continuous-integration/jenkins"]} # ReposSetStatusCheckContextsRequest |  (optional)

    try:
        # Add status check contexts
        api_response = api_instance.repos_add_status_check_contexts(owner, repo, branch, repos_set_status_check_contexts_request=repos_set_status_check_contexts_request)
        print("The response of ReposApi->repos_add_status_check_contexts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_add_status_check_contexts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **repos_set_status_check_contexts_request** | [**ReposSetStatusCheckContextsRequest**](ReposSetStatusCheckContextsRequest.md)|  | [optional] 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_add_team_access_restrictions**
> List[Team] repos_add_team_access_restrictions(owner, repo, branch, repos_add_team_access_restrictions_request=repos_add_team_access_restrictions_request)

Add team access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Grants the specified teams push access for this branch. You can also give push access to child teams.

### Example


```python
import github_openapi
from github_openapi.models.repos_add_team_access_restrictions_request import ReposAddTeamAccessRestrictionsRequest
from github_openapi.models.team import Team
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    repos_add_team_access_restrictions_request = {"teams":["justice-league"]} # ReposAddTeamAccessRestrictionsRequest |  (optional)

    try:
        # Add team access restrictions
        api_response = api_instance.repos_add_team_access_restrictions(owner, repo, branch, repos_add_team_access_restrictions_request=repos_add_team_access_restrictions_request)
        print("The response of ReposApi->repos_add_team_access_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_add_team_access_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **repos_add_team_access_restrictions_request** | [**ReposAddTeamAccessRestrictionsRequest**](ReposAddTeamAccessRestrictionsRequest.md)|  | [optional] 

### Return type

[**List[Team]**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_add_user_access_restrictions**
> List[SimpleUser] repos_add_user_access_restrictions(owner, repo, branch, repos_set_user_access_restrictions_request)

Add user access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Grants the specified people push access for this branch.  | Type    | Description                                                                                                                   | | ------- | ----------------------------------------------------------------------------------------------------------------------------- | | `array` | Usernames for people who can have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

### Example


```python
import github_openapi
from github_openapi.models.repos_set_user_access_restrictions_request import ReposSetUserAccessRestrictionsRequest
from github_openapi.models.simple_user import SimpleUser
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    repos_set_user_access_restrictions_request = {"users":["octocat"]} # ReposSetUserAccessRestrictionsRequest | 

    try:
        # Add user access restrictions
        api_response = api_instance.repos_add_user_access_restrictions(owner, repo, branch, repos_set_user_access_restrictions_request)
        print("The response of ReposApi->repos_add_user_access_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_add_user_access_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **repos_set_user_access_restrictions_request** | [**ReposSetUserAccessRestrictionsRequest**](ReposSetUserAccessRestrictionsRequest.md)|  | 

### Return type

[**List[SimpleUser]**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_cancel_pages_deployment**
> repos_cancel_pages_deployment(owner, repo, pages_deployment_id)

Cancel a GitHub Pages deployment

Cancels a GitHub Pages deployment.  The authenticated user must have write permissions for the GitHub Pages site.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    pages_deployment_id = github_openapi.ActionsGetWorkflowWorkflowIdParameter() # ActionsGetWorkflowWorkflowIdParameter | The ID of the Pages deployment. You can also give the commit SHA of the deployment.

    try:
        # Cancel a GitHub Pages deployment
        api_instance.repos_cancel_pages_deployment(owner, repo, pages_deployment_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_cancel_pages_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **pages_deployment_id** | [**ActionsGetWorkflowWorkflowIdParameter**](.md)| The ID of the Pages deployment. You can also give the commit SHA of the deployment. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | A header with no content is returned. |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_check_automated_security_fixes**
> CheckAutomatedSecurityFixes repos_check_automated_security_fixes(owner, repo)

Check if automated security fixes are enabled for a repository

Shows whether automated security fixes are enabled, disabled or paused for a repository. The authenticated user must have admin read access to the repository. For more information, see \"[Configuring automated security fixes](https://docs.github.com/articles/configuring-automated-security-fixes)\".

### Example


```python
import github_openapi
from github_openapi.models.check_automated_security_fixes import CheckAutomatedSecurityFixes
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Check if automated security fixes are enabled for a repository
        api_response = api_instance.repos_check_automated_security_fixes(owner, repo)
        print("The response of ReposApi->repos_check_automated_security_fixes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_check_automated_security_fixes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**CheckAutomatedSecurityFixes**](CheckAutomatedSecurityFixes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response if Dependabot is enabled |  -  |
**404** | Not Found if Dependabot is not enabled for the repository |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_check_collaborator**
> repos_check_collaborator(owner, repo, username)

Check if a user is a repository collaborator

For organization-owned repositories, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners.  Team members will include the members of child teams.  The authenticated user must have push access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `read:org` and `repo` scopes to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Check if a user is a repository collaborator
        api_instance.repos_check_collaborator(owner, repo, username)
    except Exception as e:
        print("Exception when calling ReposApi->repos_check_collaborator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response if user is a collaborator |  -  |
**404** | Not Found if user is not a collaborator |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_check_private_vulnerability_reporting**
> ReposCheckPrivateVulnerabilityReporting200Response repos_check_private_vulnerability_reporting(owner, repo)

Check if private vulnerability reporting is enabled for a repository

Returns a boolean indicating whether or not private vulnerability reporting is enabled for the repository. For more information, see \"[Evaluating the security settings of a repository](https://docs.github.com/code-security/security-advisories/working-with-repository-security-advisories/evaluating-the-security-settings-of-a-repository)\".

### Example


```python
import github_openapi
from github_openapi.models.repos_check_private_vulnerability_reporting200_response import ReposCheckPrivateVulnerabilityReporting200Response
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Check if private vulnerability reporting is enabled for a repository
        api_response = api_instance.repos_check_private_vulnerability_reporting(owner, repo)
        print("The response of ReposApi->repos_check_private_vulnerability_reporting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_check_private_vulnerability_reporting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**ReposCheckPrivateVulnerabilityReporting200Response**](ReposCheckPrivateVulnerabilityReporting200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Private vulnerability reporting status |  -  |
**422** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_check_vulnerability_alerts**
> repos_check_vulnerability_alerts(owner, repo)

Check if vulnerability alerts are enabled for a repository

Shows whether dependency alerts are enabled or disabled for a repository. The authenticated user must have admin read access to the repository. For more information, see \"[About security alerts for vulnerable dependencies](https://docs.github.com/articles/about-security-alerts-for-vulnerable-dependencies)\".

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Check if vulnerability alerts are enabled for a repository
        api_instance.repos_check_vulnerability_alerts(owner, repo)
    except Exception as e:
        print("Exception when calling ReposApi->repos_check_vulnerability_alerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response if repository is enabled with vulnerability alerts |  -  |
**404** | Not Found if repository is not enabled with vulnerability alerts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_codeowners_errors**
> CodeownersErrors repos_codeowners_errors(owner, repo, ref=ref)

List CODEOWNERS errors

List any syntax errors that are detected in the CODEOWNERS file.  For more information about the correct CODEOWNERS syntax, see \"[About code owners](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).\"

### Example


```python
import github_openapi
from github_openapi.models.codeowners_errors import CodeownersErrors
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ref = 'ref_example' # str | A branch, tag or commit name used to determine which version of the CODEOWNERS file to use. Default: the repository's default branch (e.g. `main`) (optional)

    try:
        # List CODEOWNERS errors
        api_response = api_instance.repos_codeowners_errors(owner, repo, ref=ref)
        print("The response of ReposApi->repos_codeowners_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_codeowners_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ref** | **str**| A branch, tag or commit name used to determine which version of the CODEOWNERS file to use. Default: the repository&#39;s default branch (e.g. &#x60;main&#x60;) | [optional] 

### Return type

[**CodeownersErrors**](CodeownersErrors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_compare_commits**
> CommitComparison repos_compare_commits(owner, repo, basehead, page=page, per_page=per_page)

Compare two commits

Compares two commits against one another. You can compare refs (branches or tags) and commit SHAs in the same repository, or you can compare refs and commit SHAs that exist in different repositories within the same repository network, including fork branches. For more information about how to view a repository's network, see \"[Understanding connections between repositories](https://docs.github.com/repositories/viewing-activity-and-data-for-your-repository/understanding-connections-between-repositories).\"  This endpoint is equivalent to running the `git log BASE..HEAD` command, but it returns commits in a different order. The `git log BASE..HEAD` command returns commits in reverse chronological order, whereas the API returns commits in chronological order.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github.diff`**: Returns the diff of the commit. - **`application/vnd.github.patch`**: Returns the patch of the commit. Diffs with binary data will have no `patch` property.  The API response includes details about the files that were changed between the two commits. This includes the status of the change (if a file was added, removed, modified, or renamed), and details of the change itself. For example, files with a `renamed` status have a `previous_filename` field showing the previous filename of the file, and files with a `modified` status have a `patch` field showing the changes made to the file.  When calling this endpoint without any paging parameter (`per_page` or `page`), the returned list is limited to 250 commits, and the last commit in the list is the most recent of the entire comparison.  **Working with large comparisons**  To process a response with a large number of commits, use a query parameter (`per_page` or `page`) to paginate the results. When using pagination:  - The list of changed files is only shown on the first page of results, and it includes up to 300 changed files for the entire comparison. - The results are returned in chronological order, but the last commit in the returned list may not be the most recent one in the entire set if there are more pages of results.  For more information on working with pagination, see \"[Using pagination in the REST API](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api).\"  **Signature verification object**  The response will include a `verification` object that describes the result of verifying the commit's signature. The `verification` object includes the following fields:  | Name | Type | Description | | ---- | ---- | ----------- | | `verified` | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified. | | `reason` | `string` | The reason for verified value. Possible values and their meanings are enumerated in table below. | | `signature` | `string` | The signature that was extracted from the commit. | | `payload` | `string` | The value that was signed. | | `verified_at` | `string` | The date the signature was verified by GitHub. |  These are the possible values for `reason` in the `verification` object:  | Value | Description | | ----- | ----------- | | `expired_key` | The key that made the signature is expired. | | `not_signing_key` | The \"signing\" flag is not among the usage flags in the GPG key that made the signature. | | `gpgverify_error` | There was an error communicating with the signature verification service. | | `gpgverify_unavailable` | The signature verification service is currently unavailable. | | `unsigned` | The object does not include a signature. | | `unknown_signature_type` | A non-PGP signature was found in the commit. | | `no_user` | No user was associated with the `committer` email address in the commit. | | `unverified_email` | The `committer` email address in the commit was associated with a user, but the email address is not verified on their account. | | `bad_email` | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. | | `unknown_key` | The key that made the signature has not been registered with any user's account. | | `malformed_signature` | There was an error parsing the signature. | | `invalid` | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | `valid` | None of the above errors applied, so the signature is considered to be verified. |

### Example


```python
import github_openapi
from github_openapi.models.commit_comparison import CommitComparison
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    basehead = 'basehead_example' # str | The base branch and head branch to compare. This parameter expects the format `BASE...HEAD`. Both must be branch names in `repo`. To compare with a branch that exists in a different repository in the same network as `repo`, the `basehead` parameter expects the format `USERNAME:BASE...USERNAME:HEAD`.
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # Compare two commits
        api_response = api_instance.repos_compare_commits(owner, repo, basehead, page=page, per_page=per_page)
        print("The response of ReposApi->repos_compare_commits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_compare_commits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **basehead** | **str**| The base branch and head branch to compare. This parameter expects the format &#x60;BASE...HEAD&#x60;. Both must be branch names in &#x60;repo&#x60;. To compare with a branch that exists in a different repository in the same network as &#x60;repo&#x60;, the &#x60;basehead&#x60; parameter expects the format &#x60;USERNAME:BASE...USERNAME:HEAD&#x60;. | 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]

### Return type

[**CommitComparison**](CommitComparison.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_attestation**
> ReposCreateAttestation201Response repos_create_attestation(owner, repo, repos_create_attestation_request)

Create an attestation

Store an artifact attestation and associate it with a repository.  The authenticated user must have write permission to the repository and, if using a fine-grained access token, the `attestations:write` permission is required.  Artifact attestations are meant to be created using the [attest action](https://github.com/actions/attest). For more information, see our guide on [using artifact attestations to establish a build's provenance](https://docs.github.com/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds).

### Example


```python
import github_openapi
from github_openapi.models.repos_create_attestation201_response import ReposCreateAttestation201Response
from github_openapi.models.repos_create_attestation_request import ReposCreateAttestationRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_create_attestation_request = {"$ref":"#/components/examples/attestation"} # ReposCreateAttestationRequest | 

    try:
        # Create an attestation
        api_response = api_instance.repos_create_attestation(owner, repo, repos_create_attestation_request)
        print("The response of ReposApi->repos_create_attestation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_attestation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_create_attestation_request** | [**ReposCreateAttestationRequest**](ReposCreateAttestationRequest.md)|  | 

### Return type

[**ReposCreateAttestation201Response**](ReposCreateAttestation201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | response |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_autolink**
> Autolink repos_create_autolink(owner, repo, repos_create_autolink_request)

Create an autolink reference for a repository

Users with admin access to the repository can create an autolink.

### Example


```python
import github_openapi
from github_openapi.models.autolink import Autolink
from github_openapi.models.repos_create_autolink_request import ReposCreateAutolinkRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_create_autolink_request = {"key_prefix":"TICKET-","url_template":"https://example.com/TICKET?query=<num>","is_alphanumeric":true} # ReposCreateAutolinkRequest | 

    try:
        # Create an autolink reference for a repository
        api_response = api_instance.repos_create_autolink(owner, repo, repos_create_autolink_request)
        print("The response of ReposApi->repos_create_autolink:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_autolink: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_create_autolink_request** | [**ReposCreateAutolinkRequest**](ReposCreateAutolinkRequest.md)|  | 

### Return type

[**Autolink**](Autolink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | response |  * Location -  <br>  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_commit_comment**
> CommitComment repos_create_commit_comment(owner, repo, commit_sha, repos_create_commit_comment_request)

Create a commit comment

Create a comment for a commit using its `:commit_sha`.  This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. For more information, see \"[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)\" and \"[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api).\"  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github-commitcomment.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.

### Example


```python
import github_openapi
from github_openapi.models.commit_comment import CommitComment
from github_openapi.models.repos_create_commit_comment_request import ReposCreateCommitCommentRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    commit_sha = 'commit_sha_example' # str | The SHA of the commit.
    repos_create_commit_comment_request = {"body":"Great stuff","path":"file1.txt","position":4,"line":1} # ReposCreateCommitCommentRequest | 

    try:
        # Create a commit comment
        api_response = api_instance.repos_create_commit_comment(owner, repo, commit_sha, repos_create_commit_comment_request)
        print("The response of ReposApi->repos_create_commit_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_commit_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **commit_sha** | **str**| The SHA of the commit. | 
 **repos_create_commit_comment_request** | [**ReposCreateCommitCommentRequest**](ReposCreateCommitCommentRequest.md)|  | 

### Return type

[**CommitComment**](CommitComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  * Location -  <br>  |
**403** | Forbidden |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_commit_signature_protection**
> ProtectedBranchAdminEnforced repos_create_commit_signature_protection(owner, repo, branch)

Create commit signature protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  When authenticated with admin or owner permissions to the repository, you can use this endpoint to require signed commits on a branch. You must enable branch protection to require signed commits.

### Example


```python
import github_openapi
from github_openapi.models.protected_branch_admin_enforced import ProtectedBranchAdminEnforced
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Create commit signature protection
        api_response = api_instance.repos_create_commit_signature_protection(owner, repo, branch)
        print("The response of ReposApi->repos_create_commit_signature_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_commit_signature_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

[**ProtectedBranchAdminEnforced**](ProtectedBranchAdminEnforced.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_commit_status**
> Status repos_create_commit_status(owner, repo, sha, repos_create_commit_status_request)

Create a commit status

Users with push access in a repository can create commit statuses for a given SHA.  Note: there is a limit of 1000 statuses per `sha` and `context` within a repository. Attempts to create more than 1000 statuses will result in a validation error.

### Example


```python
import github_openapi
from github_openapi.models.repos_create_commit_status_request import ReposCreateCommitStatusRequest
from github_openapi.models.status import Status
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    sha = 'sha_example' # str | 
    repos_create_commit_status_request = {"state":"success","target_url":"https://example.com/build/status","description":"The build succeeded!","context":"continuous-integration/jenkins"} # ReposCreateCommitStatusRequest | 

    try:
        # Create a commit status
        api_response = api_instance.repos_create_commit_status(owner, repo, sha, repos_create_commit_status_request)
        print("The response of ReposApi->repos_create_commit_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_commit_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **sha** | **str**|  | 
 **repos_create_commit_status_request** | [**ReposCreateCommitStatusRequest**](ReposCreateCommitStatusRequest.md)|  | 

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  * Location -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_deploy_key**
> DeployKey repos_create_deploy_key(owner, repo, repos_create_deploy_key_request)

Create a deploy key

You can create a read-only deploy key.

### Example


```python
import github_openapi
from github_openapi.models.deploy_key import DeployKey
from github_openapi.models.repos_create_deploy_key_request import ReposCreateDeployKeyRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_create_deploy_key_request = {"title":"octocat@octomac","key":"ssh-rsa AAA...","read_only":true} # ReposCreateDeployKeyRequest | 

    try:
        # Create a deploy key
        api_response = api_instance.repos_create_deploy_key(owner, repo, repos_create_deploy_key_request)
        print("The response of ReposApi->repos_create_deploy_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_deploy_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_create_deploy_key_request** | [**ReposCreateDeployKeyRequest**](ReposCreateDeployKeyRequest.md)|  | 

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  * Location -  <br>  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_deployment**
> Deployment repos_create_deployment(owner, repo, repos_create_deployment_request)

Create a deployment

Deployments offer a few configurable parameters with certain defaults.  The `ref` parameter can be any named branch, tag, or SHA. At GitHub we often deploy branches and verify them before we merge a pull request.  The `environment` parameter allows deployments to be issued to different runtime environments. Teams often have multiple environments for verifying their applications, such as `production`, `staging`, and `qa`. This parameter makes it easier to track which environments have requested deployments. The default environment is `production`.  The `auto_merge` parameter is used to ensure that the requested ref is not behind the repository's default branch. If the ref _is_ behind the default branch for the repository, we will attempt to merge it for you. If the merge succeeds, the API will return a successful merge commit. If merge conflicts prevent the merge from succeeding, the API will return a failure response.  By default, [commit statuses](https://docs.github.com/rest/commits/statuses) for every submitted context must be in a `success` state. The `required_contexts` parameter allows you to specify a subset of contexts that must be `success`, or to specify contexts that have not yet been submitted. You are not required to use commit statuses to deploy. If you do not require any contexts or create any commit statuses, the deployment will always succeed.  The `payload` parameter is available for any extra information that a deployment system might need. It is a JSON text field that will be passed on when a deployment event is dispatched.  The `task` parameter is used by the deployment system to allow different execution paths. In the web world this might be `deploy:migrations` to run schema changes on the system. In the compiled world this could be a flag to compile an application with debugging enabled.  Merged branch response:  You will see this response when GitHub automatically merges the base branch into the topic branch instead of creating a deployment. This auto-merge happens when: *   Auto-merge option is enabled in the repository *   Topic branch does not include the latest changes on the base branch, which is `master` in the response example *   There are no merge conflicts  If there are no new commits in the base branch, a new request to create a deployment should give a successful response.  Merge conflict response:  This error happens when the `auto_merge` option is enabled and when the default branch (in this case `master`), can't be merged into the branch that's being deployed (in this case `topic-branch`), due to merge conflicts.  Failed commit status checks:  This error happens when the `required_contexts` parameter indicates that one or more contexts need to have a `success` status for the commit to be deployed, but one or more of the required contexts do not have a state of `success`.  OAuth app tokens and personal access tokens (classic) need the `repo` or `repo_deployment` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.deployment import Deployment
from github_openapi.models.repos_create_deployment_request import ReposCreateDeploymentRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_create_deployment_request = {"ref":"topic-branch","payload":"{ \"deploy\": \"migrate\" }","description":"Deploy request from hubot"} # ReposCreateDeploymentRequest | 

    try:
        # Create a deployment
        api_response = api_instance.repos_create_deployment(owner, repo, repos_create_deployment_request)
        print("The response of ReposApi->repos_create_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_create_deployment_request** | [**ReposCreateDeploymentRequest**](ReposCreateDeploymentRequest.md)|  | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**202** | Merged branch response |  -  |
**409** | Conflict when there is a merge conflict or the commit&#39;s status checks failed |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_deployment_branch_policy**
> DeploymentBranchPolicy repos_create_deployment_branch_policy(owner, repo, environment_name, deployment_branch_policy_name_pattern_with_type)

Create a deployment branch policy

Creates a deployment branch or tag policy for an environment.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.deployment_branch_policy import DeploymentBranchPolicy
from github_openapi.models.deployment_branch_policy_name_pattern_with_type import DeploymentBranchPolicyNamePatternWithType
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    deployment_branch_policy_name_pattern_with_type = {"name":"release/*"} # DeploymentBranchPolicyNamePatternWithType | 

    try:
        # Create a deployment branch policy
        api_response = api_instance.repos_create_deployment_branch_policy(owner, repo, environment_name, deployment_branch_policy_name_pattern_with_type)
        print("The response of ReposApi->repos_create_deployment_branch_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_deployment_branch_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **deployment_branch_policy_name_pattern_with_type** | [**DeploymentBranchPolicyNamePatternWithType**](DeploymentBranchPolicyNamePatternWithType.md)|  | 

### Return type

[**DeploymentBranchPolicy**](DeploymentBranchPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Not Found or &#x60;deployment_branch_policy.custom_branch_policies&#x60; property for the environment is set to false |  -  |
**303** | Response if the same branch name pattern already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_deployment_protection_rule**
> DeploymentProtectionRule repos_create_deployment_protection_rule(environment_name, repo, owner, repos_create_deployment_protection_rule_request)

Create a custom deployment protection rule on an environment

Enable a custom deployment protection rule for an environment.  The authenticated user must have admin or owner permissions to the repository to use this endpoint.  For more information about the app that is providing this custom deployment rule, see the [documentation for the `GET /apps/{app_slug}` endpoint](https://docs.github.com/rest/apps/apps#get-an-app).  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.deployment_protection_rule import DeploymentProtectionRule
from github_openapi.models.repos_create_deployment_protection_rule_request import ReposCreateDeploymentProtectionRuleRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repos_create_deployment_protection_rule_request = {"integration_id":5} # ReposCreateDeploymentProtectionRuleRequest | 

    try:
        # Create a custom deployment protection rule on an environment
        api_response = api_instance.repos_create_deployment_protection_rule(environment_name, repo, owner, repos_create_deployment_protection_rule_request)
        print("The response of ReposApi->repos_create_deployment_protection_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_deployment_protection_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repos_create_deployment_protection_rule_request** | [**ReposCreateDeploymentProtectionRuleRequest**](ReposCreateDeploymentProtectionRuleRequest.md)|  | 

### Return type

[**DeploymentProtectionRule**](DeploymentProtectionRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The enabled custom deployment protection rule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_deployment_status**
> DeploymentStatus repos_create_deployment_status(owner, repo, deployment_id, repos_create_deployment_status_request)

Create a deployment status

Users with `push` access can create deployment statuses for a given deployment.  OAuth app tokens and personal access tokens (classic) need the `repo_deployment` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.deployment_status import DeploymentStatus
from github_openapi.models.repos_create_deployment_status_request import ReposCreateDeploymentStatusRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    deployment_id = 56 # int | deployment_id parameter
    repos_create_deployment_status_request = {"environment":"production","state":"success","log_url":"https://example.com/deployment/42/output","description":"Deployment finished successfully."} # ReposCreateDeploymentStatusRequest | 

    try:
        # Create a deployment status
        api_response = api_instance.repos_create_deployment_status(owner, repo, deployment_id, repos_create_deployment_status_request)
        print("The response of ReposApi->repos_create_deployment_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_deployment_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **deployment_id** | **int**| deployment_id parameter | 
 **repos_create_deployment_status_request** | [**ReposCreateDeploymentStatusRequest**](ReposCreateDeploymentStatusRequest.md)|  | 

### Return type

[**DeploymentStatus**](DeploymentStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  * Location -  <br>  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_dispatch_event**
> repos_create_dispatch_event(owner, repo, repos_create_dispatch_event_request)

Create a repository dispatch event

You can use this endpoint to trigger a webhook event called `repository_dispatch` when you want activity that happens outside of GitHub to trigger a GitHub Actions workflow or GitHub App webhook. You must configure your GitHub Actions workflow or GitHub App to run when the `repository_dispatch` event occurs. For an example `repository_dispatch` webhook payload, see \"[RepositoryDispatchEvent](https://docs.github.com/webhooks/event-payloads/#repository_dispatch).\"  The `client_payload` parameter is available for any extra information that your workflow might need. This parameter is a JSON payload that will be passed on when the webhook event is dispatched. For example, the `client_payload` can include a message that a user would like to send using a GitHub Actions workflow. Or the `client_payload` can be used as a test to debug your workflow.  This input example shows how you can use the `client_payload` as a test to debug your workflow.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.repos_create_dispatch_event_request import ReposCreateDispatchEventRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_create_dispatch_event_request = {"event_type":"on-demand-test","client_payload":{"unit":false,"integration":true}} # ReposCreateDispatchEventRequest | 

    try:
        # Create a repository dispatch event
        api_instance.repos_create_dispatch_event(owner, repo, repos_create_dispatch_event_request)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_dispatch_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_create_dispatch_event_request** | [**ReposCreateDispatchEventRequest**](ReposCreateDispatchEventRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_for_authenticated_user**
> FullRepository repos_create_for_authenticated_user(repos_create_for_authenticated_user_request)

Create a repository for the authenticated user

Creates a new repository for the authenticated user.  OAuth app tokens and personal access tokens (classic) need the `public_repo` or `repo` scope to create a public repository, and `repo` scope to create a private repository.

### Example


```python
import github_openapi
from github_openapi.models.full_repository import FullRepository
from github_openapi.models.repos_create_for_authenticated_user_request import ReposCreateForAuthenticatedUserRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    repos_create_for_authenticated_user_request = {"name":"Hello-World","description":"This is your first repo!","homepage":"https://github.com","private":false,"is_template":true} # ReposCreateForAuthenticatedUserRequest | 

    try:
        # Create a repository for the authenticated user
        api_response = api_instance.repos_create_for_authenticated_user(repos_create_for_authenticated_user_request)
        print("The response of ReposApi->repos_create_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repos_create_for_authenticated_user_request** | [**ReposCreateForAuthenticatedUserRequest**](ReposCreateForAuthenticatedUserRequest.md)|  | 

### Return type

[**FullRepository**](FullRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  * Location -  <br>  |
**401** | Requires authentication |  -  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_fork**
> FullRepository repos_create_fork(owner, repo, repos_create_fork_request=repos_create_fork_request)

Create a fork

Create a fork for the authenticated user.  > [!NOTE] > Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api).  > [!NOTE] > Although this endpoint works with GitHub Apps, the GitHub App must be installed on the destination account with access to all repositories and on the source account with access to the source repository.

### Example


```python
import github_openapi
from github_openapi.models.full_repository import FullRepository
from github_openapi.models.repos_create_fork_request import ReposCreateForkRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_create_fork_request = {"organization":"octocat","name":"Hello-World","default_branch_only":true} # ReposCreateForkRequest |  (optional)

    try:
        # Create a fork
        api_response = api_instance.repos_create_fork(owner, repo, repos_create_fork_request=repos_create_fork_request)
        print("The response of ReposApi->repos_create_fork:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_fork: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_create_fork_request** | [**ReposCreateForkRequest**](ReposCreateForkRequest.md)|  | [optional] 

### Return type

[**FullRepository**](FullRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_in_org**
> FullRepository repos_create_in_org(org, repos_create_in_org_request)

Create an organization repository

Creates a new repository in the specified organization. The authenticated user must be a member of the organization.  OAuth app tokens and personal access tokens (classic) need the `public_repo` or `repo` scope to create a public repository, and `repo` scope to create a private repository.

### Example


```python
import github_openapi
from github_openapi.models.full_repository import FullRepository
from github_openapi.models.repos_create_in_org_request import ReposCreateInOrgRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    repos_create_in_org_request = {"name":"Hello-World","description":"This is your first repository","homepage":"https://github.com","private":false,"has_issues":true,"has_projects":true,"has_wiki":true} # ReposCreateInOrgRequest | 

    try:
        # Create an organization repository
        api_response = api_instance.repos_create_in_org(org, repos_create_in_org_request)
        print("The response of ReposApi->repos_create_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **repos_create_in_org_request** | [**ReposCreateInOrgRequest**](ReposCreateInOrgRequest.md)|  | 

### Return type

[**FullRepository**](FullRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  * Location -  <br>  |
**403** | Forbidden |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_or_update_custom_properties_values**
> repos_create_or_update_custom_properties_values(owner, repo, repos_create_or_update_custom_properties_values_request)

Create or update custom property values for a repository

Create new or update existing custom property values for a repository. Using a value of `null` for a custom property will remove or 'unset' the property value from the repository.  Repository admins and other users with the repository-level \"edit custom property values\" fine-grained permission can use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.repos_create_or_update_custom_properties_values_request import ReposCreateOrUpdateCustomPropertiesValuesRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_create_or_update_custom_properties_values_request = github_openapi.ReposCreateOrUpdateCustomPropertiesValuesRequest() # ReposCreateOrUpdateCustomPropertiesValuesRequest | 

    try:
        # Create or update custom property values for a repository
        api_instance.repos_create_or_update_custom_properties_values(owner, repo, repos_create_or_update_custom_properties_values_request)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_or_update_custom_properties_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_create_or_update_custom_properties_values_request** | [**ReposCreateOrUpdateCustomPropertiesValuesRequest**](ReposCreateOrUpdateCustomPropertiesValuesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content when custom property values are successfully created or updated |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_or_update_environment**
> Environment repos_create_or_update_environment(owner, repo, environment_name, repos_create_or_update_environment_request=repos_create_or_update_environment_request)

Create or update an environment

Create or update an environment with protection rules, such as required reviewers. For more information about environment protection rules, see \"[Environments](/actions/reference/environments#environment-protection-rules).\"  > [!NOTE] > To create or update name patterns that branches must match in order to deploy to this environment, see \"[Deployment branch policies](/rest/deployments/branch-policies).\"  > [!NOTE] > To create or update secrets for an environment, see \"[GitHub Actions secrets](/rest/actions/secrets).\"  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.environment import Environment
from github_openapi.models.repos_create_or_update_environment_request import ReposCreateOrUpdateEnvironmentRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    repos_create_or_update_environment_request = {"wait_timer":30,"prevent_self_review":false,"reviewers":[{"type":"User","id":1},{"type":"Team","id":1}],"deployment_branch_policy":{"protected_branches":false,"custom_branch_policies":true}} # ReposCreateOrUpdateEnvironmentRequest |  (optional)

    try:
        # Create or update an environment
        api_response = api_instance.repos_create_or_update_environment(owner, repo, environment_name, repos_create_or_update_environment_request=repos_create_or_update_environment_request)
        print("The response of ReposApi->repos_create_or_update_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_or_update_environment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **repos_create_or_update_environment_request** | [**ReposCreateOrUpdateEnvironmentRequest**](ReposCreateOrUpdateEnvironmentRequest.md)|  | [optional] 

### Return type

[**Environment**](Environment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation error when the environment name is invalid or when &#x60;protected_branches&#x60; and &#x60;custom_branch_policies&#x60; in &#x60;deployment_branch_policy&#x60; are set to the same value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_or_update_file_contents**
> FileCommit repos_create_or_update_file_contents(owner, repo, path, repos_create_or_update_file_contents_request)

Create or update file contents

Creates a new file or replaces an existing file in a repository.  > [!NOTE] > If you use this endpoint and the \"[Delete a file](https://docs.github.com/rest/repos/contents/#delete-a-file)\" endpoint in parallel, the concurrent requests will conflict and you will receive errors. You must use these endpoints serially instead.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint. The `workflow` scope is also required in order to modify files in the `.github/workflows` directory.

### Example


```python
import github_openapi
from github_openapi.models.file_commit import FileCommit
from github_openapi.models.repos_create_or_update_file_contents_request import ReposCreateOrUpdateFileContentsRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    path = 'path_example' # str | path parameter
    repos_create_or_update_file_contents_request = {"message":"my commit message","committer":{"name":"Monalisa Octocat","email":"octocat@github.com"},"content":"bXkgbmV3IGZpbGUgY29udGVudHM="} # ReposCreateOrUpdateFileContentsRequest | 

    try:
        # Create or update file contents
        api_response = api_instance.repos_create_or_update_file_contents(owner, repo, path, repos_create_or_update_file_contents_request)
        print("The response of ReposApi->repos_create_or_update_file_contents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_or_update_file_contents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **path** | **str**| path parameter | 
 **repos_create_or_update_file_contents_request** | [**ReposCreateOrUpdateFileContentsRequest**](ReposCreateOrUpdateFileContentsRequest.md)|  | 

### Return type

[**FileCommit**](FileCommit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**201** | Response |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_org_ruleset**
> RepositoryRuleset repos_create_org_ruleset(org, repos_create_org_ruleset_request)

Create an organization repository ruleset

Create a repository ruleset for an organization.

### Example


```python
import github_openapi
from github_openapi.models.repos_create_org_ruleset_request import ReposCreateOrgRulesetRequest
from github_openapi.models.repository_ruleset import RepositoryRuleset
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    repos_create_org_ruleset_request = {"name":"super cool ruleset","target":"branch","enforcement":"active","bypass_actors":[{"actor_id":234,"actor_type":"Team","bypass_mode":"always"}],"conditions":{"ref_name":{"include":["refs/heads/main","refs/heads/master"],"exclude":["refs/heads/dev*"]},"repository_name":{"include":["important_repository","another_important_repository"],"exclude":["unimportant_repository"],"protected":true}},"rules":[{"type":"commit_author_email_pattern","parameters":{"operator":"contains","pattern":"github"}}]} # ReposCreateOrgRulesetRequest | Request body

    try:
        # Create an organization repository ruleset
        api_response = api_instance.repos_create_org_ruleset(org, repos_create_org_ruleset_request)
        print("The response of ReposApi->repos_create_org_ruleset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_org_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **repos_create_org_ruleset_request** | [**ReposCreateOrgRulesetRequest**](ReposCreateOrgRulesetRequest.md)| Request body | 

### Return type

[**RepositoryRuleset**](RepositoryRuleset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_pages_deployment**
> PageDeployment repos_create_pages_deployment(owner, repo, repos_create_pages_deployment_request)

Create a GitHub Pages deployment

Create a GitHub Pages deployment for a repository.  The authenticated user must have write permission to the repository.

### Example


```python
import github_openapi
from github_openapi.models.page_deployment import PageDeployment
from github_openapi.models.repos_create_pages_deployment_request import ReposCreatePagesDeploymentRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_create_pages_deployment_request = {"artifact_url":"https://downloadcontent/","environment":"github-pages","pages_build_version":"4fd754f7e594640989b406850d0bc8f06a121251","oidc_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlV2R1h4SUhlY0JFc1JCdEttemUxUEhfUERiVSIsImtpZCI6IjUyRjE5N0M0ODFERTcwMTEyQzQ0MUI0QTlCMzdCNTNDN0ZDRjBEQjUifQ.eyJqdGkiOiJhMWIwNGNjNy0zNzZiLTQ1N2QtOTMzNS05NTY5YmVjZDExYTIiLCJzdWIiOiJyZXBvOnBhcGVyLXNwYS9taW55aTplbnZpcm9ubWVudDpQcm9kdWN0aW9uIiwiYXVkIjoiaHR0cHM6Ly9naXRodWIuY29tL3BhcGVyLXNwYSIsInJlZiI6InJlZnMvaGVhZHMvbWFpbiIsInNoYSI6ImEyODU1MWJmODdiZDk3NTFiMzdiMmM0YjM3M2MxZjU3NjFmYWM2MjYiLCJyZXBvc2l0b3J5IjoicGFwZXItc3BhL21pbnlpIiwicmVwb3NpdG9yeV9vd25lciI6InBhcGVyLXNwYSIsInJ1bl9pZCI6IjE1NDY0NTkzNjQiLCJydW5fbnVtYmVyIjoiMzQiLCJydW5fYXR0ZW1wdCI6IjYiLCJhY3RvciI6IllpTXlzdHkiLCJ3b3JrZmxvdyI6IkNJIiwiaGVhZF9yZWYiOiIiLCJiYXNlX3JlZiI6IiIsImV2ZW50X25hbWUiOiJwdXNoIiwicmVmX3R5cGUiOiJicmFuY2giLCJlbnZpcm9ubWVudCI6IlByb2R1Y3Rpb24iLCJqb2Jfd29ya2Zsb3dfcmVmIjoicGFwZXItc3BhL21pbnlpLy5naXRodWIvd29ya2Zsb3dzL2JsYW5rLnltbEByZWZzL2hlYWRzL21haW4iLCJpc3MiOiJodHRwczovL3Rva2VuLmFjdGlvbnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tIiwibmJmIjoxNjM5MDAwODU2LCJleHAiOjE2MzkwMDE3NTYsImlhdCI6MTYzOTAwMTQ1Nn0.VP8WictbQECKozE2SgvKb2FqJ9hisWsoMkYRTqfBrQfZTCXi5IcFEdgDMB2X7a99C2DeUuTvHh9RMKXLL2a0zg3-Sd7YrO7a2ll2kNlnvyIypcN6AeIc7BxHsTTnZN9Ud_xmEsTrSRGOEKmzCFkULQ6N4zlVD0sidypmXlMemmWEcv_ZHqhioEI_VMp5vwXQurketWH7qX4oDgG4okyYtPrv5RQHbfQcVo9izaPJ_jnsDd0CBA0QOx9InjPidtIkMYQLyUgJy33HLJy86EFNUnAf8UhBQuQi5mAsEpEzBBuKpG3PDiPtYCHOk64JZkZGd5mR888a5sbHRiaF8hm8YA","preview":false} # ReposCreatePagesDeploymentRequest | 

    try:
        # Create a GitHub Pages deployment
        api_response = api_instance.repos_create_pages_deployment(owner, repo, repos_create_pages_deployment_request)
        print("The response of ReposApi->repos_create_pages_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_pages_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_create_pages_deployment_request** | [**ReposCreatePagesDeploymentRequest**](ReposCreatePagesDeploymentRequest.md)|  | 

### Return type

[**PageDeployment**](PageDeployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_pages_site**
> Page repos_create_pages_site(owner, repo, repos_create_pages_site_request)

Create a GitHub Pages site

Configures a GitHub Pages site. For more information, see \"[About GitHub Pages](/github/working-with-github-pages/about-github-pages).\"  The authenticated user must be a repository administrator, maintainer, or have the 'manage GitHub Pages settings' permission.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.page import Page
from github_openapi.models.repos_create_pages_site_request import ReposCreatePagesSiteRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_create_pages_site_request = {"source":{"branch":"main","path":"/docs"}} # ReposCreatePagesSiteRequest | 

    try:
        # Create a GitHub Pages site
        api_response = api_instance.repos_create_pages_site(owner, repo, repos_create_pages_site_request)
        print("The response of ReposApi->repos_create_pages_site:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_pages_site: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_create_pages_site_request** | [**ReposCreatePagesSiteRequest**](ReposCreatePagesSiteRequest.md)|  | 

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_release**
> Release repos_create_release(owner, repo, repos_create_release_request)

Create a release

Users with push access to the repository can create a release.  This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. For more information, see \"[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)\" and \"[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api).\"

### Example


```python
import github_openapi
from github_openapi.models.release import Release
from github_openapi.models.repos_create_release_request import ReposCreateReleaseRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_create_release_request = {"tag_name":"v1.0.0","target_commitish":"master","name":"v1.0.0","body":"Description of the release","draft":false,"prerelease":false,"generate_release_notes":false} # ReposCreateReleaseRequest | 

    try:
        # Create a release
        api_response = api_instance.repos_create_release(owner, repo, repos_create_release_request)
        print("The response of ReposApi->repos_create_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_create_release_request** | [**ReposCreateReleaseRequest**](ReposCreateReleaseRequest.md)|  | 

### Return type

[**Release**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  * Location -  <br>  |
**404** | Not Found if the discussion category name is invalid |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_repo_ruleset**
> RepositoryRuleset repos_create_repo_ruleset(owner, repo, repos_create_repo_ruleset_request)

Create a repository ruleset

Create a ruleset for a repository.

### Example


```python
import github_openapi
from github_openapi.models.repos_create_repo_ruleset_request import ReposCreateRepoRulesetRequest
from github_openapi.models.repository_ruleset import RepositoryRuleset
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_create_repo_ruleset_request = {"name":"super cool ruleset","target":"branch","enforcement":"active","bypass_actors":[{"actor_id":234,"actor_type":"Team","bypass_mode":"always"}],"conditions":{"ref_name":{"include":["refs/heads/main","refs/heads/master"],"exclude":["refs/heads/dev*"]}},"rules":[{"type":"commit_author_email_pattern","parameters":{"operator":"contains","pattern":"github"}}]} # ReposCreateRepoRulesetRequest | Request body

    try:
        # Create a repository ruleset
        api_response = api_instance.repos_create_repo_ruleset(owner, repo, repos_create_repo_ruleset_request)
        print("The response of ReposApi->repos_create_repo_ruleset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_repo_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_create_repo_ruleset_request** | [**ReposCreateRepoRulesetRequest**](ReposCreateRepoRulesetRequest.md)| Request body | 

### Return type

[**RepositoryRuleset**](RepositoryRuleset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_tag_protection**
> TagProtection repos_create_tag_protection(owner, repo, repos_create_tag_protection_request)

Closing down - Create a tag protection state for a repository

> [!WARNING] > **Closing down notice:** This operation is closing down and will be removed after August 30, 2024. Use the \"[Repository Rulesets](https://docs.github.com/rest/repos/rules#create-a-repository-ruleset)\" endpoint instead.  This creates a tag protection state for a repository. This endpoint is only available to repository administrators.

### Example


```python
import github_openapi
from github_openapi.models.repos_create_tag_protection_request import ReposCreateTagProtectionRequest
from github_openapi.models.tag_protection import TagProtection
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_create_tag_protection_request = {"pattern":"v1.*"} # ReposCreateTagProtectionRequest | 

    try:
        # Closing down - Create a tag protection state for a repository
        api_response = api_instance.repos_create_tag_protection(owner, repo, repos_create_tag_protection_request)
        print("The response of ReposApi->repos_create_tag_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_tag_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_create_tag_protection_request** | [**ReposCreateTagProtectionRequest**](ReposCreateTagProtectionRequest.md)|  | 

### Return type

[**TagProtection**](TagProtection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_using_template**
> FullRepository repos_create_using_template(template_owner, template_repo, repos_create_using_template_request)

Create a repository using a template

Creates a new repository using a repository template. Use the `template_owner` and `template_repo` route parameters to specify the repository to use as the template. If the repository is not public, the authenticated user must own or be a member of an organization that owns the repository. To check if a repository is available to use as a template, get the repository's information using the [Get a repository](https://docs.github.com/rest/repos/repos#get-a-repository) endpoint and check that the `is_template` key is `true`.  OAuth app tokens and personal access tokens (classic) need the `public_repo` or `repo` scope to create a public repository, and `repo` scope to create a private repository.

### Example


```python
import github_openapi
from github_openapi.models.full_repository import FullRepository
from github_openapi.models.repos_create_using_template_request import ReposCreateUsingTemplateRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    template_owner = 'template_owner_example' # str | The account owner of the template repository. The name is not case sensitive.
    template_repo = 'template_repo_example' # str | The name of the template repository without the `.git` extension. The name is not case sensitive.
    repos_create_using_template_request = {"owner":"octocat","name":"Hello-World","description":"This is your first repository","include_all_branches":false,"private":false} # ReposCreateUsingTemplateRequest | 

    try:
        # Create a repository using a template
        api_response = api_instance.repos_create_using_template(template_owner, template_repo, repos_create_using_template_request)
        print("The response of ReposApi->repos_create_using_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_using_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_owner** | **str**| The account owner of the template repository. The name is not case sensitive. | 
 **template_repo** | **str**| The name of the template repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_create_using_template_request** | [**ReposCreateUsingTemplateRequest**](ReposCreateUsingTemplateRequest.md)|  | 

### Return type

[**FullRepository**](FullRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  * Location -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_create_webhook**
> Hook repos_create_webhook(owner, repo, repos_create_webhook_request=repos_create_webhook_request)

Create a repository webhook

Repositories can have multiple webhooks installed. Each webhook should have a unique `config`. Multiple webhooks can share the same `config` as long as those webhooks do not have any `events` that overlap.

### Example


```python
import github_openapi
from github_openapi.models.hook import Hook
from github_openapi.models.repos_create_webhook_request import ReposCreateWebhookRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_create_webhook_request = {"name":"web","active":true,"events":["push","pull_request"],"config":{"url":"https://example.com/webhook","content_type":"json","insecure_ssl":"0"}} # ReposCreateWebhookRequest |  (optional)

    try:
        # Create a repository webhook
        api_response = api_instance.repos_create_webhook(owner, repo, repos_create_webhook_request=repos_create_webhook_request)
        print("The response of ReposApi->repos_create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_create_webhook_request** | [**ReposCreateWebhookRequest**](ReposCreateWebhookRequest.md)|  | [optional] 

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  * Location -  <br>  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_decline_invitation_for_authenticated_user**
> repos_decline_invitation_for_authenticated_user(invitation_id)

Decline a repository invitation



### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    invitation_id = 56 # int | The unique identifier of the invitation.

    try:
        # Decline a repository invitation
        api_instance.repos_decline_invitation_for_authenticated_user(invitation_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_decline_invitation_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **int**| The unique identifier of the invitation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**409** | Conflict |  -  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete**
> repos_delete(owner, repo)

Delete a repository

Deleting a repository requires admin access.  If an organization owner has configured the organization to prevent members from deleting organization-owned repositories, you will get a `403 Forbidden` response.  OAuth app tokens and personal access tokens (classic) need the `delete_repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Delete a repository
        api_instance.repos_delete(owner, repo)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**403** | If an organization owner has configured the organization to prevent members from deleting organization-owned repositories, a member will get this response: |  -  |
**307** | Temporary Redirect |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_access_restrictions**
> repos_delete_access_restrictions(owner, repo, branch)

Delete access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Disables the ability to restrict who can push to this branch.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Delete access restrictions
        api_instance.repos_delete_access_restrictions(owner, repo, branch)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_access_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_admin_branch_protection**
> repos_delete_admin_branch_protection(owner, repo, branch)

Delete admin branch protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Removing admin enforcement requires admin or owner permissions to the repository and branch protection to be enabled.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Delete admin branch protection
        api_instance.repos_delete_admin_branch_protection(owner, repo, branch)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_admin_branch_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_an_environment**
> repos_delete_an_environment(owner, repo, environment_name)

Delete an environment

OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.

    try:
        # Delete an environment
        api_instance.repos_delete_an_environment(owner, repo, environment_name)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_an_environment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_autolink**
> repos_delete_autolink(owner, repo, autolink_id)

Delete an autolink reference from a repository

This deletes a single autolink reference by ID that was configured for the given repository.  Information about autolinks are only available to repository administrators.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    autolink_id = 56 # int | The unique identifier of the autolink.

    try:
        # Delete an autolink reference from a repository
        api_instance.repos_delete_autolink(owner, repo, autolink_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_autolink: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **autolink_id** | **int**| The unique identifier of the autolink. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_branch_protection**
> repos_delete_branch_protection(owner, repo, branch)

Delete branch protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Delete branch protection
        api_instance.repos_delete_branch_protection(owner, repo, branch)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_branch_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_commit_comment**
> repos_delete_commit_comment(owner, repo, comment_id)

Delete a commit comment



### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    comment_id = 56 # int | The unique identifier of the comment.

    try:
        # Delete a commit comment
        api_instance.repos_delete_commit_comment(owner, repo, comment_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_commit_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **comment_id** | **int**| The unique identifier of the comment. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_commit_signature_protection**
> repos_delete_commit_signature_protection(owner, repo, branch)

Delete commit signature protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  When authenticated with admin or owner permissions to the repository, you can use this endpoint to disable required signed commits on a branch. You must enable branch protection to require signed commits.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Delete commit signature protection
        api_instance.repos_delete_commit_signature_protection(owner, repo, branch)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_commit_signature_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_deploy_key**
> repos_delete_deploy_key(owner, repo, key_id)

Delete a deploy key

Deploy keys are immutable. If you need to update a key, remove the key and create a new one instead.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    key_id = 56 # int | The unique identifier of the key.

    try:
        # Delete a deploy key
        api_instance.repos_delete_deploy_key(owner, repo, key_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_deploy_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **key_id** | **int**| The unique identifier of the key. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_deployment**
> repos_delete_deployment(owner, repo, deployment_id)

Delete a deployment

If the repository only has one deployment, you can delete the deployment regardless of its status. If the repository has more than one deployment, you can only delete inactive deployments. This ensures that repositories with multiple deployments will always have an active deployment.  To set a deployment as inactive, you must:  *   Create a new deployment that is active so that the system has a record of the current state, then delete the previously active deployment. *   Mark the active deployment as inactive by adding any non-successful deployment status.  For more information, see \"[Create a deployment](https://docs.github.com/rest/deployments/deployments/#create-a-deployment)\" and \"[Create a deployment status](https://docs.github.com/rest/deployments/statuses#create-a-deployment-status).\"  OAuth app tokens and personal access tokens (classic) need the `repo` or `repo_deployment` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    deployment_id = 56 # int | deployment_id parameter

    try:
        # Delete a deployment
        api_instance.repos_delete_deployment(owner, repo, deployment_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **deployment_id** | **int**| deployment_id parameter | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_deployment_branch_policy**
> repos_delete_deployment_branch_policy(owner, repo, environment_name, branch_policy_id)

Delete a deployment branch policy

Deletes a deployment branch or tag policy for an environment.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    branch_policy_id = 56 # int | The unique identifier of the branch policy.

    try:
        # Delete a deployment branch policy
        api_instance.repos_delete_deployment_branch_policy(owner, repo, environment_name, branch_policy_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_deployment_branch_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **branch_policy_id** | **int**| The unique identifier of the branch policy. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_file**
> FileCommit repos_delete_file(owner, repo, path, repos_delete_file_request)

Delete a file

Deletes a file in a repository.  You can provide an additional `committer` parameter, which is an object containing information about the committer. Or, you can provide an `author` parameter, which is an object containing information about the author.  The `author` section is optional and is filled in with the `committer` information if omitted. If the `committer` information is omitted, the authenticated user's information is used.  You must provide values for both `name` and `email`, whether you choose to use `author` or `committer`. Otherwise, you'll receive a `422` status code.  > [!NOTE] > If you use this endpoint and the \"[Create or update file contents](https://docs.github.com/rest/repos/contents/#create-or-update-file-contents)\" endpoint in parallel, the concurrent requests will conflict and you will receive errors. You must use these endpoints serially instead.

### Example


```python
import github_openapi
from github_openapi.models.file_commit import FileCommit
from github_openapi.models.repos_delete_file_request import ReposDeleteFileRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    path = 'path_example' # str | path parameter
    repos_delete_file_request = {"message":"my commit message","committer":{"name":"Monalisa Octocat","email":"octocat@github.com"},"sha":"329688480d39049927147c162b9d2deaf885005f"} # ReposDeleteFileRequest | 

    try:
        # Delete a file
        api_response = api_instance.repos_delete_file(owner, repo, path, repos_delete_file_request)
        print("The response of ReposApi->repos_delete_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **path** | **str**| path parameter | 
 **repos_delete_file_request** | [**ReposDeleteFileRequest**](ReposDeleteFileRequest.md)|  | 

### Return type

[**FileCommit**](FileCommit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |
**409** | Conflict |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_invitation**
> repos_delete_invitation(owner, repo, invitation_id)

Delete a repository invitation



### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    invitation_id = 56 # int | The unique identifier of the invitation.

    try:
        # Delete a repository invitation
        api_instance.repos_delete_invitation(owner, repo, invitation_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **invitation_id** | **int**| The unique identifier of the invitation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_org_ruleset**
> repos_delete_org_ruleset(org, ruleset_id)

Delete an organization repository ruleset

Delete a ruleset for an organization.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    ruleset_id = 56 # int | The ID of the ruleset.

    try:
        # Delete an organization repository ruleset
        api_instance.repos_delete_org_ruleset(org, ruleset_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_org_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **ruleset_id** | **int**| The ID of the ruleset. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_pages_site**
> repos_delete_pages_site(owner, repo)

Delete a GitHub Pages site

Deletes a GitHub Pages site. For more information, see \"[About GitHub Pages](/github/working-with-github-pages/about-github-pages).  The authenticated user must be a repository administrator, maintainer, or have the 'manage GitHub Pages settings' permission.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Delete a GitHub Pages site
        api_instance.repos_delete_pages_site(owner, repo)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_pages_site: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_pull_request_review_protection**
> repos_delete_pull_request_review_protection(owner, repo, branch)

Delete pull request review protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Delete pull request review protection
        api_instance.repos_delete_pull_request_review_protection(owner, repo, branch)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_pull_request_review_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_release**
> repos_delete_release(owner, repo, release_id)

Delete a release

Users with push access to the repository can delete a release.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    release_id = 56 # int | The unique identifier of the release.

    try:
        # Delete a release
        api_instance.repos_delete_release(owner, repo, release_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **release_id** | **int**| The unique identifier of the release. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_release_asset**
> repos_delete_release_asset(owner, repo, asset_id)

Delete a release asset



### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    asset_id = 56 # int | The unique identifier of the asset.

    try:
        # Delete a release asset
        api_instance.repos_delete_release_asset(owner, repo, asset_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_release_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **asset_id** | **int**| The unique identifier of the asset. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_repo_ruleset**
> repos_delete_repo_ruleset(owner, repo, ruleset_id)

Delete a repository ruleset

Delete a ruleset for a repository.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ruleset_id = 56 # int | The ID of the ruleset.

    try:
        # Delete a repository ruleset
        api_instance.repos_delete_repo_ruleset(owner, repo, ruleset_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_repo_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ruleset_id** | **int**| The ID of the ruleset. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_tag_protection**
> repos_delete_tag_protection(owner, repo, tag_protection_id)

Closing down - Delete a tag protection state for a repository

> [!WARNING] > **Closing down notice:** This operation is closing down and will be removed after August 30, 2024. Use the \"[Repository Rulesets](https://docs.github.com/rest/repos/rules#delete-a-repository-ruleset)\" endpoint instead.  This deletes a tag protection state for a repository. This endpoint is only available to repository administrators.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    tag_protection_id = 56 # int | The unique identifier of the tag protection.

    try:
        # Closing down - Delete a tag protection state for a repository
        api_instance.repos_delete_tag_protection(owner, repo, tag_protection_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_tag_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **tag_protection_id** | **int**| The unique identifier of the tag protection. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_delete_webhook**
> repos_delete_webhook(owner, repo, hook_id)

Delete a repository webhook

Delete a webhook for an organization.  The authenticated user must be a repository owner, or have admin access in the repository, to delete the webhook.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.

    try:
        # Delete a repository webhook
        api_instance.repos_delete_webhook(owner, repo, hook_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_disable_automated_security_fixes**
> repos_disable_automated_security_fixes(owner, repo)

Disable automated security fixes

Disables automated security fixes for a repository. The authenticated user must have admin access to the repository. For more information, see \"[Configuring automated security fixes](https://docs.github.com/articles/configuring-automated-security-fixes)\".

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Disable automated security fixes
        api_instance.repos_disable_automated_security_fixes(owner, repo)
    except Exception as e:
        print("Exception when calling ReposApi->repos_disable_automated_security_fixes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_disable_deployment_protection_rule**
> repos_disable_deployment_protection_rule(environment_name, repo, owner, protection_rule_id)

Disable a custom protection rule for an environment

Disables a custom deployment protection rule for an environment.  The authenticated user must have admin or owner permissions to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    protection_rule_id = 56 # int | The unique identifier of the protection rule.

    try:
        # Disable a custom protection rule for an environment
        api_instance.repos_disable_deployment_protection_rule(environment_name, repo, owner, protection_rule_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_disable_deployment_protection_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **protection_rule_id** | **int**| The unique identifier of the protection rule. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_disable_private_vulnerability_reporting**
> repos_disable_private_vulnerability_reporting(owner, repo)

Disable private vulnerability reporting for a repository

Disables private vulnerability reporting for a repository. The authenticated user must have admin access to the repository. For more information, see \"[Privately reporting a security vulnerability](https://docs.github.com/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability)\".

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Disable private vulnerability reporting for a repository
        api_instance.repos_disable_private_vulnerability_reporting(owner, repo)
    except Exception as e:
        print("Exception when calling ReposApi->repos_disable_private_vulnerability_reporting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | A header with no content is returned. |  -  |
**422** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_disable_vulnerability_alerts**
> repos_disable_vulnerability_alerts(owner, repo)

Disable vulnerability alerts

Disables dependency alerts and the dependency graph for a repository. The authenticated user must have admin access to the repository. For more information, see \"[About security alerts for vulnerable dependencies](https://docs.github.com/articles/about-security-alerts-for-vulnerable-dependencies)\".

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Disable vulnerability alerts
        api_instance.repos_disable_vulnerability_alerts(owner, repo)
    except Exception as e:
        print("Exception when calling ReposApi->repos_disable_vulnerability_alerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_download_tarball_archive**
> repos_download_tarball_archive(owner, repo, ref)

Download a repository archive (tar)

Gets a redirect URL to download a tar archive for a repository. If you omit `:ref`, the repository’s default branch (usually `main`) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use the `Location` header to make a second `GET` request.  > [!NOTE] > For private repositories, these links are temporary and expire after five minutes.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ref = 'ref_example' # str | 

    try:
        # Download a repository archive (tar)
        api_instance.repos_download_tarball_archive(owner, repo, ref)
    except Exception as e:
        print("Exception when calling ReposApi->repos_download_tarball_archive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ref** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Response |  * Location -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_download_zipball_archive**
> repos_download_zipball_archive(owner, repo, ref)

Download a repository archive (zip)

Gets a redirect URL to download a zip archive for a repository. If you omit `:ref`, the repository’s default branch (usually `main`) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use the `Location` header to make a second `GET` request.  > [!NOTE] > For private repositories, these links are temporary and expire after five minutes. If the repository is empty, you will receive a 404 when you follow the redirect.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ref = 'ref_example' # str | 

    try:
        # Download a repository archive (zip)
        api_instance.repos_download_zipball_archive(owner, repo, ref)
    except Exception as e:
        print("Exception when calling ReposApi->repos_download_zipball_archive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ref** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Response |  * Location -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_enable_automated_security_fixes**
> repos_enable_automated_security_fixes(owner, repo)

Enable automated security fixes

Enables automated security fixes for a repository. The authenticated user must have admin access to the repository. For more information, see \"[Configuring automated security fixes](https://docs.github.com/articles/configuring-automated-security-fixes)\".

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Enable automated security fixes
        api_instance.repos_enable_automated_security_fixes(owner, repo)
    except Exception as e:
        print("Exception when calling ReposApi->repos_enable_automated_security_fixes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_enable_private_vulnerability_reporting**
> repos_enable_private_vulnerability_reporting(owner, repo)

Enable private vulnerability reporting for a repository

Enables private vulnerability reporting for a repository. The authenticated user must have admin access to the repository. For more information, see \"[Privately reporting a security vulnerability](https://docs.github.com/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability).\"

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Enable private vulnerability reporting for a repository
        api_instance.repos_enable_private_vulnerability_reporting(owner, repo)
    except Exception as e:
        print("Exception when calling ReposApi->repos_enable_private_vulnerability_reporting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | A header with no content is returned. |  -  |
**422** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_enable_vulnerability_alerts**
> repos_enable_vulnerability_alerts(owner, repo)

Enable vulnerability alerts

Enables dependency alerts and the dependency graph for a repository. The authenticated user must have admin access to the repository. For more information, see \"[About security alerts for vulnerable dependencies](https://docs.github.com/articles/about-security-alerts-for-vulnerable-dependencies)\".

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Enable vulnerability alerts
        api_instance.repos_enable_vulnerability_alerts(owner, repo)
    except Exception as e:
        print("Exception when calling ReposApi->repos_enable_vulnerability_alerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_generate_release_notes**
> ReleaseNotesContent repos_generate_release_notes(owner, repo, repos_generate_release_notes_request)

Generate release notes content for a release

Generate a name and body describing a [release](https://docs.github.com/rest/releases/releases#get-a-release). The body content will be markdown formatted and contain information like the changes since last release and users who contributed. The generated release notes are not saved anywhere. They are intended to be generated and used when creating a new release.

### Example


```python
import github_openapi
from github_openapi.models.release_notes_content import ReleaseNotesContent
from github_openapi.models.repos_generate_release_notes_request import ReposGenerateReleaseNotesRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_generate_release_notes_request = {"tag_name":"v1.0.0","target_commitish":"main","previous_tag_name":"v0.9.2","configuration_file_path":".github/custom_release_config.yml"} # ReposGenerateReleaseNotesRequest | 

    try:
        # Generate release notes content for a release
        api_response = api_instance.repos_generate_release_notes(owner, repo, repos_generate_release_notes_request)
        print("The response of ReposApi->repos_generate_release_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_generate_release_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_generate_release_notes_request** | [**ReposGenerateReleaseNotesRequest**](ReposGenerateReleaseNotesRequest.md)|  | 

### Return type

[**ReleaseNotesContent**](ReleaseNotesContent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Name and body of generated release notes |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get**
> FullRepository repos_get(owner, repo)

Get a repository

The `parent` and `source` objects are present when the repository is a fork. `parent` is the repository this repository was forked from, `source` is the ultimate source for the network.  > [!NOTE] > In order to see the `security_and_analysis` block for a repository you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see \"[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).\"

### Example


```python
import github_openapi
from github_openapi.models.full_repository import FullRepository
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get a repository
        api_response = api_instance.repos_get(owner, repo)
        print("The response of ReposApi->repos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**FullRepository**](FullRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**301** | Moved permanently |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_access_restrictions**
> BranchRestrictionPolicy repos_get_access_restrictions(owner, repo, branch)

Get access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists who has access to this protected branch.  > [!NOTE] > Users, apps, and teams `restrictions` are only available for organization-owned repositories.

### Example


```python
import github_openapi
from github_openapi.models.branch_restriction_policy import BranchRestrictionPolicy
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Get access restrictions
        api_response = api_instance.repos_get_access_restrictions(owner, repo, branch)
        print("The response of ReposApi->repos_get_access_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_access_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

[**BranchRestrictionPolicy**](BranchRestrictionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_admin_branch_protection**
> ProtectedBranchAdminEnforced repos_get_admin_branch_protection(owner, repo, branch)

Get admin branch protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example


```python
import github_openapi
from github_openapi.models.protected_branch_admin_enforced import ProtectedBranchAdminEnforced
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Get admin branch protection
        api_response = api_instance.repos_get_admin_branch_protection(owner, repo, branch)
        print("The response of ReposApi->repos_get_admin_branch_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_admin_branch_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

[**ProtectedBranchAdminEnforced**](ProtectedBranchAdminEnforced.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_all_deployment_protection_rules**
> ReposGetAllDeploymentProtectionRules200Response repos_get_all_deployment_protection_rules(environment_name, repo, owner)

Get all deployment protection rules for an environment

Gets all custom deployment protection rules that are enabled for an environment. Anyone with read access to the repository can use this endpoint. For more information about environments, see \"[Using environments for deployment](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment).\"  For more information about the app that is providing this custom deployment rule, see the [documentation for the `GET /apps/{app_slug}` endpoint](https://docs.github.com/rest/apps/apps#get-an-app).  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.repos_get_all_deployment_protection_rules200_response import ReposGetAllDeploymentProtectionRules200Response
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.

    try:
        # Get all deployment protection rules for an environment
        api_response = api_instance.repos_get_all_deployment_protection_rules(environment_name, repo, owner)
        print("The response of ReposApi->repos_get_all_deployment_protection_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_all_deployment_protection_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 

### Return type

[**ReposGetAllDeploymentProtectionRules200Response**](ReposGetAllDeploymentProtectionRules200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of deployment protection rules |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_all_environments**
> ReposGetAllEnvironments200Response repos_get_all_environments(owner, repo, per_page=per_page, page=page)

List environments

Lists the environments for a repository.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.repos_get_all_environments200_response import ReposGetAllEnvironments200Response
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List environments
        api_response = api_instance.repos_get_all_environments(owner, repo, per_page=per_page, page=page)
        print("The response of ReposApi->repos_get_all_environments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_all_environments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ReposGetAllEnvironments200Response**](ReposGetAllEnvironments200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_all_status_check_contexts**
> List[str] repos_get_all_status_check_contexts(owner, repo, branch)

Get all status check contexts

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Get all status check contexts
        api_response = api_instance.repos_get_all_status_check_contexts(owner, repo, branch)
        print("The response of ReposApi->repos_get_all_status_check_contexts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_all_status_check_contexts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_all_topics**
> Topic repos_get_all_topics(owner, repo, page=page, per_page=per_page)

Get all repository topics



### Example


```python
import github_openapi
from github_openapi.models.topic import Topic
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # Get all repository topics
        api_response = api_instance.repos_get_all_topics(owner, repo, page=page, per_page=per_page)
        print("The response of ReposApi->repos_get_all_topics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_all_topics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]

### Return type

[**Topic**](Topic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_apps_with_access_to_protected_branch**
> List[Integration] repos_get_apps_with_access_to_protected_branch(owner, repo, branch)

Get apps with access to the protected branch

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists the GitHub Apps that have push access to this branch. Only GitHub Apps that are installed on the repository and that have been granted write access to the repository contents can be added as authorized actors on a protected branch.

### Example


```python
import github_openapi
from github_openapi.models.integration import Integration
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Get apps with access to the protected branch
        api_response = api_instance.repos_get_apps_with_access_to_protected_branch(owner, repo, branch)
        print("The response of ReposApi->repos_get_apps_with_access_to_protected_branch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_apps_with_access_to_protected_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

[**List[Integration]**](Integration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_autolink**
> Autolink repos_get_autolink(owner, repo, autolink_id)

Get an autolink reference of a repository

This returns a single autolink reference by ID that was configured for the given repository.  Information about autolinks are only available to repository administrators.

### Example


```python
import github_openapi
from github_openapi.models.autolink import Autolink
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    autolink_id = 56 # int | The unique identifier of the autolink.

    try:
        # Get an autolink reference of a repository
        api_response = api_instance.repos_get_autolink(owner, repo, autolink_id)
        print("The response of ReposApi->repos_get_autolink:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_autolink: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **autolink_id** | **int**| The unique identifier of the autolink. | 

### Return type

[**Autolink**](Autolink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_branch**
> BranchWithProtection repos_get_branch(owner, repo, branch)

Get a branch



### Example


```python
import github_openapi
from github_openapi.models.branch_with_protection import BranchWithProtection
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Get a branch
        api_response = api_instance.repos_get_branch(owner, repo, branch)
        print("The response of ReposApi->repos_get_branch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

[**BranchWithProtection**](BranchWithProtection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**301** | Moved permanently |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_branch_protection**
> BranchProtection repos_get_branch_protection(owner, repo, branch)

Get branch protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example


```python
import github_openapi
from github_openapi.models.branch_protection import BranchProtection
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Get branch protection
        api_response = api_instance.repos_get_branch_protection(owner, repo, branch)
        print("The response of ReposApi->repos_get_branch_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_branch_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

[**BranchProtection**](BranchProtection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_branch_rules**
> List[RepositoryRuleDetailed] repos_get_branch_rules(owner, repo, branch, per_page=per_page, page=page)

Get rules for a branch

Returns all active rules that apply to the specified branch. The branch does not need to exist; rules that would apply to a branch with that name will be returned. All active rules that apply will be returned, regardless of the level at which they are configured (e.g. repository or organization). Rules in rulesets with \"evaluate\" or \"disabled\" enforcement statuses are not returned.

### Example


```python
import github_openapi
from github_openapi.models.repository_rule_detailed import RepositoryRuleDetailed
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # Get rules for a branch
        api_response = api_instance.repos_get_branch_rules(owner, repo, branch, per_page=per_page, page=page)
        print("The response of ReposApi->repos_get_branch_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_branch_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[RepositoryRuleDetailed]**](RepositoryRuleDetailed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_clones**
> CloneTraffic repos_get_clones(owner, repo, per=per)

Get repository clones

Get the total number of clones and breakdown per day or week for the last 14 days. Timestamps are aligned to UTC midnight of the beginning of the day or week. Week begins on Monday.

### Example


```python
import github_openapi
from github_openapi.models.clone_traffic import CloneTraffic
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per = day # str | The time frame to display results for. (optional) (default to day)

    try:
        # Get repository clones
        api_response = api_instance.repos_get_clones(owner, repo, per=per)
        print("The response of ReposApi->repos_get_clones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_clones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per** | **str**| The time frame to display results for. | [optional] [default to day]

### Return type

[**CloneTraffic**](CloneTraffic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_code_frequency_stats**
> List[List[int]] repos_get_code_frequency_stats(owner, repo)

Get the weekly commit activity

Returns a weekly aggregate of the number of additions and deletions pushed to a repository.  > [!NOTE] > This endpoint can only be used for repositories with fewer than 10,000 commits. If the repository contains 10,000 or more commits, a 422 status code will be returned.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get the weekly commit activity
        api_response = api_instance.repos_get_code_frequency_stats(owner, repo)
        print("The response of ReposApi->repos_get_code_frequency_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_code_frequency_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

**List[List[int]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a weekly aggregate of the number of additions and deletions pushed to a repository. |  -  |
**202** | Accepted |  -  |
**204** | A header with no content is returned. |  -  |
**422** | Repository contains more than 10,000 commits |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_collaborator_permission_level**
> RepositoryCollaboratorPermission repos_get_collaborator_permission_level(owner, repo, username)

Get repository permissions for a user

Checks the repository permission of a collaborator. The possible repository permissions are `admin`, `write`, `read`, and `none`.  *Note*: The `permission` attribute provides the legacy base roles of `admin`, `write`, `read`, and `none`, where the `maintain` role is mapped to `write` and the `triage` role is mapped to `read`. To determine the role assigned to the collaborator, see the `role_name` attribute, which will provide the full role name, including custom roles. The `permissions` hash can also be used to determine which base level of access the collaborator has to the repository.

### Example


```python
import github_openapi
from github_openapi.models.repository_collaborator_permission import RepositoryCollaboratorPermission
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Get repository permissions for a user
        api_response = api_instance.repos_get_collaborator_permission_level(owner, repo, username)
        print("The response of ReposApi->repos_get_collaborator_permission_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_collaborator_permission_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 

### Return type

[**RepositoryCollaboratorPermission**](RepositoryCollaboratorPermission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | if user has admin permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_combined_status_for_ref**
> CombinedCommitStatus repos_get_combined_status_for_ref(owner, repo, ref, per_page=per_page, page=page)

Get the combined status for a specific reference

Users with pull access in a repository can access a combined view of commit statuses for a given ref. The ref can be a SHA, a branch name, or a tag name.   Additionally, a combined `state` is returned. The `state` is one of:  *   **failure** if any of the contexts report as `error` or `failure` *   **pending** if there are no statuses or a context is `pending` *   **success** if the latest status for all contexts is `success`

### Example


```python
import github_openapi
from github_openapi.models.combined_commit_status import CombinedCommitStatus
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ref = 'ref_example' # str | The commit reference. Can be a commit SHA, branch name (`heads/BRANCH_NAME`), or tag name (`tags/TAG_NAME`). For more information, see \"[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)\" in the Git documentation.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # Get the combined status for a specific reference
        api_response = api_instance.repos_get_combined_status_for_ref(owner, repo, ref, per_page=per_page, page=page)
        print("The response of ReposApi->repos_get_combined_status_for_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_combined_status_for_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ref** | **str**| The commit reference. Can be a commit SHA, branch name (&#x60;heads/BRANCH_NAME&#x60;), or tag name (&#x60;tags/TAG_NAME&#x60;). For more information, see \&quot;[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)\&quot; in the Git documentation. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**CombinedCommitStatus**](CombinedCommitStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_commit**
> Commit repos_get_commit(owner, repo, ref, page=page, per_page=per_page)

Get a commit

Returns the contents of a single commit reference. You must have `read` access for the repository to use this endpoint.  > [!NOTE] > If there are more than 300 files in the commit diff and the default JSON media type is requested, the response will include pagination link headers for the remaining files, up to a limit of 3000 files. Each page contains the static commit information, and the only changes are to the file listing.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\" Pagination query parameters are not supported for these media types.  - **`application/vnd.github.diff`**: Returns the diff of the commit. Larger diffs may time out and return a 5xx status code. - **`application/vnd.github.patch`**: Returns the patch of the commit. Diffs with binary data will have no `patch` property. Larger diffs may time out and return a 5xx status code. - **`application/vnd.github.sha`**: Returns the commit's SHA-1 hash. You can use this endpoint to check if a remote reference's SHA-1 hash is the same as your local reference's SHA-1 hash by providing the local SHA-1 reference as the ETag.  **Signature verification object**  The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:  | Name | Type | Description | | ---- | ---- | ----------- | | `verified` | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified. | | `reason` | `string` | The reason for verified value. Possible values and their meanings are enumerated in table below. | | `signature` | `string` | The signature that was extracted from the commit. | | `payload` | `string` | The value that was signed. | | `verified_at` | `string` | The date the signature was verified by GitHub. |  These are the possible values for `reason` in the `verification` object:  | Value | Description | | ----- | ----------- | | `expired_key` | The key that made the signature is expired. | | `not_signing_key` | The \"signing\" flag is not among the usage flags in the GPG key that made the signature. | | `gpgverify_error` | There was an error communicating with the signature verification service. | | `gpgverify_unavailable` | The signature verification service is currently unavailable. | | `unsigned` | The object does not include a signature. | | `unknown_signature_type` | A non-PGP signature was found in the commit. | | `no_user` | No user was associated with the `committer` email address in the commit. | | `unverified_email` | The `committer` email address in the commit was associated with a user, but the email address is not verified on their account. | | `bad_email` | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. | | `unknown_key` | The key that made the signature has not been registered with any user's account. | | `malformed_signature` | There was an error parsing the signature. | | `invalid` | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | `valid` | None of the above errors applied, so the signature is considered to be verified. |

### Example


```python
import github_openapi
from github_openapi.models.commit import Commit
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ref = 'ref_example' # str | The commit reference. Can be a commit SHA, branch name (`heads/BRANCH_NAME`), or tag name (`tags/TAG_NAME`). For more information, see \"[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)\" in the Git documentation.
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # Get a commit
        api_response = api_instance.repos_get_commit(owner, repo, ref, page=page, per_page=per_page)
        print("The response of ReposApi->repos_get_commit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_commit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ref** | **str**| The commit reference. Can be a commit SHA, branch name (&#x60;heads/BRANCH_NAME&#x60;), or tag name (&#x60;tags/TAG_NAME&#x60;). For more information, see \&quot;[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)\&quot; in the Git documentation. | 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]

### Return type

[**Commit**](Commit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |
**503** | Service unavailable |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_commit_activity_stats**
> List[CommitActivity] repos_get_commit_activity_stats(owner, repo)

Get the last year of commit activity

Returns the last year of commit activity grouped by week. The `days` array is a group of commits per day, starting on `Sunday`.

### Example


```python
import github_openapi
from github_openapi.models.commit_activity import CommitActivity
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get the last year of commit activity
        api_response = api_instance.repos_get_commit_activity_stats(owner, repo)
        print("The response of ReposApi->repos_get_commit_activity_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_commit_activity_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**List[CommitActivity]**](CommitActivity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**202** | Accepted |  -  |
**204** | A header with no content is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_commit_comment**
> CommitComment repos_get_commit_comment(owner, repo, comment_id)

Get a commit comment

Gets a specified commit comment.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github-commitcomment.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.

### Example


```python
import github_openapi
from github_openapi.models.commit_comment import CommitComment
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    comment_id = 56 # int | The unique identifier of the comment.

    try:
        # Get a commit comment
        api_response = api_instance.repos_get_commit_comment(owner, repo, comment_id)
        print("The response of ReposApi->repos_get_commit_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_commit_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **comment_id** | **int**| The unique identifier of the comment. | 

### Return type

[**CommitComment**](CommitComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_commit_signature_protection**
> ProtectedBranchAdminEnforced repos_get_commit_signature_protection(owner, repo, branch)

Get commit signature protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  When authenticated with admin or owner permissions to the repository, you can use this endpoint to check whether a branch requires signed commits. An enabled status of `true` indicates you must sign commits on this branch. For more information, see [Signing commits with GPG](https://docs.github.com/articles/signing-commits-with-gpg) in GitHub Help.  > [!NOTE] > You must enable branch protection to require signed commits.

### Example


```python
import github_openapi
from github_openapi.models.protected_branch_admin_enforced import ProtectedBranchAdminEnforced
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Get commit signature protection
        api_response = api_instance.repos_get_commit_signature_protection(owner, repo, branch)
        print("The response of ReposApi->repos_get_commit_signature_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_commit_signature_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

[**ProtectedBranchAdminEnforced**](ProtectedBranchAdminEnforced.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_community_profile_metrics**
> CommunityProfile repos_get_community_profile_metrics(owner, repo)

Get community profile metrics

Returns all community profile metrics for a repository. The repository cannot be a fork.  The returned metrics include an overall health score, the repository description, the presence of documentation, the detected code of conduct, the detected license, and the presence of ISSUE\\_TEMPLATE, PULL\\_REQUEST\\_TEMPLATE, README, and CONTRIBUTING files.  The `health_percentage` score is defined as a percentage of how many of the recommended community health files are present. For more information, see \"[About community profiles for public repositories](https://docs.github.com/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories).\"  `content_reports_enabled` is only returned for organization-owned repositories.

### Example


```python
import github_openapi
from github_openapi.models.community_profile import CommunityProfile
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get community profile metrics
        api_response = api_instance.repos_get_community_profile_metrics(owner, repo)
        print("The response of ReposApi->repos_get_community_profile_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_community_profile_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**CommunityProfile**](CommunityProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_content**
> ContentTree repos_get_content(owner, repo, path, ref=ref)

Get repository content

Gets the contents of a file or directory in a repository. Specify the file path or directory with the `path` parameter. If you omit the `path` parameter, you will receive the contents of the repository's root directory.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github.raw+json`**: Returns the raw file contents for files and symlinks. - **`application/vnd.github.html+json`**: Returns the file contents in HTML. Markup languages are rendered to HTML using GitHub's open-source [Markup library](https://github.com/github/markup). - **`application/vnd.github.object+json`**: Returns the contents in a consistent object format regardless of the content type. For example, instead of an array of objects for a directory, the response will be an object with an `entries` attribute containing the array of objects.  If the content is a directory, the response will be an array of objects, one object for each item in the directory. When listing the contents of a directory, submodules have their \"type\" specified as \"file\". Logically, the value _should_ be \"submodule\". This behavior exists [for backwards compatibility purposes](https://git.io/v1YCW). In the next major version of the API, the type will be returned as \"submodule\".  If the content is a symlink and the symlink's target is a normal file in the repository, then the API responds with the content of the file. Otherwise, the API responds with an object describing the symlink itself.  If the content is a submodule, the `submodule_git_url` field identifies the location of the submodule repository, and the `sha` identifies a specific commit within the submodule repository. Git uses the given URL when cloning the submodule repository, and checks out the submodule at that specific commit. If the submodule repository is not hosted on github.com, the Git URLs (`git_url` and `_links[\"git\"]`) and the github.com URLs (`html_url` and `_links[\"html\"]`) will have null values.  **Notes**:  - To get a repository's contents recursively, you can [recursively get the tree](https://docs.github.com/rest/git/trees#get-a-tree). - This API has an upper limit of 1,000 files for a directory. If you need to retrieve more files, use the [Git Trees API](https://docs.github.com/rest/git/trees#get-a-tree). - Download URLs expire and are meant to be used just once. To ensure the download URL does not expire, please use the contents API to obtain a fresh download URL for each download. - If the requested file's size is:   - 1 MB or smaller: All features of this endpoint are supported.   - Between 1-100 MB: Only the `raw` or `object` custom media types are supported. Both will work as normal, except that when using the `object` media type, the `content` field will be an empty string and the `encoding` field will be `\"none\"`. To get the contents of these larger files, use the `raw` media type.   - Greater than 100 MB: This endpoint is not supported.

### Example


```python
import github_openapi
from github_openapi.models.content_tree import ContentTree
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    path = 'path_example' # str | path parameter
    ref = 'ref_example' # str | The name of the commit/branch/tag. Default: the repository’s default branch. (optional)

    try:
        # Get repository content
        api_response = api_instance.repos_get_content(owner, repo, path, ref=ref)
        print("The response of ReposApi->repos_get_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **path** | **str**| path parameter | 
 **ref** | **str**| The name of the commit/branch/tag. Default: the repository’s default branch. | [optional] 

### Return type

[**ContentTree**](ContentTree.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.github.object, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**302** | Found |  -  |
**304** | Not modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_contributors_stats**
> List[ContributorActivity] repos_get_contributors_stats(owner, repo)

Get all contributor commit activity

 Returns the `total` number of commits authored by the contributor. In addition, the response includes a Weekly Hash (`weeks` array) with the following information:  *   `w` - Start of the week, given as a [Unix timestamp](https://en.wikipedia.org/wiki/Unix_time). *   `a` - Number of additions *   `d` - Number of deletions *   `c` - Number of commits  > [!NOTE] > This endpoint will return `0` values for all addition and deletion counts in repositories with 10,000 or more commits.

### Example


```python
import github_openapi
from github_openapi.models.contributor_activity import ContributorActivity
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get all contributor commit activity
        api_response = api_instance.repos_get_contributors_stats(owner, repo)
        print("The response of ReposApi->repos_get_contributors_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_contributors_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**List[ContributorActivity]**](ContributorActivity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**202** | Accepted |  -  |
**204** | A header with no content is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_custom_deployment_protection_rule**
> DeploymentProtectionRule repos_get_custom_deployment_protection_rule(owner, repo, environment_name, protection_rule_id)

Get a custom deployment protection rule

Gets an enabled custom deployment protection rule for an environment. Anyone with read access to the repository can use this endpoint. For more information about environments, see \"[Using environments for deployment](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment).\"  For more information about the app that is providing this custom deployment rule, see [`GET /apps/{app_slug}`](https://docs.github.com/rest/apps/apps#get-an-app).  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.deployment_protection_rule import DeploymentProtectionRule
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    protection_rule_id = 56 # int | The unique identifier of the protection rule.

    try:
        # Get a custom deployment protection rule
        api_response = api_instance.repos_get_custom_deployment_protection_rule(owner, repo, environment_name, protection_rule_id)
        print("The response of ReposApi->repos_get_custom_deployment_protection_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_custom_deployment_protection_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **protection_rule_id** | **int**| The unique identifier of the protection rule. | 

### Return type

[**DeploymentProtectionRule**](DeploymentProtectionRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_custom_properties_values**
> List[CustomPropertyValue] repos_get_custom_properties_values(owner, repo)

Get all custom property values for a repository

Gets all custom property values that are set for a repository. Users with read access to the repository can use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.custom_property_value import CustomPropertyValue
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get all custom property values for a repository
        api_response = api_instance.repos_get_custom_properties_values(owner, repo)
        print("The response of ReposApi->repos_get_custom_properties_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_custom_properties_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**List[CustomPropertyValue]**](CustomPropertyValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_deploy_key**
> DeployKey repos_get_deploy_key(owner, repo, key_id)

Get a deploy key



### Example


```python
import github_openapi
from github_openapi.models.deploy_key import DeployKey
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    key_id = 56 # int | The unique identifier of the key.

    try:
        # Get a deploy key
        api_response = api_instance.repos_get_deploy_key(owner, repo, key_id)
        print("The response of ReposApi->repos_get_deploy_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_deploy_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **key_id** | **int**| The unique identifier of the key. | 

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_deployment**
> Deployment repos_get_deployment(owner, repo, deployment_id)

Get a deployment



### Example


```python
import github_openapi
from github_openapi.models.deployment import Deployment
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    deployment_id = 56 # int | deployment_id parameter

    try:
        # Get a deployment
        api_response = api_instance.repos_get_deployment(owner, repo, deployment_id)
        print("The response of ReposApi->repos_get_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **deployment_id** | **int**| deployment_id parameter | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_deployment_branch_policy**
> DeploymentBranchPolicy repos_get_deployment_branch_policy(owner, repo, environment_name, branch_policy_id)

Get a deployment branch policy

Gets a deployment branch or tag policy for an environment.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.deployment_branch_policy import DeploymentBranchPolicy
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    branch_policy_id = 56 # int | The unique identifier of the branch policy.

    try:
        # Get a deployment branch policy
        api_response = api_instance.repos_get_deployment_branch_policy(owner, repo, environment_name, branch_policy_id)
        print("The response of ReposApi->repos_get_deployment_branch_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_deployment_branch_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **branch_policy_id** | **int**| The unique identifier of the branch policy. | 

### Return type

[**DeploymentBranchPolicy**](DeploymentBranchPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_deployment_status**
> DeploymentStatus repos_get_deployment_status(owner, repo, deployment_id, status_id)

Get a deployment status

Users with pull access can view a deployment status for a deployment:

### Example


```python
import github_openapi
from github_openapi.models.deployment_status import DeploymentStatus
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    deployment_id = 56 # int | deployment_id parameter
    status_id = 56 # int | 

    try:
        # Get a deployment status
        api_response = api_instance.repos_get_deployment_status(owner, repo, deployment_id, status_id)
        print("The response of ReposApi->repos_get_deployment_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_deployment_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **deployment_id** | **int**| deployment_id parameter | 
 **status_id** | **int**|  | 

### Return type

[**DeploymentStatus**](DeploymentStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_environment**
> Environment repos_get_environment(owner, repo, environment_name)

Get an environment

> [!NOTE] > To get information about name patterns that branches must match in order to deploy to this environment, see \"[Get a deployment branch policy](/rest/deployments/branch-policies#get-a-deployment-branch-policy).\"  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.environment import Environment
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.

    try:
        # Get an environment
        api_response = api_instance.repos_get_environment(owner, repo, environment_name)
        print("The response of ReposApi->repos_get_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_environment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 

### Return type

[**Environment**](Environment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_latest_pages_build**
> PageBuild repos_get_latest_pages_build(owner, repo)

Get latest Pages build

Gets information about the single most recent build of a GitHub Pages site.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.page_build import PageBuild
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get latest Pages build
        api_response = api_instance.repos_get_latest_pages_build(owner, repo)
        print("The response of ReposApi->repos_get_latest_pages_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_latest_pages_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**PageBuild**](PageBuild.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_latest_release**
> Release repos_get_latest_release(owner, repo)

Get the latest release

View the latest published full release for the repository.  The latest release is the most recent non-prerelease, non-draft release, sorted by the `created_at` attribute. The `created_at` attribute is the date of the commit used for the release, and not the date when the release was drafted or published.

### Example


```python
import github_openapi
from github_openapi.models.release import Release
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get the latest release
        api_response = api_instance.repos_get_latest_release(owner, repo)
        print("The response of ReposApi->repos_get_latest_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_latest_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**Release**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_org_rule_suite**
> RuleSuite repos_get_org_rule_suite(org, rule_suite_id)

Get an organization rule suite

Gets information about a suite of rule evaluations from within an organization. For more information, see \"[Managing rulesets for repositories in your organization](https://docs.github.com/organizations/managing-organization-settings/managing-rulesets-for-repositories-in-your-organization#viewing-insights-for-rulesets).\"

### Example


```python
import github_openapi
from github_openapi.models.rule_suite import RuleSuite
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    rule_suite_id = 56 # int | The unique identifier of the rule suite result. To get this ID, you can use [GET /repos/{owner}/{repo}/rulesets/rule-suites](https://docs.github.com/rest/repos/rule-suites#list-repository-rule-suites) for repositories and [GET /orgs/{org}/rulesets/rule-suites](https://docs.github.com/rest/orgs/rule-suites#list-organization-rule-suites) for organizations.

    try:
        # Get an organization rule suite
        api_response = api_instance.repos_get_org_rule_suite(org, rule_suite_id)
        print("The response of ReposApi->repos_get_org_rule_suite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_org_rule_suite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **rule_suite_id** | **int**| The unique identifier of the rule suite result. To get this ID, you can use [GET /repos/{owner}/{repo}/rulesets/rule-suites](https://docs.github.com/rest/repos/rule-suites#list-repository-rule-suites) for repositories and [GET /orgs/{org}/rulesets/rule-suites](https://docs.github.com/rest/orgs/rule-suites#list-organization-rule-suites) for organizations. | 

### Return type

[**RuleSuite**](RuleSuite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_org_rule_suites**
> List[RuleSuitesInner] repos_get_org_rule_suites(org, ref=ref, repository_name=repository_name, time_period=time_period, actor_name=actor_name, rule_suite_result=rule_suite_result, per_page=per_page, page=page)

List organization rule suites

Lists suites of rule evaluations at the organization level. For more information, see \"[Managing rulesets for repositories in your organization](https://docs.github.com/organizations/managing-organization-settings/managing-rulesets-for-repositories-in-your-organization#viewing-insights-for-rulesets).\"

### Example


```python
import github_openapi
from github_openapi.models.rule_suites_inner import RuleSuitesInner
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    ref = 'ref_example' # str | The name of the ref. Cannot contain wildcard characters. Optionally prefix with `refs/heads/` to limit to branches or `refs/tags/` to limit to tags. Omit the prefix to search across all refs. When specified, only rule evaluations triggered for this ref will be returned. (optional)
    repository_name = 'repository_name_example' # str | The name of the repository to filter on. (optional)
    time_period = day # str | The time period to filter by.  For example, `day` will filter for rule suites that occurred in the past 24 hours, and `week` will filter for insights that occurred in the past 7 days (168 hours). (optional) (default to day)
    actor_name = 'actor_name_example' # str | The handle for the GitHub user account to filter on. When specified, only rule evaluations triggered by this actor will be returned. (optional)
    rule_suite_result = all # str | The rule results to filter on. When specified, only suites with this result will be returned. (optional) (default to all)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List organization rule suites
        api_response = api_instance.repos_get_org_rule_suites(org, ref=ref, repository_name=repository_name, time_period=time_period, actor_name=actor_name, rule_suite_result=rule_suite_result, per_page=per_page, page=page)
        print("The response of ReposApi->repos_get_org_rule_suites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_org_rule_suites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **ref** | **str**| The name of the ref. Cannot contain wildcard characters. Optionally prefix with &#x60;refs/heads/&#x60; to limit to branches or &#x60;refs/tags/&#x60; to limit to tags. Omit the prefix to search across all refs. When specified, only rule evaluations triggered for this ref will be returned. | [optional] 
 **repository_name** | **str**| The name of the repository to filter on. | [optional] 
 **time_period** | **str**| The time period to filter by.  For example, &#x60;day&#x60; will filter for rule suites that occurred in the past 24 hours, and &#x60;week&#x60; will filter for insights that occurred in the past 7 days (168 hours). | [optional] [default to day]
 **actor_name** | **str**| The handle for the GitHub user account to filter on. When specified, only rule evaluations triggered by this actor will be returned. | [optional] 
 **rule_suite_result** | **str**| The rule results to filter on. When specified, only suites with this result will be returned. | [optional] [default to all]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[RuleSuitesInner]**](RuleSuitesInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_org_ruleset**
> RepositoryRuleset repos_get_org_ruleset(org, ruleset_id)

Get an organization repository ruleset

Get a repository ruleset for an organization.  **Note:** To prevent leaking sensitive information, the `bypass_actors` property is only returned if the user making the API request has write access to the ruleset.

### Example


```python
import github_openapi
from github_openapi.models.repository_ruleset import RepositoryRuleset
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    ruleset_id = 56 # int | The ID of the ruleset.

    try:
        # Get an organization repository ruleset
        api_response = api_instance.repos_get_org_ruleset(org, ruleset_id)
        print("The response of ReposApi->repos_get_org_ruleset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_org_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **ruleset_id** | **int**| The ID of the ruleset. | 

### Return type

[**RepositoryRuleset**](RepositoryRuleset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_org_rulesets**
> List[RepositoryRuleset] repos_get_org_rulesets(org, per_page=per_page, page=page, targets=targets)

Get all organization repository rulesets

Get all the repository rulesets for an organization.

### Example


```python
import github_openapi
from github_openapi.models.repository_ruleset import RepositoryRuleset
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    targets = 'branch,tag,push' # str | A comma-separated list of rule targets to filter by. If provided, only rulesets that apply to the specified targets will be returned. For example, `branch,tag,push`.  (optional)

    try:
        # Get all organization repository rulesets
        api_response = api_instance.repos_get_org_rulesets(org, per_page=per_page, page=page, targets=targets)
        print("The response of ReposApi->repos_get_org_rulesets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_org_rulesets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **targets** | **str**| A comma-separated list of rule targets to filter by. If provided, only rulesets that apply to the specified targets will be returned. For example, &#x60;branch,tag,push&#x60;.  | [optional] 

### Return type

[**List[RepositoryRuleset]**](RepositoryRuleset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_pages**
> Page repos_get_pages(owner, repo)

Get a GitHub Pages site

Gets information about a GitHub Pages site.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.page import Page
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get a GitHub Pages site
        api_response = api_instance.repos_get_pages(owner, repo)
        print("The response of ReposApi->repos_get_pages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_pages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_pages_build**
> PageBuild repos_get_pages_build(owner, repo, build_id)

Get GitHub Pages build

Gets information about a GitHub Pages build.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.page_build import PageBuild
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    build_id = 56 # int | 

    try:
        # Get GitHub Pages build
        api_response = api_instance.repos_get_pages_build(owner, repo, build_id)
        print("The response of ReposApi->repos_get_pages_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_pages_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **build_id** | **int**|  | 

### Return type

[**PageBuild**](PageBuild.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_pages_deployment**
> PagesDeploymentStatus repos_get_pages_deployment(owner, repo, pages_deployment_id)

Get the status of a GitHub Pages deployment

Gets the current status of a GitHub Pages deployment.  The authenticated user must have read permission for the GitHub Pages site.

### Example


```python
import github_openapi
from github_openapi.models.pages_deployment_status import PagesDeploymentStatus
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    pages_deployment_id = github_openapi.ActionsGetWorkflowWorkflowIdParameter() # ActionsGetWorkflowWorkflowIdParameter | The ID of the Pages deployment. You can also give the commit SHA of the deployment.

    try:
        # Get the status of a GitHub Pages deployment
        api_response = api_instance.repos_get_pages_deployment(owner, repo, pages_deployment_id)
        print("The response of ReposApi->repos_get_pages_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_pages_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **pages_deployment_id** | [**ActionsGetWorkflowWorkflowIdParameter**](.md)| The ID of the Pages deployment. You can also give the commit SHA of the deployment. | 

### Return type

[**PagesDeploymentStatus**](PagesDeploymentStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_pages_health_check**
> PagesHealthCheck repos_get_pages_health_check(owner, repo)

Get a DNS health check for GitHub Pages

Gets a health check of the DNS settings for the `CNAME` record configured for a repository's GitHub Pages.  The first request to this endpoint returns a `202 Accepted` status and starts an asynchronous background task to get the results for the domain. After the background task completes, subsequent requests to this endpoint return a `200 OK` status with the health check results in the response.  The authenticated user must be a repository administrator, maintainer, or have the 'manage GitHub Pages settings' permission to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.pages_health_check import PagesHealthCheck
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get a DNS health check for GitHub Pages
        api_response = api_instance.repos_get_pages_health_check(owner, repo)
        print("The response of ReposApi->repos_get_pages_health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_pages_health_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**PagesHealthCheck**](PagesHealthCheck.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**202** | Empty response |  -  |
**400** | Custom domains are not available for GitHub Pages |  -  |
**422** | There isn&#39;t a CNAME for this page |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_participation_stats**
> ParticipationStats repos_get_participation_stats(owner, repo)

Get the weekly commit count

Returns the total commit counts for the `owner` and total commit counts in `all`. `all` is everyone combined, including the `owner` in the last 52 weeks. If you'd like to get the commit counts for non-owners, you can subtract `owner` from `all`.  The array order is oldest week (index 0) to most recent week.  The most recent week is seven days ago at UTC midnight to today at UTC midnight.

### Example


```python
import github_openapi
from github_openapi.models.participation_stats import ParticipationStats
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get the weekly commit count
        api_response = api_instance.repos_get_participation_stats(owner, repo)
        print("The response of ReposApi->repos_get_participation_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_participation_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**ParticipationStats**](ParticipationStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The array order is oldest week (index 0) to most recent week. |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_pull_request_review_protection**
> ProtectedBranchPullRequestReview repos_get_pull_request_review_protection(owner, repo, branch)

Get pull request review protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example


```python
import github_openapi
from github_openapi.models.protected_branch_pull_request_review import ProtectedBranchPullRequestReview
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Get pull request review protection
        api_response = api_instance.repos_get_pull_request_review_protection(owner, repo, branch)
        print("The response of ReposApi->repos_get_pull_request_review_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_pull_request_review_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

[**ProtectedBranchPullRequestReview**](ProtectedBranchPullRequestReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_punch_card_stats**
> List[List[int]] repos_get_punch_card_stats(owner, repo)

Get the hourly commit count for each day

Each array contains the day number, hour number, and number of commits:  *   `0-6`: Sunday - Saturday *   `0-23`: Hour of day *   Number of commits  For example, `[2, 14, 25]` indicates that there were 25 total commits, during the 2:00pm hour on Tuesdays. All times are based on the time zone of individual commits.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get the hourly commit count for each day
        api_response = api_instance.repos_get_punch_card_stats(owner, repo)
        print("The response of ReposApi->repos_get_punch_card_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_punch_card_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

**List[List[int]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | For example, &#x60;[2, 14, 25]&#x60; indicates that there were 25 total commits, during the 2:00pm hour on Tuesdays. All times are based on the time zone of individual commits. |  -  |
**204** | A header with no content is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_readme**
> ContentFile repos_get_readme(owner, repo, ref=ref)

Get a repository README

Gets the preferred README for a repository.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github.raw+json`**: Returns the raw file contents. This is the default if you do not specify a media type. - **`application/vnd.github.html+json`**: Returns the README in HTML. Markup languages are rendered to HTML using GitHub's open-source [Markup library](https://github.com/github/markup).

### Example


```python
import github_openapi
from github_openapi.models.content_file import ContentFile
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ref = 'ref_example' # str | The name of the commit/branch/tag. Default: the repository’s default branch. (optional)

    try:
        # Get a repository README
        api_response = api_instance.repos_get_readme(owner, repo, ref=ref)
        print("The response of ReposApi->repos_get_readme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_readme: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ref** | **str**| The name of the commit/branch/tag. Default: the repository’s default branch. | [optional] 

### Return type

[**ContentFile**](ContentFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_readme_in_directory**
> ContentFile repos_get_readme_in_directory(owner, repo, dir, ref=ref)

Get a repository README for a directory

Gets the README from a repository directory.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github.raw+json`**: Returns the raw file contents. This is the default if you do not specify a media type. - **`application/vnd.github.html+json`**: Returns the README in HTML. Markup languages are rendered to HTML using GitHub's open-source [Markup library](https://github.com/github/markup).

### Example


```python
import github_openapi
from github_openapi.models.content_file import ContentFile
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    dir = 'dir_example' # str | The alternate path to look for a README file
    ref = 'ref_example' # str | The name of the commit/branch/tag. Default: the repository’s default branch. (optional)

    try:
        # Get a repository README for a directory
        api_response = api_instance.repos_get_readme_in_directory(owner, repo, dir, ref=ref)
        print("The response of ReposApi->repos_get_readme_in_directory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_readme_in_directory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **dir** | **str**| The alternate path to look for a README file | 
 **ref** | **str**| The name of the commit/branch/tag. Default: the repository’s default branch. | [optional] 

### Return type

[**ContentFile**](ContentFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_release**
> Release repos_get_release(owner, repo, release_id)

Get a release

Gets a public release with the specified release ID.  > [!NOTE] > This returns an `upload_url` key corresponding to the endpoint for uploading release assets. This key is a hypermedia resource. For more information, see \"[Getting started with the REST API](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#hypermedia).\"

### Example


```python
import github_openapi
from github_openapi.models.release import Release
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    release_id = 56 # int | The unique identifier of the release.

    try:
        # Get a release
        api_response = api_instance.repos_get_release(owner, repo, release_id)
        print("The response of ReposApi->repos_get_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **release_id** | **int**| The unique identifier of the release. | 

### Return type

[**Release**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | **Note:** This returns an &#x60;upload_url&#x60; key corresponding to the endpoint for uploading release assets. This key is a hypermedia resource. For more information, see \&quot;[Getting started with the REST API](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#hypermedia).\&quot; |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_release_asset**
> ReleaseAsset repos_get_release_asset(owner, repo, asset_id)

Get a release asset

To download the asset's binary content:  - If within a browser, fetch the location specified in the `browser_download_url` key provided in the response. - Alternatively, set the `Accept` header of the request to    [`application/octet-stream`](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).    The API will either redirect the client to the location, or stream it directly if possible.   API clients should handle both a `200` or `302` response.

### Example


```python
import github_openapi
from github_openapi.models.release_asset import ReleaseAsset
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    asset_id = 56 # int | The unique identifier of the asset.

    try:
        # Get a release asset
        api_response = api_instance.repos_get_release_asset(owner, repo, asset_id)
        print("The response of ReposApi->repos_get_release_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_release_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **asset_id** | **int**| The unique identifier of the asset. | 

### Return type

[**ReleaseAsset**](ReleaseAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**302** | Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_release_by_tag**
> Release repos_get_release_by_tag(owner, repo, tag)

Get a release by tag name

Get a published release with the specified tag.

### Example


```python
import github_openapi
from github_openapi.models.release import Release
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    tag = 'tag_example' # str | tag parameter

    try:
        # Get a release by tag name
        api_response = api_instance.repos_get_release_by_tag(owner, repo, tag)
        print("The response of ReposApi->repos_get_release_by_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_release_by_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **tag** | **str**| tag parameter | 

### Return type

[**Release**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_repo_rule_suite**
> RuleSuite repos_get_repo_rule_suite(owner, repo, rule_suite_id)

Get a repository rule suite

Gets information about a suite of rule evaluations from within a repository. For more information, see \"[Managing rulesets for a repository](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/managing-rulesets-for-a-repository#viewing-insights-for-rulesets).\"

### Example


```python
import github_openapi
from github_openapi.models.rule_suite import RuleSuite
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    rule_suite_id = 56 # int | The unique identifier of the rule suite result. To get this ID, you can use [GET /repos/{owner}/{repo}/rulesets/rule-suites](https://docs.github.com/rest/repos/rule-suites#list-repository-rule-suites) for repositories and [GET /orgs/{org}/rulesets/rule-suites](https://docs.github.com/rest/orgs/rule-suites#list-organization-rule-suites) for organizations.

    try:
        # Get a repository rule suite
        api_response = api_instance.repos_get_repo_rule_suite(owner, repo, rule_suite_id)
        print("The response of ReposApi->repos_get_repo_rule_suite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_repo_rule_suite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **rule_suite_id** | **int**| The unique identifier of the rule suite result. To get this ID, you can use [GET /repos/{owner}/{repo}/rulesets/rule-suites](https://docs.github.com/rest/repos/rule-suites#list-repository-rule-suites) for repositories and [GET /orgs/{org}/rulesets/rule-suites](https://docs.github.com/rest/orgs/rule-suites#list-organization-rule-suites) for organizations. | 

### Return type

[**RuleSuite**](RuleSuite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_repo_rule_suites**
> List[RuleSuitesInner] repos_get_repo_rule_suites(owner, repo, ref=ref, time_period=time_period, actor_name=actor_name, rule_suite_result=rule_suite_result, per_page=per_page, page=page)

List repository rule suites

Lists suites of rule evaluations at the repository level. For more information, see \"[Managing rulesets for a repository](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/managing-rulesets-for-a-repository#viewing-insights-for-rulesets).\"

### Example


```python
import github_openapi
from github_openapi.models.rule_suites_inner import RuleSuitesInner
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ref = 'ref_example' # str | The name of the ref. Cannot contain wildcard characters. Optionally prefix with `refs/heads/` to limit to branches or `refs/tags/` to limit to tags. Omit the prefix to search across all refs. When specified, only rule evaluations triggered for this ref will be returned. (optional)
    time_period = day # str | The time period to filter by.  For example, `day` will filter for rule suites that occurred in the past 24 hours, and `week` will filter for insights that occurred in the past 7 days (168 hours). (optional) (default to day)
    actor_name = 'actor_name_example' # str | The handle for the GitHub user account to filter on. When specified, only rule evaluations triggered by this actor will be returned. (optional)
    rule_suite_result = all # str | The rule results to filter on. When specified, only suites with this result will be returned. (optional) (default to all)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository rule suites
        api_response = api_instance.repos_get_repo_rule_suites(owner, repo, ref=ref, time_period=time_period, actor_name=actor_name, rule_suite_result=rule_suite_result, per_page=per_page, page=page)
        print("The response of ReposApi->repos_get_repo_rule_suites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_repo_rule_suites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ref** | **str**| The name of the ref. Cannot contain wildcard characters. Optionally prefix with &#x60;refs/heads/&#x60; to limit to branches or &#x60;refs/tags/&#x60; to limit to tags. Omit the prefix to search across all refs. When specified, only rule evaluations triggered for this ref will be returned. | [optional] 
 **time_period** | **str**| The time period to filter by.  For example, &#x60;day&#x60; will filter for rule suites that occurred in the past 24 hours, and &#x60;week&#x60; will filter for insights that occurred in the past 7 days (168 hours). | [optional] [default to day]
 **actor_name** | **str**| The handle for the GitHub user account to filter on. When specified, only rule evaluations triggered by this actor will be returned. | [optional] 
 **rule_suite_result** | **str**| The rule results to filter on. When specified, only suites with this result will be returned. | [optional] [default to all]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[RuleSuitesInner]**](RuleSuitesInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_repo_ruleset**
> RepositoryRuleset repos_get_repo_ruleset(owner, repo, ruleset_id, includes_parents=includes_parents)

Get a repository ruleset

Get a ruleset for a repository.  **Note:** To prevent leaking sensitive information, the `bypass_actors` property is only returned if the user making the API request has write access to the ruleset.

### Example


```python
import github_openapi
from github_openapi.models.repository_ruleset import RepositoryRuleset
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ruleset_id = 56 # int | The ID of the ruleset.
    includes_parents = True # bool | Include rulesets configured at higher levels that apply to this repository (optional) (default to True)

    try:
        # Get a repository ruleset
        api_response = api_instance.repos_get_repo_ruleset(owner, repo, ruleset_id, includes_parents=includes_parents)
        print("The response of ReposApi->repos_get_repo_ruleset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_repo_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ruleset_id** | **int**| The ID of the ruleset. | 
 **includes_parents** | **bool**| Include rulesets configured at higher levels that apply to this repository | [optional] [default to True]

### Return type

[**RepositoryRuleset**](RepositoryRuleset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_repo_rulesets**
> List[RepositoryRuleset] repos_get_repo_rulesets(owner, repo, per_page=per_page, page=page, includes_parents=includes_parents, targets=targets)

Get all repository rulesets

Get all the rulesets for a repository.

### Example


```python
import github_openapi
from github_openapi.models.repository_ruleset import RepositoryRuleset
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    includes_parents = True # bool | Include rulesets configured at higher levels that apply to this repository (optional) (default to True)
    targets = 'branch,tag,push' # str | A comma-separated list of rule targets to filter by. If provided, only rulesets that apply to the specified targets will be returned. For example, `branch,tag,push`.  (optional)

    try:
        # Get all repository rulesets
        api_response = api_instance.repos_get_repo_rulesets(owner, repo, per_page=per_page, page=page, includes_parents=includes_parents, targets=targets)
        print("The response of ReposApi->repos_get_repo_rulesets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_repo_rulesets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **includes_parents** | **bool**| Include rulesets configured at higher levels that apply to this repository | [optional] [default to True]
 **targets** | **str**| A comma-separated list of rule targets to filter by. If provided, only rulesets that apply to the specified targets will be returned. For example, &#x60;branch,tag,push&#x60;.  | [optional] 

### Return type

[**List[RepositoryRuleset]**](RepositoryRuleset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_status_checks_protection**
> StatusCheckPolicy repos_get_status_checks_protection(owner, repo, branch)

Get status checks protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example


```python
import github_openapi
from github_openapi.models.status_check_policy import StatusCheckPolicy
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Get status checks protection
        api_response = api_instance.repos_get_status_checks_protection(owner, repo, branch)
        print("The response of ReposApi->repos_get_status_checks_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_status_checks_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

[**StatusCheckPolicy**](StatusCheckPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_teams_with_access_to_protected_branch**
> List[Team] repos_get_teams_with_access_to_protected_branch(owner, repo, branch)

Get teams with access to the protected branch

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists the teams who have push access to this branch. The list includes child teams.

### Example


```python
import github_openapi
from github_openapi.models.team import Team
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Get teams with access to the protected branch
        api_response = api_instance.repos_get_teams_with_access_to_protected_branch(owner, repo, branch)
        print("The response of ReposApi->repos_get_teams_with_access_to_protected_branch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_teams_with_access_to_protected_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

[**List[Team]**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_top_paths**
> List[ContentTraffic] repos_get_top_paths(owner, repo)

Get top referral paths

Get the top 10 popular contents over the last 14 days.

### Example


```python
import github_openapi
from github_openapi.models.content_traffic import ContentTraffic
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get top referral paths
        api_response = api_instance.repos_get_top_paths(owner, repo)
        print("The response of ReposApi->repos_get_top_paths:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_top_paths: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**List[ContentTraffic]**](ContentTraffic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_top_referrers**
> List[ReferrerTraffic] repos_get_top_referrers(owner, repo)

Get top referral sources

Get the top 10 referrers over the last 14 days.

### Example


```python
import github_openapi
from github_openapi.models.referrer_traffic import ReferrerTraffic
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get top referral sources
        api_response = api_instance.repos_get_top_referrers(owner, repo)
        print("The response of ReposApi->repos_get_top_referrers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_top_referrers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**List[ReferrerTraffic]**](ReferrerTraffic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_users_with_access_to_protected_branch**
> List[SimpleUser] repos_get_users_with_access_to_protected_branch(owner, repo, branch)

Get users with access to the protected branch

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists the people who have push access to this branch.

### Example


```python
import github_openapi
from github_openapi.models.simple_user import SimpleUser
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Get users with access to the protected branch
        api_response = api_instance.repos_get_users_with_access_to_protected_branch(owner, repo, branch)
        print("The response of ReposApi->repos_get_users_with_access_to_protected_branch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_users_with_access_to_protected_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

[**List[SimpleUser]**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_views**
> ViewTraffic repos_get_views(owner, repo, per=per)

Get page views

Get the total number of views and breakdown per day or week for the last 14 days. Timestamps are aligned to UTC midnight of the beginning of the day or week. Week begins on Monday.

### Example


```python
import github_openapi
from github_openapi.models.view_traffic import ViewTraffic
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per = day # str | The time frame to display results for. (optional) (default to day)

    try:
        # Get page views
        api_response = api_instance.repos_get_views(owner, repo, per=per)
        print("The response of ReposApi->repos_get_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per** | **str**| The time frame to display results for. | [optional] [default to day]

### Return type

[**ViewTraffic**](ViewTraffic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_webhook**
> Hook repos_get_webhook(owner, repo, hook_id)

Get a repository webhook

Returns a webhook configured in a repository. To get only the webhook `config` properties, see \"[Get a webhook configuration for a repository](/rest/webhooks/repo-config#get-a-webhook-configuration-for-a-repository).\"

### Example


```python
import github_openapi
from github_openapi.models.hook import Hook
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.

    try:
        # Get a repository webhook
        api_response = api_instance.repos_get_webhook(owner, repo, hook_id)
        print("The response of ReposApi->repos_get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_webhook_config_for_repo**
> WebhookConfig repos_get_webhook_config_for_repo(owner, repo, hook_id)

Get a webhook configuration for a repository

Returns the webhook configuration for a repository. To get more information about the webhook, including the `active` state and `events`, use \"[Get a repository webhook](/rest/webhooks/repos#get-a-repository-webhook).\"  OAuth app tokens and personal access tokens (classic) need the `read:repo_hook` or `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.webhook_config import WebhookConfig
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.

    try:
        # Get a webhook configuration for a repository
        api_response = api_instance.repos_get_webhook_config_for_repo(owner, repo, hook_id)
        print("The response of ReposApi->repos_get_webhook_config_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_webhook_config_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 

### Return type

[**WebhookConfig**](WebhookConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_get_webhook_delivery**
> HookDelivery repos_get_webhook_delivery(owner, repo, hook_id, delivery_id)

Get a delivery for a repository webhook

Returns a delivery for a webhook configured in a repository.

### Example


```python
import github_openapi
from github_openapi.models.hook_delivery import HookDelivery
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.
    delivery_id = 56 # int | 

    try:
        # Get a delivery for a repository webhook
        api_response = api_instance.repos_get_webhook_delivery(owner, repo, hook_id, delivery_id)
        print("The response of ReposApi->repos_get_webhook_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_get_webhook_delivery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 
 **delivery_id** | **int**|  | 

### Return type

[**HookDelivery**](HookDelivery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_activities**
> List[Activity] repos_list_activities(owner, repo, direction=direction, per_page=per_page, before=before, after=after, ref=ref, actor=actor, time_period=time_period, activity_type=activity_type)

List repository activities

Lists a detailed history of changes to a repository, such as pushes, merges, force pushes, and branch changes, and associates these changes with commits and users.  For more information about viewing repository activity, see \"[Viewing activity and data for your repository](https://docs.github.com/repositories/viewing-activity-and-data-for-your-repository).\"

### Example


```python
import github_openapi
from github_openapi.models.activity import Activity
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    ref = 'ref_example' # str | The Git reference for the activities you want to list.  The `ref` for a branch can be formatted either as `refs/heads/BRANCH_NAME` or `BRANCH_NAME`, where `BRANCH_NAME` is the name of your branch. (optional)
    actor = 'actor_example' # str | The GitHub username to use to filter by the actor who performed the activity. (optional)
    time_period = 'time_period_example' # str | The time period to filter by.  For example, `day` will filter for activity that occurred in the past 24 hours, and `week` will filter for activity that occurred in the past 7 days (168 hours). (optional)
    activity_type = 'activity_type_example' # str | The activity type to filter by.  For example, you can choose to filter by \"force_push\", to see all force pushes to the repository. (optional)

    try:
        # List repository activities
        api_response = api_instance.repos_list_activities(owner, repo, direction=direction, per_page=per_page, before=before, after=after, ref=ref, actor=actor, time_period=time_period, activity_type=activity_type)
        print("The response of ReposApi->repos_list_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **ref** | **str**| The Git reference for the activities you want to list.  The &#x60;ref&#x60; for a branch can be formatted either as &#x60;refs/heads/BRANCH_NAME&#x60; or &#x60;BRANCH_NAME&#x60;, where &#x60;BRANCH_NAME&#x60; is the name of your branch. | [optional] 
 **actor** | **str**| The GitHub username to use to filter by the actor who performed the activity. | [optional] 
 **time_period** | **str**| The time period to filter by.  For example, &#x60;day&#x60; will filter for activity that occurred in the past 24 hours, and &#x60;week&#x60; will filter for activity that occurred in the past 7 days (168 hours). | [optional] 
 **activity_type** | **str**| The activity type to filter by.  For example, you can choose to filter by \&quot;force_push\&quot;, to see all force pushes to the repository. | [optional] 

### Return type

[**List[Activity]**](Activity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_attestations**
> OrgsListAttestations200Response repos_list_attestations(owner, repo, subject_digest, per_page=per_page, before=before, after=after)

List attestations

List a collection of artifact attestations with a given subject digest that are associated with a repository.  The authenticated user making the request must have read access to the repository. In addition, when using a fine-grained access token the `attestations:read` permission is required.  **Please note:** in order to offer meaningful security benefits, an attestation's signature and timestamps **must** be cryptographically verified, and the identity of the attestation signer **must** be validated. Attestations can be verified using the [GitHub CLI `attestation verify` command](https://cli.github.com/manual/gh_attestation_verify). For more information, see [our guide on how to use artifact attestations to establish a build's provenance](https://docs.github.com/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds).

### Example


```python
import github_openapi
from github_openapi.models.orgs_list_attestations200_response import OrgsListAttestations200Response
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    subject_digest = 'subject_digest_example' # str | The parameter should be set to the attestation's subject's SHA256 digest, in the form `sha256:HEX_DIGEST`.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)

    try:
        # List attestations
        api_response = api_instance.repos_list_attestations(owner, repo, subject_digest, per_page=per_page, before=before, after=after)
        print("The response of ReposApi->repos_list_attestations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_attestations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **subject_digest** | **str**| The parameter should be set to the attestation&#39;s subject&#39;s SHA256 digest, in the form &#x60;sha256:HEX_DIGEST&#x60;. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 

### Return type

[**OrgsListAttestations200Response**](OrgsListAttestations200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_autolinks**
> List[Autolink] repos_list_autolinks(owner, repo)

Get all autolinks of a repository

Gets all autolinks that are configured for a repository.  Information about autolinks are only available to repository administrators.

### Example


```python
import github_openapi
from github_openapi.models.autolink import Autolink
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get all autolinks of a repository
        api_response = api_instance.repos_list_autolinks(owner, repo)
        print("The response of ReposApi->repos_list_autolinks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_autolinks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**List[Autolink]**](Autolink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_branches**
> List[ShortBranch] repos_list_branches(owner, repo, protected=protected, per_page=per_page, page=page)

List branches



### Example


```python
import github_openapi
from github_openapi.models.short_branch import ShortBranch
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    protected = True # bool | Setting to `true` returns only branches protected by branch protections or rulesets. When set to `false`, only unprotected branches are returned. Omitting this parameter returns all branches. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List branches
        api_response = api_instance.repos_list_branches(owner, repo, protected=protected, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_branches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **protected** | **bool**| Setting to &#x60;true&#x60; returns only branches protected by branch protections or rulesets. When set to &#x60;false&#x60;, only unprotected branches are returned. Omitting this parameter returns all branches. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[ShortBranch]**](ShortBranch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_branches_for_head_commit**
> List[BranchShort] repos_list_branches_for_head_commit(owner, repo, commit_sha)

List branches for HEAD commit

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Returns all branches where the given commit SHA is the HEAD, or latest commit for the branch.

### Example


```python
import github_openapi
from github_openapi.models.branch_short import BranchShort
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    commit_sha = 'commit_sha_example' # str | The SHA of the commit.

    try:
        # List branches for HEAD commit
        api_response = api_instance.repos_list_branches_for_head_commit(owner, repo, commit_sha)
        print("The response of ReposApi->repos_list_branches_for_head_commit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_branches_for_head_commit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **commit_sha** | **str**| The SHA of the commit. | 

### Return type

[**List[BranchShort]**](BranchShort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_collaborators**
> List[Collaborator] repos_list_collaborators(owner, repo, affiliation=affiliation, permission=permission, per_page=per_page, page=page)

List repository collaborators

For organization-owned repositories, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners. Organization members with write, maintain, or admin privileges on the organization-owned repository can use this endpoint.  Team members will include the members of child teams.  The authenticated user must have push access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `read:org` and `repo` scopes to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.collaborator import Collaborator
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    affiliation = all # str | Filter collaborators returned by their affiliation. `outside` means all outside collaborators of an organization-owned repository. `direct` means all collaborators with permissions to an organization-owned repository, regardless of organization membership status. `all` means all collaborators the authenticated user can see. (optional) (default to all)
    permission = 'permission_example' # str | Filter collaborators by the permissions they have on the repository. If not specified, all collaborators will be returned. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository collaborators
        api_response = api_instance.repos_list_collaborators(owner, repo, affiliation=affiliation, permission=permission, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_collaborators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_collaborators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **affiliation** | **str**| Filter collaborators returned by their affiliation. &#x60;outside&#x60; means all outside collaborators of an organization-owned repository. &#x60;direct&#x60; means all collaborators with permissions to an organization-owned repository, regardless of organization membership status. &#x60;all&#x60; means all collaborators the authenticated user can see. | [optional] [default to all]
 **permission** | **str**| Filter collaborators by the permissions they have on the repository. If not specified, all collaborators will be returned. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Collaborator]**](Collaborator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_comments_for_commit**
> List[CommitComment] repos_list_comments_for_commit(owner, repo, commit_sha, per_page=per_page, page=page)

List commit comments

Lists the comments for a specified commit.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github-commitcomment.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.

### Example


```python
import github_openapi
from github_openapi.models.commit_comment import CommitComment
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    commit_sha = 'commit_sha_example' # str | The SHA of the commit.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List commit comments
        api_response = api_instance.repos_list_comments_for_commit(owner, repo, commit_sha, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_comments_for_commit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_comments_for_commit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **commit_sha** | **str**| The SHA of the commit. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[CommitComment]**](CommitComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_commit_comments_for_repo**
> List[CommitComment] repos_list_commit_comments_for_repo(owner, repo, per_page=per_page, page=page)

List commit comments for a repository

Lists the commit comments for a specified repository. Comments are ordered by ascending ID.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github-commitcomment.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.

### Example


```python
import github_openapi
from github_openapi.models.commit_comment import CommitComment
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List commit comments for a repository
        api_response = api_instance.repos_list_commit_comments_for_repo(owner, repo, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_commit_comments_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_commit_comments_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[CommitComment]**](CommitComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_commit_statuses_for_ref**
> List[Status] repos_list_commit_statuses_for_ref(owner, repo, ref, per_page=per_page, page=page)

List commit statuses for a reference

Users with pull access in a repository can view commit statuses for a given ref. The ref can be a SHA, a branch name, or a tag name. Statuses are returned in reverse chronological order. The first status in the list will be the latest one.  This resource is also available via a legacy route: `GET /repos/:owner/:repo/statuses/:ref`.

### Example


```python
import github_openapi
from github_openapi.models.status import Status
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ref = 'ref_example' # str | The commit reference. Can be a commit SHA, branch name (`heads/BRANCH_NAME`), or tag name (`tags/TAG_NAME`). For more information, see \"[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)\" in the Git documentation.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List commit statuses for a reference
        api_response = api_instance.repos_list_commit_statuses_for_ref(owner, repo, ref, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_commit_statuses_for_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_commit_statuses_for_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ref** | **str**| The commit reference. Can be a commit SHA, branch name (&#x60;heads/BRANCH_NAME&#x60;), or tag name (&#x60;tags/TAG_NAME&#x60;). For more information, see \&quot;[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)\&quot; in the Git documentation. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Status]**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**301** | Moved permanently |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_commits**
> List[Commit] repos_list_commits(owner, repo, sha=sha, path=path, author=author, committer=committer, since=since, until=until, per_page=per_page, page=page)

List commits

**Signature verification object**  The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:  | Name | Type | Description | | ---- | ---- | ----------- | | `verified` | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified. | | `reason` | `string` | The reason for verified value. Possible values and their meanings are enumerated in table below. | | `signature` | `string` | The signature that was extracted from the commit. | | `payload` | `string` | The value that was signed. | | `verified_at` | `string` | The date the signature was verified by GitHub. |  These are the possible values for `reason` in the `verification` object:  | Value | Description | | ----- | ----------- | | `expired_key` | The key that made the signature is expired. | | `not_signing_key` | The \"signing\" flag is not among the usage flags in the GPG key that made the signature. | | `gpgverify_error` | There was an error communicating with the signature verification service. | | `gpgverify_unavailable` | The signature verification service is currently unavailable. | | `unsigned` | The object does not include a signature. | | `unknown_signature_type` | A non-PGP signature was found in the commit. | | `no_user` | No user was associated with the `committer` email address in the commit. | | `unverified_email` | The `committer` email address in the commit was associated with a user, but the email address is not verified on their account. | | `bad_email` | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. | | `unknown_key` | The key that made the signature has not been registered with any user's account. | | `malformed_signature` | There was an error parsing the signature. | | `invalid` | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | `valid` | None of the above errors applied, so the signature is considered to be verified. |

### Example


```python
import github_openapi
from github_openapi.models.commit import Commit
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    sha = 'sha_example' # str | SHA or branch to start listing commits from. Default: the repository’s default branch (usually `main`). (optional)
    path = 'path_example' # str | Only commits containing this file path will be returned. (optional)
    author = 'author_example' # str | GitHub username or email address to use to filter by commit author. (optional)
    committer = 'committer_example' # str | GitHub username or email address to use to filter by commit committer. (optional)
    since = '2013-10-20T19:20:30+01:00' # datetime | Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. Due to limitations of Git, timestamps must be between 1970-01-01 and 2099-12-31 (inclusive) or unexpected results may be returned. (optional)
    until = '2013-10-20T19:20:30+01:00' # datetime | Only commits before this date will be returned. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. Due to limitations of Git, timestamps must be between 1970-01-01 and 2099-12-31 (inclusive) or unexpected results may be returned. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List commits
        api_response = api_instance.repos_list_commits(owner, repo, sha=sha, path=path, author=author, committer=committer, since=since, until=until, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_commits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_commits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **sha** | **str**| SHA or branch to start listing commits from. Default: the repository’s default branch (usually &#x60;main&#x60;). | [optional] 
 **path** | **str**| Only commits containing this file path will be returned. | [optional] 
 **author** | **str**| GitHub username or email address to use to filter by commit author. | [optional] 
 **committer** | **str**| GitHub username or email address to use to filter by commit committer. | [optional] 
 **since** | **datetime**| Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. Due to limitations of Git, timestamps must be between 1970-01-01 and 2099-12-31 (inclusive) or unexpected results may be returned. | [optional] 
 **until** | **datetime**| Only commits before this date will be returned. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. Due to limitations of Git, timestamps must be between 1970-01-01 and 2099-12-31 (inclusive) or unexpected results may be returned. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Commit]**](Commit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**500** | Internal Error |  -  |
**400** | Bad Request |  -  |
**404** | Resource not found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_contributors**
> List[Contributor] repos_list_contributors(owner, repo, anon=anon, per_page=per_page, page=page)

List repository contributors

Lists contributors to the specified repository and sorts them by the number of commits per contributor in descending order. This endpoint may return information that is a few hours old because the GitHub REST API caches contributor data to improve performance.  GitHub identifies contributors by author email address. This endpoint groups contribution counts by GitHub user, which includes all associated email addresses. To improve performance, only the first 500 author email addresses in the repository link to GitHub users. The rest will appear as anonymous contributors without associated GitHub user information.

### Example


```python
import github_openapi
from github_openapi.models.contributor import Contributor
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    anon = 'anon_example' # str | Set to `1` or `true` to include anonymous contributors in results. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository contributors
        api_response = api_instance.repos_list_contributors(owner, repo, anon=anon, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_contributors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_contributors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **anon** | **str**| Set to &#x60;1&#x60; or &#x60;true&#x60; to include anonymous contributors in results. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Contributor]**](Contributor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If repository contains content |  * Link -  <br>  |
**204** | Response if repository is empty |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_custom_deployment_rule_integrations**
> ReposListCustomDeploymentRuleIntegrations200Response repos_list_custom_deployment_rule_integrations(environment_name, repo, owner, page=page, per_page=per_page)

List custom deployment rule integrations available for an environment

Gets all custom deployment protection rule integrations that are available for an environment.  The authenticated user must have admin or owner permissions to the repository to use this endpoint.  For more information about environments, see \"[Using environments for deployment](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment).\"  For more information about the app that is providing this custom deployment rule, see \"[GET an app](https://docs.github.com/rest/apps/apps#get-an-app)\".  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.repos_list_custom_deployment_rule_integrations200_response import ReposListCustomDeploymentRuleIntegrations200Response
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # List custom deployment rule integrations available for an environment
        api_response = api_instance.repos_list_custom_deployment_rule_integrations(environment_name, repo, owner, page=page, per_page=per_page)
        print("The response of ReposApi->repos_list_custom_deployment_rule_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_custom_deployment_rule_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]

### Return type

[**ReposListCustomDeploymentRuleIntegrations200Response**](ReposListCustomDeploymentRuleIntegrations200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of custom deployment rule integrations available for this environment. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_deploy_keys**
> List[DeployKey] repos_list_deploy_keys(owner, repo, per_page=per_page, page=page)

List deploy keys



### Example


```python
import github_openapi
from github_openapi.models.deploy_key import DeployKey
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List deploy keys
        api_response = api_instance.repos_list_deploy_keys(owner, repo, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_deploy_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_deploy_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[DeployKey]**](DeployKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_deployment_branch_policies**
> ReposListDeploymentBranchPolicies200Response repos_list_deployment_branch_policies(owner, repo, environment_name, per_page=per_page, page=page)

List deployment branch policies

Lists the deployment branch policies for an environment.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.repos_list_deployment_branch_policies200_response import ReposListDeploymentBranchPolicies200Response
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List deployment branch policies
        api_response = api_instance.repos_list_deployment_branch_policies(owner, repo, environment_name, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_deployment_branch_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_deployment_branch_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ReposListDeploymentBranchPolicies200Response**](ReposListDeploymentBranchPolicies200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_deployment_statuses**
> List[DeploymentStatus] repos_list_deployment_statuses(owner, repo, deployment_id, per_page=per_page, page=page)

List deployment statuses

Users with pull access can view deployment statuses for a deployment:

### Example


```python
import github_openapi
from github_openapi.models.deployment_status import DeploymentStatus
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    deployment_id = 56 # int | deployment_id parameter
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List deployment statuses
        api_response = api_instance.repos_list_deployment_statuses(owner, repo, deployment_id, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_deployment_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_deployment_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **deployment_id** | **int**| deployment_id parameter | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[DeploymentStatus]**](DeploymentStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_deployments**
> List[Deployment] repos_list_deployments(owner, repo, sha=sha, ref=ref, task=task, environment=environment, per_page=per_page, page=page)

List deployments

Simple filtering of deployments is available via query parameters:

### Example


```python
import github_openapi
from github_openapi.models.deployment import Deployment
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    sha = 'none' # str | The SHA recorded at creation time. (optional) (default to 'none')
    ref = 'none' # str | The name of the ref. This can be a branch, tag, or SHA. (optional) (default to 'none')
    task = 'none' # str | The name of the task for the deployment (e.g., `deploy` or `deploy:migrations`). (optional) (default to 'none')
    environment = 'none' # str | The name of the environment that was deployed to (e.g., `staging` or `production`). (optional) (default to 'none')
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List deployments
        api_response = api_instance.repos_list_deployments(owner, repo, sha=sha, ref=ref, task=task, environment=environment, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_deployments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_deployments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **sha** | **str**| The SHA recorded at creation time. | [optional] [default to &#39;none&#39;]
 **ref** | **str**| The name of the ref. This can be a branch, tag, or SHA. | [optional] [default to &#39;none&#39;]
 **task** | **str**| The name of the task for the deployment (e.g., &#x60;deploy&#x60; or &#x60;deploy:migrations&#x60;). | [optional] [default to &#39;none&#39;]
 **environment** | **str**| The name of the environment that was deployed to (e.g., &#x60;staging&#x60; or &#x60;production&#x60;). | [optional] [default to &#39;none&#39;]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Deployment]**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_for_authenticated_user**
> List[Repository] repos_list_for_authenticated_user(visibility=visibility, affiliation=affiliation, type=type, sort=sort, direction=direction, per_page=per_page, page=page, since=since, before=before)

List repositories for the authenticated user

Lists repositories that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access.  The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.

### Example


```python
import github_openapi
from github_openapi.models.repository import Repository
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    visibility = all # str | Limit results to repositories with the specified visibility. (optional) (default to all)
    affiliation = 'owner,collaborator,organization_member' # str | Comma-separated list of values. Can include:    * `owner`: Repositories that are owned by the authenticated user.    * `collaborator`: Repositories that the user has been added to as a collaborator.    * `organization_member`: Repositories that the user has access to through being a member of an organization. This includes every repository on every team that the user is on. (optional) (default to 'owner,collaborator,organization_member')
    type = all # str | Limit results to repositories of the specified type. Will cause a `422` error if used in the same request as **visibility** or **affiliation**. (optional) (default to all)
    sort = full_name # str | The property to sort the results by. (optional) (default to full_name)
    direction = 'direction_example' # str | The order to sort by. Default: `asc` when using `full_name`, otherwise `desc`. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    since = '2013-10-20T19:20:30+01:00' # datetime | Only show repositories updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)
    before = '2013-10-20T19:20:30+01:00' # datetime | Only show repositories updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)

    try:
        # List repositories for the authenticated user
        api_response = api_instance.repos_list_for_authenticated_user(visibility=visibility, affiliation=affiliation, type=type, sort=sort, direction=direction, per_page=per_page, page=page, since=since, before=before)
        print("The response of ReposApi->repos_list_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visibility** | **str**| Limit results to repositories with the specified visibility. | [optional] [default to all]
 **affiliation** | **str**| Comma-separated list of values. Can include:    * &#x60;owner&#x60;: Repositories that are owned by the authenticated user.    * &#x60;collaborator&#x60;: Repositories that the user has been added to as a collaborator.    * &#x60;organization_member&#x60;: Repositories that the user has access to through being a member of an organization. This includes every repository on every team that the user is on. | [optional] [default to &#39;owner,collaborator,organization_member&#39;]
 **type** | **str**| Limit results to repositories of the specified type. Will cause a &#x60;422&#x60; error if used in the same request as **visibility** or **affiliation**. | [optional] [default to all]
 **sort** | **str**| The property to sort the results by. | [optional] [default to full_name]
 **direction** | **str**| The order to sort by. Default: &#x60;asc&#x60; when using &#x60;full_name&#x60;, otherwise &#x60;desc&#x60;. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **since** | **datetime**| Only show repositories updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **before** | **datetime**| Only show repositories updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 

### Return type

[**List[Repository]**](Repository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_for_org**
> List[MinimalRepository] repos_list_for_org(org, type=type, sort=sort, direction=direction, per_page=per_page, page=page)

List organization repositories

Lists repositories for the specified organization.  > [!NOTE] > In order to see the `security_and_analysis` block for a repository you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see \"[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).\"

### Example


```python
import github_openapi
from github_openapi.models.minimal_repository import MinimalRepository
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    type = all # str | Specifies the types of repositories you want returned. (optional) (default to all)
    sort = created # str | The property to sort the results by. (optional) (default to created)
    direction = 'direction_example' # str | The order to sort by. Default: `asc` when using `full_name`, otherwise `desc`. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List organization repositories
        api_response = api_instance.repos_list_for_org(org, type=type, sort=sort, direction=direction, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **type** | **str**| Specifies the types of repositories you want returned. | [optional] [default to all]
 **sort** | **str**| The property to sort the results by. | [optional] [default to created]
 **direction** | **str**| The order to sort by. Default: &#x60;asc&#x60; when using &#x60;full_name&#x60;, otherwise &#x60;desc&#x60;. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[MinimalRepository]**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_for_user**
> List[MinimalRepository] repos_list_for_user(username, type=type, sort=sort, direction=direction, per_page=per_page, page=page)

List repositories for a user

Lists public repositories for the specified user.

### Example


```python
import github_openapi
from github_openapi.models.minimal_repository import MinimalRepository
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    type = owner # str | Limit results to repositories of the specified type. (optional) (default to owner)
    sort = full_name # str | The property to sort the results by. (optional) (default to full_name)
    direction = 'direction_example' # str | The order to sort by. Default: `asc` when using `full_name`, otherwise `desc`. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repositories for a user
        api_response = api_instance.repos_list_for_user(username, type=type, sort=sort, direction=direction, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **type** | **str**| Limit results to repositories of the specified type. | [optional] [default to owner]
 **sort** | **str**| The property to sort the results by. | [optional] [default to full_name]
 **direction** | **str**| The order to sort by. Default: &#x60;asc&#x60; when using &#x60;full_name&#x60;, otherwise &#x60;desc&#x60;. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[MinimalRepository]**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_forks**
> List[MinimalRepository] repos_list_forks(owner, repo, sort=sort, per_page=per_page, page=page)

List forks



### Example


```python
import github_openapi
from github_openapi.models.minimal_repository import MinimalRepository
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    sort = newest # str | The sort order. `stargazers` will sort by star count. (optional) (default to newest)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List forks
        api_response = api_instance.repos_list_forks(owner, repo, sort=sort, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_forks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_forks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **sort** | **str**| The sort order. &#x60;stargazers&#x60; will sort by star count. | [optional] [default to newest]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[MinimalRepository]**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_invitations**
> List[RepositoryInvitation] repos_list_invitations(owner, repo, per_page=per_page, page=page)

List repository invitations

When authenticating as a user with admin rights to a repository, this endpoint will list all currently open repository invitations.

### Example


```python
import github_openapi
from github_openapi.models.repository_invitation import RepositoryInvitation
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository invitations
        api_response = api_instance.repos_list_invitations(owner, repo, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[RepositoryInvitation]**](RepositoryInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_invitations_for_authenticated_user**
> List[RepositoryInvitation] repos_list_invitations_for_authenticated_user(per_page=per_page, page=page)

List repository invitations for the authenticated user

When authenticating as a user, this endpoint will list all currently open repository invitations for that user.

### Example


```python
import github_openapi
from github_openapi.models.repository_invitation import RepositoryInvitation
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository invitations for the authenticated user
        api_response = api_instance.repos_list_invitations_for_authenticated_user(per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_invitations_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_invitations_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[RepositoryInvitation]**](RepositoryInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_languages**
> Dict[str, int] repos_list_languages(owner, repo)

List repository languages

Lists languages for the specified repository. The value shown for each language is the number of bytes of code written in that language.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # List repository languages
        api_response = api_instance.repos_list_languages(owner, repo)
        print("The response of ReposApi->repos_list_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_languages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

**Dict[str, int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_pages_builds**
> List[PageBuild] repos_list_pages_builds(owner, repo, per_page=per_page, page=page)

List GitHub Pages builds

Lists builts of a GitHub Pages site.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.page_build import PageBuild
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List GitHub Pages builds
        api_response = api_instance.repos_list_pages_builds(owner, repo, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_pages_builds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_pages_builds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[PageBuild]**](PageBuild.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_public**
> List[MinimalRepository] repos_list_public(since=since)

List public repositories

Lists all public repositories in the order that they were created.  Note: - For GitHub Enterprise Server, this endpoint will only list repositories available to all users on the enterprise. - Pagination is powered exclusively by the `since` parameter. Use the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers) to get the URL for the next page of repositories.

### Example


```python
import github_openapi
from github_openapi.models.minimal_repository import MinimalRepository
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    since = 56 # int | A repository ID. Only return repositories with an ID greater than this ID. (optional)

    try:
        # List public repositories
        api_response = api_instance.repos_list_public(since=since)
        print("The response of ReposApi->repos_list_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **int**| A repository ID. Only return repositories with an ID greater than this ID. | [optional] 

### Return type

[**List[MinimalRepository]**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**304** | Not modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_pull_requests_associated_with_commit**
> List[PullRequestSimple] repos_list_pull_requests_associated_with_commit(owner, repo, commit_sha, per_page=per_page, page=page)

List pull requests associated with a commit

Lists the merged pull request that introduced the commit to the repository. If the commit is not present in the default branch, will only return open pull requests associated with the commit.  To list the open or merged pull requests associated with a branch, you can set the `commit_sha` parameter to the branch name.

### Example


```python
import github_openapi
from github_openapi.models.pull_request_simple import PullRequestSimple
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    commit_sha = 'commit_sha_example' # str | The SHA of the commit.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List pull requests associated with a commit
        api_response = api_instance.repos_list_pull_requests_associated_with_commit(owner, repo, commit_sha, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_pull_requests_associated_with_commit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_pull_requests_associated_with_commit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **commit_sha** | **str**| The SHA of the commit. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[PullRequestSimple]**](PullRequestSimple.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_release_assets**
> List[ReleaseAsset] repos_list_release_assets(owner, repo, release_id, per_page=per_page, page=page)

List release assets



### Example


```python
import github_openapi
from github_openapi.models.release_asset import ReleaseAsset
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    release_id = 56 # int | The unique identifier of the release.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List release assets
        api_response = api_instance.repos_list_release_assets(owner, repo, release_id, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_release_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_release_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **release_id** | **int**| The unique identifier of the release. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[ReleaseAsset]**](ReleaseAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_releases**
> List[Release] repos_list_releases(owner, repo, per_page=per_page, page=page)

List releases

This returns a list of releases, which does not include regular Git tags that have not been associated with a release. To get a list of Git tags, use the [Repository Tags API](https://docs.github.com/rest/repos/repos#list-repository-tags).  Information about published releases are available to everyone. Only users with push access will receive listings for draft releases.

### Example


```python
import github_openapi
from github_openapi.models.release import Release
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List releases
        api_response = api_instance.repos_list_releases(owner, repo, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_releases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_releases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Release]**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_tag_protection**
> List[TagProtection] repos_list_tag_protection(owner, repo)

Closing down - List tag protection states for a repository

> [!WARNING] > **Closing down notice:** This operation is closing down and will be removed after August 30, 2024. Use the \"[Repository Rulesets](https://docs.github.com/rest/repos/rules#get-all-repository-rulesets)\" endpoint instead.  This returns the tag protection states of a repository.  This information is only available to repository administrators.

### Example


```python
import github_openapi
from github_openapi.models.tag_protection import TagProtection
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Closing down - List tag protection states for a repository
        api_response = api_instance.repos_list_tag_protection(owner, repo)
        print("The response of ReposApi->repos_list_tag_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_tag_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**List[TagProtection]**](TagProtection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_tags**
> List[Tag] repos_list_tags(owner, repo, per_page=per_page, page=page)

List repository tags



### Example


```python
import github_openapi
from github_openapi.models.tag import Tag
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository tags
        api_response = api_instance.repos_list_tags(owner, repo, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Tag]**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_teams**
> List[Team] repos_list_teams(owner, repo, per_page=per_page, page=page)

List repository teams

Lists the teams that have access to the specified repository and that are also visible to the authenticated user.  For a public repository, a team is listed only if that team added the public repository explicitly.  OAuth app tokens and personal access tokens (classic) need the `public_repo` or `repo` scope to use this endpoint with a public repository, and `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.team import Team
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository teams
        api_response = api_instance.repos_list_teams(owner, repo, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Team]**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_webhook_deliveries**
> List[HookDeliveryItem] repos_list_webhook_deliveries(owner, repo, hook_id, per_page=per_page, cursor=cursor)

List deliveries for a repository webhook

Returns a list of webhook deliveries for a webhook configured in a repository.

### Example


```python
import github_openapi
from github_openapi.models.hook_delivery_item import HookDeliveryItem
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    cursor = 'cursor_example' # str | Used for pagination: the starting delivery from which the page of deliveries is fetched. Refer to the `link` header for the next and previous page cursors. (optional)

    try:
        # List deliveries for a repository webhook
        api_response = api_instance.repos_list_webhook_deliveries(owner, repo, hook_id, per_page=per_page, cursor=cursor)
        print("The response of ReposApi->repos_list_webhook_deliveries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_webhook_deliveries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **cursor** | **str**| Used for pagination: the starting delivery from which the page of deliveries is fetched. Refer to the &#x60;link&#x60; header for the next and previous page cursors. | [optional] 

### Return type

[**List[HookDeliveryItem]**](HookDeliveryItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_list_webhooks**
> List[Hook] repos_list_webhooks(owner, repo, per_page=per_page, page=page)

List repository webhooks

Lists webhooks for a repository. `last response` may return null if there have not been any deliveries within 30 days.

### Example


```python
import github_openapi
from github_openapi.models.hook import Hook
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository webhooks
        api_response = api_instance.repos_list_webhooks(owner, repo, per_page=per_page, page=page)
        print("The response of ReposApi->repos_list_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_list_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Hook]**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_merge**
> Commit repos_merge(owner, repo, repos_merge_request)

Merge a branch



### Example


```python
import github_openapi
from github_openapi.models.commit import Commit
from github_openapi.models.repos_merge_request import ReposMergeRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_merge_request = {"base":"master","head":"cool_feature","commit_message":"Shipped cool_feature!"} # ReposMergeRequest | 

    try:
        # Merge a branch
        api_response = api_instance.repos_merge(owner, repo, repos_merge_request)
        print("The response of ReposApi->repos_merge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_merge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_merge_request** | [**ReposMergeRequest**](ReposMergeRequest.md)|  | 

### Return type

[**Commit**](Commit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response (The resulting merge commit) |  -  |
**204** | Response when already merged |  -  |
**404** | Not Found when the base or head does not exist |  -  |
**409** | Conflict when there is a merge conflict |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_merge_upstream**
> MergedUpstream repos_merge_upstream(owner, repo, repos_merge_upstream_request)

Sync a fork branch with the upstream repository

Sync a branch of a forked repository to keep it up-to-date with the upstream repository.

### Example


```python
import github_openapi
from github_openapi.models.merged_upstream import MergedUpstream
from github_openapi.models.repos_merge_upstream_request import ReposMergeUpstreamRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_merge_upstream_request = {"branch":"main"} # ReposMergeUpstreamRequest | 

    try:
        # Sync a fork branch with the upstream repository
        api_response = api_instance.repos_merge_upstream(owner, repo, repos_merge_upstream_request)
        print("The response of ReposApi->repos_merge_upstream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_merge_upstream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_merge_upstream_request** | [**ReposMergeUpstreamRequest**](ReposMergeUpstreamRequest.md)|  | 

### Return type

[**MergedUpstream**](MergedUpstream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The branch has been successfully synced with the upstream repository |  -  |
**409** | The branch could not be synced because of a merge conflict |  -  |
**422** | The branch could not be synced for some other reason |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_ping_webhook**
> repos_ping_webhook(owner, repo, hook_id)

Ping a repository webhook

This will trigger a [ping event](https://docs.github.com/webhooks/#ping-event) to be sent to the hook.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.

    try:
        # Ping a repository webhook
        api_instance.repos_ping_webhook(owner, repo, hook_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_ping_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_redeliver_webhook_delivery**
> object repos_redeliver_webhook_delivery(owner, repo, hook_id, delivery_id)

Redeliver a delivery for a repository webhook

Redeliver a webhook delivery for a webhook configured in a repository.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.
    delivery_id = 56 # int | 

    try:
        # Redeliver a delivery for a repository webhook
        api_response = api_instance.repos_redeliver_webhook_delivery(owner, repo, hook_id, delivery_id)
        print("The response of ReposApi->repos_redeliver_webhook_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_redeliver_webhook_delivery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 
 **delivery_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_remove_app_access_restrictions**
> List[Integration] repos_remove_app_access_restrictions(owner, repo, branch, repos_set_app_access_restrictions_request)

Remove app access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Removes the ability of an app to push to this branch. Only GitHub Apps that are installed on the repository and that have been granted write access to the repository contents can be added as authorized actors on a protected branch.

### Example


```python
import github_openapi
from github_openapi.models.integration import Integration
from github_openapi.models.repos_set_app_access_restrictions_request import ReposSetAppAccessRestrictionsRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    repos_set_app_access_restrictions_request = {"apps":["my-app"]} # ReposSetAppAccessRestrictionsRequest | 

    try:
        # Remove app access restrictions
        api_response = api_instance.repos_remove_app_access_restrictions(owner, repo, branch, repos_set_app_access_restrictions_request)
        print("The response of ReposApi->repos_remove_app_access_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_remove_app_access_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **repos_set_app_access_restrictions_request** | [**ReposSetAppAccessRestrictionsRequest**](ReposSetAppAccessRestrictionsRequest.md)|  | 

### Return type

[**List[Integration]**](Integration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_remove_collaborator**
> repos_remove_collaborator(owner, repo, username)

Remove a repository collaborator

Removes a collaborator from a repository.  To use this endpoint, the authenticated user must either be an administrator of the repository or target themselves for removal.  This endpoint also: - Cancels any outstanding invitations - Unasigns the user from any issues - Removes access to organization projects if the user is not an organization member and is not a collaborator on any other organization repositories. - Unstars the repository - Updates access permissions to packages  Removing a user as a collaborator has the following effects on forks:  - If the user had access to a fork through their membership to this repository, the user will also be removed from the fork.  - If the user had their own fork of the repository, the fork will be deleted.  - If the user still has read access to the repository, open pull requests by this user from a fork will be denied.  > [!NOTE] > A user can still have access to the repository through organization permissions like base repository permissions.  Although the API responds immediately, the additional permission updates might take some extra time to complete in the background.  For more information on fork permissions, see \"[About permissions and visibility of forks](https://docs.github.com/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks)\".

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Remove a repository collaborator
        api_instance.repos_remove_collaborator(owner, repo, username)
    except Exception as e:
        print("Exception when calling ReposApi->repos_remove_collaborator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content when collaborator was removed from the repository. |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_remove_status_check_contexts**
> List[str] repos_remove_status_check_contexts(owner, repo, branch, repos_set_status_check_contexts_request=repos_set_status_check_contexts_request)

Remove status check contexts

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example


```python
import github_openapi
from github_openapi.models.repos_set_status_check_contexts_request import ReposSetStatusCheckContextsRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    repos_set_status_check_contexts_request = {"contexts":["continuous-integration/jenkins"]} # ReposSetStatusCheckContextsRequest |  (optional)

    try:
        # Remove status check contexts
        api_response = api_instance.repos_remove_status_check_contexts(owner, repo, branch, repos_set_status_check_contexts_request=repos_set_status_check_contexts_request)
        print("The response of ReposApi->repos_remove_status_check_contexts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_remove_status_check_contexts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **repos_set_status_check_contexts_request** | [**ReposSetStatusCheckContextsRequest**](ReposSetStatusCheckContextsRequest.md)|  | [optional] 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_remove_status_check_protection**
> repos_remove_status_check_protection(owner, repo, branch)

Remove status check protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Remove status check protection
        api_instance.repos_remove_status_check_protection(owner, repo, branch)
    except Exception as e:
        print("Exception when calling ReposApi->repos_remove_status_check_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_remove_team_access_restrictions**
> List[Team] repos_remove_team_access_restrictions(owner, repo, branch, repos_add_team_access_restrictions_request=repos_add_team_access_restrictions_request)

Remove team access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Removes the ability of a team to push to this branch. You can also remove push access for child teams.

### Example


```python
import github_openapi
from github_openapi.models.repos_add_team_access_restrictions_request import ReposAddTeamAccessRestrictionsRequest
from github_openapi.models.team import Team
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    repos_add_team_access_restrictions_request = {"teams":["octocats"]} # ReposAddTeamAccessRestrictionsRequest |  (optional)

    try:
        # Remove team access restrictions
        api_response = api_instance.repos_remove_team_access_restrictions(owner, repo, branch, repos_add_team_access_restrictions_request=repos_add_team_access_restrictions_request)
        print("The response of ReposApi->repos_remove_team_access_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_remove_team_access_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **repos_add_team_access_restrictions_request** | [**ReposAddTeamAccessRestrictionsRequest**](ReposAddTeamAccessRestrictionsRequest.md)|  | [optional] 

### Return type

[**List[Team]**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_remove_user_access_restrictions**
> List[SimpleUser] repos_remove_user_access_restrictions(owner, repo, branch, repos_set_user_access_restrictions_request)

Remove user access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Removes the ability of a user to push to this branch.  | Type    | Description                                                                                                                                   | | ------- | --------------------------------------------------------------------------------------------------------------------------------------------- | | `array` | Usernames of the people who should no longer have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

### Example


```python
import github_openapi
from github_openapi.models.repos_set_user_access_restrictions_request import ReposSetUserAccessRestrictionsRequest
from github_openapi.models.simple_user import SimpleUser
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    repos_set_user_access_restrictions_request = {"users":["octocat"]} # ReposSetUserAccessRestrictionsRequest | 

    try:
        # Remove user access restrictions
        api_response = api_instance.repos_remove_user_access_restrictions(owner, repo, branch, repos_set_user_access_restrictions_request)
        print("The response of ReposApi->repos_remove_user_access_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_remove_user_access_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **repos_set_user_access_restrictions_request** | [**ReposSetUserAccessRestrictionsRequest**](ReposSetUserAccessRestrictionsRequest.md)|  | 

### Return type

[**List[SimpleUser]**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_rename_branch**
> BranchWithProtection repos_rename_branch(owner, repo, branch, repos_rename_branch_request)

Rename a branch

Renames a branch in a repository.  > [!NOTE] > Although the API responds immediately, the branch rename process might take some extra time to complete in the background. You won't be able to push to the old branch name while the rename process is in progress. For more information, see \"[Renaming a branch](https://docs.github.com/github/administering-a-repository/renaming-a-branch)\".  The authenticated user must have push access to the branch. If the branch is the default branch, the authenticated user must also have admin or owner permissions.  In order to rename the default branch, fine-grained access tokens also need the `administration:write` repository permission.

### Example


```python
import github_openapi
from github_openapi.models.branch_with_protection import BranchWithProtection
from github_openapi.models.repos_rename_branch_request import ReposRenameBranchRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    repos_rename_branch_request = {"new_name":"my_renamed_branch"} # ReposRenameBranchRequest | 

    try:
        # Rename a branch
        api_response = api_instance.repos_rename_branch(owner, repo, branch, repos_rename_branch_request)
        print("The response of ReposApi->repos_rename_branch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_rename_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **repos_rename_branch_request** | [**ReposRenameBranchRequest**](ReposRenameBranchRequest.md)|  | 

### Return type

[**BranchWithProtection**](BranchWithProtection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_replace_all_topics**
> Topic repos_replace_all_topics(owner, repo, repos_replace_all_topics_request)

Replace all repository topics



### Example


```python
import github_openapi
from github_openapi.models.repos_replace_all_topics_request import ReposReplaceAllTopicsRequest
from github_openapi.models.topic import Topic
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_replace_all_topics_request = {"names":["octocat","atom","electron","api"]} # ReposReplaceAllTopicsRequest | 

    try:
        # Replace all repository topics
        api_response = api_instance.repos_replace_all_topics(owner, repo, repos_replace_all_topics_request)
        print("The response of ReposApi->repos_replace_all_topics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_replace_all_topics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_replace_all_topics_request** | [**ReposReplaceAllTopicsRequest**](ReposReplaceAllTopicsRequest.md)|  | 

### Return type

[**Topic**](Topic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_request_pages_build**
> PageBuildStatus repos_request_pages_build(owner, repo)

Request a GitHub Pages build

You can request that your site be built from the latest revision on the default branch. This has the same effect as pushing a commit to your default branch, but does not require an additional commit. Manually triggering page builds can be helpful when diagnosing build warnings and failures.  Build requests are limited to one concurrent build per repository and one concurrent build per requester. If you request a build while another is still in progress, the second request will be queued until the first completes.

### Example


```python
import github_openapi
from github_openapi.models.page_build_status import PageBuildStatus
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Request a GitHub Pages build
        api_response = api_instance.repos_request_pages_build(owner, repo)
        print("The response of ReposApi->repos_request_pages_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_request_pages_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**PageBuildStatus**](PageBuildStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_set_admin_branch_protection**
> ProtectedBranchAdminEnforced repos_set_admin_branch_protection(owner, repo, branch)

Set admin branch protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Adding admin enforcement requires admin or owner permissions to the repository and branch protection to be enabled.

### Example


```python
import github_openapi
from github_openapi.models.protected_branch_admin_enforced import ProtectedBranchAdminEnforced
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).

    try:
        # Set admin branch protection
        api_response = api_instance.repos_set_admin_branch_protection(owner, repo, branch)
        print("The response of ReposApi->repos_set_admin_branch_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_set_admin_branch_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 

### Return type

[**ProtectedBranchAdminEnforced**](ProtectedBranchAdminEnforced.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_set_app_access_restrictions**
> List[Integration] repos_set_app_access_restrictions(owner, repo, branch, repos_set_app_access_restrictions_request)

Set app access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Replaces the list of apps that have push access to this branch. This removes all apps that previously had push access and grants push access to the new list of apps. Only GitHub Apps that are installed on the repository and that have been granted write access to the repository contents can be added as authorized actors on a protected branch.

### Example


```python
import github_openapi
from github_openapi.models.integration import Integration
from github_openapi.models.repos_set_app_access_restrictions_request import ReposSetAppAccessRestrictionsRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    repos_set_app_access_restrictions_request = {"apps":["octoapp"]} # ReposSetAppAccessRestrictionsRequest | 

    try:
        # Set app access restrictions
        api_response = api_instance.repos_set_app_access_restrictions(owner, repo, branch, repos_set_app_access_restrictions_request)
        print("The response of ReposApi->repos_set_app_access_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_set_app_access_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **repos_set_app_access_restrictions_request** | [**ReposSetAppAccessRestrictionsRequest**](ReposSetAppAccessRestrictionsRequest.md)|  | 

### Return type

[**List[Integration]**](Integration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_set_status_check_contexts**
> List[str] repos_set_status_check_contexts(owner, repo, branch, repos_set_status_check_contexts_request=repos_set_status_check_contexts_request)

Set status check contexts

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example


```python
import github_openapi
from github_openapi.models.repos_set_status_check_contexts_request import ReposSetStatusCheckContextsRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    repos_set_status_check_contexts_request = {"contexts":["continuous-integration/travis-ci"]} # ReposSetStatusCheckContextsRequest |  (optional)

    try:
        # Set status check contexts
        api_response = api_instance.repos_set_status_check_contexts(owner, repo, branch, repos_set_status_check_contexts_request=repos_set_status_check_contexts_request)
        print("The response of ReposApi->repos_set_status_check_contexts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_set_status_check_contexts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **repos_set_status_check_contexts_request** | [**ReposSetStatusCheckContextsRequest**](ReposSetStatusCheckContextsRequest.md)|  | [optional] 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_set_team_access_restrictions**
> List[Team] repos_set_team_access_restrictions(owner, repo, branch, repos_set_team_access_restrictions_request=repos_set_team_access_restrictions_request)

Set team access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Replaces the list of teams that have push access to this branch. This removes all teams that previously had push access and grants push access to the new list of teams. Team restrictions include child teams.

### Example


```python
import github_openapi
from github_openapi.models.repos_set_team_access_restrictions_request import ReposSetTeamAccessRestrictionsRequest
from github_openapi.models.team import Team
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    repos_set_team_access_restrictions_request = {"teams":["justice-league"]} # ReposSetTeamAccessRestrictionsRequest |  (optional)

    try:
        # Set team access restrictions
        api_response = api_instance.repos_set_team_access_restrictions(owner, repo, branch, repos_set_team_access_restrictions_request=repos_set_team_access_restrictions_request)
        print("The response of ReposApi->repos_set_team_access_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_set_team_access_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **repos_set_team_access_restrictions_request** | [**ReposSetTeamAccessRestrictionsRequest**](ReposSetTeamAccessRestrictionsRequest.md)|  | [optional] 

### Return type

[**List[Team]**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_set_user_access_restrictions**
> List[SimpleUser] repos_set_user_access_restrictions(owner, repo, branch, repos_set_user_access_restrictions_request)

Set user access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Replaces the list of people that have push access to this branch. This removes all people that previously had push access and grants push access to the new list of people.  | Type    | Description                                                                                                                   | | ------- | ----------------------------------------------------------------------------------------------------------------------------- | | `array` | Usernames for people who can have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

### Example


```python
import github_openapi
from github_openapi.models.repos_set_user_access_restrictions_request import ReposSetUserAccessRestrictionsRequest
from github_openapi.models.simple_user import SimpleUser
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    repos_set_user_access_restrictions_request = {"users":["octocat"]} # ReposSetUserAccessRestrictionsRequest | 

    try:
        # Set user access restrictions
        api_response = api_instance.repos_set_user_access_restrictions(owner, repo, branch, repos_set_user_access_restrictions_request)
        print("The response of ReposApi->repos_set_user_access_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_set_user_access_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **repos_set_user_access_restrictions_request** | [**ReposSetUserAccessRestrictionsRequest**](ReposSetUserAccessRestrictionsRequest.md)|  | 

### Return type

[**List[SimpleUser]**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_test_push_webhook**
> repos_test_push_webhook(owner, repo, hook_id)

Test the push repository webhook

This will trigger the hook with the latest push to the current repository if the hook is subscribed to `push` events. If the hook is not subscribed to `push` events, the server will respond with 204 but no test POST will be generated.  > [!NOTE] > Previously `/repos/:owner/:repo/hooks/:hook_id/test`

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.

    try:
        # Test the push repository webhook
        api_instance.repos_test_push_webhook(owner, repo, hook_id)
    except Exception as e:
        print("Exception when calling ReposApi->repos_test_push_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_transfer**
> MinimalRepository repos_transfer(owner, repo, repos_transfer_request)

Transfer a repository

A transfer request will need to be accepted by the new owner when transferring a personal repository to another user. The response will contain the original `owner`, and the transfer will continue asynchronously. For more details on the requirements to transfer personal and organization-owned repositories, see [about repository transfers](https://docs.github.com/articles/about-repository-transfers/).

### Example


```python
import github_openapi
from github_openapi.models.minimal_repository import MinimalRepository
from github_openapi.models.repos_transfer_request import ReposTransferRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_transfer_request = {"new_owner":"github","team_ids":[12,345],"new_name":"octorepo"} # ReposTransferRequest | 

    try:
        # Transfer a repository
        api_response = api_instance.repos_transfer(owner, repo, repos_transfer_request)
        print("The response of ReposApi->repos_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_transfer_request** | [**ReposTransferRequest**](ReposTransferRequest.md)|  | 

### Return type

[**MinimalRepository**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_update**
> FullRepository repos_update(owner, repo, repos_update_request=repos_update_request)

Update a repository

**Note**: To edit a repository's topics, use the [Replace all repository topics](https://docs.github.com/rest/repos/repos#replace-all-repository-topics) endpoint.

### Example


```python
import github_openapi
from github_openapi.models.full_repository import FullRepository
from github_openapi.models.repos_update_request import ReposUpdateRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_update_request = {"name":"Hello-World","description":"This is your first repository","homepage":"https://github.com","private":true,"has_issues":true,"has_projects":true,"has_wiki":true} # ReposUpdateRequest |  (optional)

    try:
        # Update a repository
        api_response = api_instance.repos_update(owner, repo, repos_update_request=repos_update_request)
        print("The response of ReposApi->repos_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_update_request** | [**ReposUpdateRequest**](ReposUpdateRequest.md)|  | [optional] 

### Return type

[**FullRepository**](FullRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**307** | Temporary Redirect |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_update_branch_protection**
> ProtectedBranch repos_update_branch_protection(owner, repo, branch, repos_update_branch_protection_request)

Update branch protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Protecting a branch requires admin or owner permissions to the repository.  > [!NOTE] > Passing new arrays of `users` and `teams` replaces their previous values.  > [!NOTE] > The list of users, apps, and teams in total is limited to 100 items.

### Example


```python
import github_openapi
from github_openapi.models.protected_branch import ProtectedBranch
from github_openapi.models.repos_update_branch_protection_request import ReposUpdateBranchProtectionRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    repos_update_branch_protection_request = {"required_status_checks":{"strict":true,"contexts":["continuous-integration/travis-ci"]},"enforce_admins":true,"required_pull_request_reviews":{"dismissal_restrictions":{"users":["octocat"],"teams":["justice-league"]},"dismiss_stale_reviews":true,"require_code_owner_reviews":true,"required_approving_review_count":2,"require_last_push_approval":true,"bypass_pull_request_allowances":{"users":["octocat"],"teams":["justice-league"]}},"restrictions":{"users":["octocat"],"teams":["justice-league"],"apps":["super-ci"]},"required_linear_history":true,"allow_force_pushes":true,"allow_deletions":true,"block_creations":true,"required_conversation_resolution":true,"lock_branch":true,"allow_fork_syncing":true} # ReposUpdateBranchProtectionRequest | 

    try:
        # Update branch protection
        api_response = api_instance.repos_update_branch_protection(owner, repo, branch, repos_update_branch_protection_request)
        print("The response of ReposApi->repos_update_branch_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_update_branch_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **repos_update_branch_protection_request** | [**ReposUpdateBranchProtectionRequest**](ReposUpdateBranchProtectionRequest.md)|  | 

### Return type

[**ProtectedBranch**](ProtectedBranch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_update_commit_comment**
> CommitComment repos_update_commit_comment(owner, repo, comment_id, repos_update_commit_comment_request)

Update a commit comment

Updates the contents of a specified commit comment.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github-commitcomment.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.

### Example


```python
import github_openapi
from github_openapi.models.commit_comment import CommitComment
from github_openapi.models.repos_update_commit_comment_request import ReposUpdateCommitCommentRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    comment_id = 56 # int | The unique identifier of the comment.
    repos_update_commit_comment_request = {"body":"Nice change"} # ReposUpdateCommitCommentRequest | 

    try:
        # Update a commit comment
        api_response = api_instance.repos_update_commit_comment(owner, repo, comment_id, repos_update_commit_comment_request)
        print("The response of ReposApi->repos_update_commit_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_update_commit_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **comment_id** | **int**| The unique identifier of the comment. | 
 **repos_update_commit_comment_request** | [**ReposUpdateCommitCommentRequest**](ReposUpdateCommitCommentRequest.md)|  | 

### Return type

[**CommitComment**](CommitComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_update_deployment_branch_policy**
> DeploymentBranchPolicy repos_update_deployment_branch_policy(owner, repo, environment_name, branch_policy_id, deployment_branch_policy_name_pattern)

Update a deployment branch policy

Updates a deployment branch or tag policy for an environment.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.deployment_branch_policy import DeploymentBranchPolicy
from github_openapi.models.deployment_branch_policy_name_pattern import DeploymentBranchPolicyNamePattern
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    branch_policy_id = 56 # int | The unique identifier of the branch policy.
    deployment_branch_policy_name_pattern = {"name":"release/*"} # DeploymentBranchPolicyNamePattern | 

    try:
        # Update a deployment branch policy
        api_response = api_instance.repos_update_deployment_branch_policy(owner, repo, environment_name, branch_policy_id, deployment_branch_policy_name_pattern)
        print("The response of ReposApi->repos_update_deployment_branch_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_update_deployment_branch_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **branch_policy_id** | **int**| The unique identifier of the branch policy. | 
 **deployment_branch_policy_name_pattern** | [**DeploymentBranchPolicyNamePattern**](DeploymentBranchPolicyNamePattern.md)|  | 

### Return type

[**DeploymentBranchPolicy**](DeploymentBranchPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_update_information_about_pages_site**
> repos_update_information_about_pages_site(owner, repo, repos_update_information_about_pages_site_request)

Update information about a GitHub Pages site

Updates information for a GitHub Pages site. For more information, see \"[About GitHub Pages](/github/working-with-github-pages/about-github-pages).  The authenticated user must be a repository administrator, maintainer, or have the 'manage GitHub Pages settings' permission.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.repos_update_information_about_pages_site_request import ReposUpdateInformationAboutPagesSiteRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repos_update_information_about_pages_site_request = {"cname":"octocatblog.com","source":{"branch":"main","path":"/"}} # ReposUpdateInformationAboutPagesSiteRequest | 

    try:
        # Update information about a GitHub Pages site
        api_instance.repos_update_information_about_pages_site(owner, repo, repos_update_information_about_pages_site_request)
    except Exception as e:
        print("Exception when calling ReposApi->repos_update_information_about_pages_site: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repos_update_information_about_pages_site_request** | [**ReposUpdateInformationAboutPagesSiteRequest**](ReposUpdateInformationAboutPagesSiteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_update_invitation**
> RepositoryInvitation repos_update_invitation(owner, repo, invitation_id, repos_update_invitation_request=repos_update_invitation_request)

Update a repository invitation



### Example


```python
import github_openapi
from github_openapi.models.repos_update_invitation_request import ReposUpdateInvitationRequest
from github_openapi.models.repository_invitation import RepositoryInvitation
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    invitation_id = 56 # int | The unique identifier of the invitation.
    repos_update_invitation_request = {"permissions":"write"} # ReposUpdateInvitationRequest |  (optional)

    try:
        # Update a repository invitation
        api_response = api_instance.repos_update_invitation(owner, repo, invitation_id, repos_update_invitation_request=repos_update_invitation_request)
        print("The response of ReposApi->repos_update_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_update_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **invitation_id** | **int**| The unique identifier of the invitation. | 
 **repos_update_invitation_request** | [**ReposUpdateInvitationRequest**](ReposUpdateInvitationRequest.md)|  | [optional] 

### Return type

[**RepositoryInvitation**](RepositoryInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_update_org_ruleset**
> RepositoryRuleset repos_update_org_ruleset(org, ruleset_id, repos_update_org_ruleset_request=repos_update_org_ruleset_request)

Update an organization repository ruleset

Update a ruleset for an organization.

### Example


```python
import github_openapi
from github_openapi.models.repos_update_org_ruleset_request import ReposUpdateOrgRulesetRequest
from github_openapi.models.repository_ruleset import RepositoryRuleset
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    ruleset_id = 56 # int | The ID of the ruleset.
    repos_update_org_ruleset_request = {"name":"super cool ruleset","target":"branch","enforcement":"active","bypass_actors":[{"actor_id":234,"actor_type":"Team","bypass_mode":"always"}],"conditions":{"ref_name":{"include":["refs/heads/main","refs/heads/master"],"exclude":["refs/heads/dev*"]},"repository_name":{"include":["important_repository","another_important_repository"],"exclude":["unimportant_repository"],"protected":true}},"rules":[{"type":"commit_author_email_pattern","parameters":{"operator":"contains","pattern":"github"}}]} # ReposUpdateOrgRulesetRequest | Request body (optional)

    try:
        # Update an organization repository ruleset
        api_response = api_instance.repos_update_org_ruleset(org, ruleset_id, repos_update_org_ruleset_request=repos_update_org_ruleset_request)
        print("The response of ReposApi->repos_update_org_ruleset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_update_org_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **ruleset_id** | **int**| The ID of the ruleset. | 
 **repos_update_org_ruleset_request** | [**ReposUpdateOrgRulesetRequest**](ReposUpdateOrgRulesetRequest.md)| Request body | [optional] 

### Return type

[**RepositoryRuleset**](RepositoryRuleset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_update_pull_request_review_protection**
> ProtectedBranchPullRequestReview repos_update_pull_request_review_protection(owner, repo, branch, repos_update_pull_request_review_protection_request=repos_update_pull_request_review_protection_request)

Update pull request review protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Updating pull request review enforcement requires admin or owner permissions to the repository and branch protection to be enabled.  > [!NOTE] > Passing new arrays of `users` and `teams` replaces their previous values.

### Example


```python
import github_openapi
from github_openapi.models.protected_branch_pull_request_review import ProtectedBranchPullRequestReview
from github_openapi.models.repos_update_pull_request_review_protection_request import ReposUpdatePullRequestReviewProtectionRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    repos_update_pull_request_review_protection_request = {"dismissal_restrictions":{"users":["octocat"],"teams":["justice-league"],"apps":["octoapp"]},"bypass_pull_request_allowances":{"users":["octocat"],"teams":["justice-league"],"apps":["octoapp"]},"dismiss_stale_reviews":true,"require_code_owner_reviews":true,"required_approving_review_count":2,"require_last_push_approval":true} # ReposUpdatePullRequestReviewProtectionRequest |  (optional)

    try:
        # Update pull request review protection
        api_response = api_instance.repos_update_pull_request_review_protection(owner, repo, branch, repos_update_pull_request_review_protection_request=repos_update_pull_request_review_protection_request)
        print("The response of ReposApi->repos_update_pull_request_review_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_update_pull_request_review_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **repos_update_pull_request_review_protection_request** | [**ReposUpdatePullRequestReviewProtectionRequest**](ReposUpdatePullRequestReviewProtectionRequest.md)|  | [optional] 

### Return type

[**ProtectedBranchPullRequestReview**](ProtectedBranchPullRequestReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_update_release**
> Release repos_update_release(owner, repo, release_id, repos_update_release_request=repos_update_release_request)

Update a release

Users with push access to the repository can edit a release.

### Example


```python
import github_openapi
from github_openapi.models.release import Release
from github_openapi.models.repos_update_release_request import ReposUpdateReleaseRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    release_id = 56 # int | The unique identifier of the release.
    repos_update_release_request = {"tag_name":"v1.0.0","target_commitish":"master","name":"v1.0.0","body":"Description of the release","draft":false,"prerelease":false} # ReposUpdateReleaseRequest |  (optional)

    try:
        # Update a release
        api_response = api_instance.repos_update_release(owner, repo, release_id, repos_update_release_request=repos_update_release_request)
        print("The response of ReposApi->repos_update_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_update_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **release_id** | **int**| The unique identifier of the release. | 
 **repos_update_release_request** | [**ReposUpdateReleaseRequest**](ReposUpdateReleaseRequest.md)|  | [optional] 

### Return type

[**Release**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Not Found if the discussion category name is invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_update_release_asset**
> ReleaseAsset repos_update_release_asset(owner, repo, asset_id, repos_update_release_asset_request=repos_update_release_asset_request)

Update a release asset

Users with push access to the repository can edit a release asset.

### Example


```python
import github_openapi
from github_openapi.models.release_asset import ReleaseAsset
from github_openapi.models.repos_update_release_asset_request import ReposUpdateReleaseAssetRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    asset_id = 56 # int | The unique identifier of the asset.
    repos_update_release_asset_request = {"name":"foo-1.0.0-osx.zip","label":"Mac binary"} # ReposUpdateReleaseAssetRequest |  (optional)

    try:
        # Update a release asset
        api_response = api_instance.repos_update_release_asset(owner, repo, asset_id, repos_update_release_asset_request=repos_update_release_asset_request)
        print("The response of ReposApi->repos_update_release_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_update_release_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **asset_id** | **int**| The unique identifier of the asset. | 
 **repos_update_release_asset_request** | [**ReposUpdateReleaseAssetRequest**](ReposUpdateReleaseAssetRequest.md)|  | [optional] 

### Return type

[**ReleaseAsset**](ReleaseAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_update_repo_ruleset**
> RepositoryRuleset repos_update_repo_ruleset(owner, repo, ruleset_id, repos_update_repo_ruleset_request=repos_update_repo_ruleset_request)

Update a repository ruleset

Update a ruleset for a repository.

### Example


```python
import github_openapi
from github_openapi.models.repos_update_repo_ruleset_request import ReposUpdateRepoRulesetRequest
from github_openapi.models.repository_ruleset import RepositoryRuleset
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ruleset_id = 56 # int | The ID of the ruleset.
    repos_update_repo_ruleset_request = {"name":"super cool ruleset","target":"branch","enforcement":"active","bypass_actors":[{"actor_id":234,"actor_type":"Team","bypass_mode":"always"}],"conditions":{"ref_name":{"include":["refs/heads/main","refs/heads/master"],"exclude":["refs/heads/dev*"]}},"rules":[{"type":"commit_author_email_pattern","parameters":{"operator":"contains","pattern":"github"}}]} # ReposUpdateRepoRulesetRequest | Request body (optional)

    try:
        # Update a repository ruleset
        api_response = api_instance.repos_update_repo_ruleset(owner, repo, ruleset_id, repos_update_repo_ruleset_request=repos_update_repo_ruleset_request)
        print("The response of ReposApi->repos_update_repo_ruleset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_update_repo_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ruleset_id** | **int**| The ID of the ruleset. | 
 **repos_update_repo_ruleset_request** | [**ReposUpdateRepoRulesetRequest**](ReposUpdateRepoRulesetRequest.md)| Request body | [optional] 

### Return type

[**RepositoryRuleset**](RepositoryRuleset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_update_status_check_protection**
> StatusCheckPolicy repos_update_status_check_protection(owner, repo, branch, repos_update_status_check_protection_request=repos_update_status_check_protection_request)

Update status check protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Updating required status checks requires admin or owner permissions to the repository and branch protection to be enabled.

### Example


```python
import github_openapi
from github_openapi.models.repos_update_status_check_protection_request import ReposUpdateStatusCheckProtectionRequest
from github_openapi.models.status_check_policy import StatusCheckPolicy
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    branch = 'branch_example' # str | The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql).
    repos_update_status_check_protection_request = {"strict":true,"contexts":["continuous-integration/travis-ci"]} # ReposUpdateStatusCheckProtectionRequest |  (optional)

    try:
        # Update status check protection
        api_response = api_instance.repos_update_status_check_protection(owner, repo, branch, repos_update_status_check_protection_request=repos_update_status_check_protection_request)
        print("The response of ReposApi->repos_update_status_check_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_update_status_check_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **branch** | **str**| The name of the branch. Cannot contain wildcard characters. To use wildcard characters in branch names, use [the GraphQL API](https://docs.github.com/graphql). | 
 **repos_update_status_check_protection_request** | [**ReposUpdateStatusCheckProtectionRequest**](ReposUpdateStatusCheckProtectionRequest.md)|  | [optional] 

### Return type

[**StatusCheckPolicy**](StatusCheckPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_update_webhook**
> Hook repos_update_webhook(owner, repo, hook_id, repos_update_webhook_request)

Update a repository webhook

Updates a webhook configured in a repository. If you previously had a `secret` set, you must provide the same `secret` or set a new `secret` or the secret will be removed. If you are only updating individual webhook `config` properties, use \"[Update a webhook configuration for a repository](/rest/webhooks/repo-config#update-a-webhook-configuration-for-a-repository).\"

### Example


```python
import github_openapi
from github_openapi.models.hook import Hook
from github_openapi.models.repos_update_webhook_request import ReposUpdateWebhookRequest
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.
    repos_update_webhook_request = {"active":true,"add_events":["pull_request"]} # ReposUpdateWebhookRequest | 

    try:
        # Update a repository webhook
        api_response = api_instance.repos_update_webhook(owner, repo, hook_id, repos_update_webhook_request)
        print("The response of ReposApi->repos_update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 
 **repos_update_webhook_request** | [**ReposUpdateWebhookRequest**](ReposUpdateWebhookRequest.md)|  | 

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_update_webhook_config_for_repo**
> WebhookConfig repos_update_webhook_config_for_repo(owner, repo, hook_id, repos_update_webhook_config_for_repo_request=repos_update_webhook_config_for_repo_request)

Update a webhook configuration for a repository

Updates the webhook configuration for a repository. To update more information about the webhook, including the `active` state and `events`, use \"[Update a repository webhook](/rest/webhooks/repos#update-a-repository-webhook).\"  OAuth app tokens and personal access tokens (classic) need the `write:repo_hook` or `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.repos_update_webhook_config_for_repo_request import ReposUpdateWebhookConfigForRepoRequest
from github_openapi.models.webhook_config import WebhookConfig
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.
    repos_update_webhook_config_for_repo_request = {"content_type":"json","url":"https://example.com/webhook"} # ReposUpdateWebhookConfigForRepoRequest |  (optional)

    try:
        # Update a webhook configuration for a repository
        api_response = api_instance.repos_update_webhook_config_for_repo(owner, repo, hook_id, repos_update_webhook_config_for_repo_request=repos_update_webhook_config_for_repo_request)
        print("The response of ReposApi->repos_update_webhook_config_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_update_webhook_config_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 
 **repos_update_webhook_config_for_repo_request** | [**ReposUpdateWebhookConfigForRepoRequest**](ReposUpdateWebhookConfigForRepoRequest.md)|  | [optional] 

### Return type

[**WebhookConfig**](WebhookConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repos_upload_release_asset**
> ReleaseAsset repos_upload_release_asset(owner, repo, release_id, name, label=label, body=body)

Upload a release asset

This endpoint makes use of a [Hypermedia relation](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#hypermedia) to determine which URL to access. The endpoint you call to upload release assets is specific to your release. Use the `upload_url` returned in the response of the [Create a release endpoint](https://docs.github.com/rest/releases/releases#create-a-release) to upload a release asset.  You need to use an HTTP client which supports [SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) to make calls to this endpoint.  Most libraries will set the required `Content-Length` header automatically. Use the required `Content-Type` header to provide the media type of the asset. For a list of media types, see [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml). For example:   `application/zip`  GitHub expects the asset data in its raw binary form, rather than JSON. You will send the raw binary content of the asset as the request body. Everything else about the endpoint is the same as the rest of the API. For example, you'll still need to pass your authentication to be able to upload an asset.  When an upstream failure occurs, you will receive a `502 Bad Gateway` status. This may leave an empty asset with a state of `starter`. It can be safely deleted.  **Notes:** *   GitHub renames asset filenames that have special characters, non-alphanumeric characters, and leading or trailing periods. The \"[List release assets](https://docs.github.com/rest/releases/assets#list-release-assets)\" endpoint lists the renamed filenames. For more information and help, contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api). *   To find the `release_id` query the [`GET /repos/{owner}/{repo}/releases/latest` endpoint](https://docs.github.com/rest/releases/releases#get-the-latest-release).  *   If you upload an asset with the same filename as another uploaded asset, you'll receive an error and must delete the old file before you can re-upload the new asset.

### Example


```python
import github_openapi
from github_openapi.models.release_asset import ReleaseAsset
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.ReposApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    release_id = 56 # int | The unique identifier of the release.
    name = 'name_example' # str | 
    label = 'label_example' # str |  (optional)
    body = @example.zip # bytearray |  (optional)

    try:
        # Upload a release asset
        api_response = api_instance.repos_upload_release_asset(owner, repo, release_id, name, label=label, body=body)
        print("The response of ReposApi->repos_upload_release_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReposApi->repos_upload_release_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **release_id** | **int**| The unique identifier of the release. | 
 **name** | **str**|  | 
 **label** | **str**|  | [optional] 
 **body** | **bytearray**|  | [optional] 

### Return type

[**ReleaseAsset**](ReleaseAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response for successful upload |  -  |
**422** | Response if you upload an asset with the same filename as another uploaded asset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

