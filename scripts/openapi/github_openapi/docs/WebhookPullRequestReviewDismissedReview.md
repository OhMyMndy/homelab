# WebhookPullRequestReviewDismissedReview

The review that was affected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**WebhooksReviewLinks**](WebhooksReviewLinks.md) |  | 
**author_association** | **str** | How the author is associated with the repository. | 
**body** | **str** | The text of the review. | 
**commit_id** | **str** | A commit SHA for the review. | 
**html_url** | **str** |  | 
**id** | **int** | Unique identifier of the review | 
**node_id** | **str** |  | 
**pull_request_url** | **str** |  | 
**state** | **str** |  | 
**submitted_at** | **datetime** |  | 
**user** | [**User3**](User3.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_dismissed_review import WebhookPullRequestReviewDismissedReview

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewDismissedReview from a JSON string
webhook_pull_request_review_dismissed_review_instance = WebhookPullRequestReviewDismissedReview.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewDismissedReview.to_json())

# convert the object into a dict
webhook_pull_request_review_dismissed_review_dict = webhook_pull_request_review_dismissed_review_instance.to_dict()
# create an instance of WebhookPullRequestReviewDismissedReview from a dict
webhook_pull_request_review_dismissed_review_from_dict = WebhookPullRequestReviewDismissedReview.from_dict(webhook_pull_request_review_dismissed_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


