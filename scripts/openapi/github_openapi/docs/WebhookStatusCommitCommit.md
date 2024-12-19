# WebhookStatusCommitCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**WebhookStatusCommitCommitAuthor**](WebhookStatusCommitCommitAuthor.md) |  | 
**comment_count** | **int** |  | 
**committer** | [**WebhookStatusCommitCommitAuthor**](WebhookStatusCommitCommitAuthor.md) |  | 
**message** | **str** |  | 
**tree** | [**ShortBranchCommit**](ShortBranchCommit.md) |  | 
**url** | **str** |  | 
**verification** | [**WebhookStatusCommitCommitVerification**](WebhookStatusCommitCommitVerification.md) |  | 

## Example

```python
from github_openapi.models.webhook_status_commit_commit import WebhookStatusCommitCommit

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookStatusCommitCommit from a JSON string
webhook_status_commit_commit_instance = WebhookStatusCommitCommit.from_json(json)
# print the JSON string representation of the object
print(WebhookStatusCommitCommit.to_json())

# convert the object into a dict
webhook_status_commit_commit_dict = webhook_status_commit_commit_instance.to_dict()
# create an instance of WebhookStatusCommitCommit from a dict
webhook_status_commit_commit_from_dict = WebhookStatusCommitCommit.from_dict(webhook_status_commit_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


