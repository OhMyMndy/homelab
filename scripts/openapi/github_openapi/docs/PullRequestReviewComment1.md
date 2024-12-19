# PullRequestReviewComment1

The [comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request) itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**WebhooksReviewCommentLinks**](WebhooksReviewCommentLinks.md) |  | 
**author_association** | **str** | How the author is associated with the repository. | 
**body** | **str** | The text of the comment. | 
**commit_id** | **str** | The SHA of the commit to which the comment applies. | 
**created_at** | **datetime** |  | 
**diff_hunk** | **str** | The diff of the line that the comment refers to. | 
**html_url** | **str** | HTML URL for the pull request review comment. | 
**id** | **int** | The ID of the pull request review comment. | 
**in_reply_to_id** | **int** | The comment ID to reply to. | [optional] 
**line** | **int** | The line of the blob to which the comment applies. The last line of the range for a multi-line comment | 
**node_id** | **str** | The node ID of the pull request review comment. | 
**original_commit_id** | **str** | The SHA of the original commit to which the comment applies. | 
**original_line** | **int** | The line of the blob to which the comment applies. The last line of the range for a multi-line comment | 
**original_position** | **int** | The index of the original line in the diff to which the comment applies. | 
**original_start_line** | **int** | The first line of the range for a multi-line comment. | 
**path** | **str** | The relative path of the file to which the comment applies. | 
**position** | **int** | The line index in the diff to which the comment applies. | 
**pull_request_review_id** | **int** | The ID of the pull request review to which the comment belongs. | 
**pull_request_url** | **str** | URL for the pull request that the review comment belongs to. | 
**reactions** | [**Reactions**](Reactions.md) |  | 
**side** | **str** | The side of the first line of the range for a multi-line comment. | 
**start_line** | **int** | The first line of the range for a multi-line comment. | 
**start_side** | **str** | The side of the first line of the range for a multi-line comment. | [default to 'RIGHT']
**subject_type** | **str** | The level at which the comment is targeted, can be a diff line or a file. | [optional] 
**updated_at** | **datetime** |  | 
**url** | **str** | URL for the pull request review comment | 
**user** | [**User3**](User3.md) |  | 

## Example

```python
from github_openapi.models.pull_request_review_comment1 import PullRequestReviewComment1

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestReviewComment1 from a JSON string
pull_request_review_comment1_instance = PullRequestReviewComment1.from_json(json)
# print the JSON string representation of the object
print(PullRequestReviewComment1.to_json())

# convert the object into a dict
pull_request_review_comment1_dict = pull_request_review_comment1_instance.to_dict()
# create an instance of PullRequestReviewComment1 from a dict
pull_request_review_comment1_from_dict = PullRequestReviewComment1.from_dict(pull_request_review_comment1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


