# WebhookRepositoryRenamedChangesRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**WebhookDiscussionCommentEditedChangesBody**](WebhookDiscussionCommentEditedChangesBody.md) |  | 

## Example

```python
from github_openapi.models.webhook_repository_renamed_changes_repository import WebhookRepositoryRenamedChangesRepository

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryRenamedChangesRepository from a JSON string
webhook_repository_renamed_changes_repository_instance = WebhookRepositoryRenamedChangesRepository.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryRenamedChangesRepository.to_json())

# convert the object into a dict
webhook_repository_renamed_changes_repository_dict = webhook_repository_renamed_changes_repository_instance.to_dict()
# create an instance of WebhookRepositoryRenamedChangesRepository from a dict
webhook_repository_renamed_changes_repository_from_dict = WebhookRepositoryRenamedChangesRepository.from_dict(webhook_repository_renamed_changes_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


