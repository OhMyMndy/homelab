# ActionsCreateWorkflowDispatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | The git reference for the workflow. The reference can be a branch or tag name. | 
**inputs** | **Dict[str, object]** | Input keys and values configured in the workflow file. The maximum number of properties is 10. Any default properties configured in the workflow file will be used when &#x60;inputs&#x60; are omitted. | [optional] 

## Example

```python
from github_openapi.models.actions_create_workflow_dispatch_request import ActionsCreateWorkflowDispatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsCreateWorkflowDispatchRequest from a JSON string
actions_create_workflow_dispatch_request_instance = ActionsCreateWorkflowDispatchRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsCreateWorkflowDispatchRequest.to_json())

# convert the object into a dict
actions_create_workflow_dispatch_request_dict = actions_create_workflow_dispatch_request_instance.to_dict()
# create an instance of ActionsCreateWorkflowDispatchRequest from a dict
actions_create_workflow_dispatch_request_from_dict = ActionsCreateWorkflowDispatchRequest.from_dict(actions_create_workflow_dispatch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


