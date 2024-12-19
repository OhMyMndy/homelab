# github_openapi.ActionsApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actions_add_custom_labels_to_self_hosted_runner_for_org**](ActionsApi.md#actions_add_custom_labels_to_self_hosted_runner_for_org) | **POST** /orgs/{org}/actions/runners/{runner_id}/labels | Add custom labels to a self-hosted runner for an organization
[**actions_add_custom_labels_to_self_hosted_runner_for_repo**](ActionsApi.md#actions_add_custom_labels_to_self_hosted_runner_for_repo) | **POST** /repos/{owner}/{repo}/actions/runners/{runner_id}/labels | Add custom labels to a self-hosted runner for a repository
[**actions_add_repo_access_to_self_hosted_runner_group_in_org**](ActionsApi.md#actions_add_repo_access_to_self_hosted_runner_group_in_org) | **PUT** /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id} | Add repository access to a self-hosted runner group in an organization
[**actions_add_selected_repo_to_org_secret**](ActionsApi.md#actions_add_selected_repo_to_org_secret) | **PUT** /orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id} | Add selected repository to an organization secret
[**actions_add_selected_repo_to_org_variable**](ActionsApi.md#actions_add_selected_repo_to_org_variable) | **PUT** /orgs/{org}/actions/variables/{name}/repositories/{repository_id} | Add selected repository to an organization variable
[**actions_add_self_hosted_runner_to_group_for_org**](ActionsApi.md#actions_add_self_hosted_runner_to_group_for_org) | **PUT** /orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id} | Add a self-hosted runner to a group for an organization
[**actions_approve_workflow_run**](ActionsApi.md#actions_approve_workflow_run) | **POST** /repos/{owner}/{repo}/actions/runs/{run_id}/approve | Approve a workflow run for a fork pull request
[**actions_cancel_workflow_run**](ActionsApi.md#actions_cancel_workflow_run) | **POST** /repos/{owner}/{repo}/actions/runs/{run_id}/cancel | Cancel a workflow run
[**actions_create_environment_variable**](ActionsApi.md#actions_create_environment_variable) | **POST** /repos/{owner}/{repo}/environments/{environment_name}/variables | Create an environment variable
[**actions_create_or_update_environment_secret**](ActionsApi.md#actions_create_or_update_environment_secret) | **PUT** /repos/{owner}/{repo}/environments/{environment_name}/secrets/{secret_name} | Create or update an environment secret
[**actions_create_or_update_org_secret**](ActionsApi.md#actions_create_or_update_org_secret) | **PUT** /orgs/{org}/actions/secrets/{secret_name} | Create or update an organization secret
[**actions_create_or_update_repo_secret**](ActionsApi.md#actions_create_or_update_repo_secret) | **PUT** /repos/{owner}/{repo}/actions/secrets/{secret_name} | Create or update a repository secret
[**actions_create_org_variable**](ActionsApi.md#actions_create_org_variable) | **POST** /orgs/{org}/actions/variables | Create an organization variable
[**actions_create_registration_token_for_org**](ActionsApi.md#actions_create_registration_token_for_org) | **POST** /orgs/{org}/actions/runners/registration-token | Create a registration token for an organization
[**actions_create_registration_token_for_repo**](ActionsApi.md#actions_create_registration_token_for_repo) | **POST** /repos/{owner}/{repo}/actions/runners/registration-token | Create a registration token for a repository
[**actions_create_remove_token_for_org**](ActionsApi.md#actions_create_remove_token_for_org) | **POST** /orgs/{org}/actions/runners/remove-token | Create a remove token for an organization
[**actions_create_remove_token_for_repo**](ActionsApi.md#actions_create_remove_token_for_repo) | **POST** /repos/{owner}/{repo}/actions/runners/remove-token | Create a remove token for a repository
[**actions_create_repo_variable**](ActionsApi.md#actions_create_repo_variable) | **POST** /repos/{owner}/{repo}/actions/variables | Create a repository variable
[**actions_create_self_hosted_runner_group_for_org**](ActionsApi.md#actions_create_self_hosted_runner_group_for_org) | **POST** /orgs/{org}/actions/runner-groups | Create a self-hosted runner group for an organization
[**actions_create_workflow_dispatch**](ActionsApi.md#actions_create_workflow_dispatch) | **POST** /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches | Create a workflow dispatch event
[**actions_delete_actions_cache_by_id**](ActionsApi.md#actions_delete_actions_cache_by_id) | **DELETE** /repos/{owner}/{repo}/actions/caches/{cache_id} | Delete a GitHub Actions cache for a repository (using a cache ID)
[**actions_delete_actions_cache_by_key**](ActionsApi.md#actions_delete_actions_cache_by_key) | **DELETE** /repos/{owner}/{repo}/actions/caches | Delete GitHub Actions caches for a repository (using a cache key)
[**actions_delete_artifact**](ActionsApi.md#actions_delete_artifact) | **DELETE** /repos/{owner}/{repo}/actions/artifacts/{artifact_id} | Delete an artifact
[**actions_delete_environment_secret**](ActionsApi.md#actions_delete_environment_secret) | **DELETE** /repos/{owner}/{repo}/environments/{environment_name}/secrets/{secret_name} | Delete an environment secret
[**actions_delete_environment_variable**](ActionsApi.md#actions_delete_environment_variable) | **DELETE** /repos/{owner}/{repo}/environments/{environment_name}/variables/{name} | Delete an environment variable
[**actions_delete_org_secret**](ActionsApi.md#actions_delete_org_secret) | **DELETE** /orgs/{org}/actions/secrets/{secret_name} | Delete an organization secret
[**actions_delete_org_variable**](ActionsApi.md#actions_delete_org_variable) | **DELETE** /orgs/{org}/actions/variables/{name} | Delete an organization variable
[**actions_delete_repo_secret**](ActionsApi.md#actions_delete_repo_secret) | **DELETE** /repos/{owner}/{repo}/actions/secrets/{secret_name} | Delete a repository secret
[**actions_delete_repo_variable**](ActionsApi.md#actions_delete_repo_variable) | **DELETE** /repos/{owner}/{repo}/actions/variables/{name} | Delete a repository variable
[**actions_delete_self_hosted_runner_from_org**](ActionsApi.md#actions_delete_self_hosted_runner_from_org) | **DELETE** /orgs/{org}/actions/runners/{runner_id} | Delete a self-hosted runner from an organization
[**actions_delete_self_hosted_runner_from_repo**](ActionsApi.md#actions_delete_self_hosted_runner_from_repo) | **DELETE** /repos/{owner}/{repo}/actions/runners/{runner_id} | Delete a self-hosted runner from a repository
[**actions_delete_self_hosted_runner_group_from_org**](ActionsApi.md#actions_delete_self_hosted_runner_group_from_org) | **DELETE** /orgs/{org}/actions/runner-groups/{runner_group_id} | Delete a self-hosted runner group from an organization
[**actions_delete_workflow_run**](ActionsApi.md#actions_delete_workflow_run) | **DELETE** /repos/{owner}/{repo}/actions/runs/{run_id} | Delete a workflow run
[**actions_delete_workflow_run_logs**](ActionsApi.md#actions_delete_workflow_run_logs) | **DELETE** /repos/{owner}/{repo}/actions/runs/{run_id}/logs | Delete workflow run logs
[**actions_disable_selected_repository_github_actions_organization**](ActionsApi.md#actions_disable_selected_repository_github_actions_organization) | **DELETE** /orgs/{org}/actions/permissions/repositories/{repository_id} | Disable a selected repository for GitHub Actions in an organization
[**actions_disable_workflow**](ActionsApi.md#actions_disable_workflow) | **PUT** /repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable | Disable a workflow
[**actions_download_artifact**](ActionsApi.md#actions_download_artifact) | **GET** /repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format} | Download an artifact
[**actions_download_job_logs_for_workflow_run**](ActionsApi.md#actions_download_job_logs_for_workflow_run) | **GET** /repos/{owner}/{repo}/actions/jobs/{job_id}/logs | Download job logs for a workflow run
[**actions_download_workflow_run_attempt_logs**](ActionsApi.md#actions_download_workflow_run_attempt_logs) | **GET** /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/logs | Download workflow run attempt logs
[**actions_download_workflow_run_logs**](ActionsApi.md#actions_download_workflow_run_logs) | **GET** /repos/{owner}/{repo}/actions/runs/{run_id}/logs | Download workflow run logs
[**actions_enable_selected_repository_github_actions_organization**](ActionsApi.md#actions_enable_selected_repository_github_actions_organization) | **PUT** /orgs/{org}/actions/permissions/repositories/{repository_id} | Enable a selected repository for GitHub Actions in an organization
[**actions_enable_workflow**](ActionsApi.md#actions_enable_workflow) | **PUT** /repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable | Enable a workflow
[**actions_force_cancel_workflow_run**](ActionsApi.md#actions_force_cancel_workflow_run) | **POST** /repos/{owner}/{repo}/actions/runs/{run_id}/force-cancel | Force cancel a workflow run
[**actions_generate_runner_jitconfig_for_org**](ActionsApi.md#actions_generate_runner_jitconfig_for_org) | **POST** /orgs/{org}/actions/runners/generate-jitconfig | Create configuration for a just-in-time runner for an organization
[**actions_generate_runner_jitconfig_for_repo**](ActionsApi.md#actions_generate_runner_jitconfig_for_repo) | **POST** /repos/{owner}/{repo}/actions/runners/generate-jitconfig | Create configuration for a just-in-time runner for a repository
[**actions_get_actions_cache_list**](ActionsApi.md#actions_get_actions_cache_list) | **GET** /repos/{owner}/{repo}/actions/caches | List GitHub Actions caches for a repository
[**actions_get_actions_cache_usage**](ActionsApi.md#actions_get_actions_cache_usage) | **GET** /repos/{owner}/{repo}/actions/cache/usage | Get GitHub Actions cache usage for a repository
[**actions_get_actions_cache_usage_by_repo_for_org**](ActionsApi.md#actions_get_actions_cache_usage_by_repo_for_org) | **GET** /orgs/{org}/actions/cache/usage-by-repository | List repositories with GitHub Actions cache usage for an organization
[**actions_get_actions_cache_usage_for_org**](ActionsApi.md#actions_get_actions_cache_usage_for_org) | **GET** /orgs/{org}/actions/cache/usage | Get GitHub Actions cache usage for an organization
[**actions_get_allowed_actions_organization**](ActionsApi.md#actions_get_allowed_actions_organization) | **GET** /orgs/{org}/actions/permissions/selected-actions | Get allowed actions and reusable workflows for an organization
[**actions_get_allowed_actions_repository**](ActionsApi.md#actions_get_allowed_actions_repository) | **GET** /repos/{owner}/{repo}/actions/permissions/selected-actions | Get allowed actions and reusable workflows for a repository
[**actions_get_artifact**](ActionsApi.md#actions_get_artifact) | **GET** /repos/{owner}/{repo}/actions/artifacts/{artifact_id} | Get an artifact
[**actions_get_custom_oidc_sub_claim_for_repo**](ActionsApi.md#actions_get_custom_oidc_sub_claim_for_repo) | **GET** /repos/{owner}/{repo}/actions/oidc/customization/sub | Get the customization template for an OIDC subject claim for a repository
[**actions_get_environment_public_key**](ActionsApi.md#actions_get_environment_public_key) | **GET** /repos/{owner}/{repo}/environments/{environment_name}/secrets/public-key | Get an environment public key
[**actions_get_environment_secret**](ActionsApi.md#actions_get_environment_secret) | **GET** /repos/{owner}/{repo}/environments/{environment_name}/secrets/{secret_name} | Get an environment secret
[**actions_get_environment_variable**](ActionsApi.md#actions_get_environment_variable) | **GET** /repos/{owner}/{repo}/environments/{environment_name}/variables/{name} | Get an environment variable
[**actions_get_github_actions_default_workflow_permissions_organization**](ActionsApi.md#actions_get_github_actions_default_workflow_permissions_organization) | **GET** /orgs/{org}/actions/permissions/workflow | Get default workflow permissions for an organization
[**actions_get_github_actions_default_workflow_permissions_repository**](ActionsApi.md#actions_get_github_actions_default_workflow_permissions_repository) | **GET** /repos/{owner}/{repo}/actions/permissions/workflow | Get default workflow permissions for a repository
[**actions_get_github_actions_permissions_organization**](ActionsApi.md#actions_get_github_actions_permissions_organization) | **GET** /orgs/{org}/actions/permissions | Get GitHub Actions permissions for an organization
[**actions_get_github_actions_permissions_repository**](ActionsApi.md#actions_get_github_actions_permissions_repository) | **GET** /repos/{owner}/{repo}/actions/permissions | Get GitHub Actions permissions for a repository
[**actions_get_job_for_workflow_run**](ActionsApi.md#actions_get_job_for_workflow_run) | **GET** /repos/{owner}/{repo}/actions/jobs/{job_id} | Get a job for a workflow run
[**actions_get_org_public_key**](ActionsApi.md#actions_get_org_public_key) | **GET** /orgs/{org}/actions/secrets/public-key | Get an organization public key
[**actions_get_org_secret**](ActionsApi.md#actions_get_org_secret) | **GET** /orgs/{org}/actions/secrets/{secret_name} | Get an organization secret
[**actions_get_org_variable**](ActionsApi.md#actions_get_org_variable) | **GET** /orgs/{org}/actions/variables/{name} | Get an organization variable
[**actions_get_pending_deployments_for_run**](ActionsApi.md#actions_get_pending_deployments_for_run) | **GET** /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments | Get pending deployments for a workflow run
[**actions_get_repo_public_key**](ActionsApi.md#actions_get_repo_public_key) | **GET** /repos/{owner}/{repo}/actions/secrets/public-key | Get a repository public key
[**actions_get_repo_secret**](ActionsApi.md#actions_get_repo_secret) | **GET** /repos/{owner}/{repo}/actions/secrets/{secret_name} | Get a repository secret
[**actions_get_repo_variable**](ActionsApi.md#actions_get_repo_variable) | **GET** /repos/{owner}/{repo}/actions/variables/{name} | Get a repository variable
[**actions_get_reviews_for_run**](ActionsApi.md#actions_get_reviews_for_run) | **GET** /repos/{owner}/{repo}/actions/runs/{run_id}/approvals | Get the review history for a workflow run
[**actions_get_self_hosted_runner_for_org**](ActionsApi.md#actions_get_self_hosted_runner_for_org) | **GET** /orgs/{org}/actions/runners/{runner_id} | Get a self-hosted runner for an organization
[**actions_get_self_hosted_runner_for_repo**](ActionsApi.md#actions_get_self_hosted_runner_for_repo) | **GET** /repos/{owner}/{repo}/actions/runners/{runner_id} | Get a self-hosted runner for a repository
[**actions_get_self_hosted_runner_group_for_org**](ActionsApi.md#actions_get_self_hosted_runner_group_for_org) | **GET** /orgs/{org}/actions/runner-groups/{runner_group_id} | Get a self-hosted runner group for an organization
[**actions_get_workflow**](ActionsApi.md#actions_get_workflow) | **GET** /repos/{owner}/{repo}/actions/workflows/{workflow_id} | Get a workflow
[**actions_get_workflow_access_to_repository**](ActionsApi.md#actions_get_workflow_access_to_repository) | **GET** /repos/{owner}/{repo}/actions/permissions/access | Get the level of access for workflows outside of the repository
[**actions_get_workflow_run**](ActionsApi.md#actions_get_workflow_run) | **GET** /repos/{owner}/{repo}/actions/runs/{run_id} | Get a workflow run
[**actions_get_workflow_run_attempt**](ActionsApi.md#actions_get_workflow_run_attempt) | **GET** /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number} | Get a workflow run attempt
[**actions_get_workflow_run_usage**](ActionsApi.md#actions_get_workflow_run_usage) | **GET** /repos/{owner}/{repo}/actions/runs/{run_id}/timing | Get workflow run usage
[**actions_get_workflow_usage**](ActionsApi.md#actions_get_workflow_usage) | **GET** /repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing | Get workflow usage
[**actions_list_artifacts_for_repo**](ActionsApi.md#actions_list_artifacts_for_repo) | **GET** /repos/{owner}/{repo}/actions/artifacts | List artifacts for a repository
[**actions_list_environment_secrets**](ActionsApi.md#actions_list_environment_secrets) | **GET** /repos/{owner}/{repo}/environments/{environment_name}/secrets | List environment secrets
[**actions_list_environment_variables**](ActionsApi.md#actions_list_environment_variables) | **GET** /repos/{owner}/{repo}/environments/{environment_name}/variables | List environment variables
[**actions_list_jobs_for_workflow_run**](ActionsApi.md#actions_list_jobs_for_workflow_run) | **GET** /repos/{owner}/{repo}/actions/runs/{run_id}/jobs | List jobs for a workflow run
[**actions_list_jobs_for_workflow_run_attempt**](ActionsApi.md#actions_list_jobs_for_workflow_run_attempt) | **GET** /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs | List jobs for a workflow run attempt
[**actions_list_labels_for_self_hosted_runner_for_org**](ActionsApi.md#actions_list_labels_for_self_hosted_runner_for_org) | **GET** /orgs/{org}/actions/runners/{runner_id}/labels | List labels for a self-hosted runner for an organization
[**actions_list_labels_for_self_hosted_runner_for_repo**](ActionsApi.md#actions_list_labels_for_self_hosted_runner_for_repo) | **GET** /repos/{owner}/{repo}/actions/runners/{runner_id}/labels | List labels for a self-hosted runner for a repository
[**actions_list_org_secrets**](ActionsApi.md#actions_list_org_secrets) | **GET** /orgs/{org}/actions/secrets | List organization secrets
[**actions_list_org_variables**](ActionsApi.md#actions_list_org_variables) | **GET** /orgs/{org}/actions/variables | List organization variables
[**actions_list_repo_access_to_self_hosted_runner_group_in_org**](ActionsApi.md#actions_list_repo_access_to_self_hosted_runner_group_in_org) | **GET** /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories | List repository access to a self-hosted runner group in an organization
[**actions_list_repo_organization_secrets**](ActionsApi.md#actions_list_repo_organization_secrets) | **GET** /repos/{owner}/{repo}/actions/organization-secrets | List repository organization secrets
[**actions_list_repo_organization_variables**](ActionsApi.md#actions_list_repo_organization_variables) | **GET** /repos/{owner}/{repo}/actions/organization-variables | List repository organization variables
[**actions_list_repo_secrets**](ActionsApi.md#actions_list_repo_secrets) | **GET** /repos/{owner}/{repo}/actions/secrets | List repository secrets
[**actions_list_repo_variables**](ActionsApi.md#actions_list_repo_variables) | **GET** /repos/{owner}/{repo}/actions/variables | List repository variables
[**actions_list_repo_workflows**](ActionsApi.md#actions_list_repo_workflows) | **GET** /repos/{owner}/{repo}/actions/workflows | List repository workflows
[**actions_list_runner_applications_for_org**](ActionsApi.md#actions_list_runner_applications_for_org) | **GET** /orgs/{org}/actions/runners/downloads | List runner applications for an organization
[**actions_list_runner_applications_for_repo**](ActionsApi.md#actions_list_runner_applications_for_repo) | **GET** /repos/{owner}/{repo}/actions/runners/downloads | List runner applications for a repository
[**actions_list_selected_repos_for_org_secret**](ActionsApi.md#actions_list_selected_repos_for_org_secret) | **GET** /orgs/{org}/actions/secrets/{secret_name}/repositories | List selected repositories for an organization secret
[**actions_list_selected_repos_for_org_variable**](ActionsApi.md#actions_list_selected_repos_for_org_variable) | **GET** /orgs/{org}/actions/variables/{name}/repositories | List selected repositories for an organization variable
[**actions_list_selected_repositories_enabled_github_actions_organization**](ActionsApi.md#actions_list_selected_repositories_enabled_github_actions_organization) | **GET** /orgs/{org}/actions/permissions/repositories | List selected repositories enabled for GitHub Actions in an organization
[**actions_list_self_hosted_runner_groups_for_org**](ActionsApi.md#actions_list_self_hosted_runner_groups_for_org) | **GET** /orgs/{org}/actions/runner-groups | List self-hosted runner groups for an organization
[**actions_list_self_hosted_runners_for_org**](ActionsApi.md#actions_list_self_hosted_runners_for_org) | **GET** /orgs/{org}/actions/runners | List self-hosted runners for an organization
[**actions_list_self_hosted_runners_for_repo**](ActionsApi.md#actions_list_self_hosted_runners_for_repo) | **GET** /repos/{owner}/{repo}/actions/runners | List self-hosted runners for a repository
[**actions_list_self_hosted_runners_in_group_for_org**](ActionsApi.md#actions_list_self_hosted_runners_in_group_for_org) | **GET** /orgs/{org}/actions/runner-groups/{runner_group_id}/runners | List self-hosted runners in a group for an organization
[**actions_list_workflow_run_artifacts**](ActionsApi.md#actions_list_workflow_run_artifacts) | **GET** /repos/{owner}/{repo}/actions/runs/{run_id}/artifacts | List workflow run artifacts
[**actions_list_workflow_runs**](ActionsApi.md#actions_list_workflow_runs) | **GET** /repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs | List workflow runs for a workflow
[**actions_list_workflow_runs_for_repo**](ActionsApi.md#actions_list_workflow_runs_for_repo) | **GET** /repos/{owner}/{repo}/actions/runs | List workflow runs for a repository
[**actions_re_run_job_for_workflow_run**](ActionsApi.md#actions_re_run_job_for_workflow_run) | **POST** /repos/{owner}/{repo}/actions/jobs/{job_id}/rerun | Re-run a job from a workflow run
[**actions_re_run_workflow**](ActionsApi.md#actions_re_run_workflow) | **POST** /repos/{owner}/{repo}/actions/runs/{run_id}/rerun | Re-run a workflow
[**actions_re_run_workflow_failed_jobs**](ActionsApi.md#actions_re_run_workflow_failed_jobs) | **POST** /repos/{owner}/{repo}/actions/runs/{run_id}/rerun-failed-jobs | Re-run failed jobs from a workflow run
[**actions_remove_all_custom_labels_from_self_hosted_runner_for_org**](ActionsApi.md#actions_remove_all_custom_labels_from_self_hosted_runner_for_org) | **DELETE** /orgs/{org}/actions/runners/{runner_id}/labels | Remove all custom labels from a self-hosted runner for an organization
[**actions_remove_all_custom_labels_from_self_hosted_runner_for_repo**](ActionsApi.md#actions_remove_all_custom_labels_from_self_hosted_runner_for_repo) | **DELETE** /repos/{owner}/{repo}/actions/runners/{runner_id}/labels | Remove all custom labels from a self-hosted runner for a repository
[**actions_remove_custom_label_from_self_hosted_runner_for_org**](ActionsApi.md#actions_remove_custom_label_from_self_hosted_runner_for_org) | **DELETE** /orgs/{org}/actions/runners/{runner_id}/labels/{name} | Remove a custom label from a self-hosted runner for an organization
[**actions_remove_custom_label_from_self_hosted_runner_for_repo**](ActionsApi.md#actions_remove_custom_label_from_self_hosted_runner_for_repo) | **DELETE** /repos/{owner}/{repo}/actions/runners/{runner_id}/labels/{name} | Remove a custom label from a self-hosted runner for a repository
[**actions_remove_repo_access_to_self_hosted_runner_group_in_org**](ActionsApi.md#actions_remove_repo_access_to_self_hosted_runner_group_in_org) | **DELETE** /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id} | Remove repository access to a self-hosted runner group in an organization
[**actions_remove_selected_repo_from_org_secret**](ActionsApi.md#actions_remove_selected_repo_from_org_secret) | **DELETE** /orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id} | Remove selected repository from an organization secret
[**actions_remove_selected_repo_from_org_variable**](ActionsApi.md#actions_remove_selected_repo_from_org_variable) | **DELETE** /orgs/{org}/actions/variables/{name}/repositories/{repository_id} | Remove selected repository from an organization variable
[**actions_remove_self_hosted_runner_from_group_for_org**](ActionsApi.md#actions_remove_self_hosted_runner_from_group_for_org) | **DELETE** /orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id} | Remove a self-hosted runner from a group for an organization
[**actions_review_custom_gates_for_run**](ActionsApi.md#actions_review_custom_gates_for_run) | **POST** /repos/{owner}/{repo}/actions/runs/{run_id}/deployment_protection_rule | Review custom deployment protection rules for a workflow run
[**actions_review_pending_deployments_for_run**](ActionsApi.md#actions_review_pending_deployments_for_run) | **POST** /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments | Review pending deployments for a workflow run
[**actions_set_allowed_actions_organization**](ActionsApi.md#actions_set_allowed_actions_organization) | **PUT** /orgs/{org}/actions/permissions/selected-actions | Set allowed actions and reusable workflows for an organization
[**actions_set_allowed_actions_repository**](ActionsApi.md#actions_set_allowed_actions_repository) | **PUT** /repos/{owner}/{repo}/actions/permissions/selected-actions | Set allowed actions and reusable workflows for a repository
[**actions_set_custom_labels_for_self_hosted_runner_for_org**](ActionsApi.md#actions_set_custom_labels_for_self_hosted_runner_for_org) | **PUT** /orgs/{org}/actions/runners/{runner_id}/labels | Set custom labels for a self-hosted runner for an organization
[**actions_set_custom_labels_for_self_hosted_runner_for_repo**](ActionsApi.md#actions_set_custom_labels_for_self_hosted_runner_for_repo) | **PUT** /repos/{owner}/{repo}/actions/runners/{runner_id}/labels | Set custom labels for a self-hosted runner for a repository
[**actions_set_custom_oidc_sub_claim_for_repo**](ActionsApi.md#actions_set_custom_oidc_sub_claim_for_repo) | **PUT** /repos/{owner}/{repo}/actions/oidc/customization/sub | Set the customization template for an OIDC subject claim for a repository
[**actions_set_github_actions_default_workflow_permissions_organization**](ActionsApi.md#actions_set_github_actions_default_workflow_permissions_organization) | **PUT** /orgs/{org}/actions/permissions/workflow | Set default workflow permissions for an organization
[**actions_set_github_actions_default_workflow_permissions_repository**](ActionsApi.md#actions_set_github_actions_default_workflow_permissions_repository) | **PUT** /repos/{owner}/{repo}/actions/permissions/workflow | Set default workflow permissions for a repository
[**actions_set_github_actions_permissions_organization**](ActionsApi.md#actions_set_github_actions_permissions_organization) | **PUT** /orgs/{org}/actions/permissions | Set GitHub Actions permissions for an organization
[**actions_set_github_actions_permissions_repository**](ActionsApi.md#actions_set_github_actions_permissions_repository) | **PUT** /repos/{owner}/{repo}/actions/permissions | Set GitHub Actions permissions for a repository
[**actions_set_repo_access_to_self_hosted_runner_group_in_org**](ActionsApi.md#actions_set_repo_access_to_self_hosted_runner_group_in_org) | **PUT** /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories | Set repository access for a self-hosted runner group in an organization
[**actions_set_selected_repos_for_org_secret**](ActionsApi.md#actions_set_selected_repos_for_org_secret) | **PUT** /orgs/{org}/actions/secrets/{secret_name}/repositories | Set selected repositories for an organization secret
[**actions_set_selected_repos_for_org_variable**](ActionsApi.md#actions_set_selected_repos_for_org_variable) | **PUT** /orgs/{org}/actions/variables/{name}/repositories | Set selected repositories for an organization variable
[**actions_set_selected_repositories_enabled_github_actions_organization**](ActionsApi.md#actions_set_selected_repositories_enabled_github_actions_organization) | **PUT** /orgs/{org}/actions/permissions/repositories | Set selected repositories enabled for GitHub Actions in an organization
[**actions_set_self_hosted_runners_in_group_for_org**](ActionsApi.md#actions_set_self_hosted_runners_in_group_for_org) | **PUT** /orgs/{org}/actions/runner-groups/{runner_group_id}/runners | Set self-hosted runners in a group for an organization
[**actions_set_workflow_access_to_repository**](ActionsApi.md#actions_set_workflow_access_to_repository) | **PUT** /repos/{owner}/{repo}/actions/permissions/access | Set the level of access for workflows outside of the repository
[**actions_update_environment_variable**](ActionsApi.md#actions_update_environment_variable) | **PATCH** /repos/{owner}/{repo}/environments/{environment_name}/variables/{name} | Update an environment variable
[**actions_update_org_variable**](ActionsApi.md#actions_update_org_variable) | **PATCH** /orgs/{org}/actions/variables/{name} | Update an organization variable
[**actions_update_repo_variable**](ActionsApi.md#actions_update_repo_variable) | **PATCH** /repos/{owner}/{repo}/actions/variables/{name} | Update a repository variable
[**actions_update_self_hosted_runner_group_for_org**](ActionsApi.md#actions_update_self_hosted_runner_group_for_org) | **PATCH** /orgs/{org}/actions/runner-groups/{runner_group_id} | Update a self-hosted runner group for an organization


# **actions_add_custom_labels_to_self_hosted_runner_for_org**
> ActionsListLabelsForSelfHostedRunnerForOrg200Response actions_add_custom_labels_to_self_hosted_runner_for_org(org, runner_id, actions_add_custom_labels_to_self_hosted_runner_for_org_request)

Add custom labels to a self-hosted runner for an organization

Adds custom labels to a self-hosted runner configured in an organization.  Authenticated users must have admin access to the organization to use this endpoint.  OAuth tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_add_custom_labels_to_self_hosted_runner_for_org_request import ActionsAddCustomLabelsToSelfHostedRunnerForOrgRequest
from github_openapi.models.actions_list_labels_for_self_hosted_runner_for_org200_response import ActionsListLabelsForSelfHostedRunnerForOrg200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_id = 56 # int | Unique identifier of the self-hosted runner.
    actions_add_custom_labels_to_self_hosted_runner_for_org_request = {"labels":["gpu","accelerated"]} # ActionsAddCustomLabelsToSelfHostedRunnerForOrgRequest | 

    try:
        # Add custom labels to a self-hosted runner for an organization
        api_response = api_instance.actions_add_custom_labels_to_self_hosted_runner_for_org(org, runner_id, actions_add_custom_labels_to_self_hosted_runner_for_org_request)
        print("The response of ActionsApi->actions_add_custom_labels_to_self_hosted_runner_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_add_custom_labels_to_self_hosted_runner_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_id** | **int**| Unique identifier of the self-hosted runner. | 
 **actions_add_custom_labels_to_self_hosted_runner_for_org_request** | [**ActionsAddCustomLabelsToSelfHostedRunnerForOrgRequest**](ActionsAddCustomLabelsToSelfHostedRunnerForOrgRequest.md)|  | 

### Return type

[**ActionsListLabelsForSelfHostedRunnerForOrg200Response**](ActionsListLabelsForSelfHostedRunnerForOrg200Response.md)

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

# **actions_add_custom_labels_to_self_hosted_runner_for_repo**
> ActionsListLabelsForSelfHostedRunnerForOrg200Response actions_add_custom_labels_to_self_hosted_runner_for_repo(owner, repo, runner_id, actions_add_custom_labels_to_self_hosted_runner_for_org_request)

Add custom labels to a self-hosted runner for a repository

Adds custom labels to a self-hosted runner configured in a repository.  Authenticated users must have admin access to the organization to use this endpoint.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_add_custom_labels_to_self_hosted_runner_for_org_request import ActionsAddCustomLabelsToSelfHostedRunnerForOrgRequest
from github_openapi.models.actions_list_labels_for_self_hosted_runner_for_org200_response import ActionsListLabelsForSelfHostedRunnerForOrg200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    runner_id = 56 # int | Unique identifier of the self-hosted runner.
    actions_add_custom_labels_to_self_hosted_runner_for_org_request = {"labels":["gpu","accelerated"]} # ActionsAddCustomLabelsToSelfHostedRunnerForOrgRequest | 

    try:
        # Add custom labels to a self-hosted runner for a repository
        api_response = api_instance.actions_add_custom_labels_to_self_hosted_runner_for_repo(owner, repo, runner_id, actions_add_custom_labels_to_self_hosted_runner_for_org_request)
        print("The response of ActionsApi->actions_add_custom_labels_to_self_hosted_runner_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_add_custom_labels_to_self_hosted_runner_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **runner_id** | **int**| Unique identifier of the self-hosted runner. | 
 **actions_add_custom_labels_to_self_hosted_runner_for_org_request** | [**ActionsAddCustomLabelsToSelfHostedRunnerForOrgRequest**](ActionsAddCustomLabelsToSelfHostedRunnerForOrgRequest.md)|  | 

### Return type

[**ActionsListLabelsForSelfHostedRunnerForOrg200Response**](ActionsListLabelsForSelfHostedRunnerForOrg200Response.md)

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

# **actions_add_repo_access_to_self_hosted_runner_group_in_org**
> actions_add_repo_access_to_self_hosted_runner_group_in_org(org, runner_group_id, repository_id)

Add repository access to a self-hosted runner group in an organization

Adds a repository to the list of repositories that can access a self-hosted runner group. The runner group must have `visibility` set to `selected`. For more information, see \"[Create a self-hosted runner group for an organization](#create-a-self-hosted-runner-group-for-an-organization).\"  OAuth tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_group_id = 56 # int | Unique identifier of the self-hosted runner group.
    repository_id = 56 # int | The unique identifier of the repository.

    try:
        # Add repository access to a self-hosted runner group in an organization
        api_instance.actions_add_repo_access_to_self_hosted_runner_group_in_org(org, runner_group_id, repository_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_add_repo_access_to_self_hosted_runner_group_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_group_id** | **int**| Unique identifier of the self-hosted runner group. | 
 **repository_id** | **int**| The unique identifier of the repository. | 

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

# **actions_add_selected_repo_to_org_secret**
> actions_add_selected_repo_to_org_secret(org, secret_name, repository_id)

Add selected repository to an organization secret

Adds a repository to an organization secret when the `visibility` for repository access is set to `selected`. For more information about setting the visibility, see [Create or update an organization secret](https://docs.github.com/rest/actions/secrets#create-or-update-an-organization-secret).  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    repository_id = 56 # int | 

    try:
        # Add selected repository to an organization secret
        api_instance.actions_add_selected_repo_to_org_secret(org, secret_name, repository_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_add_selected_repo_to_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 
 **repository_id** | **int**|  | 

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
**204** | No Content when repository was added to the selected list |  -  |
**409** | Conflict when visibility type is not set to selected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_add_selected_repo_to_org_variable**
> actions_add_selected_repo_to_org_variable(org, name, repository_id)

Add selected repository to an organization variable

Adds a repository to an organization variable that is available to selected repositories. Organization variables that are available to selected repositories have their `visibility` field set to `selected`.  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    name = 'name_example' # str | The name of the variable.
    repository_id = 56 # int | 

    try:
        # Add selected repository to an organization variable
        api_instance.actions_add_selected_repo_to_org_variable(org, name, repository_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_add_selected_repo_to_org_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **name** | **str**| The name of the variable. | 
 **repository_id** | **int**|  | 

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
**409** | Response when the visibility of the variable is not set to &#x60;selected&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_add_self_hosted_runner_to_group_for_org**
> actions_add_self_hosted_runner_to_group_for_org(org, runner_group_id, runner_id)

Add a self-hosted runner to a group for an organization

Adds a self-hosted runner to a runner group configured in an organization.  OAuth tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_group_id = 56 # int | Unique identifier of the self-hosted runner group.
    runner_id = 56 # int | Unique identifier of the self-hosted runner.

    try:
        # Add a self-hosted runner to a group for an organization
        api_instance.actions_add_self_hosted_runner_to_group_for_org(org, runner_group_id, runner_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_add_self_hosted_runner_to_group_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_group_id** | **int**| Unique identifier of the self-hosted runner group. | 
 **runner_id** | **int**| Unique identifier of the self-hosted runner. | 

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

# **actions_approve_workflow_run**
> object actions_approve_workflow_run(owner, repo, run_id)

Approve a workflow run for a fork pull request

Approves a workflow run for a pull request from a public fork of a first time contributor. For more information, see [\"Approving workflow runs from public forks](https://docs.github.com/actions/managing-workflow-runs/approving-workflow-runs-from-public-forks).\"  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.

    try:
        # Approve a workflow run for a fork pull request
        api_response = api_instance.actions_approve_workflow_run(owner, repo, run_id)
        print("The response of ActionsApi->actions_approve_workflow_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_approve_workflow_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_cancel_workflow_run**
> object actions_cancel_workflow_run(owner, repo, run_id)

Cancel a workflow run

Cancels a workflow run using its `id`.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.

    try:
        # Cancel a workflow run
        api_response = api_instance.actions_cancel_workflow_run(owner, repo, run_id)
        print("The response of ActionsApi->actions_cancel_workflow_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_cancel_workflow_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Response |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_create_environment_variable**
> object actions_create_environment_variable(owner, repo, environment_name, actions_create_repo_variable_request)

Create an environment variable

Create an environment variable that you can reference in a GitHub Actions workflow.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_create_repo_variable_request import ActionsCreateRepoVariableRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    actions_create_repo_variable_request = {"name":"USERNAME","value":"octocat"} # ActionsCreateRepoVariableRequest | 

    try:
        # Create an environment variable
        api_response = api_instance.actions_create_environment_variable(owner, repo, environment_name, actions_create_repo_variable_request)
        print("The response of ActionsApi->actions_create_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_create_environment_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **actions_create_repo_variable_request** | [**ActionsCreateRepoVariableRequest**](ActionsCreateRepoVariableRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_create_or_update_environment_secret**
> object actions_create_or_update_environment_secret(owner, repo, environment_name, secret_name, actions_create_or_update_environment_secret_request)

Create or update an environment secret

Creates or updates an environment secret with an encrypted value. Encrypt your secret using [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see \"[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api).\"  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_create_or_update_environment_secret_request import ActionsCreateOrUpdateEnvironmentSecretRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    secret_name = 'secret_name_example' # str | The name of the secret.
    actions_create_or_update_environment_secret_request = {"encrypted_value":"c2VjcmV0","key_id":"012345678912345678"} # ActionsCreateOrUpdateEnvironmentSecretRequest | 

    try:
        # Create or update an environment secret
        api_response = api_instance.actions_create_or_update_environment_secret(owner, repo, environment_name, secret_name, actions_create_or_update_environment_secret_request)
        print("The response of ActionsApi->actions_create_or_update_environment_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_create_or_update_environment_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **secret_name** | **str**| The name of the secret. | 
 **actions_create_or_update_environment_secret_request** | [**ActionsCreateOrUpdateEnvironmentSecretRequest**](ActionsCreateOrUpdateEnvironmentSecretRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response when creating a secret |  -  |
**204** | Response when updating a secret |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_create_or_update_org_secret**
> object actions_create_or_update_org_secret(org, secret_name, actions_create_or_update_org_secret_request)

Create or update an organization secret

Creates or updates an organization secret with an encrypted value. Encrypt your secret using [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see \"[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api).\"  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth tokens and personal access tokens (classic) need the`admin:org` scope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_create_or_update_org_secret_request import ActionsCreateOrUpdateOrgSecretRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    actions_create_or_update_org_secret_request = {"encrypted_value":"c2VjcmV0","key_id":"012345678912345678","visibility":"selected","selected_repository_ids":[1296269,1296280]} # ActionsCreateOrUpdateOrgSecretRequest | 

    try:
        # Create or update an organization secret
        api_response = api_instance.actions_create_or_update_org_secret(org, secret_name, actions_create_or_update_org_secret_request)
        print("The response of ActionsApi->actions_create_or_update_org_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_create_or_update_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 
 **actions_create_or_update_org_secret_request** | [**ActionsCreateOrUpdateOrgSecretRequest**](ActionsCreateOrUpdateOrgSecretRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response when creating a secret |  -  |
**204** | Response when updating a secret |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_create_or_update_repo_secret**
> object actions_create_or_update_repo_secret(owner, repo, secret_name, actions_create_or_update_repo_secret_request)

Create or update a repository secret

Creates or updates a repository secret with an encrypted value. Encrypt your secret using [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see \"[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api).\"  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_create_or_update_repo_secret_request import ActionsCreateOrUpdateRepoSecretRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    actions_create_or_update_repo_secret_request = {"encrypted_value":"c2VjcmV0","key_id":"012345678912345678"} # ActionsCreateOrUpdateRepoSecretRequest | 

    try:
        # Create or update a repository secret
        api_response = api_instance.actions_create_or_update_repo_secret(owner, repo, secret_name, actions_create_or_update_repo_secret_request)
        print("The response of ActionsApi->actions_create_or_update_repo_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_create_or_update_repo_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 
 **actions_create_or_update_repo_secret_request** | [**ActionsCreateOrUpdateRepoSecretRequest**](ActionsCreateOrUpdateRepoSecretRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response when creating a secret |  -  |
**204** | Response when updating a secret |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_create_org_variable**
> object actions_create_org_variable(org, actions_create_org_variable_request)

Create an organization variable

Creates an organization variable that you can reference in a GitHub Actions workflow.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth tokens and personal access tokens (classic) need the`admin:org` scope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_create_org_variable_request import ActionsCreateOrgVariableRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    actions_create_org_variable_request = {"name":"USERNAME","value":"octocat","visibility":"selected","selected_repository_ids":[1296269,1296280]} # ActionsCreateOrgVariableRequest | 

    try:
        # Create an organization variable
        api_response = api_instance.actions_create_org_variable(org, actions_create_org_variable_request)
        print("The response of ActionsApi->actions_create_org_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_create_org_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **actions_create_org_variable_request** | [**ActionsCreateOrgVariableRequest**](ActionsCreateOrgVariableRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response when creating a variable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_create_registration_token_for_org**
> AuthenticationToken actions_create_registration_token_for_org(org)

Create a registration token for an organization

Returns a token that you can pass to the `config` script. The token expires after one hour.  For example, you can replace `TOKEN` in the following example with the registration token provided by this endpoint to configure your self-hosted runner:  ``` ./config.sh --url https://github.com/octo-org --token TOKEN ```  Authenticated users must have admin access to the organization to use this endpoint.  OAuth tokens and personal access tokens (classic) need the`admin:org` scope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.authentication_token import AuthenticationToken
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Create a registration token for an organization
        api_response = api_instance.actions_create_registration_token_for_org(org)
        print("The response of ActionsApi->actions_create_registration_token_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_create_registration_token_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**AuthenticationToken**](AuthenticationToken.md)

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

# **actions_create_registration_token_for_repo**
> AuthenticationToken actions_create_registration_token_for_repo(owner, repo)

Create a registration token for a repository

Returns a token that you can pass to the `config` script. The token expires after one hour.  For example, you can replace `TOKEN` in the following example with the registration token provided by this endpoint to configure your self-hosted runner:  ``` ./config.sh --url https://github.com/octo-org --token TOKEN ```  Authenticated users must have admin access to the repository to use this endpoint.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.authentication_token import AuthenticationToken
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Create a registration token for a repository
        api_response = api_instance.actions_create_registration_token_for_repo(owner, repo)
        print("The response of ActionsApi->actions_create_registration_token_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_create_registration_token_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**AuthenticationToken**](AuthenticationToken.md)

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

# **actions_create_remove_token_for_org**
> AuthenticationToken actions_create_remove_token_for_org(org)

Create a remove token for an organization

Returns a token that you can pass to the `config` script to remove a self-hosted runner from an organization. The token expires after one hour.  For example, you can replace `TOKEN` in the following example with the registration token provided by this endpoint to remove your self-hosted runner from an organization:  ``` ./config.sh remove --token TOKEN ```  Authenticated users must have admin access to the organization to use this endpoint.  OAuth tokens and personal access tokens (classic) need the`admin:org` scope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.authentication_token import AuthenticationToken
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Create a remove token for an organization
        api_response = api_instance.actions_create_remove_token_for_org(org)
        print("The response of ActionsApi->actions_create_remove_token_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_create_remove_token_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**AuthenticationToken**](AuthenticationToken.md)

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

# **actions_create_remove_token_for_repo**
> AuthenticationToken actions_create_remove_token_for_repo(owner, repo)

Create a remove token for a repository

Returns a token that you can pass to the `config` script to remove a self-hosted runner from an repository. The token expires after one hour.  For example, you can replace `TOKEN` in the following example with the registration token provided by this endpoint to remove your self-hosted runner from an organization:  ``` ./config.sh remove --token TOKEN ```  Authenticated users must have admin access to the repository to use this endpoint.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.authentication_token import AuthenticationToken
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Create a remove token for a repository
        api_response = api_instance.actions_create_remove_token_for_repo(owner, repo)
        print("The response of ActionsApi->actions_create_remove_token_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_create_remove_token_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**AuthenticationToken**](AuthenticationToken.md)

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

# **actions_create_repo_variable**
> object actions_create_repo_variable(owner, repo, actions_create_repo_variable_request)

Create a repository variable

Creates a repository variable that you can reference in a GitHub Actions workflow.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_create_repo_variable_request import ActionsCreateRepoVariableRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    actions_create_repo_variable_request = {"name":"USERNAME","value":"octocat"} # ActionsCreateRepoVariableRequest | 

    try:
        # Create a repository variable
        api_response = api_instance.actions_create_repo_variable(owner, repo, actions_create_repo_variable_request)
        print("The response of ActionsApi->actions_create_repo_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_create_repo_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **actions_create_repo_variable_request** | [**ActionsCreateRepoVariableRequest**](ActionsCreateRepoVariableRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_create_self_hosted_runner_group_for_org**
> RunnerGroupsOrg actions_create_self_hosted_runner_group_for_org(org, actions_create_self_hosted_runner_group_for_org_request)

Create a self-hosted runner group for an organization

Creates a new self-hosted runner group for an organization.  OAuth tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_create_self_hosted_runner_group_for_org_request import ActionsCreateSelfHostedRunnerGroupForOrgRequest
from github_openapi.models.runner_groups_org import RunnerGroupsOrg
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    actions_create_self_hosted_runner_group_for_org_request = {"name":"Expensive hardware runners","visibility":"selected","selected_repository_ids":[32,91],"runners":[9,2]} # ActionsCreateSelfHostedRunnerGroupForOrgRequest | 

    try:
        # Create a self-hosted runner group for an organization
        api_response = api_instance.actions_create_self_hosted_runner_group_for_org(org, actions_create_self_hosted_runner_group_for_org_request)
        print("The response of ActionsApi->actions_create_self_hosted_runner_group_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_create_self_hosted_runner_group_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **actions_create_self_hosted_runner_group_for_org_request** | [**ActionsCreateSelfHostedRunnerGroupForOrgRequest**](ActionsCreateSelfHostedRunnerGroupForOrgRequest.md)|  | 

### Return type

[**RunnerGroupsOrg**](RunnerGroupsOrg.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_create_workflow_dispatch**
> actions_create_workflow_dispatch(owner, repo, workflow_id, actions_create_workflow_dispatch_request)

Create a workflow dispatch event

You can use this endpoint to manually trigger a GitHub Actions workflow run. You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`.  You must configure your GitHub Actions workflow to run when the [`workflow_dispatch` webhook](/developers/webhooks-and-events/webhook-events-and-payloads#workflow_dispatch) event occurs. The `inputs` are configured in the workflow file. For more information about how to configure the `workflow_dispatch` event in the workflow file, see \"[Events that trigger workflows](/actions/reference/events-that-trigger-workflows#workflow_dispatch).\"  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_create_workflow_dispatch_request import ActionsCreateWorkflowDispatchRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    workflow_id = github_openapi.ActionsGetWorkflowWorkflowIdParameter() # ActionsGetWorkflowWorkflowIdParameter | The ID of the workflow. You can also pass the workflow file name as a string.
    actions_create_workflow_dispatch_request = {"ref":"topic-branch","inputs":{"name":"Mona the Octocat","home":"San Francisco, CA"}} # ActionsCreateWorkflowDispatchRequest | 

    try:
        # Create a workflow dispatch event
        api_instance.actions_create_workflow_dispatch(owner, repo, workflow_id, actions_create_workflow_dispatch_request)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_create_workflow_dispatch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **workflow_id** | [**ActionsGetWorkflowWorkflowIdParameter**](.md)| The ID of the workflow. You can also pass the workflow file name as a string. | 
 **actions_create_workflow_dispatch_request** | [**ActionsCreateWorkflowDispatchRequest**](ActionsCreateWorkflowDispatchRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_delete_actions_cache_by_id**
> actions_delete_actions_cache_by_id(owner, repo, cache_id)

Delete a GitHub Actions cache for a repository (using a cache ID)

Deletes a GitHub Actions cache for a repository, using a cache ID.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    cache_id = 56 # int | The unique identifier of the GitHub Actions cache.

    try:
        # Delete a GitHub Actions cache for a repository (using a cache ID)
        api_instance.actions_delete_actions_cache_by_id(owner, repo, cache_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_delete_actions_cache_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **cache_id** | **int**| The unique identifier of the GitHub Actions cache. | 

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

# **actions_delete_actions_cache_by_key**
> ActionsCacheList actions_delete_actions_cache_by_key(owner, repo, key, ref=ref)

Delete GitHub Actions caches for a repository (using a cache key)

Deletes one or more GitHub Actions caches for a repository, using a complete cache key. By default, all caches that match the provided key are deleted, but you can optionally provide a Git ref to restrict deletions to caches that match both the provided key and the Git ref.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_cache_list import ActionsCacheList
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    key = 'key_example' # str | A key for identifying the cache.
    ref = 'ref_example' # str | The full Git reference for narrowing down the cache. The `ref` for a branch should be formatted as `refs/heads/<branch name>`. To reference a pull request use `refs/pull/<number>/merge`. (optional)

    try:
        # Delete GitHub Actions caches for a repository (using a cache key)
        api_response = api_instance.actions_delete_actions_cache_by_key(owner, repo, key, ref=ref)
        print("The response of ActionsApi->actions_delete_actions_cache_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_delete_actions_cache_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **key** | **str**| A key for identifying the cache. | 
 **ref** | **str**| The full Git reference for narrowing down the cache. The &#x60;ref&#x60; for a branch should be formatted as &#x60;refs/heads/&lt;branch name&gt;&#x60;. To reference a pull request use &#x60;refs/pull/&lt;number&gt;/merge&#x60;. | [optional] 

### Return type

[**ActionsCacheList**](ActionsCacheList.md)

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

# **actions_delete_artifact**
> actions_delete_artifact(owner, repo, artifact_id)

Delete an artifact

Deletes an artifact for a workflow run. OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    artifact_id = 56 # int | The unique identifier of the artifact.

    try:
        # Delete an artifact
        api_instance.actions_delete_artifact(owner, repo, artifact_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_delete_artifact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **artifact_id** | **int**| The unique identifier of the artifact. | 

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

# **actions_delete_environment_secret**
> actions_delete_environment_secret(owner, repo, environment_name, secret_name)

Delete an environment secret

Deletes a secret in an environment using the secret name.  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # Delete an environment secret
        api_instance.actions_delete_environment_secret(owner, repo, environment_name, secret_name)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_delete_environment_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **secret_name** | **str**| The name of the secret. | 

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

# **actions_delete_environment_variable**
> actions_delete_environment_variable(owner, repo, name, environment_name)

Delete an environment variable

Deletes an environment variable using the variable name.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    name = 'name_example' # str | The name of the variable.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.

    try:
        # Delete an environment variable
        api_instance.actions_delete_environment_variable(owner, repo, name, environment_name)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_delete_environment_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **name** | **str**| The name of the variable. | 
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
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_delete_org_secret**
> actions_delete_org_secret(org, secret_name)

Delete an organization secret

Deletes a secret in an organization using the secret name.  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth tokens and personal access tokens (classic) need the`admin:org` scope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # Delete an organization secret
        api_instance.actions_delete_org_secret(org, secret_name)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_delete_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 

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

# **actions_delete_org_variable**
> actions_delete_org_variable(org, name)

Delete an organization variable

Deletes an organization variable using the variable name.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth tokens and personal access tokens (classic) need the`admin:org` scope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    name = 'name_example' # str | The name of the variable.

    try:
        # Delete an organization variable
        api_instance.actions_delete_org_variable(org, name)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_delete_org_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **name** | **str**| The name of the variable. | 

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

# **actions_delete_repo_secret**
> actions_delete_repo_secret(owner, repo, secret_name)

Delete a repository secret

Deletes a secret in a repository using the secret name.  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # Delete a repository secret
        api_instance.actions_delete_repo_secret(owner, repo, secret_name)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_delete_repo_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 

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

# **actions_delete_repo_variable**
> actions_delete_repo_variable(owner, repo, name)

Delete a repository variable

Deletes a repository variable using the variable name.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    name = 'name_example' # str | The name of the variable.

    try:
        # Delete a repository variable
        api_instance.actions_delete_repo_variable(owner, repo, name)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_delete_repo_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **name** | **str**| The name of the variable. | 

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

# **actions_delete_self_hosted_runner_from_org**
> actions_delete_self_hosted_runner_from_org(org, runner_id)

Delete a self-hosted runner from an organization

Forces the removal of a self-hosted runner from an organization. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.  Authenticated users must have admin access to the organization to use this endpoint.  OAuth tokens and personal access tokens (classic) need the`admin:org` scope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_id = 56 # int | Unique identifier of the self-hosted runner.

    try:
        # Delete a self-hosted runner from an organization
        api_instance.actions_delete_self_hosted_runner_from_org(org, runner_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_delete_self_hosted_runner_from_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_id** | **int**| Unique identifier of the self-hosted runner. | 

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

# **actions_delete_self_hosted_runner_from_repo**
> actions_delete_self_hosted_runner_from_repo(owner, repo, runner_id)

Delete a self-hosted runner from a repository

Forces the removal of a self-hosted runner from a repository. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.  Authenticated users must have admin access to the repository to use this endpoint.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    runner_id = 56 # int | Unique identifier of the self-hosted runner.

    try:
        # Delete a self-hosted runner from a repository
        api_instance.actions_delete_self_hosted_runner_from_repo(owner, repo, runner_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_delete_self_hosted_runner_from_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **runner_id** | **int**| Unique identifier of the self-hosted runner. | 

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

# **actions_delete_self_hosted_runner_group_from_org**
> actions_delete_self_hosted_runner_group_from_org(org, runner_group_id)

Delete a self-hosted runner group from an organization

Deletes a self-hosted runner group for an organization.  OAuth tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_group_id = 56 # int | Unique identifier of the self-hosted runner group.

    try:
        # Delete a self-hosted runner group from an organization
        api_instance.actions_delete_self_hosted_runner_group_from_org(org, runner_group_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_delete_self_hosted_runner_group_from_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_group_id** | **int**| Unique identifier of the self-hosted runner group. | 

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

# **actions_delete_workflow_run**
> actions_delete_workflow_run(owner, repo, run_id)

Delete a workflow run

Deletes a specific workflow run.  Anyone with write access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.

    try:
        # Delete a workflow run
        api_instance.actions_delete_workflow_run(owner, repo, run_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_delete_workflow_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 

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

# **actions_delete_workflow_run_logs**
> actions_delete_workflow_run_logs(owner, repo, run_id)

Delete workflow run logs

Deletes all logs for a workflow run.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.

    try:
        # Delete workflow run logs
        api_instance.actions_delete_workflow_run_logs(owner, repo, run_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_delete_workflow_run_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 

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
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_disable_selected_repository_github_actions_organization**
> actions_disable_selected_repository_github_actions_organization(org, repository_id)

Disable a selected repository for GitHub Actions in an organization

Removes a repository from the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be configured to `selected`. For more information, see \"[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization).\"  OAuth tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    repository_id = 56 # int | The unique identifier of the repository.

    try:
        # Disable a selected repository for GitHub Actions in an organization
        api_instance.actions_disable_selected_repository_github_actions_organization(org, repository_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_disable_selected_repository_github_actions_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **repository_id** | **int**| The unique identifier of the repository. | 

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

# **actions_disable_workflow**
> actions_disable_workflow(owner, repo, workflow_id)

Disable a workflow

Disables a workflow and sets the `state` of the workflow to `disabled_manually`. You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    workflow_id = github_openapi.ActionsGetWorkflowWorkflowIdParameter() # ActionsGetWorkflowWorkflowIdParameter | The ID of the workflow. You can also pass the workflow file name as a string.

    try:
        # Disable a workflow
        api_instance.actions_disable_workflow(owner, repo, workflow_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_disable_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **workflow_id** | [**ActionsGetWorkflowWorkflowIdParameter**](.md)| The ID of the workflow. You can also pass the workflow file name as a string. | 

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

# **actions_download_artifact**
> actions_download_artifact(owner, repo, artifact_id, archive_format)

Download an artifact

Gets a redirect URL to download an archive for a repository. This URL expires after 1 minute. Look for `Location:` in the response header to find the URL for the download. The `:archive_format` must be `zip`.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    artifact_id = 56 # int | The unique identifier of the artifact.
    archive_format = 'archive_format_example' # str | 

    try:
        # Download an artifact
        api_instance.actions_download_artifact(owner, repo, artifact_id, archive_format)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_download_artifact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **artifact_id** | **int**| The unique identifier of the artifact. | 
 **archive_format** | **str**|  | 

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
**302** | Response |  * Location -  <br>  |
**410** | Gone |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_download_job_logs_for_workflow_run**
> actions_download_job_logs_for_workflow_run(owner, repo, job_id)

Download job logs for a workflow run

Gets a redirect URL to download a plain text file of logs for a workflow job. This link expires after 1 minute. Look for `Location:` in the response header to find the URL for the download.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    job_id = 56 # int | The unique identifier of the job.

    try:
        # Download job logs for a workflow run
        api_instance.actions_download_job_logs_for_workflow_run(owner, repo, job_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_download_job_logs_for_workflow_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **job_id** | **int**| The unique identifier of the job. | 

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

# **actions_download_workflow_run_attempt_logs**
> actions_download_workflow_run_attempt_logs(owner, repo, run_id, attempt_number)

Download workflow run attempt logs

Gets a redirect URL to download an archive of log files for a specific workflow run attempt. This link expires after 1 minute. Look for `Location:` in the response header to find the URL for the download.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.
    attempt_number = 56 # int | The attempt number of the workflow run.

    try:
        # Download workflow run attempt logs
        api_instance.actions_download_workflow_run_attempt_logs(owner, repo, run_id, attempt_number)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_download_workflow_run_attempt_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 
 **attempt_number** | **int**| The attempt number of the workflow run. | 

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

# **actions_download_workflow_run_logs**
> actions_download_workflow_run_logs(owner, repo, run_id)

Download workflow run logs

Gets a redirect URL to download an archive of log files for a workflow run. This link expires after 1 minute. Look for `Location:` in the response header to find the URL for the download.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.

    try:
        # Download workflow run logs
        api_instance.actions_download_workflow_run_logs(owner, repo, run_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_download_workflow_run_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 

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

# **actions_enable_selected_repository_github_actions_organization**
> actions_enable_selected_repository_github_actions_organization(org, repository_id)

Enable a selected repository for GitHub Actions in an organization

Adds a repository to the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be must be configured to `selected`. For more information, see \"[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization).\"  OAuth tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    repository_id = 56 # int | The unique identifier of the repository.

    try:
        # Enable a selected repository for GitHub Actions in an organization
        api_instance.actions_enable_selected_repository_github_actions_organization(org, repository_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_enable_selected_repository_github_actions_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **repository_id** | **int**| The unique identifier of the repository. | 

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

# **actions_enable_workflow**
> actions_enable_workflow(owner, repo, workflow_id)

Enable a workflow

Enables a workflow and sets the `state` of the workflow to `active`. You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    workflow_id = github_openapi.ActionsGetWorkflowWorkflowIdParameter() # ActionsGetWorkflowWorkflowIdParameter | The ID of the workflow. You can also pass the workflow file name as a string.

    try:
        # Enable a workflow
        api_instance.actions_enable_workflow(owner, repo, workflow_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_enable_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **workflow_id** | [**ActionsGetWorkflowWorkflowIdParameter**](.md)| The ID of the workflow. You can also pass the workflow file name as a string. | 

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

# **actions_force_cancel_workflow_run**
> object actions_force_cancel_workflow_run(owner, repo, run_id)

Force cancel a workflow run

Cancels a workflow run and bypasses conditions that would otherwise cause a workflow execution to continue, such as an `always()` condition on a job. You should only use this endpoint to cancel a workflow run when the workflow run is not responding to [`POST /repos/{owner}/{repo}/actions/runs/{run_id}/cancel`](/rest/actions/workflow-runs#cancel-a-workflow-run).  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.

    try:
        # Force cancel a workflow run
        api_response = api_instance.actions_force_cancel_workflow_run(owner, repo, run_id)
        print("The response of ActionsApi->actions_force_cancel_workflow_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_force_cancel_workflow_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Response |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_generate_runner_jitconfig_for_org**
> ActionsGenerateRunnerJitconfigForOrg201Response actions_generate_runner_jitconfig_for_org(org, actions_generate_runner_jitconfig_for_org_request)

Create configuration for a just-in-time runner for an organization

Generates a configuration that can be passed to the runner application at startup.  The authenticated user must have admin access to the organization.  OAuth tokens and personal access tokens (classic) need the`admin:org` scope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_generate_runner_jitconfig_for_org201_response import ActionsGenerateRunnerJitconfigForOrg201Response
from github_openapi.models.actions_generate_runner_jitconfig_for_org_request import ActionsGenerateRunnerJitconfigForOrgRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    actions_generate_runner_jitconfig_for_org_request = {"name":"New runner","runner_group_id":1,"labels":["self-hosted","X64","macOS","no-gpu"],"work_folder":"_work"} # ActionsGenerateRunnerJitconfigForOrgRequest | 

    try:
        # Create configuration for a just-in-time runner for an organization
        api_response = api_instance.actions_generate_runner_jitconfig_for_org(org, actions_generate_runner_jitconfig_for_org_request)
        print("The response of ActionsApi->actions_generate_runner_jitconfig_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_generate_runner_jitconfig_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **actions_generate_runner_jitconfig_for_org_request** | [**ActionsGenerateRunnerJitconfigForOrgRequest**](ActionsGenerateRunnerJitconfigForOrgRequest.md)|  | 

### Return type

[**ActionsGenerateRunnerJitconfigForOrg201Response**](ActionsGenerateRunnerJitconfigForOrg201Response.md)

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_generate_runner_jitconfig_for_repo**
> ActionsGenerateRunnerJitconfigForOrg201Response actions_generate_runner_jitconfig_for_repo(owner, repo, actions_generate_runner_jitconfig_for_org_request)

Create configuration for a just-in-time runner for a repository

Generates a configuration that can be passed to the runner application at startup.  The authenticated user must have admin access to the repository.  OAuth tokens and personal access tokens (classic) need the`repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_generate_runner_jitconfig_for_org201_response import ActionsGenerateRunnerJitconfigForOrg201Response
from github_openapi.models.actions_generate_runner_jitconfig_for_org_request import ActionsGenerateRunnerJitconfigForOrgRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    actions_generate_runner_jitconfig_for_org_request = {"name":"New runner","runner_group_id":1,"labels":["self-hosted","X64","macOS","no-gpu"],"work_folder":"_work"} # ActionsGenerateRunnerJitconfigForOrgRequest | 

    try:
        # Create configuration for a just-in-time runner for a repository
        api_response = api_instance.actions_generate_runner_jitconfig_for_repo(owner, repo, actions_generate_runner_jitconfig_for_org_request)
        print("The response of ActionsApi->actions_generate_runner_jitconfig_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_generate_runner_jitconfig_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **actions_generate_runner_jitconfig_for_org_request** | [**ActionsGenerateRunnerJitconfigForOrgRequest**](ActionsGenerateRunnerJitconfigForOrgRequest.md)|  | 

### Return type

[**ActionsGenerateRunnerJitconfigForOrg201Response**](ActionsGenerateRunnerJitconfigForOrg201Response.md)

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_get_actions_cache_list**
> ActionsCacheList actions_get_actions_cache_list(owner, repo, per_page=per_page, page=page, ref=ref, key=key, sort=sort, direction=direction)

List GitHub Actions caches for a repository

Lists the GitHub Actions caches for a repository.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_cache_list import ActionsCacheList
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    ref = 'ref_example' # str | The full Git reference for narrowing down the cache. The `ref` for a branch should be formatted as `refs/heads/<branch name>`. To reference a pull request use `refs/pull/<number>/merge`. (optional)
    key = 'key_example' # str | An explicit key or prefix for identifying the cache (optional)
    sort = last_accessed_at # str | The property to sort the results by. `created_at` means when the cache was created. `last_accessed_at` means when the cache was last accessed. `size_in_bytes` is the size of the cache in bytes. (optional) (default to last_accessed_at)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)

    try:
        # List GitHub Actions caches for a repository
        api_response = api_instance.actions_get_actions_cache_list(owner, repo, per_page=per_page, page=page, ref=ref, key=key, sort=sort, direction=direction)
        print("The response of ActionsApi->actions_get_actions_cache_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_actions_cache_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **ref** | **str**| The full Git reference for narrowing down the cache. The &#x60;ref&#x60; for a branch should be formatted as &#x60;refs/heads/&lt;branch name&gt;&#x60;. To reference a pull request use &#x60;refs/pull/&lt;number&gt;/merge&#x60;. | [optional] 
 **key** | **str**| An explicit key or prefix for identifying the cache | [optional] 
 **sort** | **str**| The property to sort the results by. &#x60;created_at&#x60; means when the cache was created. &#x60;last_accessed_at&#x60; means when the cache was last accessed. &#x60;size_in_bytes&#x60; is the size of the cache in bytes. | [optional] [default to last_accessed_at]
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]

### Return type

[**ActionsCacheList**](ActionsCacheList.md)

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

# **actions_get_actions_cache_usage**
> ActionsCacheUsageByRepository actions_get_actions_cache_usage(owner, repo)

Get GitHub Actions cache usage for a repository

Gets GitHub Actions cache usage for a repository. The data fetched using this API is refreshed approximately every 5 minutes, so values returned from this endpoint may take at least 5 minutes to get updated.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_cache_usage_by_repository import ActionsCacheUsageByRepository
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get GitHub Actions cache usage for a repository
        api_response = api_instance.actions_get_actions_cache_usage(owner, repo)
        print("The response of ActionsApi->actions_get_actions_cache_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_actions_cache_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**ActionsCacheUsageByRepository**](ActionsCacheUsageByRepository.md)

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

# **actions_get_actions_cache_usage_by_repo_for_org**
> ActionsGetActionsCacheUsageByRepoForOrg200Response actions_get_actions_cache_usage_by_repo_for_org(org, per_page=per_page, page=page)

List repositories with GitHub Actions cache usage for an organization

Lists repositories and their GitHub Actions cache usage for an organization. The data fetched using this API is refreshed approximately every 5 minutes, so values returned from this endpoint may take at least 5 minutes to get updated.  OAuth tokens and personal access tokens (classic) need the `read:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_get_actions_cache_usage_by_repo_for_org200_response import ActionsGetActionsCacheUsageByRepoForOrg200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repositories with GitHub Actions cache usage for an organization
        api_response = api_instance.actions_get_actions_cache_usage_by_repo_for_org(org, per_page=per_page, page=page)
        print("The response of ActionsApi->actions_get_actions_cache_usage_by_repo_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_actions_cache_usage_by_repo_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActionsGetActionsCacheUsageByRepoForOrg200Response**](ActionsGetActionsCacheUsageByRepoForOrg200Response.md)

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

# **actions_get_actions_cache_usage_for_org**
> ActionsCacheUsageOrgEnterprise actions_get_actions_cache_usage_for_org(org)

Get GitHub Actions cache usage for an organization

Gets the total GitHub Actions cache usage for an organization. The data fetched using this API is refreshed approximately every 5 minutes, so values returned from this endpoint may take at least 5 minutes to get updated.  OAuth tokens and personal access tokens (classic) need the `read:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_cache_usage_org_enterprise import ActionsCacheUsageOrgEnterprise
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get GitHub Actions cache usage for an organization
        api_response = api_instance.actions_get_actions_cache_usage_for_org(org)
        print("The response of ActionsApi->actions_get_actions_cache_usage_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_actions_cache_usage_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**ActionsCacheUsageOrgEnterprise**](ActionsCacheUsageOrgEnterprise.md)

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

# **actions_get_allowed_actions_organization**
> SelectedActions actions_get_allowed_actions_organization(org)

Get allowed actions and reusable workflows for an organization

Gets the selected actions and reusable workflows that are allowed in an organization. To use this endpoint, the organization permission policy for `allowed_actions` must be configured to `selected`. For more information, see \"[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization).\"  OAuth tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.selected_actions import SelectedActions
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get allowed actions and reusable workflows for an organization
        api_response = api_instance.actions_get_allowed_actions_organization(org)
        print("The response of ActionsApi->actions_get_allowed_actions_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_allowed_actions_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**SelectedActions**](SelectedActions.md)

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

# **actions_get_allowed_actions_repository**
> SelectedActions actions_get_allowed_actions_repository(owner, repo)

Get allowed actions and reusable workflows for a repository

Gets the settings for selected actions and reusable workflows that are allowed in a repository. To use this endpoint, the repository policy for `allowed_actions` must be configured to `selected`. For more information, see \"[Set GitHub Actions permissions for a repository](#set-github-actions-permissions-for-a-repository).\"  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.selected_actions import SelectedActions
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get allowed actions and reusable workflows for a repository
        api_response = api_instance.actions_get_allowed_actions_repository(owner, repo)
        print("The response of ActionsApi->actions_get_allowed_actions_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_allowed_actions_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**SelectedActions**](SelectedActions.md)

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

# **actions_get_artifact**
> Artifact actions_get_artifact(owner, repo, artifact_id)

Get an artifact

Gets a specific artifact for a workflow run.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.artifact import Artifact
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    artifact_id = 56 # int | The unique identifier of the artifact.

    try:
        # Get an artifact
        api_response = api_instance.actions_get_artifact(owner, repo, artifact_id)
        print("The response of ActionsApi->actions_get_artifact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_artifact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **artifact_id** | **int**| The unique identifier of the artifact. | 

### Return type

[**Artifact**](Artifact.md)

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

# **actions_get_custom_oidc_sub_claim_for_repo**
> OidcCustomSubRepo actions_get_custom_oidc_sub_claim_for_repo(owner, repo)

Get the customization template for an OIDC subject claim for a repository

Gets the customization template for an OpenID Connect (OIDC) subject claim.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.oidc_custom_sub_repo import OidcCustomSubRepo
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get the customization template for an OIDC subject claim for a repository
        api_response = api_instance.actions_get_custom_oidc_sub_claim_for_repo(owner, repo)
        print("The response of ActionsApi->actions_get_custom_oidc_sub_claim_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_custom_oidc_sub_claim_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**OidcCustomSubRepo**](OidcCustomSubRepo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status response |  -  |
**400** | Bad Request |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_get_environment_public_key**
> ActionsPublicKey actions_get_environment_public_key(owner, repo, environment_name)

Get an environment public key

Get the public key for an environment, which you need to encrypt environment secrets. You need to encrypt a secret before you can create or update secrets.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_public_key import ActionsPublicKey
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.

    try:
        # Get an environment public key
        api_response = api_instance.actions_get_environment_public_key(owner, repo, environment_name)
        print("The response of ActionsApi->actions_get_environment_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_environment_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 

### Return type

[**ActionsPublicKey**](ActionsPublicKey.md)

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

# **actions_get_environment_secret**
> ActionsSecret actions_get_environment_secret(owner, repo, environment_name, secret_name)

Get an environment secret

Gets a single environment secret without revealing its encrypted value.  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_secret import ActionsSecret
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # Get an environment secret
        api_response = api_instance.actions_get_environment_secret(owner, repo, environment_name, secret_name)
        print("The response of ActionsApi->actions_get_environment_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_environment_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **secret_name** | **str**| The name of the secret. | 

### Return type

[**ActionsSecret**](ActionsSecret.md)

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

# **actions_get_environment_variable**
> ActionsVariable actions_get_environment_variable(owner, repo, environment_name, name)

Get an environment variable

Gets a specific variable in an environment.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_variable import ActionsVariable
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    name = 'name_example' # str | The name of the variable.

    try:
        # Get an environment variable
        api_response = api_instance.actions_get_environment_variable(owner, repo, environment_name, name)
        print("The response of ActionsApi->actions_get_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_environment_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **name** | **str**| The name of the variable. | 

### Return type

[**ActionsVariable**](ActionsVariable.md)

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

# **actions_get_github_actions_default_workflow_permissions_organization**
> ActionsGetDefaultWorkflowPermissions actions_get_github_actions_default_workflow_permissions_organization(org)

Get default workflow permissions for an organization

Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an organization, as well as whether GitHub Actions can submit approving pull request reviews. For more information, see \"[Setting the permissions of the GITHUB_TOKEN for your organization](https://docs.github.com/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-organization).\"  OAuth tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_get_default_workflow_permissions import ActionsGetDefaultWorkflowPermissions
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get default workflow permissions for an organization
        api_response = api_instance.actions_get_github_actions_default_workflow_permissions_organization(org)
        print("The response of ActionsApi->actions_get_github_actions_default_workflow_permissions_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_github_actions_default_workflow_permissions_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**ActionsGetDefaultWorkflowPermissions**](ActionsGetDefaultWorkflowPermissions.md)

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

# **actions_get_github_actions_default_workflow_permissions_repository**
> ActionsGetDefaultWorkflowPermissions actions_get_github_actions_default_workflow_permissions_repository(owner, repo)

Get default workflow permissions for a repository

Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in a repository, as well as if GitHub Actions can submit approving pull request reviews. For more information, see \"[Setting the permissions of the GITHUB_TOKEN for your repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#setting-the-permissions-of-the-github_token-for-your-repository).\"  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_get_default_workflow_permissions import ActionsGetDefaultWorkflowPermissions
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get default workflow permissions for a repository
        api_response = api_instance.actions_get_github_actions_default_workflow_permissions_repository(owner, repo)
        print("The response of ActionsApi->actions_get_github_actions_default_workflow_permissions_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_github_actions_default_workflow_permissions_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**ActionsGetDefaultWorkflowPermissions**](ActionsGetDefaultWorkflowPermissions.md)

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

# **actions_get_github_actions_permissions_organization**
> ActionsOrganizationPermissions actions_get_github_actions_permissions_organization(org)

Get GitHub Actions permissions for an organization

Gets the GitHub Actions permissions policy for repositories and allowed actions and reusable workflows in an organization.  OAuth tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_organization_permissions import ActionsOrganizationPermissions
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get GitHub Actions permissions for an organization
        api_response = api_instance.actions_get_github_actions_permissions_organization(org)
        print("The response of ActionsApi->actions_get_github_actions_permissions_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_github_actions_permissions_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**ActionsOrganizationPermissions**](ActionsOrganizationPermissions.md)

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

# **actions_get_github_actions_permissions_repository**
> ActionsRepositoryPermissions actions_get_github_actions_permissions_repository(owner, repo)

Get GitHub Actions permissions for a repository

Gets the GitHub Actions permissions policy for a repository, including whether GitHub Actions is enabled and the actions and reusable workflows allowed to run in the repository.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_repository_permissions import ActionsRepositoryPermissions
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get GitHub Actions permissions for a repository
        api_response = api_instance.actions_get_github_actions_permissions_repository(owner, repo)
        print("The response of ActionsApi->actions_get_github_actions_permissions_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_github_actions_permissions_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**ActionsRepositoryPermissions**](ActionsRepositoryPermissions.md)

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

# **actions_get_job_for_workflow_run**
> Job actions_get_job_for_workflow_run(owner, repo, job_id)

Get a job for a workflow run

Gets a specific job in a workflow run.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.job import Job
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    job_id = 56 # int | The unique identifier of the job.

    try:
        # Get a job for a workflow run
        api_response = api_instance.actions_get_job_for_workflow_run(owner, repo, job_id)
        print("The response of ActionsApi->actions_get_job_for_workflow_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_job_for_workflow_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **job_id** | **int**| The unique identifier of the job. | 

### Return type

[**Job**](Job.md)

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

# **actions_get_org_public_key**
> ActionsPublicKey actions_get_org_public_key(org)

Get an organization public key

Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets.  The authenticated user must have collaborator access to a repository to create, update, or read secrets.  OAuth tokens and personal access tokens (classic) need the`admin:org` scope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_public_key import ActionsPublicKey
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get an organization public key
        api_response = api_instance.actions_get_org_public_key(org)
        print("The response of ActionsApi->actions_get_org_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_org_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**ActionsPublicKey**](ActionsPublicKey.md)

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

# **actions_get_org_secret**
> OrganizationActionsSecret actions_get_org_secret(org, secret_name)

Get an organization secret

Gets a single organization secret without revealing its encrypted value.  The authenticated user must have collaborator access to a repository to create, update, or read secrets  OAuth tokens and personal access tokens (classic) need the`admin:org` scope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.organization_actions_secret import OrganizationActionsSecret
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # Get an organization secret
        api_response = api_instance.actions_get_org_secret(org, secret_name)
        print("The response of ActionsApi->actions_get_org_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 

### Return type

[**OrganizationActionsSecret**](OrganizationActionsSecret.md)

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

# **actions_get_org_variable**
> OrganizationActionsVariable actions_get_org_variable(org, name)

Get an organization variable

Gets a specific variable in an organization.  The authenticated user must have collaborator access to a repository to create, update, or read variables.  OAuth tokens and personal access tokens (classic) need the`admin:org` scope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.organization_actions_variable import OrganizationActionsVariable
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    name = 'name_example' # str | The name of the variable.

    try:
        # Get an organization variable
        api_response = api_instance.actions_get_org_variable(org, name)
        print("The response of ActionsApi->actions_get_org_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_org_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **name** | **str**| The name of the variable. | 

### Return type

[**OrganizationActionsVariable**](OrganizationActionsVariable.md)

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

# **actions_get_pending_deployments_for_run**
> List[PendingDeployment] actions_get_pending_deployments_for_run(owner, repo, run_id)

Get pending deployments for a workflow run

Get all deployment environments for a workflow run that are waiting for protection rules to pass.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.pending_deployment import PendingDeployment
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.

    try:
        # Get pending deployments for a workflow run
        api_response = api_instance.actions_get_pending_deployments_for_run(owner, repo, run_id)
        print("The response of ActionsApi->actions_get_pending_deployments_for_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_pending_deployments_for_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 

### Return type

[**List[PendingDeployment]**](PendingDeployment.md)

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

# **actions_get_repo_public_key**
> ActionsPublicKey actions_get_repo_public_key(owner, repo)

Get a repository public key

Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_public_key import ActionsPublicKey
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get a repository public key
        api_response = api_instance.actions_get_repo_public_key(owner, repo)
        print("The response of ActionsApi->actions_get_repo_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_repo_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**ActionsPublicKey**](ActionsPublicKey.md)

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

# **actions_get_repo_secret**
> ActionsSecret actions_get_repo_secret(owner, repo, secret_name)

Get a repository secret

Gets a single repository secret without revealing its encrypted value.  The authenticated user must have collaborator access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_secret import ActionsSecret
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # Get a repository secret
        api_response = api_instance.actions_get_repo_secret(owner, repo, secret_name)
        print("The response of ActionsApi->actions_get_repo_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_repo_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 

### Return type

[**ActionsSecret**](ActionsSecret.md)

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

# **actions_get_repo_variable**
> ActionsVariable actions_get_repo_variable(owner, repo, name)

Get a repository variable

Gets a specific variable in a repository.  The authenticated user must have collaborator access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_variable import ActionsVariable
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    name = 'name_example' # str | The name of the variable.

    try:
        # Get a repository variable
        api_response = api_instance.actions_get_repo_variable(owner, repo, name)
        print("The response of ActionsApi->actions_get_repo_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_repo_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **name** | **str**| The name of the variable. | 

### Return type

[**ActionsVariable**](ActionsVariable.md)

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

# **actions_get_reviews_for_run**
> List[EnvironmentApprovals] actions_get_reviews_for_run(owner, repo, run_id)

Get the review history for a workflow run

Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.environment_approvals import EnvironmentApprovals
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.

    try:
        # Get the review history for a workflow run
        api_response = api_instance.actions_get_reviews_for_run(owner, repo, run_id)
        print("The response of ActionsApi->actions_get_reviews_for_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_reviews_for_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 

### Return type

[**List[EnvironmentApprovals]**](EnvironmentApprovals.md)

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

# **actions_get_self_hosted_runner_for_org**
> Runner actions_get_self_hosted_runner_for_org(org, runner_id)

Get a self-hosted runner for an organization

Gets a specific self-hosted runner configured in an organization.  Authenticated users must have admin access to the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.

### Example


```python
import github_openapi
from github_openapi.models.runner import Runner
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_id = 56 # int | Unique identifier of the self-hosted runner.

    try:
        # Get a self-hosted runner for an organization
        api_response = api_instance.actions_get_self_hosted_runner_for_org(org, runner_id)
        print("The response of ActionsApi->actions_get_self_hosted_runner_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_self_hosted_runner_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_id** | **int**| Unique identifier of the self-hosted runner. | 

### Return type

[**Runner**](Runner.md)

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

# **actions_get_self_hosted_runner_for_repo**
> Runner actions_get_self_hosted_runner_for_repo(owner, repo, runner_id)

Get a self-hosted runner for a repository

Gets a specific self-hosted runner configured in a repository.  Authenticated users must have admin access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.runner import Runner
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    runner_id = 56 # int | Unique identifier of the self-hosted runner.

    try:
        # Get a self-hosted runner for a repository
        api_response = api_instance.actions_get_self_hosted_runner_for_repo(owner, repo, runner_id)
        print("The response of ActionsApi->actions_get_self_hosted_runner_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_self_hosted_runner_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **runner_id** | **int**| Unique identifier of the self-hosted runner. | 

### Return type

[**Runner**](Runner.md)

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

# **actions_get_self_hosted_runner_group_for_org**
> RunnerGroupsOrg actions_get_self_hosted_runner_group_for_org(org, runner_group_id)

Get a self-hosted runner group for an organization

Gets a specific self-hosted runner group for an organization.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.runner_groups_org import RunnerGroupsOrg
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_group_id = 56 # int | Unique identifier of the self-hosted runner group.

    try:
        # Get a self-hosted runner group for an organization
        api_response = api_instance.actions_get_self_hosted_runner_group_for_org(org, runner_group_id)
        print("The response of ActionsApi->actions_get_self_hosted_runner_group_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_self_hosted_runner_group_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_group_id** | **int**| Unique identifier of the self-hosted runner group. | 

### Return type

[**RunnerGroupsOrg**](RunnerGroupsOrg.md)

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

# **actions_get_workflow**
> Workflow actions_get_workflow(owner, repo, workflow_id)

Get a workflow

Gets a specific workflow. You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.workflow import Workflow
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    workflow_id = github_openapi.ActionsGetWorkflowWorkflowIdParameter() # ActionsGetWorkflowWorkflowIdParameter | The ID of the workflow. You can also pass the workflow file name as a string.

    try:
        # Get a workflow
        api_response = api_instance.actions_get_workflow(owner, repo, workflow_id)
        print("The response of ActionsApi->actions_get_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **workflow_id** | [**ActionsGetWorkflowWorkflowIdParameter**](.md)| The ID of the workflow. You can also pass the workflow file name as a string. | 

### Return type

[**Workflow**](Workflow.md)

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

# **actions_get_workflow_access_to_repository**
> ActionsWorkflowAccessToRepository actions_get_workflow_access_to_repository(owner, repo)

Get the level of access for workflows outside of the repository

Gets the level of access that workflows outside of the repository have to actions and reusable workflows in the repository. This endpoint only applies to private repositories. For more information, see \"[Allowing access to components in a private repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#allowing-access-to-components-in-a-private-repository).\"  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_workflow_access_to_repository import ActionsWorkflowAccessToRepository
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get the level of access for workflows outside of the repository
        api_response = api_instance.actions_get_workflow_access_to_repository(owner, repo)
        print("The response of ActionsApi->actions_get_workflow_access_to_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_workflow_access_to_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**ActionsWorkflowAccessToRepository**](ActionsWorkflowAccessToRepository.md)

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

# **actions_get_workflow_run**
> WorkflowRun actions_get_workflow_run(owner, repo, run_id, exclude_pull_requests=exclude_pull_requests)

Get a workflow run

Gets a specific workflow run.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.workflow_run import WorkflowRun
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.
    exclude_pull_requests = False # bool | If `true` pull requests are omitted from the response (empty array). (optional) (default to False)

    try:
        # Get a workflow run
        api_response = api_instance.actions_get_workflow_run(owner, repo, run_id, exclude_pull_requests=exclude_pull_requests)
        print("The response of ActionsApi->actions_get_workflow_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_workflow_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 
 **exclude_pull_requests** | **bool**| If &#x60;true&#x60; pull requests are omitted from the response (empty array). | [optional] [default to False]

### Return type

[**WorkflowRun**](WorkflowRun.md)

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

# **actions_get_workflow_run_attempt**
> WorkflowRun actions_get_workflow_run_attempt(owner, repo, run_id, attempt_number, exclude_pull_requests=exclude_pull_requests)

Get a workflow run attempt

Gets a specific workflow run attempt.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.workflow_run import WorkflowRun
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.
    attempt_number = 56 # int | The attempt number of the workflow run.
    exclude_pull_requests = False # bool | If `true` pull requests are omitted from the response (empty array). (optional) (default to False)

    try:
        # Get a workflow run attempt
        api_response = api_instance.actions_get_workflow_run_attempt(owner, repo, run_id, attempt_number, exclude_pull_requests=exclude_pull_requests)
        print("The response of ActionsApi->actions_get_workflow_run_attempt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_workflow_run_attempt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 
 **attempt_number** | **int**| The attempt number of the workflow run. | 
 **exclude_pull_requests** | **bool**| If &#x60;true&#x60; pull requests are omitted from the response (empty array). | [optional] [default to False]

### Return type

[**WorkflowRun**](WorkflowRun.md)

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

# **actions_get_workflow_run_usage**
> WorkflowRunUsage actions_get_workflow_run_usage(owner, repo, run_id)

Get workflow run usage

Gets the number of billable minutes and total run time for a specific workflow run. Billable minutes only apply to workflows in private repositories that use GitHub-hosted runners. Usage is listed for each GitHub-hosted runner operating system in milliseconds. Any job re-runs are also included in the usage. The usage does not include the multiplier for macOS and Windows runners and is not rounded up to the nearest whole minute. For more information, see \"[Managing billing for GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)\".  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.workflow_run_usage import WorkflowRunUsage
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.

    try:
        # Get workflow run usage
        api_response = api_instance.actions_get_workflow_run_usage(owner, repo, run_id)
        print("The response of ActionsApi->actions_get_workflow_run_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_workflow_run_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 

### Return type

[**WorkflowRunUsage**](WorkflowRunUsage.md)

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

# **actions_get_workflow_usage**
> WorkflowUsage actions_get_workflow_usage(owner, repo, workflow_id)

Get workflow usage

Gets the number of billable minutes used by a specific workflow during the current billing cycle. Billable minutes only apply to workflows in private repositories that use GitHub-hosted runners. Usage is listed for each GitHub-hosted runner operating system in milliseconds. Any job re-runs are also included in the usage. The usage does not include the multiplier for macOS and Windows runners and is not rounded up to the nearest whole minute. For more information, see \"[Managing billing for GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)\".  You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.workflow_usage import WorkflowUsage
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    workflow_id = github_openapi.ActionsGetWorkflowWorkflowIdParameter() # ActionsGetWorkflowWorkflowIdParameter | The ID of the workflow. You can also pass the workflow file name as a string.

    try:
        # Get workflow usage
        api_response = api_instance.actions_get_workflow_usage(owner, repo, workflow_id)
        print("The response of ActionsApi->actions_get_workflow_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_get_workflow_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **workflow_id** | [**ActionsGetWorkflowWorkflowIdParameter**](.md)| The ID of the workflow. You can also pass the workflow file name as a string. | 

### Return type

[**WorkflowUsage**](WorkflowUsage.md)

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

# **actions_list_artifacts_for_repo**
> ActionsListArtifactsForRepo200Response actions_list_artifacts_for_repo(owner, repo, per_page=per_page, page=page, name=name)

List artifacts for a repository

Lists all artifacts for a repository.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_artifacts_for_repo200_response import ActionsListArtifactsForRepo200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    name = 'name_example' # str | The name field of an artifact. When specified, only artifacts with this name will be returned. (optional)

    try:
        # List artifacts for a repository
        api_response = api_instance.actions_list_artifacts_for_repo(owner, repo, per_page=per_page, page=page, name=name)
        print("The response of ActionsApi->actions_list_artifacts_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_artifacts_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **name** | **str**| The name field of an artifact. When specified, only artifacts with this name will be returned. | [optional] 

### Return type

[**ActionsListArtifactsForRepo200Response**](ActionsListArtifactsForRepo200Response.md)

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

# **actions_list_environment_secrets**
> ActionsListRepoOrganizationSecrets200Response actions_list_environment_secrets(owner, repo, environment_name, per_page=per_page, page=page)

List environment secrets

Lists all secrets available in an environment without revealing their encrypted values.  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_repo_organization_secrets200_response import ActionsListRepoOrganizationSecrets200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List environment secrets
        api_response = api_instance.actions_list_environment_secrets(owner, repo, environment_name, per_page=per_page, page=page)
        print("The response of ActionsApi->actions_list_environment_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_environment_secrets: %s\n" % e)
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

[**ActionsListRepoOrganizationSecrets200Response**](ActionsListRepoOrganizationSecrets200Response.md)

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

# **actions_list_environment_variables**
> ActionsListRepoOrganizationVariables200Response actions_list_environment_variables(owner, repo, environment_name, per_page=per_page, page=page)

List environment variables

Lists all environment variables.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_repo_organization_variables200_response import ActionsListRepoOrganizationVariables200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    per_page = 10 # int | The number of results per page (max 30). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 10)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List environment variables
        api_response = api_instance.actions_list_environment_variables(owner, repo, environment_name, per_page=per_page, page=page)
        print("The response of ActionsApi->actions_list_environment_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_environment_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **per_page** | **int**| The number of results per page (max 30). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 10]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActionsListRepoOrganizationVariables200Response**](ActionsListRepoOrganizationVariables200Response.md)

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

# **actions_list_jobs_for_workflow_run**
> ActionsListJobsForWorkflowRunAttempt200Response actions_list_jobs_for_workflow_run(owner, repo, run_id, filter=filter, per_page=per_page, page=page)

List jobs for a workflow run

Lists jobs for a workflow run. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#parameters).  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_jobs_for_workflow_run_attempt200_response import ActionsListJobsForWorkflowRunAttempt200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.
    filter = latest # str | Filters jobs by their `completed_at` timestamp. `latest` returns jobs from the most recent execution of the workflow run. `all` returns all jobs for a workflow run, including from old executions of the workflow run. (optional) (default to latest)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List jobs for a workflow run
        api_response = api_instance.actions_list_jobs_for_workflow_run(owner, repo, run_id, filter=filter, per_page=per_page, page=page)
        print("The response of ActionsApi->actions_list_jobs_for_workflow_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_jobs_for_workflow_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 
 **filter** | **str**| Filters jobs by their &#x60;completed_at&#x60; timestamp. &#x60;latest&#x60; returns jobs from the most recent execution of the workflow run. &#x60;all&#x60; returns all jobs for a workflow run, including from old executions of the workflow run. | [optional] [default to latest]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActionsListJobsForWorkflowRunAttempt200Response**](ActionsListJobsForWorkflowRunAttempt200Response.md)

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

# **actions_list_jobs_for_workflow_run_attempt**
> ActionsListJobsForWorkflowRunAttempt200Response actions_list_jobs_for_workflow_run_attempt(owner, repo, run_id, attempt_number, per_page=per_page, page=page)

List jobs for a workflow run attempt

Lists jobs for a specific workflow run attempt. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#parameters).  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint  with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_jobs_for_workflow_run_attempt200_response import ActionsListJobsForWorkflowRunAttempt200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.
    attempt_number = 56 # int | The attempt number of the workflow run.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List jobs for a workflow run attempt
        api_response = api_instance.actions_list_jobs_for_workflow_run_attempt(owner, repo, run_id, attempt_number, per_page=per_page, page=page)
        print("The response of ActionsApi->actions_list_jobs_for_workflow_run_attempt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_jobs_for_workflow_run_attempt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 
 **attempt_number** | **int**| The attempt number of the workflow run. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActionsListJobsForWorkflowRunAttempt200Response**](ActionsListJobsForWorkflowRunAttempt200Response.md)

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

# **actions_list_labels_for_self_hosted_runner_for_org**
> ActionsListLabelsForSelfHostedRunnerForOrg200Response actions_list_labels_for_self_hosted_runner_for_org(org, runner_id)

List labels for a self-hosted runner for an organization

Lists all labels for a self-hosted runner configured in an organization.  Authenticated users must have admin access to the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_labels_for_self_hosted_runner_for_org200_response import ActionsListLabelsForSelfHostedRunnerForOrg200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_id = 56 # int | Unique identifier of the self-hosted runner.

    try:
        # List labels for a self-hosted runner for an organization
        api_response = api_instance.actions_list_labels_for_self_hosted_runner_for_org(org, runner_id)
        print("The response of ActionsApi->actions_list_labels_for_self_hosted_runner_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_labels_for_self_hosted_runner_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_id** | **int**| Unique identifier of the self-hosted runner. | 

### Return type

[**ActionsListLabelsForSelfHostedRunnerForOrg200Response**](ActionsListLabelsForSelfHostedRunnerForOrg200Response.md)

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

# **actions_list_labels_for_self_hosted_runner_for_repo**
> ActionsListLabelsForSelfHostedRunnerForOrg200Response actions_list_labels_for_self_hosted_runner_for_repo(owner, repo, runner_id)

List labels for a self-hosted runner for a repository

Lists all labels for a self-hosted runner configured in a repository.  Authenticated users must have admin access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_labels_for_self_hosted_runner_for_org200_response import ActionsListLabelsForSelfHostedRunnerForOrg200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    runner_id = 56 # int | Unique identifier of the self-hosted runner.

    try:
        # List labels for a self-hosted runner for a repository
        api_response = api_instance.actions_list_labels_for_self_hosted_runner_for_repo(owner, repo, runner_id)
        print("The response of ActionsApi->actions_list_labels_for_self_hosted_runner_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_labels_for_self_hosted_runner_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **runner_id** | **int**| Unique identifier of the self-hosted runner. | 

### Return type

[**ActionsListLabelsForSelfHostedRunnerForOrg200Response**](ActionsListLabelsForSelfHostedRunnerForOrg200Response.md)

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

# **actions_list_org_secrets**
> ActionsListOrgSecrets200Response actions_list_org_secrets(org, per_page=per_page, page=page)

List organization secrets

Lists all secrets available in an organization without revealing their encrypted values.  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_org_secrets200_response import ActionsListOrgSecrets200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List organization secrets
        api_response = api_instance.actions_list_org_secrets(org, per_page=per_page, page=page)
        print("The response of ActionsApi->actions_list_org_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_org_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActionsListOrgSecrets200Response**](ActionsListOrgSecrets200Response.md)

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

# **actions_list_org_variables**
> ActionsListOrgVariables200Response actions_list_org_variables(org, per_page=per_page, page=page)

List organization variables

Lists all organization variables.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_org_variables200_response import ActionsListOrgVariables200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 10 # int | The number of results per page (max 30). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 10)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List organization variables
        api_response = api_instance.actions_list_org_variables(org, per_page=per_page, page=page)
        print("The response of ActionsApi->actions_list_org_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_org_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 30). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 10]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActionsListOrgVariables200Response**](ActionsListOrgVariables200Response.md)

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

# **actions_list_repo_access_to_self_hosted_runner_group_in_org**
> ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response actions_list_repo_access_to_self_hosted_runner_group_in_org(org, runner_group_id, page=page, per_page=per_page)

List repository access to a self-hosted runner group in an organization

Lists the repositories with access to a self-hosted runner group configured in an organization.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_repo_access_to_self_hosted_runner_group_in_org200_response import ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_group_id = 56 # int | Unique identifier of the self-hosted runner group.
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # List repository access to a self-hosted runner group in an organization
        api_response = api_instance.actions_list_repo_access_to_self_hosted_runner_group_in_org(org, runner_group_id, page=page, per_page=per_page)
        print("The response of ActionsApi->actions_list_repo_access_to_self_hosted_runner_group_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_repo_access_to_self_hosted_runner_group_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_group_id** | **int**| Unique identifier of the self-hosted runner group. | 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]

### Return type

[**ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response**](ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response.md)

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

# **actions_list_repo_organization_secrets**
> ActionsListRepoOrganizationSecrets200Response actions_list_repo_organization_secrets(owner, repo, per_page=per_page, page=page)

List repository organization secrets

Lists all organization secrets shared with a repository without revealing their encrypted values.  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_repo_organization_secrets200_response import ActionsListRepoOrganizationSecrets200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository organization secrets
        api_response = api_instance.actions_list_repo_organization_secrets(owner, repo, per_page=per_page, page=page)
        print("The response of ActionsApi->actions_list_repo_organization_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_repo_organization_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActionsListRepoOrganizationSecrets200Response**](ActionsListRepoOrganizationSecrets200Response.md)

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

# **actions_list_repo_organization_variables**
> ActionsListRepoOrganizationVariables200Response actions_list_repo_organization_variables(owner, repo, per_page=per_page, page=page)

List repository organization variables

Lists all organization variables shared with a repository.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_repo_organization_variables200_response import ActionsListRepoOrganizationVariables200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 10 # int | The number of results per page (max 30). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 10)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository organization variables
        api_response = api_instance.actions_list_repo_organization_variables(owner, repo, per_page=per_page, page=page)
        print("The response of ActionsApi->actions_list_repo_organization_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_repo_organization_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 30). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 10]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActionsListRepoOrganizationVariables200Response**](ActionsListRepoOrganizationVariables200Response.md)

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

# **actions_list_repo_secrets**
> ActionsListRepoOrganizationSecrets200Response actions_list_repo_secrets(owner, repo, per_page=per_page, page=page)

List repository secrets

Lists all secrets available in a repository without revealing their encrypted values.  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_repo_organization_secrets200_response import ActionsListRepoOrganizationSecrets200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository secrets
        api_response = api_instance.actions_list_repo_secrets(owner, repo, per_page=per_page, page=page)
        print("The response of ActionsApi->actions_list_repo_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_repo_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActionsListRepoOrganizationSecrets200Response**](ActionsListRepoOrganizationSecrets200Response.md)

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

# **actions_list_repo_variables**
> ActionsListRepoOrganizationVariables200Response actions_list_repo_variables(owner, repo, per_page=per_page, page=page)

List repository variables

Lists all repository variables.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_repo_organization_variables200_response import ActionsListRepoOrganizationVariables200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 10 # int | The number of results per page (max 30). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 10)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository variables
        api_response = api_instance.actions_list_repo_variables(owner, repo, per_page=per_page, page=page)
        print("The response of ActionsApi->actions_list_repo_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_repo_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 30). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 10]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActionsListRepoOrganizationVariables200Response**](ActionsListRepoOrganizationVariables200Response.md)

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

# **actions_list_repo_workflows**
> ActionsListRepoWorkflows200Response actions_list_repo_workflows(owner, repo, per_page=per_page, page=page)

List repository workflows

Lists the workflows in a repository.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_repo_workflows200_response import ActionsListRepoWorkflows200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository workflows
        api_response = api_instance.actions_list_repo_workflows(owner, repo, per_page=per_page, page=page)
        print("The response of ActionsApi->actions_list_repo_workflows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_repo_workflows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActionsListRepoWorkflows200Response**](ActionsListRepoWorkflows200Response.md)

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

# **actions_list_runner_applications_for_org**
> List[RunnerApplication] actions_list_runner_applications_for_org(org)

List runner applications for an organization

Lists binaries for the runner application that you can download and run.  Authenticated users must have admin access to the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.  If the repository is private, the `repo` scope is also required.

### Example


```python
import github_openapi
from github_openapi.models.runner_application import RunnerApplication
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # List runner applications for an organization
        api_response = api_instance.actions_list_runner_applications_for_org(org)
        print("The response of ActionsApi->actions_list_runner_applications_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_runner_applications_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**List[RunnerApplication]**](RunnerApplication.md)

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

# **actions_list_runner_applications_for_repo**
> List[RunnerApplication] actions_list_runner_applications_for_repo(owner, repo)

List runner applications for a repository

Lists binaries for the runner application that you can download and run.  Authenticated users must have admin access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.runner_application import RunnerApplication
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # List runner applications for a repository
        api_response = api_instance.actions_list_runner_applications_for_repo(owner, repo)
        print("The response of ActionsApi->actions_list_runner_applications_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_runner_applications_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**List[RunnerApplication]**](RunnerApplication.md)

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

# **actions_list_selected_repos_for_org_secret**
> ActionsListSelectedReposForOrgSecret200Response actions_list_selected_repos_for_org_secret(org, secret_name, page=page, per_page=per_page)

List selected repositories for an organization secret

Lists all repositories that have been selected when the `visibility` for repository access to a secret is set to `selected`.  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_selected_repos_for_org_secret200_response import ActionsListSelectedReposForOrgSecret200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # List selected repositories for an organization secret
        api_response = api_instance.actions_list_selected_repos_for_org_secret(org, secret_name, page=page, per_page=per_page)
        print("The response of ActionsApi->actions_list_selected_repos_for_org_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_selected_repos_for_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]

### Return type

[**ActionsListSelectedReposForOrgSecret200Response**](ActionsListSelectedReposForOrgSecret200Response.md)

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

# **actions_list_selected_repos_for_org_variable**
> ActionsListSelectedReposForOrgSecret200Response actions_list_selected_repos_for_org_variable(org, name, page=page, per_page=per_page)

List selected repositories for an organization variable

Lists all repositories that can access an organization variable that is available to selected repositories.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_selected_repos_for_org_secret200_response import ActionsListSelectedReposForOrgSecret200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    name = 'name_example' # str | The name of the variable.
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # List selected repositories for an organization variable
        api_response = api_instance.actions_list_selected_repos_for_org_variable(org, name, page=page, per_page=per_page)
        print("The response of ActionsApi->actions_list_selected_repos_for_org_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_selected_repos_for_org_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **name** | **str**| The name of the variable. | 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]

### Return type

[**ActionsListSelectedReposForOrgSecret200Response**](ActionsListSelectedReposForOrgSecret200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**409** | Response when the visibility of the variable is not set to &#x60;selected&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_list_selected_repositories_enabled_github_actions_organization**
> ActionsListSelectedRepositoriesEnabledGithubActionsOrganization200Response actions_list_selected_repositories_enabled_github_actions_organization(org, per_page=per_page, page=page)

List selected repositories enabled for GitHub Actions in an organization

Lists the selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be configured to `selected`. For more information, see \"[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization).\"  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_selected_repositories_enabled_github_actions_organization200_response import ActionsListSelectedRepositoriesEnabledGithubActionsOrganization200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List selected repositories enabled for GitHub Actions in an organization
        api_response = api_instance.actions_list_selected_repositories_enabled_github_actions_organization(org, per_page=per_page, page=page)
        print("The response of ActionsApi->actions_list_selected_repositories_enabled_github_actions_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_selected_repositories_enabled_github_actions_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActionsListSelectedRepositoriesEnabledGithubActionsOrganization200Response**](ActionsListSelectedRepositoriesEnabledGithubActionsOrganization200Response.md)

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

# **actions_list_self_hosted_runner_groups_for_org**
> ActionsListSelfHostedRunnerGroupsForOrg200Response actions_list_self_hosted_runner_groups_for_org(org, per_page=per_page, page=page, visible_to_repository=visible_to_repository)

List self-hosted runner groups for an organization

Lists all self-hosted runner groups configured in an organization and inherited from an enterprise.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_self_hosted_runner_groups_for_org200_response import ActionsListSelfHostedRunnerGroupsForOrg200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    visible_to_repository = 'visible_to_repository_example' # str | Only return runner groups that are allowed to be used by this repository. (optional)

    try:
        # List self-hosted runner groups for an organization
        api_response = api_instance.actions_list_self_hosted_runner_groups_for_org(org, per_page=per_page, page=page, visible_to_repository=visible_to_repository)
        print("The response of ActionsApi->actions_list_self_hosted_runner_groups_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_self_hosted_runner_groups_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **visible_to_repository** | **str**| Only return runner groups that are allowed to be used by this repository. | [optional] 

### Return type

[**ActionsListSelfHostedRunnerGroupsForOrg200Response**](ActionsListSelfHostedRunnerGroupsForOrg200Response.md)

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

# **actions_list_self_hosted_runners_for_org**
> ActionsListSelfHostedRunnersForOrg200Response actions_list_self_hosted_runners_for_org(org, name=name, per_page=per_page, page=page)

List self-hosted runners for an organization

Lists all self-hosted runners configured in an organization.  Authenticated users must have admin access to the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_self_hosted_runners_for_org200_response import ActionsListSelfHostedRunnersForOrg200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    name = 'name_example' # str | The name of a self-hosted runner. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List self-hosted runners for an organization
        api_response = api_instance.actions_list_self_hosted_runners_for_org(org, name=name, per_page=per_page, page=page)
        print("The response of ActionsApi->actions_list_self_hosted_runners_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_self_hosted_runners_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **name** | **str**| The name of a self-hosted runner. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActionsListSelfHostedRunnersForOrg200Response**](ActionsListSelfHostedRunnersForOrg200Response.md)

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

# **actions_list_self_hosted_runners_for_repo**
> ActionsListSelfHostedRunnersForOrg200Response actions_list_self_hosted_runners_for_repo(owner, repo, name=name, per_page=per_page, page=page)

List self-hosted runners for a repository

Lists all self-hosted runners configured in a repository.  Authenticated users must have admin access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_self_hosted_runners_for_org200_response import ActionsListSelfHostedRunnersForOrg200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    name = 'name_example' # str | The name of a self-hosted runner. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List self-hosted runners for a repository
        api_response = api_instance.actions_list_self_hosted_runners_for_repo(owner, repo, name=name, per_page=per_page, page=page)
        print("The response of ActionsApi->actions_list_self_hosted_runners_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_self_hosted_runners_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **name** | **str**| The name of a self-hosted runner. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActionsListSelfHostedRunnersForOrg200Response**](ActionsListSelfHostedRunnersForOrg200Response.md)

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

# **actions_list_self_hosted_runners_in_group_for_org**
> ActionsListSelfHostedRunnersInGroupForOrg200Response actions_list_self_hosted_runners_in_group_for_org(org, runner_group_id, per_page=per_page, page=page)

List self-hosted runners in a group for an organization

Lists self-hosted runners that are in a specific organization group.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_self_hosted_runners_in_group_for_org200_response import ActionsListSelfHostedRunnersInGroupForOrg200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_group_id = 56 # int | Unique identifier of the self-hosted runner group.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List self-hosted runners in a group for an organization
        api_response = api_instance.actions_list_self_hosted_runners_in_group_for_org(org, runner_group_id, per_page=per_page, page=page)
        print("The response of ActionsApi->actions_list_self_hosted_runners_in_group_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_self_hosted_runners_in_group_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_group_id** | **int**| Unique identifier of the self-hosted runner group. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActionsListSelfHostedRunnersInGroupForOrg200Response**](ActionsListSelfHostedRunnersInGroupForOrg200Response.md)

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

# **actions_list_workflow_run_artifacts**
> ActionsListArtifactsForRepo200Response actions_list_workflow_run_artifacts(owner, repo, run_id, per_page=per_page, page=page, name=name)

List workflow run artifacts

Lists artifacts for a workflow run.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_artifacts_for_repo200_response import ActionsListArtifactsForRepo200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    name = 'name_example' # str | The name field of an artifact. When specified, only artifacts with this name will be returned. (optional)

    try:
        # List workflow run artifacts
        api_response = api_instance.actions_list_workflow_run_artifacts(owner, repo, run_id, per_page=per_page, page=page, name=name)
        print("The response of ActionsApi->actions_list_workflow_run_artifacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_workflow_run_artifacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **name** | **str**| The name field of an artifact. When specified, only artifacts with this name will be returned. | [optional] 

### Return type

[**ActionsListArtifactsForRepo200Response**](ActionsListArtifactsForRepo200Response.md)

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

# **actions_list_workflow_runs**
> ActionsListWorkflowRunsForRepo200Response actions_list_workflow_runs(owner, repo, workflow_id, actor=actor, branch=branch, event=event, status=status, per_page=per_page, page=page, created=created, exclude_pull_requests=exclude_pull_requests, check_suite_id=check_suite_id, head_sha=head_sha)

List workflow runs for a workflow

List all workflow runs for a workflow. You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#parameters).  Anyone with read access to the repository can use this endpoint  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.  This endpoint will return up to 1,000 results for each search when using the following parameters: `actor`, `branch`, `check_suite_id`, `created`, `event`, `head_sha`, `status`.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_workflow_runs_for_repo200_response import ActionsListWorkflowRunsForRepo200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    workflow_id = github_openapi.ActionsGetWorkflowWorkflowIdParameter() # ActionsGetWorkflowWorkflowIdParameter | The ID of the workflow. You can also pass the workflow file name as a string.
    actor = 'actor_example' # str | Returns someone's workflow runs. Use the login for the user who created the `push` associated with the check suite or workflow run. (optional)
    branch = 'branch_example' # str | Returns workflow runs associated with a branch. Use the name of the branch of the `push`. (optional)
    event = 'event_example' # str | Returns workflow run triggered by the event you specify. For example, `push`, `pull_request` or `issue`. For more information, see \"[Events that trigger workflows](https://docs.github.com/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows).\" (optional)
    status = 'status_example' # str | Returns workflow runs with the check run `status` or `conclusion` that you specify. For example, a conclusion can be `success` or a status can be `in_progress`. Only GitHub Actions can set a status of `waiting`, `pending`, or `requested`. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    created = '2013-10-20T19:20:30+01:00' # datetime | Returns workflow runs created within the given date-time range. For more information on the syntax, see \"[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates).\" (optional)
    exclude_pull_requests = False # bool | If `true` pull requests are omitted from the response (empty array). (optional) (default to False)
    check_suite_id = 56 # int | Returns workflow runs with the `check_suite_id` that you specify. (optional)
    head_sha = 'head_sha_example' # str | Only returns workflow runs that are associated with the specified `head_sha`. (optional)

    try:
        # List workflow runs for a workflow
        api_response = api_instance.actions_list_workflow_runs(owner, repo, workflow_id, actor=actor, branch=branch, event=event, status=status, per_page=per_page, page=page, created=created, exclude_pull_requests=exclude_pull_requests, check_suite_id=check_suite_id, head_sha=head_sha)
        print("The response of ActionsApi->actions_list_workflow_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_workflow_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **workflow_id** | [**ActionsGetWorkflowWorkflowIdParameter**](.md)| The ID of the workflow. You can also pass the workflow file name as a string. | 
 **actor** | **str**| Returns someone&#39;s workflow runs. Use the login for the user who created the &#x60;push&#x60; associated with the check suite or workflow run. | [optional] 
 **branch** | **str**| Returns workflow runs associated with a branch. Use the name of the branch of the &#x60;push&#x60;. | [optional] 
 **event** | **str**| Returns workflow run triggered by the event you specify. For example, &#x60;push&#x60;, &#x60;pull_request&#x60; or &#x60;issue&#x60;. For more information, see \&quot;[Events that trigger workflows](https://docs.github.com/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows).\&quot; | [optional] 
 **status** | **str**| Returns workflow runs with the check run &#x60;status&#x60; or &#x60;conclusion&#x60; that you specify. For example, a conclusion can be &#x60;success&#x60; or a status can be &#x60;in_progress&#x60;. Only GitHub Actions can set a status of &#x60;waiting&#x60;, &#x60;pending&#x60;, or &#x60;requested&#x60;. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **created** | **datetime**| Returns workflow runs created within the given date-time range. For more information on the syntax, see \&quot;[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates).\&quot; | [optional] 
 **exclude_pull_requests** | **bool**| If &#x60;true&#x60; pull requests are omitted from the response (empty array). | [optional] [default to False]
 **check_suite_id** | **int**| Returns workflow runs with the &#x60;check_suite_id&#x60; that you specify. | [optional] 
 **head_sha** | **str**| Only returns workflow runs that are associated with the specified &#x60;head_sha&#x60;. | [optional] 

### Return type

[**ActionsListWorkflowRunsForRepo200Response**](ActionsListWorkflowRunsForRepo200Response.md)

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

# **actions_list_workflow_runs_for_repo**
> ActionsListWorkflowRunsForRepo200Response actions_list_workflow_runs_for_repo(owner, repo, actor=actor, branch=branch, event=event, status=status, per_page=per_page, page=page, created=created, exclude_pull_requests=exclude_pull_requests, check_suite_id=check_suite_id, head_sha=head_sha)

List workflow runs for a repository

Lists all workflow runs for a repository. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#parameters).  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.  This endpoint will return up to 1,000 results for each search when using the following parameters: `actor`, `branch`, `check_suite_id`, `created`, `event`, `head_sha`, `status`.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_workflow_runs_for_repo200_response import ActionsListWorkflowRunsForRepo200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    actor = 'actor_example' # str | Returns someone's workflow runs. Use the login for the user who created the `push` associated with the check suite or workflow run. (optional)
    branch = 'branch_example' # str | Returns workflow runs associated with a branch. Use the name of the branch of the `push`. (optional)
    event = 'event_example' # str | Returns workflow run triggered by the event you specify. For example, `push`, `pull_request` or `issue`. For more information, see \"[Events that trigger workflows](https://docs.github.com/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows).\" (optional)
    status = 'status_example' # str | Returns workflow runs with the check run `status` or `conclusion` that you specify. For example, a conclusion can be `success` or a status can be `in_progress`. Only GitHub Actions can set a status of `waiting`, `pending`, or `requested`. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    created = '2013-10-20T19:20:30+01:00' # datetime | Returns workflow runs created within the given date-time range. For more information on the syntax, see \"[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates).\" (optional)
    exclude_pull_requests = False # bool | If `true` pull requests are omitted from the response (empty array). (optional) (default to False)
    check_suite_id = 56 # int | Returns workflow runs with the `check_suite_id` that you specify. (optional)
    head_sha = 'head_sha_example' # str | Only returns workflow runs that are associated with the specified `head_sha`. (optional)

    try:
        # List workflow runs for a repository
        api_response = api_instance.actions_list_workflow_runs_for_repo(owner, repo, actor=actor, branch=branch, event=event, status=status, per_page=per_page, page=page, created=created, exclude_pull_requests=exclude_pull_requests, check_suite_id=check_suite_id, head_sha=head_sha)
        print("The response of ActionsApi->actions_list_workflow_runs_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list_workflow_runs_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **actor** | **str**| Returns someone&#39;s workflow runs. Use the login for the user who created the &#x60;push&#x60; associated with the check suite or workflow run. | [optional] 
 **branch** | **str**| Returns workflow runs associated with a branch. Use the name of the branch of the &#x60;push&#x60;. | [optional] 
 **event** | **str**| Returns workflow run triggered by the event you specify. For example, &#x60;push&#x60;, &#x60;pull_request&#x60; or &#x60;issue&#x60;. For more information, see \&quot;[Events that trigger workflows](https://docs.github.com/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows).\&quot; | [optional] 
 **status** | **str**| Returns workflow runs with the check run &#x60;status&#x60; or &#x60;conclusion&#x60; that you specify. For example, a conclusion can be &#x60;success&#x60; or a status can be &#x60;in_progress&#x60;. Only GitHub Actions can set a status of &#x60;waiting&#x60;, &#x60;pending&#x60;, or &#x60;requested&#x60;. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **created** | **datetime**| Returns workflow runs created within the given date-time range. For more information on the syntax, see \&quot;[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates).\&quot; | [optional] 
 **exclude_pull_requests** | **bool**| If &#x60;true&#x60; pull requests are omitted from the response (empty array). | [optional] [default to False]
 **check_suite_id** | **int**| Returns workflow runs with the &#x60;check_suite_id&#x60; that you specify. | [optional] 
 **head_sha** | **str**| Only returns workflow runs that are associated with the specified &#x60;head_sha&#x60;. | [optional] 

### Return type

[**ActionsListWorkflowRunsForRepo200Response**](ActionsListWorkflowRunsForRepo200Response.md)

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

# **actions_re_run_job_for_workflow_run**
> object actions_re_run_job_for_workflow_run(owner, repo, job_id, actions_re_run_job_for_workflow_run_request=actions_re_run_job_for_workflow_run_request)

Re-run a job from a workflow run

Re-run a job and its dependent jobs in a workflow run.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_re_run_job_for_workflow_run_request import ActionsReRunJobForWorkflowRunRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    job_id = 56 # int | The unique identifier of the job.
    actions_re_run_job_for_workflow_run_request = github_openapi.ActionsReRunJobForWorkflowRunRequest() # ActionsReRunJobForWorkflowRunRequest |  (optional)

    try:
        # Re-run a job from a workflow run
        api_response = api_instance.actions_re_run_job_for_workflow_run(owner, repo, job_id, actions_re_run_job_for_workflow_run_request=actions_re_run_job_for_workflow_run_request)
        print("The response of ActionsApi->actions_re_run_job_for_workflow_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_re_run_job_for_workflow_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **job_id** | **int**| The unique identifier of the job. | 
 **actions_re_run_job_for_workflow_run_request** | [**ActionsReRunJobForWorkflowRunRequest**](ActionsReRunJobForWorkflowRunRequest.md)|  | [optional] 

### Return type

**object**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_re_run_workflow**
> object actions_re_run_workflow(owner, repo, run_id, actions_re_run_job_for_workflow_run_request=actions_re_run_job_for_workflow_run_request)

Re-run a workflow

Re-runs your workflow run using its `id`.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_re_run_job_for_workflow_run_request import ActionsReRunJobForWorkflowRunRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.
    actions_re_run_job_for_workflow_run_request = github_openapi.ActionsReRunJobForWorkflowRunRequest() # ActionsReRunJobForWorkflowRunRequest |  (optional)

    try:
        # Re-run a workflow
        api_response = api_instance.actions_re_run_workflow(owner, repo, run_id, actions_re_run_job_for_workflow_run_request=actions_re_run_job_for_workflow_run_request)
        print("The response of ActionsApi->actions_re_run_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_re_run_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 
 **actions_re_run_job_for_workflow_run_request** | [**ActionsReRunJobForWorkflowRunRequest**](ActionsReRunJobForWorkflowRunRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_re_run_workflow_failed_jobs**
> object actions_re_run_workflow_failed_jobs(owner, repo, run_id, actions_re_run_job_for_workflow_run_request=actions_re_run_job_for_workflow_run_request)

Re-run failed jobs from a workflow run

Re-run all of the failed jobs and their dependent jobs in a workflow run using the `id` of the workflow run.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_re_run_job_for_workflow_run_request import ActionsReRunJobForWorkflowRunRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.
    actions_re_run_job_for_workflow_run_request = github_openapi.ActionsReRunJobForWorkflowRunRequest() # ActionsReRunJobForWorkflowRunRequest |  (optional)

    try:
        # Re-run failed jobs from a workflow run
        api_response = api_instance.actions_re_run_workflow_failed_jobs(owner, repo, run_id, actions_re_run_job_for_workflow_run_request=actions_re_run_job_for_workflow_run_request)
        print("The response of ActionsApi->actions_re_run_workflow_failed_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_re_run_workflow_failed_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 
 **actions_re_run_job_for_workflow_run_request** | [**ActionsReRunJobForWorkflowRunRequest**](ActionsReRunJobForWorkflowRunRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_remove_all_custom_labels_from_self_hosted_runner_for_org**
> ActionsListLabelsForSelfHostedRunnerForOrg200Response actions_remove_all_custom_labels_from_self_hosted_runner_for_org(org, runner_id)

Remove all custom labels from a self-hosted runner for an organization

Remove all custom labels from a self-hosted runner configured in an organization. Returns the remaining read-only labels from the runner.  Authenticated users must have admin access to the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_labels_for_self_hosted_runner_for_org200_response import ActionsListLabelsForSelfHostedRunnerForOrg200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_id = 56 # int | Unique identifier of the self-hosted runner.

    try:
        # Remove all custom labels from a self-hosted runner for an organization
        api_response = api_instance.actions_remove_all_custom_labels_from_self_hosted_runner_for_org(org, runner_id)
        print("The response of ActionsApi->actions_remove_all_custom_labels_from_self_hosted_runner_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_remove_all_custom_labels_from_self_hosted_runner_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_id** | **int**| Unique identifier of the self-hosted runner. | 

### Return type

[**ActionsListLabelsForSelfHostedRunnerForOrg200Response**](ActionsListLabelsForSelfHostedRunnerForOrg200Response.md)

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

# **actions_remove_all_custom_labels_from_self_hosted_runner_for_repo**
> ActionsListLabelsForSelfHostedRunnerForOrg200Response actions_remove_all_custom_labels_from_self_hosted_runner_for_repo(owner, repo, runner_id)

Remove all custom labels from a self-hosted runner for a repository

Remove all custom labels from a self-hosted runner configured in a repository. Returns the remaining read-only labels from the runner.  Authenticated users must have admin access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_labels_for_self_hosted_runner_for_org200_response import ActionsListLabelsForSelfHostedRunnerForOrg200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    runner_id = 56 # int | Unique identifier of the self-hosted runner.

    try:
        # Remove all custom labels from a self-hosted runner for a repository
        api_response = api_instance.actions_remove_all_custom_labels_from_self_hosted_runner_for_repo(owner, repo, runner_id)
        print("The response of ActionsApi->actions_remove_all_custom_labels_from_self_hosted_runner_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_remove_all_custom_labels_from_self_hosted_runner_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **runner_id** | **int**| Unique identifier of the self-hosted runner. | 

### Return type

[**ActionsListLabelsForSelfHostedRunnerForOrg200Response**](ActionsListLabelsForSelfHostedRunnerForOrg200Response.md)

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

# **actions_remove_custom_label_from_self_hosted_runner_for_org**
> ActionsListLabelsForSelfHostedRunnerForOrg200Response actions_remove_custom_label_from_self_hosted_runner_for_org(org, runner_id, name)

Remove a custom label from a self-hosted runner for an organization

Remove a custom label from a self-hosted runner configured in an organization. Returns the remaining labels from the runner.  This endpoint returns a `404 Not Found` status if the custom label is not present on the runner.  Authenticated users must have admin access to the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_labels_for_self_hosted_runner_for_org200_response import ActionsListLabelsForSelfHostedRunnerForOrg200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_id = 56 # int | Unique identifier of the self-hosted runner.
    name = 'name_example' # str | The name of a self-hosted runner's custom label.

    try:
        # Remove a custom label from a self-hosted runner for an organization
        api_response = api_instance.actions_remove_custom_label_from_self_hosted_runner_for_org(org, runner_id, name)
        print("The response of ActionsApi->actions_remove_custom_label_from_self_hosted_runner_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_remove_custom_label_from_self_hosted_runner_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_id** | **int**| Unique identifier of the self-hosted runner. | 
 **name** | **str**| The name of a self-hosted runner&#39;s custom label. | 

### Return type

[**ActionsListLabelsForSelfHostedRunnerForOrg200Response**](ActionsListLabelsForSelfHostedRunnerForOrg200Response.md)

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

# **actions_remove_custom_label_from_self_hosted_runner_for_repo**
> ActionsListLabelsForSelfHostedRunnerForOrg200Response actions_remove_custom_label_from_self_hosted_runner_for_repo(owner, repo, runner_id, name)

Remove a custom label from a self-hosted runner for a repository

Remove a custom label from a self-hosted runner configured in a repository. Returns the remaining labels from the runner.  This endpoint returns a `404 Not Found` status if the custom label is not present on the runner.  Authenticated users must have admin access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_labels_for_self_hosted_runner_for_org200_response import ActionsListLabelsForSelfHostedRunnerForOrg200Response
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    runner_id = 56 # int | Unique identifier of the self-hosted runner.
    name = 'name_example' # str | The name of a self-hosted runner's custom label.

    try:
        # Remove a custom label from a self-hosted runner for a repository
        api_response = api_instance.actions_remove_custom_label_from_self_hosted_runner_for_repo(owner, repo, runner_id, name)
        print("The response of ActionsApi->actions_remove_custom_label_from_self_hosted_runner_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_remove_custom_label_from_self_hosted_runner_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **runner_id** | **int**| Unique identifier of the self-hosted runner. | 
 **name** | **str**| The name of a self-hosted runner&#39;s custom label. | 

### Return type

[**ActionsListLabelsForSelfHostedRunnerForOrg200Response**](ActionsListLabelsForSelfHostedRunnerForOrg200Response.md)

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

# **actions_remove_repo_access_to_self_hosted_runner_group_in_org**
> actions_remove_repo_access_to_self_hosted_runner_group_in_org(org, runner_group_id, repository_id)

Remove repository access to a self-hosted runner group in an organization

Removes a repository from the list of selected repositories that can access a self-hosted runner group. The runner group must have `visibility` set to `selected`. For more information, see \"[Create a self-hosted runner group for an organization](#create-a-self-hosted-runner-group-for-an-organization).\"  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_group_id = 56 # int | Unique identifier of the self-hosted runner group.
    repository_id = 56 # int | The unique identifier of the repository.

    try:
        # Remove repository access to a self-hosted runner group in an organization
        api_instance.actions_remove_repo_access_to_self_hosted_runner_group_in_org(org, runner_group_id, repository_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_remove_repo_access_to_self_hosted_runner_group_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_group_id** | **int**| Unique identifier of the self-hosted runner group. | 
 **repository_id** | **int**| The unique identifier of the repository. | 

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

# **actions_remove_selected_repo_from_org_secret**
> actions_remove_selected_repo_from_org_secret(org, secret_name, repository_id)

Remove selected repository from an organization secret

Removes a repository from an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/actions/secrets#create-or-update-an-organization-secret).  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.

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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    repository_id = 56 # int | 

    try:
        # Remove selected repository from an organization secret
        api_instance.actions_remove_selected_repo_from_org_secret(org, secret_name, repository_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_remove_selected_repo_from_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 
 **repository_id** | **int**|  | 

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
**204** | Response when repository was removed from the selected list |  -  |
**409** | Conflict when visibility type not set to selected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_remove_selected_repo_from_org_variable**
> actions_remove_selected_repo_from_org_variable(org, name, repository_id)

Remove selected repository from an organization variable

Removes a repository from an organization variable that is available to selected repositories. Organization variables that are available to selected repositories have their `visibility` field set to `selected`.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.

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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    name = 'name_example' # str | The name of the variable.
    repository_id = 56 # int | 

    try:
        # Remove selected repository from an organization variable
        api_instance.actions_remove_selected_repo_from_org_variable(org, name, repository_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_remove_selected_repo_from_org_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **name** | **str**| The name of the variable. | 
 **repository_id** | **int**|  | 

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
**409** | Response when the visibility of the variable is not set to &#x60;selected&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_remove_self_hosted_runner_from_group_for_org**
> actions_remove_self_hosted_runner_from_group_for_org(org, runner_group_id, runner_id)

Remove a self-hosted runner from a group for an organization

Removes a self-hosted runner from a group configured in an organization. The runner is then returned to the default group.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_group_id = 56 # int | Unique identifier of the self-hosted runner group.
    runner_id = 56 # int | Unique identifier of the self-hosted runner.

    try:
        # Remove a self-hosted runner from a group for an organization
        api_instance.actions_remove_self_hosted_runner_from_group_for_org(org, runner_group_id, runner_id)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_remove_self_hosted_runner_from_group_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_group_id** | **int**| Unique identifier of the self-hosted runner group. | 
 **runner_id** | **int**| Unique identifier of the self-hosted runner. | 

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

# **actions_review_custom_gates_for_run**
> actions_review_custom_gates_for_run(owner, repo, run_id, actions_review_custom_gates_for_run_request)

Review custom deployment protection rules for a workflow run

Approve or reject custom deployment protection rules provided by a GitHub App for a workflow run. For more information, see \"[Using environments for deployment](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment).\"  > [!NOTE] > GitHub Apps can only review their own custom deployment protection rules. To approve or reject pending deployments that are waiting for review from a specific person or team, see [`POST /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments`](/rest/actions/workflow-runs#review-pending-deployments-for-a-workflow-run).  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.

### Example


```python
import github_openapi
from github_openapi.models.actions_review_custom_gates_for_run_request import ActionsReviewCustomGatesForRunRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.
    actions_review_custom_gates_for_run_request = {"environment_name":"prod-eus","state":"approved","comment":"All health checks passed."} # ActionsReviewCustomGatesForRunRequest | 

    try:
        # Review custom deployment protection rules for a workflow run
        api_instance.actions_review_custom_gates_for_run(owner, repo, run_id, actions_review_custom_gates_for_run_request)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_review_custom_gates_for_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 
 **actions_review_custom_gates_for_run_request** | [**ActionsReviewCustomGatesForRunRequest**](ActionsReviewCustomGatesForRunRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_review_pending_deployments_for_run**
> List[Deployment] actions_review_pending_deployments_for_run(owner, repo, run_id, actions_review_pending_deployments_for_run_request)

Review pending deployments for a workflow run

Approve or reject pending deployments that are waiting on approval by a required reviewer.  Required reviewers with read access to the repository contents and deployments can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_review_pending_deployments_for_run_request import ActionsReviewPendingDeploymentsForRunRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    run_id = 56 # int | The unique identifier of the workflow run.
    actions_review_pending_deployments_for_run_request = {"environment_ids":[161171787],"state":"approved","comment":"Ship it!"} # ActionsReviewPendingDeploymentsForRunRequest | 

    try:
        # Review pending deployments for a workflow run
        api_response = api_instance.actions_review_pending_deployments_for_run(owner, repo, run_id, actions_review_pending_deployments_for_run_request)
        print("The response of ActionsApi->actions_review_pending_deployments_for_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_review_pending_deployments_for_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **run_id** | **int**| The unique identifier of the workflow run. | 
 **actions_review_pending_deployments_for_run_request** | [**ActionsReviewPendingDeploymentsForRunRequest**](ActionsReviewPendingDeploymentsForRunRequest.md)|  | 

### Return type

[**List[Deployment]**](Deployment.md)

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

# **actions_set_allowed_actions_organization**
> actions_set_allowed_actions_organization(org, selected_actions=selected_actions)

Set allowed actions and reusable workflows for an organization

Sets the actions and reusable workflows that are allowed in an organization. To use this endpoint, the organization permission policy for `allowed_actions` must be configured to `selected`. For more information, see \"[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization).\"  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.selected_actions import SelectedActions
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    selected_actions = github_openapi.SelectedActions() # SelectedActions |  (optional)

    try:
        # Set allowed actions and reusable workflows for an organization
        api_instance.actions_set_allowed_actions_organization(org, selected_actions=selected_actions)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_set_allowed_actions_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **selected_actions** | [**SelectedActions**](SelectedActions.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_set_allowed_actions_repository**
> actions_set_allowed_actions_repository(owner, repo, selected_actions=selected_actions)

Set allowed actions and reusable workflows for a repository

Sets the actions and reusable workflows that are allowed in a repository. To use this endpoint, the repository permission policy for `allowed_actions` must be configured to `selected`. For more information, see \"[Set GitHub Actions permissions for a repository](#set-github-actions-permissions-for-a-repository).\"  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.selected_actions import SelectedActions
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    selected_actions = github_openapi.SelectedActions() # SelectedActions |  (optional)

    try:
        # Set allowed actions and reusable workflows for a repository
        api_instance.actions_set_allowed_actions_repository(owner, repo, selected_actions=selected_actions)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_set_allowed_actions_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **selected_actions** | [**SelectedActions**](SelectedActions.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_set_custom_labels_for_self_hosted_runner_for_org**
> ActionsListLabelsForSelfHostedRunnerForOrg200Response actions_set_custom_labels_for_self_hosted_runner_for_org(org, runner_id, actions_set_custom_labels_for_self_hosted_runner_for_org_request)

Set custom labels for a self-hosted runner for an organization

Remove all previous custom labels and set the new custom labels for a specific self-hosted runner configured in an organization.  Authenticated users must have admin access to the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_labels_for_self_hosted_runner_for_org200_response import ActionsListLabelsForSelfHostedRunnerForOrg200Response
from github_openapi.models.actions_set_custom_labels_for_self_hosted_runner_for_org_request import ActionsSetCustomLabelsForSelfHostedRunnerForOrgRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_id = 56 # int | Unique identifier of the self-hosted runner.
    actions_set_custom_labels_for_self_hosted_runner_for_org_request = {"labels":["gpu","accelerated"]} # ActionsSetCustomLabelsForSelfHostedRunnerForOrgRequest | 

    try:
        # Set custom labels for a self-hosted runner for an organization
        api_response = api_instance.actions_set_custom_labels_for_self_hosted_runner_for_org(org, runner_id, actions_set_custom_labels_for_self_hosted_runner_for_org_request)
        print("The response of ActionsApi->actions_set_custom_labels_for_self_hosted_runner_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_set_custom_labels_for_self_hosted_runner_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_id** | **int**| Unique identifier of the self-hosted runner. | 
 **actions_set_custom_labels_for_self_hosted_runner_for_org_request** | [**ActionsSetCustomLabelsForSelfHostedRunnerForOrgRequest**](ActionsSetCustomLabelsForSelfHostedRunnerForOrgRequest.md)|  | 

### Return type

[**ActionsListLabelsForSelfHostedRunnerForOrg200Response**](ActionsListLabelsForSelfHostedRunnerForOrg200Response.md)

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

# **actions_set_custom_labels_for_self_hosted_runner_for_repo**
> ActionsListLabelsForSelfHostedRunnerForOrg200Response actions_set_custom_labels_for_self_hosted_runner_for_repo(owner, repo, runner_id, actions_set_custom_labels_for_self_hosted_runner_for_org_request)

Set custom labels for a self-hosted runner for a repository

Remove all previous custom labels and set the new custom labels for a specific self-hosted runner configured in a repository.  Authenticated users must have admin access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_labels_for_self_hosted_runner_for_org200_response import ActionsListLabelsForSelfHostedRunnerForOrg200Response
from github_openapi.models.actions_set_custom_labels_for_self_hosted_runner_for_org_request import ActionsSetCustomLabelsForSelfHostedRunnerForOrgRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    runner_id = 56 # int | Unique identifier of the self-hosted runner.
    actions_set_custom_labels_for_self_hosted_runner_for_org_request = {"labels":["gpu","accelerated"]} # ActionsSetCustomLabelsForSelfHostedRunnerForOrgRequest | 

    try:
        # Set custom labels for a self-hosted runner for a repository
        api_response = api_instance.actions_set_custom_labels_for_self_hosted_runner_for_repo(owner, repo, runner_id, actions_set_custom_labels_for_self_hosted_runner_for_org_request)
        print("The response of ActionsApi->actions_set_custom_labels_for_self_hosted_runner_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_set_custom_labels_for_self_hosted_runner_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **runner_id** | **int**| Unique identifier of the self-hosted runner. | 
 **actions_set_custom_labels_for_self_hosted_runner_for_org_request** | [**ActionsSetCustomLabelsForSelfHostedRunnerForOrgRequest**](ActionsSetCustomLabelsForSelfHostedRunnerForOrgRequest.md)|  | 

### Return type

[**ActionsListLabelsForSelfHostedRunnerForOrg200Response**](ActionsListLabelsForSelfHostedRunnerForOrg200Response.md)

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

# **actions_set_custom_oidc_sub_claim_for_repo**
> object actions_set_custom_oidc_sub_claim_for_repo(owner, repo, actions_oidc_subject_customization_for_a_repository)

Set the customization template for an OIDC subject claim for a repository

Sets the customization template and `opt-in` or `opt-out` flag for an OpenID Connect (OIDC) subject claim for a repository.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_oidc_subject_customization_for_a_repository import ActionsOIDCSubjectCustomizationForARepository
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    actions_oidc_subject_customization_for_a_repository = {"use_default":false,"include_claim_keys":["repo","context"]} # ActionsOIDCSubjectCustomizationForARepository | 

    try:
        # Set the customization template for an OIDC subject claim for a repository
        api_response = api_instance.actions_set_custom_oidc_sub_claim_for_repo(owner, repo, actions_oidc_subject_customization_for_a_repository)
        print("The response of ActionsApi->actions_set_custom_oidc_sub_claim_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_set_custom_oidc_sub_claim_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **actions_oidc_subject_customization_for_a_repository** | [**ActionsOIDCSubjectCustomizationForARepository**](ActionsOIDCSubjectCustomizationForARepository.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Empty response |  -  |
**404** | Resource not found |  -  |
**400** | Bad Request |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_set_github_actions_default_workflow_permissions_organization**
> actions_set_github_actions_default_workflow_permissions_organization(org, actions_set_default_workflow_permissions=actions_set_default_workflow_permissions)

Set default workflow permissions for an organization

Sets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an organization, and sets if GitHub Actions can submit approving pull request reviews. For more information, see \"[Setting the permissions of the GITHUB_TOKEN for your organization](https://docs.github.com/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-organization).\"  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_set_default_workflow_permissions import ActionsSetDefaultWorkflowPermissions
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    actions_set_default_workflow_permissions = github_openapi.ActionsSetDefaultWorkflowPermissions() # ActionsSetDefaultWorkflowPermissions |  (optional)

    try:
        # Set default workflow permissions for an organization
        api_instance.actions_set_github_actions_default_workflow_permissions_organization(org, actions_set_default_workflow_permissions=actions_set_default_workflow_permissions)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_set_github_actions_default_workflow_permissions_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **actions_set_default_workflow_permissions** | [**ActionsSetDefaultWorkflowPermissions**](ActionsSetDefaultWorkflowPermissions.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_set_github_actions_default_workflow_permissions_repository**
> actions_set_github_actions_default_workflow_permissions_repository(owner, repo, actions_set_default_workflow_permissions)

Set default workflow permissions for a repository

Sets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in a repository, and sets if GitHub Actions can submit approving pull request reviews. For more information, see \"[Setting the permissions of the GITHUB_TOKEN for your repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#setting-the-permissions-of-the-github_token-for-your-repository).\"  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_set_default_workflow_permissions import ActionsSetDefaultWorkflowPermissions
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    actions_set_default_workflow_permissions = github_openapi.ActionsSetDefaultWorkflowPermissions() # ActionsSetDefaultWorkflowPermissions | 

    try:
        # Set default workflow permissions for a repository
        api_instance.actions_set_github_actions_default_workflow_permissions_repository(owner, repo, actions_set_default_workflow_permissions)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_set_github_actions_default_workflow_permissions_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **actions_set_default_workflow_permissions** | [**ActionsSetDefaultWorkflowPermissions**](ActionsSetDefaultWorkflowPermissions.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success response |  -  |
**409** | Conflict response when changing a setting is prevented by the owning organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_set_github_actions_permissions_organization**
> actions_set_github_actions_permissions_organization(org, actions_set_github_actions_permissions_organization_request)

Set GitHub Actions permissions for an organization

Sets the GitHub Actions permissions policy for repositories and allowed actions and reusable workflows in an organization.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_set_github_actions_permissions_organization_request import ActionsSetGithubActionsPermissionsOrganizationRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    actions_set_github_actions_permissions_organization_request = {"enabled_repositories":"all","allowed_actions":"selected"} # ActionsSetGithubActionsPermissionsOrganizationRequest | 

    try:
        # Set GitHub Actions permissions for an organization
        api_instance.actions_set_github_actions_permissions_organization(org, actions_set_github_actions_permissions_organization_request)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_set_github_actions_permissions_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **actions_set_github_actions_permissions_organization_request** | [**ActionsSetGithubActionsPermissionsOrganizationRequest**](ActionsSetGithubActionsPermissionsOrganizationRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_set_github_actions_permissions_repository**
> actions_set_github_actions_permissions_repository(owner, repo, actions_set_github_actions_permissions_repository_request)

Set GitHub Actions permissions for a repository

Sets the GitHub Actions permissions policy for enabling GitHub Actions and allowed actions and reusable workflows in the repository.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_set_github_actions_permissions_repository_request import ActionsSetGithubActionsPermissionsRepositoryRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    actions_set_github_actions_permissions_repository_request = {"enabled":true,"allowed_actions":"selected"} # ActionsSetGithubActionsPermissionsRepositoryRequest | 

    try:
        # Set GitHub Actions permissions for a repository
        api_instance.actions_set_github_actions_permissions_repository(owner, repo, actions_set_github_actions_permissions_repository_request)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_set_github_actions_permissions_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **actions_set_github_actions_permissions_repository_request** | [**ActionsSetGithubActionsPermissionsRepositoryRequest**](ActionsSetGithubActionsPermissionsRepositoryRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_set_repo_access_to_self_hosted_runner_group_in_org**
> actions_set_repo_access_to_self_hosted_runner_group_in_org(org, runner_group_id, actions_set_repo_access_to_self_hosted_runner_group_in_org_request)

Set repository access for a self-hosted runner group in an organization

Replaces the list of repositories that have access to a self-hosted runner group configured in an organization.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_set_repo_access_to_self_hosted_runner_group_in_org_request import ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_group_id = 56 # int | Unique identifier of the self-hosted runner group.
    actions_set_repo_access_to_self_hosted_runner_group_in_org_request = {"selected_repository_ids":[32,91]} # ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest | 

    try:
        # Set repository access for a self-hosted runner group in an organization
        api_instance.actions_set_repo_access_to_self_hosted_runner_group_in_org(org, runner_group_id, actions_set_repo_access_to_self_hosted_runner_group_in_org_request)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_set_repo_access_to_self_hosted_runner_group_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_group_id** | **int**| Unique identifier of the self-hosted runner group. | 
 **actions_set_repo_access_to_self_hosted_runner_group_in_org_request** | [**ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest**](ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_set_selected_repos_for_org_secret**
> actions_set_selected_repos_for_org_secret(org, secret_name, actions_set_selected_repos_for_org_secret_request)

Set selected repositories for an organization secret

Replaces all repositories for an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/actions/secrets#create-or-update-an-organization-secret).  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.

### Example


```python
import github_openapi
from github_openapi.models.actions_set_selected_repos_for_org_secret_request import ActionsSetSelectedReposForOrgSecretRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    actions_set_selected_repos_for_org_secret_request = {"selected_repository_ids":[64780797]} # ActionsSetSelectedReposForOrgSecretRequest | 

    try:
        # Set selected repositories for an organization secret
        api_instance.actions_set_selected_repos_for_org_secret(org, secret_name, actions_set_selected_repos_for_org_secret_request)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_set_selected_repos_for_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 
 **actions_set_selected_repos_for_org_secret_request** | [**ActionsSetSelectedReposForOrgSecretRequest**](ActionsSetSelectedReposForOrgSecretRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_set_selected_repos_for_org_variable**
> actions_set_selected_repos_for_org_variable(org, name, actions_set_selected_repos_for_org_variable_request)

Set selected repositories for an organization variable

Replaces all repositories for an organization variable that is available to selected repositories. Organization variables that are available to selected repositories have their `visibility` field set to `selected`.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.

### Example


```python
import github_openapi
from github_openapi.models.actions_set_selected_repos_for_org_variable_request import ActionsSetSelectedReposForOrgVariableRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    name = 'name_example' # str | The name of the variable.
    actions_set_selected_repos_for_org_variable_request = {"selected_repository_ids":[64780797]} # ActionsSetSelectedReposForOrgVariableRequest | 

    try:
        # Set selected repositories for an organization variable
        api_instance.actions_set_selected_repos_for_org_variable(org, name, actions_set_selected_repos_for_org_variable_request)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_set_selected_repos_for_org_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **name** | **str**| The name of the variable. | 
 **actions_set_selected_repos_for_org_variable_request** | [**ActionsSetSelectedReposForOrgVariableRequest**](ActionsSetSelectedReposForOrgVariableRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**409** | Response when the visibility of the variable is not set to &#x60;selected&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_set_selected_repositories_enabled_github_actions_organization**
> actions_set_selected_repositories_enabled_github_actions_organization(org, actions_set_selected_repositories_enabled_github_actions_organization_request)

Set selected repositories enabled for GitHub Actions in an organization

Replaces the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be configured to `selected`. For more information, see \"[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization).\"   OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_set_selected_repositories_enabled_github_actions_organization_request import ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    actions_set_selected_repositories_enabled_github_actions_organization_request = {"selected_repository_ids":[32,42]} # ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest | 

    try:
        # Set selected repositories enabled for GitHub Actions in an organization
        api_instance.actions_set_selected_repositories_enabled_github_actions_organization(org, actions_set_selected_repositories_enabled_github_actions_organization_request)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_set_selected_repositories_enabled_github_actions_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **actions_set_selected_repositories_enabled_github_actions_organization_request** | [**ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest**](ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_set_self_hosted_runners_in_group_for_org**
> actions_set_self_hosted_runners_in_group_for_org(org, runner_group_id, actions_set_self_hosted_runners_in_group_for_org_request)

Set self-hosted runners in a group for an organization

Replaces the list of self-hosted runners that are part of an organization runner group.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_set_self_hosted_runners_in_group_for_org_request import ActionsSetSelfHostedRunnersInGroupForOrgRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_group_id = 56 # int | Unique identifier of the self-hosted runner group.
    actions_set_self_hosted_runners_in_group_for_org_request = {"runners":[9,2]} # ActionsSetSelfHostedRunnersInGroupForOrgRequest | 

    try:
        # Set self-hosted runners in a group for an organization
        api_instance.actions_set_self_hosted_runners_in_group_for_org(org, runner_group_id, actions_set_self_hosted_runners_in_group_for_org_request)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_set_self_hosted_runners_in_group_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_group_id** | **int**| Unique identifier of the self-hosted runner group. | 
 **actions_set_self_hosted_runners_in_group_for_org_request** | [**ActionsSetSelfHostedRunnersInGroupForOrgRequest**](ActionsSetSelfHostedRunnersInGroupForOrgRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_set_workflow_access_to_repository**
> actions_set_workflow_access_to_repository(owner, repo, actions_workflow_access_to_repository)

Set the level of access for workflows outside of the repository

Sets the level of access that workflows outside of the repository have to actions and reusable workflows in the repository. This endpoint only applies to private repositories. For more information, see \"[Allowing access to components in a private repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#allowing-access-to-components-in-a-private-repository)\".  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_workflow_access_to_repository import ActionsWorkflowAccessToRepository
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    actions_workflow_access_to_repository = github_openapi.ActionsWorkflowAccessToRepository() # ActionsWorkflowAccessToRepository | 

    try:
        # Set the level of access for workflows outside of the repository
        api_instance.actions_set_workflow_access_to_repository(owner, repo, actions_workflow_access_to_repository)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_set_workflow_access_to_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **actions_workflow_access_to_repository** | [**ActionsWorkflowAccessToRepository**](ActionsWorkflowAccessToRepository.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_update_environment_variable**
> actions_update_environment_variable(owner, repo, name, environment_name, actions_update_repo_variable_request)

Update an environment variable

Updates an environment variable that you can reference in a GitHub Actions workflow.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_update_repo_variable_request import ActionsUpdateRepoVariableRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    name = 'name_example' # str | The name of the variable.
    environment_name = 'environment_name_example' # str | The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with `%2F`.
    actions_update_repo_variable_request = {"name":"USERNAME","value":"octocat"} # ActionsUpdateRepoVariableRequest | 

    try:
        # Update an environment variable
        api_instance.actions_update_environment_variable(owner, repo, name, environment_name, actions_update_repo_variable_request)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_update_environment_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **name** | **str**| The name of the variable. | 
 **environment_name** | **str**| The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with &#x60;%2F&#x60;. | 
 **actions_update_repo_variable_request** | [**ActionsUpdateRepoVariableRequest**](ActionsUpdateRepoVariableRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_update_org_variable**
> actions_update_org_variable(org, name, actions_update_org_variable_request)

Update an organization variable

Updates an organization variable that you can reference in a GitHub Actions workflow.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.

### Example


```python
import github_openapi
from github_openapi.models.actions_update_org_variable_request import ActionsUpdateOrgVariableRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    name = 'name_example' # str | The name of the variable.
    actions_update_org_variable_request = {"name":"USERNAME","value":"octocat","visibility":"selected","selected_repository_ids":[1296269,1296280]} # ActionsUpdateOrgVariableRequest | 

    try:
        # Update an organization variable
        api_instance.actions_update_org_variable(org, name, actions_update_org_variable_request)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_update_org_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **name** | **str**| The name of the variable. | 
 **actions_update_org_variable_request** | [**ActionsUpdateOrgVariableRequest**](ActionsUpdateOrgVariableRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_update_repo_variable**
> actions_update_repo_variable(owner, repo, name, actions_update_repo_variable_request)

Update a repository variable

Updates a repository variable that you can reference in a GitHub Actions workflow.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_update_repo_variable_request import ActionsUpdateRepoVariableRequest
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
    api_instance = github_openapi.ActionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    name = 'name_example' # str | The name of the variable.
    actions_update_repo_variable_request = {"name":"USERNAME","value":"octocat"} # ActionsUpdateRepoVariableRequest | 

    try:
        # Update a repository variable
        api_instance.actions_update_repo_variable(owner, repo, name, actions_update_repo_variable_request)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_update_repo_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **name** | **str**| The name of the variable. | 
 **actions_update_repo_variable_request** | [**ActionsUpdateRepoVariableRequest**](ActionsUpdateRepoVariableRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_update_self_hosted_runner_group_for_org**
> RunnerGroupsOrg actions_update_self_hosted_runner_group_for_org(org, runner_group_id, actions_update_self_hosted_runner_group_for_org_request)

Update a self-hosted runner group for an organization

Updates the `name` and `visibility` of a self-hosted runner group in an organization.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_update_self_hosted_runner_group_for_org_request import ActionsUpdateSelfHostedRunnerGroupForOrgRequest
from github_openapi.models.runner_groups_org import RunnerGroupsOrg
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
    api_instance = github_openapi.ActionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    runner_group_id = 56 # int | Unique identifier of the self-hosted runner group.
    actions_update_self_hosted_runner_group_for_org_request = {"name":"Expensive hardware runners","visibility":"selected"} # ActionsUpdateSelfHostedRunnerGroupForOrgRequest | 

    try:
        # Update a self-hosted runner group for an organization
        api_response = api_instance.actions_update_self_hosted_runner_group_for_org(org, runner_group_id, actions_update_self_hosted_runner_group_for_org_request)
        print("The response of ActionsApi->actions_update_self_hosted_runner_group_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_update_self_hosted_runner_group_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **runner_group_id** | **int**| Unique identifier of the self-hosted runner group. | 
 **actions_update_self_hosted_runner_group_for_org_request** | [**ActionsUpdateSelfHostedRunnerGroupForOrgRequest**](ActionsUpdateSelfHostedRunnerGroupForOrgRequest.md)|  | 

### Return type

[**RunnerGroupsOrg**](RunnerGroupsOrg.md)

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

