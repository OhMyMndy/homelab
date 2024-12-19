# TimelineCommittedEvent

Timeline Committed Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | [optional] 
**sha** | **str** | SHA for the commit | 
**node_id** | **str** |  | 
**url** | **str** |  | 
**author** | [**GitCommitAuthor**](GitCommitAuthor.md) |  | 
**committer** | [**GitCommitAuthor**](GitCommitAuthor.md) |  | 
**message** | **str** | Message describing the purpose of the commit | 
**tree** | [**GitCommitTree**](GitCommitTree.md) |  | 
**parents** | [**List[GitCommitParentsInner]**](GitCommitParentsInner.md) |  | 
**verification** | [**GitCommitVerification**](GitCommitVerification.md) |  | 
**html_url** | **str** |  | 

## Example

```python
from github_openapi.models.timeline_committed_event import TimelineCommittedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineCommittedEvent from a JSON string
timeline_committed_event_instance = TimelineCommittedEvent.from_json(json)
# print the JSON string representation of the object
print(TimelineCommittedEvent.to_json())

# convert the object into a dict
timeline_committed_event_dict = timeline_committed_event_instance.to_dict()
# create an instance of TimelineCommittedEvent from a dict
timeline_committed_event_from_dict = TimelineCommittedEvent.from_dict(timeline_committed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


