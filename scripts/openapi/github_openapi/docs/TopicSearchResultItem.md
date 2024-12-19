# TopicSearchResultItem

Topic Search Result Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**display_name** | **str** |  | 
**short_description** | **str** |  | 
**description** | **str** |  | 
**created_by** | **str** |  | 
**released** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**featured** | **bool** |  | 
**curated** | **bool** |  | 
**score** | **float** |  | 
**repository_count** | **int** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**text_matches** | [**List[SearchResultTextMatchesInner]**](SearchResultTextMatchesInner.md) |  | [optional] 
**related** | [**List[TopicSearchResultItemRelatedInner]**](TopicSearchResultItemRelatedInner.md) |  | [optional] 
**aliases** | [**List[TopicSearchResultItemRelatedInner]**](TopicSearchResultItemRelatedInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.topic_search_result_item import TopicSearchResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of TopicSearchResultItem from a JSON string
topic_search_result_item_instance = TopicSearchResultItem.from_json(json)
# print the JSON string representation of the object
print(TopicSearchResultItem.to_json())

# convert the object into a dict
topic_search_result_item_dict = topic_search_result_item_instance.to_dict()
# create an instance of TopicSearchResultItem from a dict
topic_search_result_item_from_dict = TopicSearchResultItem.from_dict(topic_search_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


