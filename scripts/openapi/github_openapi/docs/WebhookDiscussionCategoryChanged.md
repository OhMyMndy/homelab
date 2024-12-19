# WebhookDiscussionCategoryChanged


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookDiscussionCategoryChangedChanges**](WebhookDiscussionCategoryChangedChanges.md) |  | 
**discussion** | [**Discussion**](Discussion.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_discussion_category_changed import WebhookDiscussionCategoryChanged

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionCategoryChanged from a JSON string
webhook_discussion_category_changed_instance = WebhookDiscussionCategoryChanged.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionCategoryChanged.to_json())

# convert the object into a dict
webhook_discussion_category_changed_dict = webhook_discussion_category_changed_instance.to_dict()
# create an instance of WebhookDiscussionCategoryChanged from a dict
webhook_discussion_category_changed_from_dict = WebhookDiscussionCategoryChanged.from_dict(webhook_discussion_category_changed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


