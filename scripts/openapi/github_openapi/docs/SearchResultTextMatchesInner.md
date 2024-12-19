# SearchResultTextMatchesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_url** | **str** |  | [optional] 
**object_type** | **str** |  | [optional] 
**var_property** | **str** |  | [optional] 
**fragment** | **str** |  | [optional] 
**matches** | [**List[SearchResultTextMatchesInnerMatchesInner]**](SearchResultTextMatchesInnerMatchesInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.search_result_text_matches_inner import SearchResultTextMatchesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultTextMatchesInner from a JSON string
search_result_text_matches_inner_instance = SearchResultTextMatchesInner.from_json(json)
# print the JSON string representation of the object
print(SearchResultTextMatchesInner.to_json())

# convert the object into a dict
search_result_text_matches_inner_dict = search_result_text_matches_inner_instance.to_dict()
# create an instance of SearchResultTextMatchesInner from a dict
search_result_text_matches_inner_from_dict = SearchResultTextMatchesInner.from_dict(search_result_text_matches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


