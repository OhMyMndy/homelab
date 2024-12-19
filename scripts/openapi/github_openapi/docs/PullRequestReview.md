# PullRequestReview

Pull Request Reviews are reviews on pull requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the review | 
**node_id** | **str** |  | 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**body** | **str** | The text of the review. | 
**state** | **str** |  | 
**html_url** | **str** |  | 
**pull_request_url** | **str** |  | 
**links** | [**TimelineReviewedEventLinks**](TimelineReviewedEventLinks.md) |  | 
**submitted_at** | **datetime** |  | [optional] 
**commit_id** | **str** | A commit SHA for the review. If the commit object was garbage collected or forcibly deleted, then it no longer exists in Git and this value will be &#x60;null&#x60;. | 
**body_html** | **str** |  | [optional] 
**body_text** | **str** |  | [optional] 
**author_association** | [**AuthorAssociation**](AuthorAssociation.md) |  | 

## Example

```python
from github_openapi.models.pull_request_review import PullRequestReview

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestReview from a JSON string
pull_request_review_instance = PullRequestReview.from_json(json)
# print the JSON string representation of the object
print(PullRequestReview.to_json())

# convert the object into a dict
pull_request_review_dict = pull_request_review_instance.to_dict()
# create an instance of PullRequestReview from a dict
pull_request_review_from_dict = PullRequestReview.from_dict(pull_request_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


