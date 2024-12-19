# WebhookDiscussionUnlabeled


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**discussion** | [**Discussion**](Discussion.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**label** | [**WebhooksLabel**](WebhooksLabel.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_discussion_unlabeled import WebhookDiscussionUnlabeled

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionUnlabeled from a JSON string
webhook_discussion_unlabeled_instance = WebhookDiscussionUnlabeled.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionUnlabeled.to_json())

# convert the object into a dict
webhook_discussion_unlabeled_dict = webhook_discussion_unlabeled_instance.to_dict()
# create an instance of WebhookDiscussionUnlabeled from a dict
webhook_discussion_unlabeled_from_dict = WebhookDiscussionUnlabeled.from_dict(webhook_discussion_unlabeled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


