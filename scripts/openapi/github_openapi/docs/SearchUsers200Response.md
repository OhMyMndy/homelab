# SearchUsers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**incomplete_results** | **bool** |  | 
**items** | [**List[UserSearchResultItem]**](UserSearchResultItem.md) |  | 

## Example

```python
from github_openapi.models.search_users200_response import SearchUsers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchUsers200Response from a JSON string
search_users200_response_instance = SearchUsers200Response.from_json(json)
# print the JSON string representation of the object
print(SearchUsers200Response.to_json())

# convert the object into a dict
search_users200_response_dict = search_users200_response_instance.to_dict()
# create an instance of SearchUsers200Response from a dict
search_users200_response_from_dict = SearchUsers200Response.from_dict(search_users200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


