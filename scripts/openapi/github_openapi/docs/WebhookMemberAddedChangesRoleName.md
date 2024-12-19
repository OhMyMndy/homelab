# WebhookMemberAddedChangesRoleName

The role assigned to the collaborator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_member_added_changes_role_name import WebhookMemberAddedChangesRoleName

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMemberAddedChangesRoleName from a JSON string
webhook_member_added_changes_role_name_instance = WebhookMemberAddedChangesRoleName.from_json(json)
# print the JSON string representation of the object
print(WebhookMemberAddedChangesRoleName.to_json())

# convert the object into a dict
webhook_member_added_changes_role_name_dict = webhook_member_added_changes_role_name_instance.to_dict()
# create an instance of WebhookMemberAddedChangesRoleName from a dict
webhook_member_added_changes_role_name_from_dict = WebhookMemberAddedChangesRoleName.from_dict(webhook_member_added_changes_role_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


