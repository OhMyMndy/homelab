# WebhookPullRequestReviewThreadUnresolvedThread


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**List[PullRequestReviewComment2]**](PullRequestReviewComment2.md) |  | 
**node_id** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_thread_unresolved_thread import WebhookPullRequestReviewThreadUnresolvedThread

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewThreadUnresolvedThread from a JSON string
webhook_pull_request_review_thread_unresolved_thread_instance = WebhookPullRequestReviewThreadUnresolvedThread.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewThreadUnresolvedThread.to_json())

# convert the object into a dict
webhook_pull_request_review_thread_unresolved_thread_dict = webhook_pull_request_review_thread_unresolved_thread_instance.to_dict()
# create an instance of WebhookPullRequestReviewThreadUnresolvedThread from a dict
webhook_pull_request_review_thread_unresolved_thread_from_dict = WebhookPullRequestReviewThreadUnresolvedThread.from_dict(webhook_pull_request_review_thread_unresolved_thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


