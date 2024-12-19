# PullsCreateReviewCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The text of the review comment. | 
**commit_id** | **str** | The SHA of the commit needing a comment. Not using the latest commit SHA may render your comment outdated if a subsequent commit modifies the line you specify as the &#x60;position&#x60;. | 
**path** | **str** | The relative path to the file that necessitates a comment. | 
**position** | **int** | **This parameter is closing down. Use &#x60;line&#x60; instead**. The position in the diff where you want to add a review comment. Note this value is not the same as the line number in the file. The position value equals the number of lines down from the first \&quot;@@\&quot; hunk header in the file you want to add a comment. The line just below the \&quot;@@\&quot; line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file. | [optional] 
**side** | **str** | In a split diff view, the side of the diff that the pull request&#39;s changes appear on. Can be &#x60;LEFT&#x60; or &#x60;RIGHT&#x60;. Use &#x60;LEFT&#x60; for deletions that appear in red. Use &#x60;RIGHT&#x60; for additions that appear in green or unchanged lines that appear in white and are shown for context. For a multi-line comment, side represents whether the last line of the comment range is a deletion or addition. For more information, see \&quot;[Diff view options](https://docs.github.com/articles/about-comparing-branches-in-pull-requests#diff-view-options)\&quot; in the GitHub Help documentation. | [optional] 
**line** | **int** | **Required unless using &#x60;subject_type:file&#x60;**. The line of the blob in the pull request diff that the comment applies to. For a multi-line comment, the last line of the range that your comment applies to. | [optional] 
**start_line** | **int** | **Required when using multi-line comments unless using &#x60;in_reply_to&#x60;**. The &#x60;start_line&#x60; is the first line in the pull request diff that your multi-line comment applies to. To learn more about multi-line comments, see \&quot;[Commenting on a pull request](https://docs.github.com/articles/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request)\&quot; in the GitHub Help documentation. | [optional] 
**start_side** | **str** | **Required when using multi-line comments unless using &#x60;in_reply_to&#x60;**. The &#x60;start_side&#x60; is the starting side of the diff that the comment applies to. Can be &#x60;LEFT&#x60; or &#x60;RIGHT&#x60;. To learn more about multi-line comments, see \&quot;[Commenting on a pull request](https://docs.github.com/articles/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request)\&quot; in the GitHub Help documentation. See &#x60;side&#x60; in this table for additional context. | [optional] 
**in_reply_to** | **int** | The ID of the review comment to reply to. To find the ID of a review comment with [\&quot;List review comments on a pull request\&quot;](#list-review-comments-on-a-pull-request). When specified, all parameters other than &#x60;body&#x60; in the request body are ignored. | [optional] 
**subject_type** | **str** | The level at which the comment is targeted. | [optional] 

## Example

```python
from github_openapi.models.pulls_create_review_comment_request import PullsCreateReviewCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PullsCreateReviewCommentRequest from a JSON string
pulls_create_review_comment_request_instance = PullsCreateReviewCommentRequest.from_json(json)
# print the JSON string representation of the object
print(PullsCreateReviewCommentRequest.to_json())

# convert the object into a dict
pulls_create_review_comment_request_dict = pulls_create_review_comment_request_instance.to_dict()
# create an instance of PullsCreateReviewCommentRequest from a dict
pulls_create_review_comment_request_from_dict = PullsCreateReviewCommentRequest.from_dict(pulls_create_review_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


