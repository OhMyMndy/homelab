# WebhookDiscussionUnanswered


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**discussion** | [**Discussion**](Discussion.md) |  | 
**old_answer** | [**WebhooksAnswer**](WebhooksAnswer.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_discussion_unanswered import WebhookDiscussionUnanswered

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionUnanswered from a JSON string
webhook_discussion_unanswered_instance = WebhookDiscussionUnanswered.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionUnanswered.to_json())

# convert the object into a dict
webhook_discussion_unanswered_dict = webhook_discussion_unanswered_instance.to_dict()
# create an instance of WebhookDiscussionUnanswered from a dict
webhook_discussion_unanswered_from_dict = WebhookDiscussionUnanswered.from_dict(webhook_discussion_unanswered_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


