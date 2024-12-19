# TimelineReviewedEvent

Timeline Reviewed Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | 
**id** | **int** | Unique identifier of the review | 
**node_id** | **str** |  | 
**user** | [**SimpleUser**](SimpleUser.md) |  | 
**body** | **str** | The text of the review. | 
**state** | **str** |  | 
**html_url** | **str** |  | 
**pull_request_url** | **str** |  | 
**links** | [**TimelineReviewedEventLinks**](TimelineReviewedEventLinks.md) |  | 
**submitted_at** | **datetime** |  | [optional] 
**commit_id** | **str** | A commit SHA for the review. | 
**body_html** | **str** |  | [optional] 
**body_text** | **str** |  | [optional] 
**author_association** | [**AuthorAssociation**](AuthorAssociation.md) |  | 

## Example

```python
from github_openapi.models.timeline_reviewed_event import TimelineReviewedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineReviewedEvent from a JSON string
timeline_reviewed_event_instance = TimelineReviewedEvent.from_json(json)
# print the JSON string representation of the object
print(TimelineReviewedEvent.to_json())

# convert the object into a dict
timeline_reviewed_event_dict = timeline_reviewed_event_instance.to_dict()
# create an instance of TimelineReviewedEvent from a dict
timeline_reviewed_event_from_dict = TimelineReviewedEvent.from_dict(timeline_reviewed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


