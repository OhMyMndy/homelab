# WebhookDiscussionCategoryChangedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**WebhookDiscussionCategoryChangedChangesCategory**](WebhookDiscussionCategoryChangedChangesCategory.md) |  | 

## Example

```python
from github_openapi.models.webhook_discussion_category_changed_changes import WebhookDiscussionCategoryChangedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionCategoryChangedChanges from a JSON string
webhook_discussion_category_changed_changes_instance = WebhookDiscussionCategoryChangedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionCategoryChangedChanges.to_json())

# convert the object into a dict
webhook_discussion_category_changed_changes_dict = webhook_discussion_category_changed_changes_instance.to_dict()
# create an instance of WebhookDiscussionCategoryChangedChanges from a dict
webhook_discussion_category_changed_changes_from_dict = WebhookDiscussionCategoryChangedChanges.from_dict(webhook_discussion_category_changed_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


