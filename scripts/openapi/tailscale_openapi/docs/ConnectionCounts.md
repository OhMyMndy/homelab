# ConnectionCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proto** | **str** | IP protocol name (or number if no name used). | [optional] 
**src** | **str** | Source addr:port. | [optional] 
**dst** | **str** | Destination addr:port. | [optional] 
**tx_pkts** | **int** | Number of packets sent. | [optional] 
**tx_bytes** | **int** | Number of bytes sent. | [optional] 
**rx_pkts** | **int** | Number of packets received. | [optional] 
**rx_bytes** | **int** | Number of bytes received. | [optional] 

## Example

```python
from tailscale_openapi.models.connection_counts import ConnectionCounts

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionCounts from a JSON string
connection_counts_instance = ConnectionCounts.from_json(json)
# print the JSON string representation of the object
print(ConnectionCounts.to_json())

# convert the object into a dict
connection_counts_dict = connection_counts_instance.to_dict()
# create an instance of ConnectionCounts from a dict
connection_counts_from_dict = ConnectionCounts.from_dict(connection_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


