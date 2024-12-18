# LogstreamEndpointPublishingStatus

Latest status of log stream publishing for a specific type of log.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_activity** | **str** | Timestamp of the most recent publishing activity, in RFC 3339 format. | 
**last_error** | **str** | The most recent error (if any). | 
**max_body_size** | **int** | The size of the largest single request body. | 
**num_bytes_sent** | **int** | Total bytes published across all requests. | 
**num_entries_sent** | **int** | The total number of entries published. | 
**num_spoofed_entries** | **int** | The number of spoofed entries published. A spoofed entry is one that failed to validate because we did not see receive a matching flow log from the other side of the connection. | 
**num_total_requests** | **int** | The total number of requests made to the streaming endpoint. | 
**num_failed_requests** | **int** | The total number of requests to the streaming endpoint that have failed. | 
**rate_bytes_sent** | **float** | The exponentially weighted moving average rate at which data is being streamed to the endpoint, in bytes per second. | 
**rate_entries_sent** | **float** | The exponentially weighted moving average rate at which entries are being sent to the endpoint, in entries per second. | 
**rate_total_requests** | **float** | The exponentially weighted moving average rate at which requests are being made to the endpoint, in requests per second. | 
**rate_failed_requests** | **float** | The exponentially weighted moving average rate at which requests are failing, in requests per second. | 

## Example

```python
from tailscale_openapi.models.logstream_endpoint_publishing_status import LogstreamEndpointPublishingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of LogstreamEndpointPublishingStatus from a JSON string
logstream_endpoint_publishing_status_instance = LogstreamEndpointPublishingStatus.from_json(json)
# print the JSON string representation of the object
print(LogstreamEndpointPublishingStatus.to_json())

# convert the object into a dict
logstream_endpoint_publishing_status_dict = logstream_endpoint_publishing_status_instance.to_dict()
# create an instance of LogstreamEndpointPublishingStatus from a dict
logstream_endpoint_publishing_status_from_dict = LogstreamEndpointPublishingStatus.from_dict(logstream_endpoint_publishing_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


