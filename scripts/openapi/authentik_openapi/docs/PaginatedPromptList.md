# PaginatedPromptList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Prompt]**](Prompt.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_prompt_list import PaginatedPromptList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPromptList from a JSON string
paginated_prompt_list_instance = PaginatedPromptList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPromptList.to_json())

# convert the object into a dict
paginated_prompt_list_dict = paginated_prompt_list_instance.to_dict()
# create an instance of PaginatedPromptList from a dict
paginated_prompt_list_from_dict = PaginatedPromptList.from_dict(paginated_prompt_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


