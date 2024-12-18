# PostureIntegrationStatus

Most recent status for this integration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_sync** | **str** | Timestamp of the last synchronization with the device posture provider, in RFC 3339 format. | [optional] 
**error** | **str** | If the last synchronization failed, this shows the error message associated with the failed synchronization. | [optional] 
**provider_host_count** | **int** | The number of devices known to the provider. | [optional] 
**matched_count** | **int** | The number of Tailscale nodes that were matched with provider. | [optional] 
**possible_matched_count** | **int** | The number of Tailscale nodes with identifiers for matching. | [optional] 

## Example

```python
from tailscale_openapi.models.posture_integration_status import PostureIntegrationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PostureIntegrationStatus from a JSON string
posture_integration_status_instance = PostureIntegrationStatus.from_json(json)
# print the JSON string representation of the object
print(PostureIntegrationStatus.to_json())

# convert the object into a dict
posture_integration_status_dict = posture_integration_status_instance.to_dict()
# create an instance of PostureIntegrationStatus from a dict
posture_integration_status_from_dict = PostureIntegrationStatus.from_dict(posture_integration_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


