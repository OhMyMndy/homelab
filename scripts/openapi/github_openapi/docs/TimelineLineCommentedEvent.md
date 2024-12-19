# TimelineLineCommentedEvent

Timeline Line Commented Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | [optional] 
**node_id** | **str** |  | [optional] 
**comments** | [**List[PullRequestReviewComment]**](PullRequestReviewComment.md) |  | [optional] 

## Example

```python
from github_openapi.models.timeline_line_commented_event import TimelineLineCommentedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineLineCommentedEvent from a JSON string
timeline_line_commented_event_instance = TimelineLineCommentedEvent.from_json(json)
# print the JSON string representation of the object
print(TimelineLineCommentedEvent.to_json())

# convert the object into a dict
timeline_line_commented_event_dict = timeline_line_commented_event_instance.to_dict()
# create an instance of TimelineLineCommentedEvent from a dict
timeline_line_commented_event_from_dict = TimelineLineCommentedEvent.from_dict(timeline_line_commented_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


