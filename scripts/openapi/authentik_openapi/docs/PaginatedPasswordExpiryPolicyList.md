# PaginatedPasswordExpiryPolicyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[PasswordExpiryPolicy]**](PasswordExpiryPolicy.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_password_expiry_policy_list import PaginatedPasswordExpiryPolicyList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPasswordExpiryPolicyList from a JSON string
paginated_password_expiry_policy_list_instance = PaginatedPasswordExpiryPolicyList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPasswordExpiryPolicyList.to_json())

# convert the object into a dict
paginated_password_expiry_policy_list_dict = paginated_password_expiry_policy_list_instance.to_dict()
# create an instance of PaginatedPasswordExpiryPolicyList from a dict
paginated_password_expiry_policy_list_from_dict = PaginatedPasswordExpiryPolicyList.from_dict(paginated_password_expiry_policy_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


