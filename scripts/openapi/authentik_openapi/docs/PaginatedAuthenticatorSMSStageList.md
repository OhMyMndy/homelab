# PaginatedAuthenticatorSMSStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[AuthenticatorSMSStage]**](AuthenticatorSMSStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_authenticator_sms_stage_list import PaginatedAuthenticatorSMSStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAuthenticatorSMSStageList from a JSON string
paginated_authenticator_sms_stage_list_instance = PaginatedAuthenticatorSMSStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAuthenticatorSMSStageList.to_json())

# convert the object into a dict
paginated_authenticator_sms_stage_list_dict = paginated_authenticator_sms_stage_list_instance.to_dict()
# create an instance of PaginatedAuthenticatorSMSStageList from a dict
paginated_authenticator_sms_stage_list_from_dict = PaginatedAuthenticatorSMSStageList.from_dict(paginated_authenticator_sms_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


