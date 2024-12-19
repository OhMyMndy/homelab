# WebhookStatusCommitCommitVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** |  | 
**reason** | **str** |  | 
**signature** | **str** |  | 
**verified** | **bool** |  | 
**verified_at** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhook_status_commit_commit_verification import WebhookStatusCommitCommitVerification

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookStatusCommitCommitVerification from a JSON string
webhook_status_commit_commit_verification_instance = WebhookStatusCommitCommitVerification.from_json(json)
# print the JSON string representation of the object
print(WebhookStatusCommitCommitVerification.to_json())

# convert the object into a dict
webhook_status_commit_commit_verification_dict = webhook_status_commit_commit_verification_instance.to_dict()
# create an instance of WebhookStatusCommitCommitVerification from a dict
webhook_status_commit_commit_verification_from_dict = WebhookStatusCommitCommitVerification.from_dict(webhook_status_commit_commit_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


