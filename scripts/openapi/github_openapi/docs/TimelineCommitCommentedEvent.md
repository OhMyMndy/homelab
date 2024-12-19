# TimelineCommitCommentedEvent

Timeline Commit Commented Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | [optional] 
**node_id** | **str** |  | [optional] 
**commit_id** | **str** |  | [optional] 
**comments** | [**List[CommitComment]**](CommitComment.md) |  | [optional] 

## Example

```python
from github_openapi.models.timeline_commit_commented_event import TimelineCommitCommentedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineCommitCommentedEvent from a JSON string
timeline_commit_commented_event_instance = TimelineCommitCommentedEvent.from_json(json)
# print the JSON string representation of the object
print(TimelineCommitCommentedEvent.to_json())

# convert the object into a dict
timeline_commit_commented_event_dict = timeline_commit_commented_event_instance.to_dict()
# create an instance of TimelineCommitCommentedEvent from a dict
timeline_commit_commented_event_from_dict = TimelineCommitCommentedEvent.from_dict(timeline_commit_commented_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


