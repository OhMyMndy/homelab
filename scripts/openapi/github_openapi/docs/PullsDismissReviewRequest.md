# PullsDismissReviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The message for the pull request review dismissal | 
**event** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.pulls_dismiss_review_request import PullsDismissReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PullsDismissReviewRequest from a JSON string
pulls_dismiss_review_request_instance = PullsDismissReviewRequest.from_json(json)
# print the JSON string representation of the object
print(PullsDismissReviewRequest.to_json())

# convert the object into a dict
pulls_dismiss_review_request_dict = pulls_dismiss_review_request_instance.to_dict()
# create an instance of PullsDismissReviewRequest from a dict
pulls_dismiss_review_request_from_dict = PullsDismissReviewRequest.from_dict(pulls_dismiss_review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


