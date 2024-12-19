# WebhookMemberEditedChangesPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | [optional] 
**to** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhook_member_edited_changes_permission import WebhookMemberEditedChangesPermission

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMemberEditedChangesPermission from a JSON string
webhook_member_edited_changes_permission_instance = WebhookMemberEditedChangesPermission.from_json(json)
# print the JSON string representation of the object
print(WebhookMemberEditedChangesPermission.to_json())

# convert the object into a dict
webhook_member_edited_changes_permission_dict = webhook_member_edited_changes_permission_instance.to_dict()
# create an instance of WebhookMemberEditedChangesPermission from a dict
webhook_member_edited_changes_permission_from_dict = WebhookMemberEditedChangesPermission.from_dict(webhook_member_edited_changes_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


