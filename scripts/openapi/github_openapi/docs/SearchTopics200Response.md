# SearchTopics200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**incomplete_results** | **bool** |  | 
**items** | [**List[TopicSearchResultItem]**](TopicSearchResultItem.md) |  | 

## Example

```python
from github_openapi.models.search_topics200_response import SearchTopics200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTopics200Response from a JSON string
search_topics200_response_instance = SearchTopics200Response.from_json(json)
# print the JSON string representation of the object
print(SearchTopics200Response.to_json())

# convert the object into a dict
search_topics200_response_dict = search_topics200_response_instance.to_dict()
# create an instance of SearchTopics200Response from a dict
search_topics200_response_from_dict = SearchTopics200Response.from_dict(search_topics200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


