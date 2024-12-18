# DeviceClientConnectivityLatencyValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preferred** | **bool** | &#39;true&#39; for the node&#39;s preferred DERP server for incoming traffic.  | [optional] 
**latency_ms** | **float** | Current latency to DERP server.  | [optional] 

## Example

```python
from tailscale_openapi.models.device_client_connectivity_latency_value import DeviceClientConnectivityLatencyValue

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceClientConnectivityLatencyValue from a JSON string
device_client_connectivity_latency_value_instance = DeviceClientConnectivityLatencyValue.from_json(json)
# print the JSON string representation of the object
print(DeviceClientConnectivityLatencyValue.to_json())

# convert the object into a dict
device_client_connectivity_latency_value_dict = device_client_connectivity_latency_value_instance.to_dict()
# create an instance of DeviceClientConnectivityLatencyValue from a dict
device_client_connectivity_latency_value_from_dict = DeviceClientConnectivityLatencyValue.from_dict(device_client_connectivity_latency_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


