# WebhookMilestoneEditedChangesTitle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The previous version of the title if the action was &#x60;edited&#x60;. | 

## Example

```python
from github_openapi.models.webhook_milestone_edited_changes_title import WebhookMilestoneEditedChangesTitle

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMilestoneEditedChangesTitle from a JSON string
webhook_milestone_edited_changes_title_instance = WebhookMilestoneEditedChangesTitle.from_json(json)
# print the JSON string representation of the object
print(WebhookMilestoneEditedChangesTitle.to_json())

# convert the object into a dict
webhook_milestone_edited_changes_title_dict = webhook_milestone_edited_changes_title_instance.to_dict()
# create an instance of WebhookMilestoneEditedChangesTitle from a dict
webhook_milestone_edited_changes_title_from_dict = WebhookMilestoneEditedChangesTitle.from_dict(webhook_milestone_edited_changes_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


