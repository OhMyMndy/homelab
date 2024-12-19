# ActionsGetDefaultWorkflowPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_workflow_permissions** | [**ActionsDefaultWorkflowPermissions**](ActionsDefaultWorkflowPermissions.md) |  | 
**can_approve_pull_request_reviews** | **bool** | Whether GitHub Actions can approve pull requests. Enabling this can be a security risk. | 

## Example

```python
from github_openapi.models.actions_get_default_workflow_permissions import ActionsGetDefaultWorkflowPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsGetDefaultWorkflowPermissions from a JSON string
actions_get_default_workflow_permissions_instance = ActionsGetDefaultWorkflowPermissions.from_json(json)
# print the JSON string representation of the object
print(ActionsGetDefaultWorkflowPermissions.to_json())

# convert the object into a dict
actions_get_default_workflow_permissions_dict = actions_get_default_workflow_permissions_instance.to_dict()
# create an instance of ActionsGetDefaultWorkflowPermissions from a dict
actions_get_default_workflow_permissions_from_dict = ActionsGetDefaultWorkflowPermissions.from_dict(actions_get_default_workflow_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


