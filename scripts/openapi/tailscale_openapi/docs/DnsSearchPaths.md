# DnsSearchPaths


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_paths** | **List[str]** | The search domains for the given tailnet.  | 

## Example

```python
from tailscale_openapi.models.dns_search_paths import DnsSearchPaths

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSearchPaths from a JSON string
dns_search_paths_instance = DnsSearchPaths.from_json(json)
# print the JSON string representation of the object
print(DnsSearchPaths.to_json())

# convert the object into a dict
dns_search_paths_dict = dns_search_paths_instance.to_dict()
# create an instance of DnsSearchPaths from a dict
dns_search_paths_from_dict = DnsSearchPaths.from_dict(dns_search_paths_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


