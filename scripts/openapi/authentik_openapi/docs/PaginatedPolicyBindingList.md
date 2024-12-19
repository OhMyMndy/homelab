# PaginatedPolicyBindingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[PolicyBinding]**](PolicyBinding.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_policy_binding_list import PaginatedPolicyBindingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPolicyBindingList from a JSON string
paginated_policy_binding_list_instance = PaginatedPolicyBindingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPolicyBindingList.to_json())

# convert the object into a dict
paginated_policy_binding_list_dict = paginated_policy_binding_list_instance.to_dict()
# create an instance of PaginatedPolicyBindingList from a dict
paginated_policy_binding_list_from_dict = PaginatedPolicyBindingList.from_dict(paginated_policy_binding_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


