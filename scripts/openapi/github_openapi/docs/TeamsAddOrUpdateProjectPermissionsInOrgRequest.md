# TeamsAddOrUpdateProjectPermissionsInOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **str** | The permission to grant to the team for this project. Default: the team&#39;s &#x60;permission&#x60; attribute will be used to determine what permission to grant the team on this project. Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling this endpoint. For more information, see \&quot;[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method).\&quot; | [optional] 

## Example

```python
from github_openapi.models.teams_add_or_update_project_permissions_in_org_request import TeamsAddOrUpdateProjectPermissionsInOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsAddOrUpdateProjectPermissionsInOrgRequest from a JSON string
teams_add_or_update_project_permissions_in_org_request_instance = TeamsAddOrUpdateProjectPermissionsInOrgRequest.from_json(json)
# print the JSON string representation of the object
print(TeamsAddOrUpdateProjectPermissionsInOrgRequest.to_json())

# convert the object into a dict
teams_add_or_update_project_permissions_in_org_request_dict = teams_add_or_update_project_permissions_in_org_request_instance.to_dict()
# create an instance of TeamsAddOrUpdateProjectPermissionsInOrgRequest from a dict
teams_add_or_update_project_permissions_in_org_request_from_dict = TeamsAddOrUpdateProjectPermissionsInOrgRequest.from_dict(teams_add_or_update_project_permissions_in_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


