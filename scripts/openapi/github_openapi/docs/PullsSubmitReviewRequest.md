# PullsSubmitReviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The body text of the pull request review | [optional] 
**event** | **str** | The review action you want to perform. The review actions include: &#x60;APPROVE&#x60;, &#x60;REQUEST_CHANGES&#x60;, or &#x60;COMMENT&#x60;. When you leave this blank, the API returns _HTTP 422 (Unrecognizable entity)_ and sets the review action state to &#x60;PENDING&#x60;, which means you will need to re-submit the pull request review using a review action. | 

## Example

```python
from github_openapi.models.pulls_submit_review_request import PullsSubmitReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PullsSubmitReviewRequest from a JSON string
pulls_submit_review_request_instance = PullsSubmitReviewRequest.from_json(json)
# print the JSON string representation of the object
print(PullsSubmitReviewRequest.to_json())

# convert the object into a dict
pulls_submit_review_request_dict = pulls_submit_review_request_instance.to_dict()
# create an instance of PullsSubmitReviewRequest from a dict
pulls_submit_review_request_from_dict = PullsSubmitReviewRequest.from_dict(pulls_submit_review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


