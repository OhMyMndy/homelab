# ListNetworkFlowLogs200Response

A structured response for all of a Tailnet's network flow logs over a period of time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[NetworkFlowLog]**](NetworkFlowLog.md) | Matching log entries, ordered chronologically. | [optional] 

## Example

```python
from tailscale_openapi.models.list_network_flow_logs200_response import ListNetworkFlowLogs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListNetworkFlowLogs200Response from a JSON string
list_network_flow_logs200_response_instance = ListNetworkFlowLogs200Response.from_json(json)
# print the JSON string representation of the object
print(ListNetworkFlowLogs200Response.to_json())

# convert the object into a dict
list_network_flow_logs200_response_dict = list_network_flow_logs200_response_instance.to_dict()
# create an instance of ListNetworkFlowLogs200Response from a dict
list_network_flow_logs200_response_from_dict = ListNetworkFlowLogs200Response.from_dict(list_network_flow_logs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


