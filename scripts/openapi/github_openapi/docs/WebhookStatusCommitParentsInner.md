# WebhookStatusCommitParentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html_url** | **str** |  | 
**sha** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_status_commit_parents_inner import WebhookStatusCommitParentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookStatusCommitParentsInner from a JSON string
webhook_status_commit_parents_inner_instance = WebhookStatusCommitParentsInner.from_json(json)
# print the JSON string representation of the object
print(WebhookStatusCommitParentsInner.to_json())

# convert the object into a dict
webhook_status_commit_parents_inner_dict = webhook_status_commit_parents_inner_instance.to_dict()
# create an instance of WebhookStatusCommitParentsInner from a dict
webhook_status_commit_parents_inner_from_dict = WebhookStatusCommitParentsInner.from_dict(webhook_status_commit_parents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


