# PaginatedDummyPolicyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[DummyPolicy]**](DummyPolicy.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_dummy_policy_list import PaginatedDummyPolicyList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDummyPolicyList from a JSON string
paginated_dummy_policy_list_instance = PaginatedDummyPolicyList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDummyPolicyList.to_json())

# convert the object into a dict
paginated_dummy_policy_list_dict = paginated_dummy_policy_list_instance.to_dict()
# create an instance of PaginatedDummyPolicyList from a dict
paginated_dummy_policy_list_from_dict = PaginatedDummyPolicyList.from_dict(paginated_dummy_policy_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


