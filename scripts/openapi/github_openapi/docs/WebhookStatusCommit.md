# WebhookStatusCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**User8**](User8.md) |  | 
**comments_url** | **str** |  | 
**commit** | [**WebhookStatusCommitCommit**](WebhookStatusCommitCommit.md) |  | 
**committer** | [**User8**](User8.md) |  | 
**html_url** | **str** |  | 
**node_id** | **str** |  | 
**parents** | [**List[WebhookStatusCommitParentsInner]**](WebhookStatusCommitParentsInner.md) |  | 
**sha** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_status_commit import WebhookStatusCommit

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookStatusCommit from a JSON string
webhook_status_commit_instance = WebhookStatusCommit.from_json(json)
# print the JSON string representation of the object
print(WebhookStatusCommit.to_json())

# convert the object into a dict
webhook_status_commit_dict = webhook_status_commit_instance.to_dict()
# create an instance of WebhookStatusCommit from a dict
webhook_status_commit_from_dict = WebhookStatusCommit.from_dict(webhook_status_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


