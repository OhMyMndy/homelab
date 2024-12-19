# PaginatedExpressionPolicyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[ExpressionPolicy]**](ExpressionPolicy.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_expression_policy_list import PaginatedExpressionPolicyList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedExpressionPolicyList from a JSON string
paginated_expression_policy_list_instance = PaginatedExpressionPolicyList.from_json(json)
# print the JSON string representation of the object
print(PaginatedExpressionPolicyList.to_json())

# convert the object into a dict
paginated_expression_policy_list_dict = paginated_expression_policy_list_instance.to_dict()
# create an instance of PaginatedExpressionPolicyList from a dict
paginated_expression_policy_list_from_dict = PaginatedExpressionPolicyList.from_dict(paginated_expression_policy_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


