# PullsUpdateReviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The body text of the pull request review. | 

## Example

```python
from github_openapi.models.pulls_update_review_request import PullsUpdateReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PullsUpdateReviewRequest from a JSON string
pulls_update_review_request_instance = PullsUpdateReviewRequest.from_json(json)
# print the JSON string representation of the object
print(PullsUpdateReviewRequest.to_json())

# convert the object into a dict
pulls_update_review_request_dict = pulls_update_review_request_instance.to_dict()
# create an instance of PullsUpdateReviewRequest from a dict
pulls_update_review_request_from_dict = PullsUpdateReviewRequest.from_dict(pulls_update_review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


