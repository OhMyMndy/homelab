# DnsPreferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**magic_dns** | **bool** | Whether MagicDNS is active for this tailnet.  | 

## Example

```python
from tailscale_openapi.models.dns_preferences import DnsPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of DnsPreferences from a JSON string
dns_preferences_instance = DnsPreferences.from_json(json)
# print the JSON string representation of the object
print(DnsPreferences.to_json())

# convert the object into a dict
dns_preferences_dict = dns_preferences_instance.to_dict()
# create an instance of DnsPreferences from a dict
dns_preferences_from_dict = DnsPreferences.from_dict(dns_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


