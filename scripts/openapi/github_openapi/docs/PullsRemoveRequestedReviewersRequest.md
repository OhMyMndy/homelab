# PullsRemoveRequestedReviewersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviewers** | **List[str]** | An array of user &#x60;login&#x60;s that will be removed. | 
**team_reviewers** | **List[str]** | An array of team &#x60;slug&#x60;s that will be removed. | [optional] 

## Example

```python
from github_openapi.models.pulls_remove_requested_reviewers_request import PullsRemoveRequestedReviewersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PullsRemoveRequestedReviewersRequest from a JSON string
pulls_remove_requested_reviewers_request_instance = PullsRemoveRequestedReviewersRequest.from_json(json)
# print the JSON string representation of the object
print(PullsRemoveRequestedReviewersRequest.to_json())

# convert the object into a dict
pulls_remove_requested_reviewers_request_dict = pulls_remove_requested_reviewers_request_instance.to_dict()
# create an instance of PullsRemoveRequestedReviewersRequest from a dict
pulls_remove_requested_reviewers_request_from_dict = PullsRemoveRequestedReviewersRequest.from_dict(pulls_remove_requested_reviewers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


