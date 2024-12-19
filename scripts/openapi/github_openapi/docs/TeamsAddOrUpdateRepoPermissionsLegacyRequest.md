# TeamsAddOrUpdateRepoPermissionsLegacyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **str** | The permission to grant the team on this repository. If no permission is specified, the team&#39;s &#x60;permission&#x60; attribute will be used to determine what permission to grant the team on this repository. | [optional] 

## Example

```python
from github_openapi.models.teams_add_or_update_repo_permissions_legacy_request import TeamsAddOrUpdateRepoPermissionsLegacyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsAddOrUpdateRepoPermissionsLegacyRequest from a JSON string
teams_add_or_update_repo_permissions_legacy_request_instance = TeamsAddOrUpdateRepoPermissionsLegacyRequest.from_json(json)
# print the JSON string representation of the object
print(TeamsAddOrUpdateRepoPermissionsLegacyRequest.to_json())

# convert the object into a dict
teams_add_or_update_repo_permissions_legacy_request_dict = teams_add_or_update_repo_permissions_legacy_request_instance.to_dict()
# create an instance of TeamsAddOrUpdateRepoPermissionsLegacyRequest from a dict
teams_add_or_update_repo_permissions_legacy_request_from_dict = TeamsAddOrUpdateRepoPermissionsLegacyRequest.from_dict(teams_add_or_update_repo_permissions_legacy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


