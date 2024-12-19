# PaginatedAuthenticatorStaticStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[AuthenticatorStaticStage]**](AuthenticatorStaticStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_authenticator_static_stage_list import PaginatedAuthenticatorStaticStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAuthenticatorStaticStageList from a JSON string
paginated_authenticator_static_stage_list_instance = PaginatedAuthenticatorStaticStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAuthenticatorStaticStageList.to_json())

# convert the object into a dict
paginated_authenticator_static_stage_list_dict = paginated_authenticator_static_stage_list_instance.to_dict()
# create an instance of PaginatedAuthenticatorStaticStageList from a dict
paginated_authenticator_static_stage_list_from_dict = PaginatedAuthenticatorStaticStageList.from_dict(paginated_authenticator_static_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


