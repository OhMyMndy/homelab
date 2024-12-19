# WebhookRepositoryTransferredChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | [**WebhookRepositoryTransferredChangesOwner**](WebhookRepositoryTransferredChangesOwner.md) |  | 

## Example

```python
from github_openapi.models.webhook_repository_transferred_changes import WebhookRepositoryTransferredChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryTransferredChanges from a JSON string
webhook_repository_transferred_changes_instance = WebhookRepositoryTransferredChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryTransferredChanges.to_json())

# convert the object into a dict
webhook_repository_transferred_changes_dict = webhook_repository_transferred_changes_instance.to_dict()
# create an instance of WebhookRepositoryTransferredChanges from a dict
webhook_repository_transferred_changes_from_dict = WebhookRepositoryTransferredChanges.from_dict(webhook_repository_transferred_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


