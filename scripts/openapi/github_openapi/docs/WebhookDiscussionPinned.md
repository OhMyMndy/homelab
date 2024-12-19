# WebhookDiscussionPinned


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
from github_openapi.models.webhook_discussion_pinned import WebhookDiscussionPinned

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionPinned from a JSON string
webhook_discussion_pinned_instance = WebhookDiscussionPinned.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionPinned.to_json())

# convert the object into a dict
webhook_discussion_pinned_dict = webhook_discussion_pinned_instance.to_dict()
# create an instance of WebhookDiscussionPinned from a dict
webhook_discussion_pinned_from_dict = WebhookDiscussionPinned.from_dict(webhook_discussion_pinned_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


