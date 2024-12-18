# NetworkFlowLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logged** | **str** | Timestamp of the flow log, in RFC 3339 format. | [optional] 
**node_id** | **str** | Identifier of the node. | [optional] 
**start** | **str** | Time at which flow started, in RFC 3339 format. | [optional] 
**end** | **str** | Time at which flow ended, in RFC 3339 format. | [optional] 
**virtual_traffic** | [**List[ConnectionCounts]**](ConnectionCounts.md) |  | [optional] 
**subnet_traffic** | [**List[ConnectionCounts]**](ConnectionCounts.md) |  | [optional] 
**exit_traffic** | [**List[ConnectionCounts]**](ConnectionCounts.md) |  | [optional] 
**physical_traffic** | [**List[ConnectionCounts]**](ConnectionCounts.md) |  | [optional] 

## Example

```python
from tailscale_openapi.models.network_flow_log import NetworkFlowLog

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkFlowLog from a JSON string
network_flow_log_instance = NetworkFlowLog.from_json(json)
# print the JSON string representation of the object
print(NetworkFlowLog.to_json())

# convert the object into a dict
network_flow_log_dict = network_flow_log_instance.to_dict()
# create an instance of NetworkFlowLog from a dict
network_flow_log_from_dict = NetworkFlowLog.from_dict(network_flow_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


