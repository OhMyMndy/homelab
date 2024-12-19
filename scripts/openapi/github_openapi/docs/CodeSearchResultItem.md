# CodeSearchResultItem

Code Search Result Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**path** | **str** |  | 
**sha** | **str** |  | 
**url** | **str** |  | 
**git_url** | **str** |  | 
**html_url** | **str** |  | 
**repository** | [**MinimalRepository**](MinimalRepository.md) |  | 
**score** | **float** |  | 
**file_size** | **int** |  | [optional] 
**language** | **str** |  | [optional] 
**last_modified_at** | **datetime** |  | [optional] 
**line_numbers** | **List[str]** |  | [optional] 
**text_matches** | [**List[SearchResultTextMatchesInner]**](SearchResultTextMatchesInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.code_search_result_item import CodeSearchResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSearchResultItem from a JSON string
code_search_result_item_instance = CodeSearchResultItem.from_json(json)
# print the JSON string representation of the object
print(CodeSearchResultItem.to_json())

# convert the object into a dict
code_search_result_item_dict = code_search_result_item_instance.to_dict()
# create an instance of CodeSearchResultItem from a dict
code_search_result_item_from_dict = CodeSearchResultItem.from_dict(code_search_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


