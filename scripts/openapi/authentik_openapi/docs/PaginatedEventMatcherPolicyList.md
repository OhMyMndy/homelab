# PaginatedEventMatcherPolicyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[EventMatcherPolicy]**](EventMatcherPolicy.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_event_matcher_policy_list import PaginatedEventMatcherPolicyList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEventMatcherPolicyList from a JSON string
paginated_event_matcher_policy_list_instance = PaginatedEventMatcherPolicyList.from_json(json)
# print the JSON string representation of the object
print(PaginatedEventMatcherPolicyList.to_json())

# convert the object into a dict
paginated_event_matcher_policy_list_dict = paginated_event_matcher_policy_list_instance.to_dict()
# create an instance of PaginatedEventMatcherPolicyList from a dict
paginated_event_matcher_policy_list_from_dict = PaginatedEventMatcherPolicyList.from_dict(paginated_event_matcher_policy_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


