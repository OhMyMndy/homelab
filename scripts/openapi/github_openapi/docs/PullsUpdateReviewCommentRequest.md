# PullsUpdateReviewCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The text of the reply to the review comment. | 

## Example

```python
from github_openapi.models.pulls_update_review_comment_request import PullsUpdateReviewCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PullsUpdateReviewCommentRequest from a JSON string
pulls_update_review_comment_request_instance = PullsUpdateReviewCommentRequest.from_json(json)
# print the JSON string representation of the object
print(PullsUpdateReviewCommentRequest.to_json())

# convert the object into a dict
pulls_update_review_comment_request_dict = pulls_update_review_comment_request_instance.to_dict()
# create an instance of PullsUpdateReviewCommentRequest from a dict
pulls_update_review_comment_request_from_dict = PullsUpdateReviewCommentRequest.from_dict(pulls_update_review_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


