# PaginatedPasswordPolicyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[PasswordPolicy]**](PasswordPolicy.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_password_policy_list import PaginatedPasswordPolicyList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPasswordPolicyList from a JSON string
paginated_password_policy_list_instance = PaginatedPasswordPolicyList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPasswordPolicyList.to_json())

# convert the object into a dict
paginated_password_policy_list_dict = paginated_password_policy_list_instance.to_dict()
# create an instance of PaginatedPasswordPolicyList from a dict
paginated_password_policy_list_from_dict = PaginatedPasswordPolicyList.from_dict(paginated_password_policy_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


