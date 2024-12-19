# WebhookPullRequestReviewThreadResolvedThread


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**List[PullRequestReviewComment1]**](PullRequestReviewComment1.md) |  | 
**node_id** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_thread_resolved_thread import WebhookPullRequestReviewThreadResolvedThread

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewThreadResolvedThread from a JSON string
webhook_pull_request_review_thread_resolved_thread_instance = WebhookPullRequestReviewThreadResolvedThread.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewThreadResolvedThread.to_json())

# convert the object into a dict
webhook_pull_request_review_thread_resolved_thread_dict = webhook_pull_request_review_thread_resolved_thread_instance.to_dict()
# create an instance of WebhookPullRequestReviewThreadResolvedThread from a dict
webhook_pull_request_review_thread_resolved_thread_from_dict = WebhookPullRequestReviewThreadResolvedThread.from_dict(webhook_pull_request_review_thread_resolved_thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


