# PaginatedOAuth2ProviderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[OAuth2Provider]**](OAuth2Provider.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_o_auth2_provider_list import PaginatedOAuth2ProviderList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedOAuth2ProviderList from a JSON string
paginated_o_auth2_provider_list_instance = PaginatedOAuth2ProviderList.from_json(json)
# print the JSON string representation of the object
print(PaginatedOAuth2ProviderList.to_json())

# convert the object into a dict
paginated_o_auth2_provider_list_dict = paginated_o_auth2_provider_list_instance.to_dict()
# create an instance of PaginatedOAuth2ProviderList from a dict
paginated_o_auth2_provider_list_from_dict = PaginatedOAuth2ProviderList.from_dict(paginated_o_auth2_provider_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


