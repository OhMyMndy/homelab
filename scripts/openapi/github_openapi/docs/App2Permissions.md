# App2Permissions

The set of permissions for the GitHub app

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **str** |  | [optional] 
**administration** | **str** |  | [optional] 
**checks** | **str** |  | [optional] 
**content_references** | **str** |  | [optional] 
**contents** | **str** |  | [optional] 
**deployments** | **str** |  | [optional] 
**discussions** | **str** |  | [optional] 
**emails** | **str** |  | [optional] 
**environments** | **str** |  | [optional] 
**issues** | **str** |  | [optional] 
**keys** | **str** |  | [optional] 
**members** | **str** |  | [optional] 
**metadata** | **str** |  | [optional] 
**organization_administration** | **str** |  | [optional] 
**organization_hooks** | **str** |  | [optional] 
**organization_packages** | **str** |  | [optional] 
**organization_plan** | **str** |  | [optional] 
**organization_projects** | **str** |  | [optional] 
**organization_secrets** | **str** |  | [optional] 
**organization_self_hosted_runners** | **str** |  | [optional] 
**organization_user_blocking** | **str** |  | [optional] 
**packages** | **str** |  | [optional] 
**pages** | **str** |  | [optional] 
**pull_requests** | **str** |  | [optional] 
**repository_hooks** | **str** |  | [optional] 
**repository_projects** | **str** |  | [optional] 
**secret_scanning_alerts** | **str** |  | [optional] 
**secrets** | **str** |  | [optional] 
**security_events** | **str** |  | [optional] 
**security_scanning_alert** | **str** |  | [optional] 
**single_file** | **str** |  | [optional] 
**statuses** | **str** |  | [optional] 
**team_discussions** | **str** |  | [optional] 
**vulnerability_alerts** | **str** |  | [optional] 
**workflows** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.app2_permissions import App2Permissions

# TODO update the JSON string below
json = "{}"
# create an instance of App2Permissions from a JSON string
app2_permissions_instance = App2Permissions.from_json(json)
# print the JSON string representation of the object
print(App2Permissions.to_json())

# convert the object into a dict
app2_permissions_dict = app2_permissions_instance.to_dict()
# create an instance of App2Permissions from a dict
app2_permissions_from_dict = App2Permissions.from_dict(app2_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


