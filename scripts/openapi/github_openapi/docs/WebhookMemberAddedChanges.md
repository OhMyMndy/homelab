# WebhookMemberAddedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | [**WebhookMemberAddedChangesPermission**](WebhookMemberAddedChangesPermission.md) |  | [optional] 
**role_name** | [**WebhookMemberAddedChangesRoleName**](WebhookMemberAddedChangesRoleName.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_member_added_changes import WebhookMemberAddedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMemberAddedChanges from a JSON string
webhook_member_added_changes_instance = WebhookMemberAddedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookMemberAddedChanges.to_json())

# convert the object into a dict
webhook_member_added_changes_dict = webhook_member_added_changes_instance.to_dict()
# create an instance of WebhookMemberAddedChanges from a dict
webhook_member_added_changes_from_dict = WebhookMemberAddedChanges.from_dict(webhook_member_added_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


