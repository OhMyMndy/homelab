# WebhookProjectsV2ItemEditedChangesOneOfFieldValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_node_id** | **str** |  | [optional] 
**field_type** | **str** |  | [optional] 
**field_name** | **str** |  | [optional] 
**project_number** | **int** |  | [optional] 
**var_from** | [**WebhookProjectsV2ItemEditedChangesOneOfFieldValueFrom**](WebhookProjectsV2ItemEditedChangesOneOfFieldValueFrom.md) |  | [optional] 
**to** | [**WebhookProjectsV2ItemEditedChangesOneOfFieldValueFrom**](WebhookProjectsV2ItemEditedChangesOneOfFieldValueFrom.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_projects_v2_item_edited_changes_one_of_field_value import WebhookProjectsV2ItemEditedChangesOneOfFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectsV2ItemEditedChangesOneOfFieldValue from a JSON string
webhook_projects_v2_item_edited_changes_one_of_field_value_instance = WebhookProjectsV2ItemEditedChangesOneOfFieldValue.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectsV2ItemEditedChangesOneOfFieldValue.to_json())

# convert the object into a dict
webhook_projects_v2_item_edited_changes_one_of_field_value_dict = webhook_projects_v2_item_edited_changes_one_of_field_value_instance.to_dict()
# create an instance of WebhookProjectsV2ItemEditedChangesOneOfFieldValue from a dict
webhook_projects_v2_item_edited_changes_one_of_field_value_from_dict = WebhookProjectsV2ItemEditedChangesOneOfFieldValue.from_dict(webhook_projects_v2_item_edited_changes_one_of_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


