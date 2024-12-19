# WebhookMemberEditedChangesOldPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The previous permissions of the collaborator if the action was edited. | 

## Example

```python
from github_openapi.models.webhook_member_edited_changes_old_permission import WebhookMemberEditedChangesOldPermission

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMemberEditedChangesOldPermission from a JSON string
webhook_member_edited_changes_old_permission_instance = WebhookMemberEditedChangesOldPermission.from_json(json)
# print the JSON string representation of the object
print(WebhookMemberEditedChangesOldPermission.to_json())

# convert the object into a dict
webhook_member_edited_changes_old_permission_dict = webhook_member_edited_changes_old_permission_instance.to_dict()
# create an instance of WebhookMemberEditedChangesOldPermission from a dict
webhook_member_edited_changes_old_permission_from_dict = WebhookMemberEditedChangesOldPermission.from_dict(webhook_member_edited_changes_old_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


