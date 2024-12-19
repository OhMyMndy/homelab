# IssueEventDismissedReview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**review_id** | **int** |  | 
**dismissal_message** | **str** |  | 
**dismissal_commit_id** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.issue_event_dismissed_review import IssueEventDismissedReview

# TODO update the JSON string below
json = "{}"
# create an instance of IssueEventDismissedReview from a JSON string
issue_event_dismissed_review_instance = IssueEventDismissedReview.from_json(json)
# print the JSON string representation of the object
print(IssueEventDismissedReview.to_json())

# convert the object into a dict
issue_event_dismissed_review_dict = issue_event_dismissed_review_instance.to_dict()
# create an instance of IssueEventDismissedReview from a dict
issue_event_dismissed_review_from_dict = IssueEventDismissedReview.from_dict(issue_event_dismissed_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


