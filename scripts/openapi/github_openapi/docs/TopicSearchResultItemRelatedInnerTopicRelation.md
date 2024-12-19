# TopicSearchResultItemRelatedInnerTopicRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**topic_id** | **int** |  | [optional] 
**relation_type** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.topic_search_result_item_related_inner_topic_relation import TopicSearchResultItemRelatedInnerTopicRelation

# TODO update the JSON string below
json = "{}"
# create an instance of TopicSearchResultItemRelatedInnerTopicRelation from a JSON string
topic_search_result_item_related_inner_topic_relation_instance = TopicSearchResultItemRelatedInnerTopicRelation.from_json(json)
# print the JSON string representation of the object
print(TopicSearchResultItemRelatedInnerTopicRelation.to_json())

# convert the object into a dict
topic_search_result_item_related_inner_topic_relation_dict = topic_search_result_item_related_inner_topic_relation_instance.to_dict()
# create an instance of TopicSearchResultItemRelatedInnerTopicRelation from a dict
topic_search_result_item_related_inner_topic_relation_from_dict = TopicSearchResultItemRelatedInnerTopicRelation.from_dict(topic_search_result_item_related_inner_topic_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


