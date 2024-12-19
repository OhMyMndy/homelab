# MilestonedIssueEventMilestone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 

## Example

```python
from github_openapi.models.milestoned_issue_event_milestone import MilestonedIssueEventMilestone

# TODO update the JSON string below
json = "{}"
# create an instance of MilestonedIssueEventMilestone from a JSON string
milestoned_issue_event_milestone_instance = MilestonedIssueEventMilestone.from_json(json)
# print the JSON string representation of the object
print(MilestonedIssueEventMilestone.to_json())

# convert the object into a dict
milestoned_issue_event_milestone_dict = milestoned_issue_event_milestone_instance.to_dict()
# create an instance of MilestonedIssueEventMilestone from a dict
milestoned_issue_event_milestone_from_dict = MilestonedIssueEventMilestone.from_dict(milestoned_issue_event_milestone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


