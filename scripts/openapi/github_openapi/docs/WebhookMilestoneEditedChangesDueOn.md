# WebhookMilestoneEditedChangesDueOn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The previous version of the due date if the action was &#x60;edited&#x60;. | 

## Example

```python
from github_openapi.models.webhook_milestone_edited_changes_due_on import WebhookMilestoneEditedChangesDueOn

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMilestoneEditedChangesDueOn from a JSON string
webhook_milestone_edited_changes_due_on_instance = WebhookMilestoneEditedChangesDueOn.from_json(json)
# print the JSON string representation of the object
print(WebhookMilestoneEditedChangesDueOn.to_json())

# convert the object into a dict
webhook_milestone_edited_changes_due_on_dict = webhook_milestone_edited_changes_due_on_instance.to_dict()
# create an instance of WebhookMilestoneEditedChangesDueOn from a dict
webhook_milestone_edited_changes_due_on_from_dict = WebhookMilestoneEditedChangesDueOn.from_dict(webhook_milestone_edited_changes_due_on_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


