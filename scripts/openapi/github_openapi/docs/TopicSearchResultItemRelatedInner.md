# TopicSearchResultItemRelatedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic_relation** | [**TopicSearchResultItemRelatedInnerTopicRelation**](TopicSearchResultItemRelatedInnerTopicRelation.md) |  | [optional] 

## Example

```python
from github_openapi.models.topic_search_result_item_related_inner import TopicSearchResultItemRelatedInner

# TODO update the JSON string below
json = "{}"
# create an instance of TopicSearchResultItemRelatedInner from a JSON string
topic_search_result_item_related_inner_instance = TopicSearchResultItemRelatedInner.from_json(json)
# print the JSON string representation of the object
print(TopicSearchResultItemRelatedInner.to_json())

# convert the object into a dict
topic_search_result_item_related_inner_dict = topic_search_result_item_related_inner_instance.to_dict()
# create an instance of TopicSearchResultItemRelatedInner from a dict
topic_search_result_item_related_inner_from_dict = TopicSearchResultItemRelatedInner.from_dict(topic_search_result_item_related_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


