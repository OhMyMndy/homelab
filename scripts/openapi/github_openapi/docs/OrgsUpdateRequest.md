# OrgsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_email** | **str** | Billing email address. This address is not publicized. | [optional] 
**company** | **str** | The company name. | [optional] 
**email** | **str** | The publicly visible email address. | [optional] 
**twitter_username** | **str** | The Twitter username of the company. | [optional] 
**location** | **str** | The location. | [optional] 
**name** | **str** | The shorthand name of the company. | [optional] 
**description** | **str** | The description of the company. The maximum size is 160 characters. | [optional] 
**has_organization_projects** | **bool** | Whether an organization can use organization projects. | [optional] 
**has_repository_projects** | **bool** | Whether repositories that belong to the organization can use repository projects. | [optional] 
**default_repository_permission** | **str** | Default permission level members have for organization repositories. | [optional] [default to 'read']
**members_can_create_repositories** | **bool** | Whether of non-admin organization members can create repositories. **Note:** A parameter can override this parameter. See &#x60;members_allowed_repository_creation_type&#x60; in this table for details. | [optional] [default to True]
**members_can_create_internal_repositories** | **bool** | Whether organization members can create internal repositories, which are visible to all enterprise members. You can only allow members to create internal repositories if your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+. For more information, see \&quot;[Restricting repository creation in your organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)\&quot; in the GitHub Help documentation. | [optional] 
**members_can_create_private_repositories** | **bool** | Whether organization members can create private repositories, which are visible to organization members with permission. For more information, see \&quot;[Restricting repository creation in your organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)\&quot; in the GitHub Help documentation. | [optional] 
**members_can_create_public_repositories** | **bool** | Whether organization members can create public repositories, which are visible to anyone. For more information, see \&quot;[Restricting repository creation in your organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)\&quot; in the GitHub Help documentation. | [optional] 
**members_allowed_repository_creation_type** | **str** | Specifies which types of repositories non-admin organization members can create. &#x60;private&#x60; is only available to repositories that are part of an organization on GitHub Enterprise Cloud.  **Note:** This parameter is closing down and will be removed in the future. Its return value ignores internal repositories. Using this parameter overrides values set in &#x60;members_can_create_repositories&#x60;. See the parameter deprecation notice in the operation description for details. | [optional] 
**members_can_create_pages** | **bool** | Whether organization members can create GitHub Pages sites. Existing published sites will not be impacted. | [optional] [default to True]
**members_can_create_public_pages** | **bool** | Whether organization members can create public GitHub Pages sites. Existing published sites will not be impacted. | [optional] [default to True]
**members_can_create_private_pages** | **bool** | Whether organization members can create private GitHub Pages sites. Existing published sites will not be impacted. | [optional] [default to True]
**members_can_fork_private_repositories** | **bool** | Whether organization members can fork private organization repositories. | [optional] [default to False]
**web_commit_signoff_required** | **bool** | Whether contributors to organization repositories are required to sign off on commits they make through GitHub&#39;s web interface. | [optional] [default to False]
**blog** | **str** |  | [optional] 
**advanced_security_enabled_for_new_repositories** | **bool** | **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.  Whether GitHub Advanced Security is automatically enabled for new repositories and repositories transferred to this organization.  To use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see \&quot;[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).\&quot;  You can check which security and analysis features are currently enabled by using a &#x60;GET /orgs/{org}&#x60; request. | [optional] 
**dependabot_alerts_enabled_for_new_repositories** | **bool** | **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.  Whether Dependabot alerts are automatically enabled for new repositories and repositories transferred to this organization.  To use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see \&quot;[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).\&quot;  You can check which security and analysis features are currently enabled by using a &#x60;GET /orgs/{org}&#x60; request. | [optional] 
**dependabot_security_updates_enabled_for_new_repositories** | **bool** | **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.  Whether Dependabot security updates are automatically enabled for new repositories and repositories transferred to this organization.  To use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see \&quot;[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).\&quot;  You can check which security and analysis features are currently enabled by using a &#x60;GET /orgs/{org}&#x60; request. | [optional] 
**dependency_graph_enabled_for_new_repositories** | **bool** | **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.  Whether dependency graph is automatically enabled for new repositories and repositories transferred to this organization.  To use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see \&quot;[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).\&quot;  You can check which security and analysis features are currently enabled by using a &#x60;GET /orgs/{org}&#x60; request. | [optional] 
**secret_scanning_enabled_for_new_repositories** | **bool** | **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.  Whether secret scanning is automatically enabled for new repositories and repositories transferred to this organization.  To use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see \&quot;[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).\&quot;  You can check which security and analysis features are currently enabled by using a &#x60;GET /orgs/{org}&#x60; request. | [optional] 
**secret_scanning_push_protection_enabled_for_new_repositories** | **bool** | **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.  Whether secret scanning push protection is automatically enabled for new repositories and repositories transferred to this organization.  To use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see \&quot;[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).\&quot;  You can check which security and analysis features are currently enabled by using a &#x60;GET /orgs/{org}&#x60; request. | [optional] 
**secret_scanning_push_protection_custom_link_enabled** | **bool** | Whether a custom link is shown to contributors who are blocked from pushing a secret by push protection. | [optional] 
**secret_scanning_push_protection_custom_link** | **str** | If &#x60;secret_scanning_push_protection_custom_link_enabled&#x60; is true, the URL that will be displayed to contributors who are blocked from pushing a secret. | [optional] 
**deploy_keys_enabled_for_repositories** | **bool** | Controls whether or not deploy keys may be added and used for repositories in the organization. | [optional] 

## Example

```python
from github_openapi.models.orgs_update_request import OrgsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsUpdateRequest from a JSON string
orgs_update_request_instance = OrgsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(OrgsUpdateRequest.to_json())

# convert the object into a dict
orgs_update_request_dict = orgs_update_request_instance.to_dict()
# create an instance of OrgsUpdateRequest from a dict
orgs_update_request_from_dict = OrgsUpdateRequest.from_dict(orgs_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


