# TeamsAddOrUpdateRepoPermissionsInOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **str** | The permission to grant the team on this repository. We accept the following permissions to be set: &#x60;pull&#x60;, &#x60;triage&#x60;, &#x60;push&#x60;, &#x60;maintain&#x60;, &#x60;admin&#x60; and you can also specify a custom repository role name, if the owning organization has defined any. If no permission is specified, the team&#39;s &#x60;permission&#x60; attribute will be used to determine what permission to grant the team on this repository. | [optional] 

## Example

```python
from github_openapi.models.teams_add_or_update_repo_permissions_in_org_request import TeamsAddOrUpdateRepoPermissionsInOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsAddOrUpdateRepoPermissionsInOrgRequest from a JSON string
teams_add_or_update_repo_permissions_in_org_request_instance = TeamsAddOrUpdateRepoPermissionsInOrgRequest.from_json(json)
# print the JSON string representation of the object
print(TeamsAddOrUpdateRepoPermissionsInOrgRequest.to_json())

# convert the object into a dict
teams_add_or_update_repo_permissions_in_org_request_dict = teams_add_or_update_repo_permissions_in_org_request_instance.to_dict()
# create an instance of TeamsAddOrUpdateRepoPermissionsInOrgRequest from a dict
teams_add_or_update_repo_permissions_in_org_request_from_dict = TeamsAddOrUpdateRepoPermissionsInOrgRequest.from_dict(teams_add_or_update_repo_permissions_in_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


