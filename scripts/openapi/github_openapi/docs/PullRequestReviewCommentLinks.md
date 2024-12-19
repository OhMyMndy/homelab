# PullRequestReviewCommentLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**PullRequestReviewCommentLinksSelf**](PullRequestReviewCommentLinksSelf.md) |  | 
**html** | [**PullRequestReviewCommentLinksHtml**](PullRequestReviewCommentLinksHtml.md) |  | 
**pull_request** | [**PullRequestReviewCommentLinksPullRequest**](PullRequestReviewCommentLinksPullRequest.md) |  | 

## Example

```python
from github_openapi.models.pull_request_review_comment_links import PullRequestReviewCommentLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestReviewCommentLinks from a JSON string
pull_request_review_comment_links_instance = PullRequestReviewCommentLinks.from_json(json)
# print the JSON string representation of the object
print(PullRequestReviewCommentLinks.to_json())

# convert the object into a dict
pull_request_review_comment_links_dict = pull_request_review_comment_links_instance.to_dict()
# create an instance of PullRequestReviewCommentLinks from a dict
pull_request_review_comment_links_from_dict = PullRequestReviewCommentLinks.from_dict(pull_request_review_comment_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


