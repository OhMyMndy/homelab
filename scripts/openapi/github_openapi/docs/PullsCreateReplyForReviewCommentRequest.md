# PullsCreateReplyForReviewCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The text of the review comment. | 

## Example

```python
from github_openapi.models.pulls_create_reply_for_review_comment_request import PullsCreateReplyForReviewCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PullsCreateReplyForReviewCommentRequest from a JSON string
pulls_create_reply_for_review_comment_request_instance = PullsCreateReplyForReviewCommentRequest.from_json(json)
# print the JSON string representation of the object
print(PullsCreateReplyForReviewCommentRequest.to_json())

# convert the object into a dict
pulls_create_reply_for_review_comment_request_dict = pulls_create_reply_for_review_comment_request_instance.to_dict()
# create an instance of PullsCreateReplyForReviewCommentRequest from a dict
pulls_create_reply_for_review_comment_request_from_dict = PullsCreateReplyForReviewCommentRequest.from_dict(pulls_create_reply_for_review_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


