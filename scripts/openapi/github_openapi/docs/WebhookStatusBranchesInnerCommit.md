# WebhookStatusBranchesInnerCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_status_branches_inner_commit import WebhookStatusBranchesInnerCommit

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookStatusBranchesInnerCommit from a JSON string
webhook_status_branches_inner_commit_instance = WebhookStatusBranchesInnerCommit.from_json(json)
# print the JSON string representation of the object
print(WebhookStatusBranchesInnerCommit.to_json())

# convert the object into a dict
webhook_status_branches_inner_commit_dict = webhook_status_branches_inner_commit_instance.to_dict()
# create an instance of WebhookStatusBranchesInnerCommit from a dict
webhook_status_branches_inner_commit_from_dict = WebhookStatusBranchesInnerCommit.from_dict(webhook_status_branches_inner_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


