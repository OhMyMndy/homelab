# PaginatedAuthenticatorTOTPStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[AuthenticatorTOTPStage]**](AuthenticatorTOTPStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_authenticator_totp_stage_list import PaginatedAuthenticatorTOTPStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAuthenticatorTOTPStageList from a JSON string
paginated_authenticator_totp_stage_list_instance = PaginatedAuthenticatorTOTPStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAuthenticatorTOTPStageList.to_json())

# convert the object into a dict
paginated_authenticator_totp_stage_list_dict = paginated_authenticator_totp_stage_list_instance.to_dict()
# create an instance of PaginatedAuthenticatorTOTPStageList from a dict
paginated_authenticator_totp_stage_list_from_dict = PaginatedAuthenticatorTOTPStageList.from_dict(paginated_authenticator_totp_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


