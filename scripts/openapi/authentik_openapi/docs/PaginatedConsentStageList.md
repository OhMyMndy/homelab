# PaginatedConsentStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[ConsentStage]**](ConsentStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_consent_stage_list import PaginatedConsentStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedConsentStageList from a JSON string
paginated_consent_stage_list_instance = PaginatedConsentStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedConsentStageList.to_json())

# convert the object into a dict
paginated_consent_stage_list_dict = paginated_consent_stage_list_instance.to_dict()
# create an instance of PaginatedConsentStageList from a dict
paginated_consent_stage_list_from_dict = PaginatedConsentStageList.from_dict(paginated_consent_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


