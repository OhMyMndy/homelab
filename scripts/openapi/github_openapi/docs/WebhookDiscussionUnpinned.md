# WebhookDiscussionUnpinned


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
from github_openapi.models.webhook_discussion_unpinned import WebhookDiscussionUnpinned

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionUnpinned from a JSON string
webhook_discussion_unpinned_instance = WebhookDiscussionUnpinned.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionUnpinned.to_json())

# convert the object into a dict
webhook_discussion_unpinned_dict = webhook_discussion_unpinned_instance.to_dict()
# create an instance of WebhookDiscussionUnpinned from a dict
webhook_discussion_unpinned_from_dict = WebhookDiscussionUnpinned.from_dict(webhook_discussion_unpinned_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


