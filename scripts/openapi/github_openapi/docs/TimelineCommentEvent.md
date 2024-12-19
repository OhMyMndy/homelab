# TimelineCommentEvent

Timeline Comment Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | 
**actor** | [**SimpleUser**](SimpleUser.md) |  | 
**id** | **int** | Unique identifier of the issue comment | 
**node_id** | **str** |  | 
**url** | **str** | URL for the issue comment | 
**body** | **str** | Contents of the issue comment | [optional] 
**body_text** | **str** |  | [optional] 
**body_html** | **str** |  | [optional] 
**html_url** | **str** |  | 
**user** | [**SimpleUser**](SimpleUser.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**issue_url** | **str** |  | 
**author_association** | [**AuthorAssociation**](AuthorAssociation.md) |  | 
**performed_via_github_app** | [**NullableIntegration**](NullableIntegration.md) |  | [optional] 
**reactions** | [**ReactionRollup**](ReactionRollup.md) |  | [optional] 

## Example

```python
from github_openapi.models.timeline_comment_event import TimelineCommentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineCommentEvent from a JSON string
timeline_comment_event_instance = TimelineCommentEvent.from_json(json)
# print the JSON string representation of the object
print(TimelineCommentEvent.to_json())

# convert the object into a dict
timeline_comment_event_dict = timeline_comment_event_instance.to_dict()
# create an instance of TimelineCommentEvent from a dict
timeline_comment_event_from_dict = TimelineCommentEvent.from_dict(timeline_comment_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


