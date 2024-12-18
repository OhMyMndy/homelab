# DeviceClientConnectivityClientSupports

Identifies features supported by the client. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hair_pinning** | **bool** | &#39;true&#39; if your router can route connections from endpoints on your LAN back to your LAN using those endpoints’ globally-mapped IPv4 addresses/ports.  | [optional] 
**ipv6** | **bool** | &#39;true&#39; if the device OS supports IPv6, regardless of whether IPv6 internet connectivity is available.  | [optional] 
**pcp** | **bool** | &#39;true&#39; if PCP port-mapping service exists on your router.  | [optional] 
**pmp** | **bool** | &#39;true&#39; if NAT-PMP port-mapping service exists on your router.  | [optional] 
**udp** | **bool** | &#39;true&#39; if UDP traffic is enabled on the current network; if &#39;false&#39;, Tailscale may be unable to make direct connections, and will rely on our DERP servers.  | [optional] 
**upnp** | **bool** | &#39;true&#39; if UPnP port-mapping service exists on your router.  | [optional] 

## Example

```python
from tailscale_openapi.models.device_client_connectivity_client_supports import DeviceClientConnectivityClientSupports

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceClientConnectivityClientSupports from a JSON string
device_client_connectivity_client_supports_instance = DeviceClientConnectivityClientSupports.from_json(json)
# print the JSON string representation of the object
print(DeviceClientConnectivityClientSupports.to_json())

# convert the object into a dict
device_client_connectivity_client_supports_dict = device_client_connectivity_client_supports_instance.to_dict()
# create an instance of DeviceClientConnectivityClientSupports from a dict
device_client_connectivity_client_supports_from_dict = DeviceClientConnectivityClientSupports.from_dict(device_client_connectivity_client_supports_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


