# WebhookStatusBranchesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | [**WebhookStatusBranchesInnerCommit**](WebhookStatusBranchesInnerCommit.md) |  | 
**name** | **str** |  | 
**protected** | **bool** |  | 

## Example

```python
from github_openapi.models.webhook_status_branches_inner import WebhookStatusBranchesInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookStatusBranchesInner from a JSON string
webhook_status_branches_inner_instance = WebhookStatusBranchesInner.from_json(json)
# print the JSON string representation of the object
print(WebhookStatusBranchesInner.to_json())

# convert the object into a dict
webhook_status_branches_inner_dict = webhook_status_branches_inner_instance.to_dict()
# create an instance of WebhookStatusBranchesInner from a dict
webhook_status_branches_inner_from_dict = WebhookStatusBranchesInner.from_dict(webhook_status_branches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


