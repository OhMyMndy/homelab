# WebhookMemberAddedChangesPermission

This field is included for legacy purposes; use the `role_name` field instead. The `maintain` role is mapped to `write` and the `triage` role is mapped to `read`. To determine the role assigned to the collaborator, use the `role_name` field instead, which will provide the full role name, including custom roles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_member_added_changes_permission import WebhookMemberAddedChangesPermission

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMemberAddedChangesPermission from a JSON string
webhook_member_added_changes_permission_instance = WebhookMemberAddedChangesPermission.from_json(json)
# print the JSON string representation of the object
print(WebhookMemberAddedChangesPermission.to_json())

# convert the object into a dict
webhook_member_added_changes_permission_dict = webhook_member_added_changes_permission_instance.to_dict()
# create an instance of WebhookMemberAddedChangesPermission from a dict
webhook_member_added_changes_permission_from_dict = WebhookMemberAddedChangesPermission.from_dict(webhook_member_added_changes_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


