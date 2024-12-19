# PaginatedPolicyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Policy]**](Policy.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_policy_list import PaginatedPolicyList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPolicyList from a JSON string
paginated_policy_list_instance = PaginatedPolicyList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPolicyList.to_json())

# convert the object into a dict
paginated_policy_list_dict = paginated_policy_list_instance.to_dict()
# create an instance of PaginatedPolicyList from a dict
paginated_policy_list_from_dict = PaginatedPolicyList.from_dict(paginated_policy_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


