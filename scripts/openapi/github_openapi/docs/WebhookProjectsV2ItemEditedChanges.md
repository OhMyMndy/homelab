# WebhookProjectsV2ItemEditedChanges

The changes made to the item may involve modifications in the item's fields and draft issue body. It includes altered values for text, number, date, single select, and iteration fields, along with the GraphQL node ID of the changed field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_value** | [**WebhookProjectsV2ItemEditedChangesOneOfFieldValue**](WebhookProjectsV2ItemEditedChangesOneOfFieldValue.md) |  | 
**body** | [**WebhookMemberEditedChangesPermission**](WebhookMemberEditedChangesPermission.md) |  | 

## Example

```python
from github_openapi.models.webhook_projects_v2_item_edited_changes import WebhookProjectsV2ItemEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectsV2ItemEditedChanges from a JSON string
webhook_projects_v2_item_edited_changes_instance = WebhookProjectsV2ItemEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectsV2ItemEditedChanges.to_json())

# convert the object into a dict
webhook_projects_v2_item_edited_changes_dict = webhook_projects_v2_item_edited_changes_instance.to_dict()
# create an instance of WebhookProjectsV2ItemEditedChanges from a dict
webhook_projects_v2_item_edited_changes_from_dict = WebhookProjectsV2ItemEditedChanges.from_dict(webhook_projects_v2_item_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


