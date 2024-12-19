# PaginatedAuthenticatorWebAuthnStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[AuthenticatorWebAuthnStage]**](AuthenticatorWebAuthnStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_authenticator_web_authn_stage_list import PaginatedAuthenticatorWebAuthnStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAuthenticatorWebAuthnStageList from a JSON string
paginated_authenticator_web_authn_stage_list_instance = PaginatedAuthenticatorWebAuthnStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAuthenticatorWebAuthnStageList.to_json())

# convert the object into a dict
paginated_authenticator_web_authn_stage_list_dict = paginated_authenticator_web_authn_stage_list_instance.to_dict()
# create an instance of PaginatedAuthenticatorWebAuthnStageList from a dict
paginated_authenticator_web_authn_stage_list_from_dict = PaginatedAuthenticatorWebAuthnStageList.from_dict(paginated_authenticator_web_authn_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


