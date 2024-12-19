# ReviewComment

Legacy Review Comment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**pull_request_review_id** | **int** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**diff_hunk** | **str** |  | 
**path** | **str** |  | 
**position** | **int** |  | 
**original_position** | **int** |  | 
**commit_id** | **str** |  | 
**original_commit_id** | **str** |  | 
**in_reply_to_id** | **int** |  | [optional] 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**body** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**html_url** | **str** |  | 
**pull_request_url** | **str** |  | 
**author_association** | [**AuthorAssociation**](AuthorAssociation.md) |  | 
**links** | [**ReviewCommentLinks**](ReviewCommentLinks.md) |  | 
**body_text** | **str** |  | [optional] 
**body_html** | **str** |  | [optional] 
**reactions** | [**ReactionRollup**](ReactionRollup.md) |  | [optional] 
**side** | **str** | The side of the first line of the range for a multi-line comment. | [optional] [default to 'RIGHT']
**start_side** | **str** | The side of the first line of the range for a multi-line comment. | [optional] [default to 'RIGHT']
**line** | **int** | The line of the blob to which the comment applies. The last line of the range for a multi-line comment | [optional] 
**original_line** | **int** | The original line of the blob to which the comment applies. The last line of the range for a multi-line comment | [optional] 
**start_line** | **int** | The first line of the range for a multi-line comment. | [optional] 
**original_start_line** | **int** | The original first line of the range for a multi-line comment. | [optional] 

## Example

```python
from github_openapi.models.review_comment import ReviewComment

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewComment from a JSON string
review_comment_instance = ReviewComment.from_json(json)
# print the JSON string representation of the object
print(ReviewComment.to_json())

# convert the object into a dict
review_comment_dict = review_comment_instance.to_dict()
# create an instance of ReviewComment from a dict
review_comment_from_dict = ReviewComment.from_dict(review_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


