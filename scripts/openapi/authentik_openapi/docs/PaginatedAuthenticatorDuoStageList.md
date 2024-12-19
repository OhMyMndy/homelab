# PaginatedAuthenticatorDuoStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[AuthenticatorDuoStage]**](AuthenticatorDuoStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_authenticator_duo_stage_list import PaginatedAuthenticatorDuoStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAuthenticatorDuoStageList from a JSON string
paginated_authenticator_duo_stage_list_instance = PaginatedAuthenticatorDuoStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAuthenticatorDuoStageList.to_json())

# convert the object into a dict
paginated_authenticator_duo_stage_list_dict = paginated_authenticator_duo_stage_list_instance.to_dict()
# create an instance of PaginatedAuthenticatorDuoStageList from a dict
paginated_authenticator_duo_stage_list_from_dict = PaginatedAuthenticatorDuoStageList.from_dict(paginated_authenticator_duo_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


