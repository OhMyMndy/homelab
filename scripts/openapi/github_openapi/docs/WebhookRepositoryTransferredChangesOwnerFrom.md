# WebhookRepositoryTransferredChangesOwnerFrom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | [**Organization**](Organization.md) |  | [optional] 
**user** | [**User1**](User1.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_repository_transferred_changes_owner_from import WebhookRepositoryTransferredChangesOwnerFrom

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryTransferredChangesOwnerFrom from a JSON string
webhook_repository_transferred_changes_owner_from_instance = WebhookRepositoryTransferredChangesOwnerFrom.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryTransferredChangesOwnerFrom.to_json())

# convert the object into a dict
webhook_repository_transferred_changes_owner_from_dict = webhook_repository_transferred_changes_owner_from_instance.to_dict()
# create an instance of WebhookRepositoryTransferredChangesOwnerFrom from a dict
webhook_repository_transferred_changes_owner_from_from_dict = WebhookRepositoryTransferredChangesOwnerFrom.from_dict(webhook_repository_transferred_changes_owner_from_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


