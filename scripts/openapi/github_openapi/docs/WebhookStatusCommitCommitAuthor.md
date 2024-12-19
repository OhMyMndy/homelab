# WebhookStatusCommitCommitAuthor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | 
**email** | **str** |  | 
**name** | **str** |  | 
**username** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhook_status_commit_commit_author import WebhookStatusCommitCommitAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookStatusCommitCommitAuthor from a JSON string
webhook_status_commit_commit_author_instance = WebhookStatusCommitCommitAuthor.from_json(json)
# print the JSON string representation of the object
print(WebhookStatusCommitCommitAuthor.to_json())

# convert the object into a dict
webhook_status_commit_commit_author_dict = webhook_status_commit_commit_author_instance.to_dict()
# create an instance of WebhookStatusCommitCommitAuthor from a dict
webhook_status_commit_commit_author_from_dict = WebhookStatusCommitCommitAuthor.from_dict(webhook_status_commit_commit_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


