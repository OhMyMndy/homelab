# PullsCreateReviewRequestCommentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The relative path to the file that necessitates a review comment. | 
**position** | **int** | The position in the diff where you want to add a review comment. Note this value is not the same as the line number in the file. The &#x60;position&#x60; value equals the number of lines down from the first \&quot;@@\&quot; hunk header in the file you want to add a comment. The line just below the \&quot;@@\&quot; line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file. | [optional] 
**body** | **str** | Text of the review comment. | 
**line** | **int** |  | [optional] 
**side** | **str** |  | [optional] 
**start_line** | **int** |  | [optional] 
**start_side** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.pulls_create_review_request_comments_inner import PullsCreateReviewRequestCommentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PullsCreateReviewRequestCommentsInner from a JSON string
pulls_create_review_request_comments_inner_instance = PullsCreateReviewRequestCommentsInner.from_json(json)
# print the JSON string representation of the object
print(PullsCreateReviewRequestCommentsInner.to_json())

# convert the object into a dict
pulls_create_review_request_comments_inner_dict = pulls_create_review_request_comments_inner_instance.to_dict()
# create an instance of PullsCreateReviewRequestCommentsInner from a dict
pulls_create_review_request_comments_inner_from_dict = PullsCreateReviewRequestCommentsInner.from_dict(pulls_create_review_request_comments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


