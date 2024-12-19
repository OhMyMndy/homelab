# PaginatedReputationPolicyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[ReputationPolicy]**](ReputationPolicy.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_reputation_policy_list import PaginatedReputationPolicyList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedReputationPolicyList from a JSON string
paginated_reputation_policy_list_instance = PaginatedReputationPolicyList.from_json(json)
# print the JSON string representation of the object
print(PaginatedReputationPolicyList.to_json())

# convert the object into a dict
paginated_reputation_policy_list_dict = paginated_reputation_policy_list_instance.to_dict()
# create an instance of PaginatedReputationPolicyList from a dict
paginated_reputation_policy_list_from_dict = PaginatedReputationPolicyList.from_dict(paginated_reputation_policy_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


