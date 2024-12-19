# PaginatedEmailStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[EmailStage]**](EmailStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_email_stage_list import PaginatedEmailStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEmailStageList from a JSON string
paginated_email_stage_list_instance = PaginatedEmailStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedEmailStageList.to_json())

# convert the object into a dict
paginated_email_stage_list_dict = paginated_email_stage_list_instance.to_dict()
# create an instance of PaginatedEmailStageList from a dict
paginated_email_stage_list_from_dict = PaginatedEmailStageList.from_dict(paginated_email_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


