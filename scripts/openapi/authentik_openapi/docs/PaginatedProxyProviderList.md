# PaginatedProxyProviderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[ProxyProvider]**](ProxyProvider.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_proxy_provider_list import PaginatedProxyProviderList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProxyProviderList from a JSON string
paginated_proxy_provider_list_instance = PaginatedProxyProviderList.from_json(json)
# print the JSON string representation of the object
print(PaginatedProxyProviderList.to_json())

# convert the object into a dict
paginated_proxy_provider_list_dict = paginated_proxy_provider_list_instance.to_dict()
# create an instance of PaginatedProxyProviderList from a dict
paginated_proxy_provider_list_from_dict = PaginatedProxyProviderList.from_dict(paginated_proxy_provider_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


