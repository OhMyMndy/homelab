# PaginatedUserConsentList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[UserConsent]**](UserConsent.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_user_consent_list import PaginatedUserConsentList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserConsentList from a JSON string
paginated_user_consent_list_instance = PaginatedUserConsentList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserConsentList.to_json())

# convert the object into a dict
paginated_user_consent_list_dict = paginated_user_consent_list_instance.to_dict()
# create an instance of PaginatedUserConsentList from a dict
paginated_user_consent_list_from_dict = PaginatedUserConsentList.from_dict(paginated_user_consent_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


