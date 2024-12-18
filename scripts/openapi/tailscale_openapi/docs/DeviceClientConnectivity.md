# DeviceClientConnectivity

clientConnectivity provides a report on the device's current physical network conditions. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | **List[str]** | Client&#39;s magicsock UDP IP:port endpoints (IPv4 or IPv6).  | [optional] 
**mapping_varies_by_dest_ip** | **bool** | &#39;true&#39; if the host&#39;s NAT mappings vary based on the destination IP.  | [optional] 
**latency** | [**Dict[str, DeviceClientConnectivityLatencyValue]**](DeviceClientConnectivityLatencyValue.md) | Map of DERP server locations and their current latency. | [optional] 
**client_supports** | [**DeviceClientConnectivityClientSupports**](DeviceClientConnectivityClientSupports.md) |  | [optional] 

## Example

```python
from tailscale_openapi.models.device_client_connectivity import DeviceClientConnectivity

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceClientConnectivity from a JSON string
device_client_connectivity_instance = DeviceClientConnectivity.from_json(json)
# print the JSON string representation of the object
print(DeviceClientConnectivity.to_json())

# convert the object into a dict
device_client_connectivity_dict = device_client_connectivity_instance.to_dict()
# create an instance of DeviceClientConnectivity from a dict
device_client_connectivity_from_dict = DeviceClientConnectivity.from_dict(device_client_connectivity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


