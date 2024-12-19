# WebhookDiscussionUnlocked


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**discussion** | [**Discussion**](Discussion.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_discussion_unlocked import WebhookDiscussionUnlocked

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionUnlocked from a JSON string
webhook_discussion_unlocked_instance = WebhookDiscussionUnlocked.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionUnlocked.to_json())

# convert the object into a dict
webhook_discussion_unlocked_dict = webhook_discussion_unlocked_instance.to_dict()
# create an instance of WebhookDiscussionUnlocked from a dict
webhook_discussion_unlocked_from_dict = WebhookDiscussionUnlocked.from_dict(webhook_discussion_unlocked_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


