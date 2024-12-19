# WebhookMemberEditedChanges

The changes to the collaborator permissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_permission** | [**WebhookMemberEditedChangesOldPermission**](WebhookMemberEditedChangesOldPermission.md) |  | [optional] 
**permission** | [**WebhookMemberEditedChangesPermission**](WebhookMemberEditedChangesPermission.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_member_edited_changes import WebhookMemberEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMemberEditedChanges from a JSON string
webhook_member_edited_changes_instance = WebhookMemberEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookMemberEditedChanges.to_json())

# convert the object into a dict
webhook_member_edited_changes_dict = webhook_member_edited_changes_instance.to_dict()
# create an instance of WebhookMemberEditedChanges from a dict
webhook_member_edited_changes_from_dict = WebhookMemberEditedChanges.from_dict(webhook_member_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


