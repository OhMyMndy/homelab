# SetDnsNameservers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns** | **List[str]** | DNS nameservers.  | [optional] 
**magic_dns** | **bool** | Whether MagicDNS is active for this tailnet.  | [optional] 

## Example

```python
from tailscale_openapi.models.set_dns_nameservers200_response import SetDnsNameservers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetDnsNameservers200Response from a JSON string
set_dns_nameservers200_response_instance = SetDnsNameservers200Response.from_json(json)
# print the JSON string representation of the object
print(SetDnsNameservers200Response.to_json())

# convert the object into a dict
set_dns_nameservers200_response_dict = set_dns_nameservers200_response_instance.to_dict()
# create an instance of SetDnsNameservers200Response from a dict
set_dns_nameservers200_response_from_dict = SetDnsNameservers200Response.from_dict(set_dns_nameservers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


