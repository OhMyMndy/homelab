# WebhookDiscussionDeleted


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
from github_openapi.models.webhook_discussion_deleted import WebhookDiscussionDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionDeleted from a JSON string
webhook_discussion_deleted_instance = WebhookDiscussionDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionDeleted.to_json())

# convert the object into a dict
webhook_discussion_deleted_dict = webhook_discussion_deleted_instance.to_dict()
# create an instance of WebhookDiscussionDeleted from a dict
webhook_discussion_deleted_from_dict = WebhookDiscussionDeleted.from_dict(webhook_discussion_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


