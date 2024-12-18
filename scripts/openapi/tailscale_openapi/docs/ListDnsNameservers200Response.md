# ListDnsNameservers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns** | **List[str]** | DNS nameservers.  | [optional] 

## Example

```python
from tailscale_openapi.models.list_dns_nameservers200_response import ListDnsNameservers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDnsNameservers200Response from a JSON string
list_dns_nameservers200_response_instance = ListDnsNameservers200Response.from_json(json)
# print the JSON string representation of the object
print(ListDnsNameservers200Response.to_json())

# convert the object into a dict
list_dns_nameservers200_response_dict = list_dns_nameservers200_response_instance.to_dict()
# create an instance of ListDnsNameservers200Response from a dict
list_dns_nameservers200_response_from_dict = ListDnsNameservers200Response.from_dict(list_dns_nameservers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


