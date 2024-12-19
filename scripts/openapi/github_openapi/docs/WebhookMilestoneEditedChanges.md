# WebhookMilestoneEditedChanges

The changes to the milestone if the action was `edited`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**WebhookLabelEditedChangesDescription**](WebhookLabelEditedChangesDescription.md) |  | [optional] 
**due_on** | [**WebhookMilestoneEditedChangesDueOn**](WebhookMilestoneEditedChangesDueOn.md) |  | [optional] 
**title** | [**WebhookMilestoneEditedChangesTitle**](WebhookMilestoneEditedChangesTitle.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_milestone_edited_changes import WebhookMilestoneEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMilestoneEditedChanges from a JSON string
webhook_milestone_edited_changes_instance = WebhookMilestoneEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookMilestoneEditedChanges.to_json())

# convert the object into a dict
webhook_milestone_edited_changes_dict = webhook_milestone_edited_changes_instance.to_dict()
# create an instance of WebhookMilestoneEditedChanges from a dict
webhook_milestone_edited_changes_from_dict = WebhookMilestoneEditedChanges.from_dict(webhook_milestone_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


