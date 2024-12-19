# ReviewRequestRemovedIssueEvent

Review Request Removed Issue Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**node_id** | **str** |  | 
**url** | **str** |  | 
**actor** | [**SimpleUser**](SimpleUser.md) |  | 
**event** | **str** |  | 
**commit_id** | **str** |  | 
**commit_url** | **str** |  | 
**created_at** | **str** |  | 
**performed_via_github_app** | [**NullableIntegration**](NullableIntegration.md) |  | 
**review_requester** | [**SimpleUser**](SimpleUser.md) |  | 
**requested_team** | [**Team**](Team.md) |  | [optional] 
**requested_reviewer** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.review_request_removed_issue_event import ReviewRequestRemovedIssueEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewRequestRemovedIssueEvent from a JSON string
review_request_removed_issue_event_instance = ReviewRequestRemovedIssueEvent.from_json(json)
# print the JSON string representation of the object
print(ReviewRequestRemovedIssueEvent.to_json())

# convert the object into a dict
review_request_removed_issue_event_dict = review_request_removed_issue_event_instance.to_dict()
# create an instance of ReviewRequestRemovedIssueEvent from a dict
review_request_removed_issue_event_from_dict = ReviewRequestRemovedIssueEvent.from_dict(review_request_removed_issue_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


