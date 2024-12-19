# SecretScanningUpdateAlertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**SecretScanningAlertState**](SecretScanningAlertState.md) |  | 
**resolution** | [**SecretScanningAlertResolution**](SecretScanningAlertResolution.md) |  | [optional] 
**resolution_comment** | **str** | An optional comment when closing an alert. Cannot be updated or deleted. Must be &#x60;null&#x60; when changing &#x60;state&#x60; to &#x60;open&#x60;. | [optional] 

## Example

```python
from github_openapi.models.secret_scanning_update_alert_request import SecretScanningUpdateAlertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningUpdateAlertRequest from a JSON string
secret_scanning_update_alert_request_instance = SecretScanningUpdateAlertRequest.from_json(json)
# print the JSON string representation of the object
print(SecretScanningUpdateAlertRequest.to_json())

# convert the object into a dict
secret_scanning_update_alert_request_dict = secret_scanning_update_alert_request_instance.to_dict()
# create an instance of SecretScanningUpdateAlertRequest from a dict
secret_scanning_update_alert_request_from_dict = SecretScanningUpdateAlertRequest.from_dict(secret_scanning_update_alert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


