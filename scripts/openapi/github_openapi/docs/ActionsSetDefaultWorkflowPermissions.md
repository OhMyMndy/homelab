# ActionsSetDefaultWorkflowPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_workflow_permissions** | [**ActionsDefaultWorkflowPermissions**](ActionsDefaultWorkflowPermissions.md) |  | [optional] 
**can_approve_pull_request_reviews** | **bool** | Whether GitHub Actions can approve pull requests. Enabling this can be a security risk. | [optional] 

## Example

```python
from github_openapi.models.actions_set_default_workflow_permissions import ActionsSetDefaultWorkflowPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsSetDefaultWorkflowPermissions from a JSON string
actions_set_default_workflow_permissions_instance = ActionsSetDefaultWorkflowPermissions.from_json(json)
# print the JSON string representation of the object
print(ActionsSetDefaultWorkflowPermissions.to_json())

# convert the object into a dict
actions_set_default_workflow_permissions_dict = actions_set_default_workflow_permissions_instance.to_dict()
# create an instance of ActionsSetDefaultWorkflowPermissions from a dict
actions_set_default_workflow_permissions_from_dict = ActionsSetDefaultWorkflowPermissions.from_dict(actions_set_default_workflow_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


