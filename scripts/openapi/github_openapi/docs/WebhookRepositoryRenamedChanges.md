# WebhookRepositoryRenamedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | [**WebhookRepositoryRenamedChangesRepository**](WebhookRepositoryRenamedChangesRepository.md) |  | 

## Example

```python
from github_openapi.models.webhook_repository_renamed_changes import WebhookRepositoryRenamedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryRenamedChanges from a JSON string
webhook_repository_renamed_changes_instance = WebhookRepositoryRenamedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryRenamedChanges.to_json())

# convert the object into a dict
webhook_repository_renamed_changes_dict = webhook_repository_renamed_changes_instance.to_dict()
# create an instance of WebhookRepositoryRenamedChanges from a dict
webhook_repository_renamed_changes_from_dict = WebhookRepositoryRenamedChanges.from_dict(webhook_repository_renamed_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


