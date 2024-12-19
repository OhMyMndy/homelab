# PaginatedAuthenticatorValidateStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[AuthenticatorValidateStage]**](AuthenticatorValidateStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_authenticator_validate_stage_list import PaginatedAuthenticatorValidateStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAuthenticatorValidateStageList from a JSON string
paginated_authenticator_validate_stage_list_instance = PaginatedAuthenticatorValidateStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAuthenticatorValidateStageList.to_json())

# convert the object into a dict
paginated_authenticator_validate_stage_list_dict = paginated_authenticator_validate_stage_list_instance.to_dict()
# create an instance of PaginatedAuthenticatorValidateStageList from a dict
paginated_authenticator_validate_stage_list_from_dict = PaginatedAuthenticatorValidateStageList.from_dict(paginated_authenticator_validate_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


