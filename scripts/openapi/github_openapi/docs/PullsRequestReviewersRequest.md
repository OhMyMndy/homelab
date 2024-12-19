# PullsRequestReviewersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviewers** | **List[str]** | An array of user &#x60;login&#x60;s that will be requested. | [optional] 
**team_reviewers** | **List[str]** | An array of team &#x60;slug&#x60;s that will be requested. | [optional] 

## Example

```python
from github_openapi.models.pulls_request_reviewers_request import PullsRequestReviewersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PullsRequestReviewersRequest from a JSON string
pulls_request_reviewers_request_instance = PullsRequestReviewersRequest.from_json(json)
# print the JSON string representation of the object
print(PullsRequestReviewersRequest.to_json())

# convert the object into a dict
pulls_request_reviewers_request_dict = pulls_request_reviewers_request_instance.to_dict()
# create an instance of PullsRequestReviewersRequest from a dict
pulls_request_reviewers_request_from_dict = PullsRequestReviewersRequest.from_dict(pulls_request_reviewers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


