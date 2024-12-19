# IssueEventMilestone

Issue Event Milestone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 

## Example

```python
from github_openapi.models.issue_event_milestone import IssueEventMilestone

# TODO update the JSON string below
json = "{}"
# create an instance of IssueEventMilestone from a JSON string
issue_event_milestone_instance = IssueEventMilestone.from_json(json)
# print the JSON string representation of the object
print(IssueEventMilestone.to_json())

# convert the object into a dict
issue_event_milestone_dict = issue_event_milestone_instance.to_dict()
# create an instance of IssueEventMilestone from a dict
issue_event_milestone_from_dict = IssueEventMilestone.from_dict(issue_event_milestone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


