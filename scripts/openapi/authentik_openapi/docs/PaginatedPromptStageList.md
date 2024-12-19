# PaginatedPromptStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[PromptStage]**](PromptStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_prompt_stage_list import PaginatedPromptStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPromptStageList from a JSON string
paginated_prompt_stage_list_instance = PaginatedPromptStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPromptStageList.to_json())

# convert the object into a dict
paginated_prompt_stage_list_dict = paginated_prompt_stage_list_instance.to_dict()
# create an instance of PaginatedPromptStageList from a dict
paginated_prompt_stage_list_from_dict = PaginatedPromptStageList.from_dict(paginated_prompt_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


