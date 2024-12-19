# TeamOrganization

Team Organization

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
**created_at** | **datetime** |  | 
**type** | **str** |  | 
**total_private_repos** | **int** |  | [optional] 
**owned_private_repos** | **int** |  | [optional] 
**private_gists** | **int** |  | [optional] 
**disk_usage** | **int** |  | [optional] 
**collaborators** | **int** |  | [optional] 
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
**updated_at** | **datetime** |  | 
**archived_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.team_organization import TeamOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of TeamOrganization from a JSON string
team_organization_instance = TeamOrganization.from_json(json)
# print the JSON string representation of the object
print(TeamOrganization.to_json())

# convert the object into a dict
team_organization_dict = team_organization_instance.to_dict()
# create an instance of TeamOrganization from a dict
team_organization_from_dict = TeamOrganization.from_dict(team_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


