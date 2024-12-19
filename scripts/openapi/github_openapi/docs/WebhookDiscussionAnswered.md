# WebhookDiscussionAnswered


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**answer** | [**WebhooksAnswer**](WebhooksAnswer.md) |  | 
**discussion** | [**Discussion**](Discussion.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_discussion_answered import WebhookDiscussionAnswered

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionAnswered from a JSON string
webhook_discussion_answered_instance = WebhookDiscussionAnswered.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionAnswered.to_json())

# convert the object into a dict
webhook_discussion_answered_dict = webhook_discussion_answered_instance.to_dict()
# create an instance of WebhookDiscussionAnswered from a dict
webhook_discussion_answered_from_dict = WebhookDiscussionAnswered.from_dict(webhook_discussion_answered_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


