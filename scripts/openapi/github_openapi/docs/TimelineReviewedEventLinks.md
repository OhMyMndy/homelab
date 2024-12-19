# TimelineReviewedEventLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html** | [**TimelineReviewedEventLinksHtml**](TimelineReviewedEventLinksHtml.md) |  | 
**pull_request** | [**TimelineReviewedEventLinksHtml**](TimelineReviewedEventLinksHtml.md) |  | 

## Example

```python
from github_openapi.models.timeline_reviewed_event_links import TimelineReviewedEventLinks

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineReviewedEventLinks from a JSON string
timeline_reviewed_event_links_instance = TimelineReviewedEventLinks.from_json(json)
# print the JSON string representation of the object
print(TimelineReviewedEventLinks.to_json())

# convert the object into a dict
timeline_reviewed_event_links_dict = timeline_reviewed_event_links_instance.to_dict()
# create an instance of TimelineReviewedEventLinks from a dict
timeline_reviewed_event_links_from_dict = TimelineReviewedEventLinks.from_dict(timeline_reviewed_event_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


