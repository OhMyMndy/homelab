# OrganizationFull

Organization Full

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**url** | **str** |  | 
**repos_url** | **str** |  | 
**events_url** | **str** |  | 
**hooks_url** | **str** |  | 
**issues_url** | **str** |  | 
**members_url** | **str** |  | 
**public_members_url** | **str** |  | 
**avatar_url** | **str** |  | 
**description** | **str** |  | 
**name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**blog** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**twitter_username** | **str** |  | [optional] 
**is_verified** | **bool** |  | [optional] 
**has_organization_projects** | **bool** |  | 
**has_repository_projects** | **bool** |  | 
**public_repos** | **int** |  | 
**public_gists** | **int** |  | 
**followers** | **int** |  | 
**following** | **int** |  | 
**html_url** | **str** |  | 
**type** | **str** |  | 
**total_private_repos** | **int** |  | [optional] 
**owned_private_repos** | **int** |  | [optional] 
**private_gists** | **int** |  | [optional] 
**disk_usage** | **int** |  | [optional] 
**collaborators** | **int** | The number of collaborators on private repositories.  This field may be null if the number of private repositories is over 50,000. | [optional] 
**billing_email** | **str** |  | [optional] 
**plan** | [**OrganizationFullPlan**](OrganizationFullPlan.md) |  | [optional] 
**default_repository_permission** | **str** |  | [optional] 
**members_can_create_repositories** | **bool** |  | [optional] 
**two_factor_requirement_enabled** | **bool** |  | [optional] 
**members_allowed_repository_creation_type** | **str** |  | [optional] 
**members_can_create_public_repositories** | **bool** |  | [optional] 
**members_can_create_private_repositories** | **bool** |  | [optional] 
**members_can_create_internal_repositories** | **bool** |  | [optional] 
**members_can_create_pages** | **bool** |  | [optional] 
**members_can_create_public_pages** | **bool** |  | [optional] 
**members_can_create_private_pages** | **bool** |  | [optional] 
**members_can_fork_private_repositories** | **bool** |  | [optional] 
**web_commit_signoff_required** | **bool** |  | [optional] 
**advanced_security_enabled_for_new_repositories** | **bool** | **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.  Whether GitHub Advanced Security is enabled for new repositories and repositories transferred to this organization.  This field is only visible to organization owners or members of a team with the security manager role. | [optional] 
**dependabot_alerts_enabled_for_new_repositories** | **bool** | **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.  Whether Dependabot alerts are automatically enabled for new repositories and repositories transferred to this organization.  This field is only visible to organization owners or members of a team with the security manager role. | [optional] 
**dependabot_security_updates_enabled_for_new_repositories** | **bool** | **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.  Whether Dependabot security updates are automatically enabled for new repositories and repositories transferred to this organization.  This field is only visible to organization owners or members of a team with the security manager role. | [optional] 
**dependency_graph_enabled_for_new_repositories** | **bool** | **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.  Whether dependency graph is automatically enabled for new repositories and repositories transferred to this organization.  This field is only visible to organization owners or members of a team with the security manager role. | [optional] 
**secret_scanning_enabled_for_new_repositories** | **bool** | **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.  Whether secret scanning is automatically enabled for new repositories and repositories transferred to this organization.  This field is only visible to organization owners or members of a team with the security manager role. | [optional] 
**secret_scanning_push_protection_enabled_for_new_repositories** | **bool** | **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.  Whether secret scanning push protection is automatically enabled for new repositories and repositories transferred to this organization.  This field is only visible to organization owners or members of a team with the security manager role. | [optional] 
**secret_scanning_push_protection_custom_link_enabled** | **bool** | Whether a custom link is shown to contributors who are blocked from pushing a secret by push protection. | [optional] 
**secret_scanning_push_protection_custom_link** | **str** | An optional URL string to display to contributors who are blocked from pushing a secret. | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**archived_at** | **datetime** |  | 
**deploy_keys_enabled_for_repositories** | **bool** | Controls whether or not deploy keys may be added and used for repositories in the organization. | [optional] 

## Example

```python
from github_openapi.models.organization_full import OrganizationFull

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationFull from a JSON string
organization_full_instance = OrganizationFull.from_json(json)
# print the JSON string representation of the object
print(OrganizationFull.to_json())

# convert the object into a dict
organization_full_dict = organization_full_instance.to_dict()
# create an instance of OrganizationFull from a dict
organization_full_from_dict = OrganizationFull.from_dict(organization_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


