# TeamsAddOrUpdateProjectPermissionsLegacyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **str** | The permission to grant to the team for this project. Default: the team&#39;s &#x60;permission&#x60; attribute will be used to determine what permission to grant the team on this project. Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling this endpoint. For more information, see \&quot;[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method).\&quot; | [optional] 

## Example

```python
from github_openapi.models.teams_add_or_update_project_permissions_legacy_request import TeamsAddOrUpdateProjectPermissionsLegacyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsAddOrUpdateProjectPermissionsLegacyRequest from a JSON string
teams_add_or_update_project_permissions_legacy_request_instance = TeamsAddOrUpdateProjectPermissionsLegacyRequest.from_json(json)
# print the JSON string representation of the object
print(TeamsAddOrUpdateProjectPermissionsLegacyRequest.to_json())

# convert the object into a dict
teams_add_or_update_project_permissions_legacy_request_dict = teams_add_or_update_project_permissions_legacy_request_instance.to_dict()
# create an instance of TeamsAddOrUpdateProjectPermissionsLegacyRequest from a dict
teams_add_or_update_project_permissions_legacy_request_from_dict = TeamsAddOrUpdateProjectPermissionsLegacyRequest.from_dict(teams_add_or_update_project_permissions_legacy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


