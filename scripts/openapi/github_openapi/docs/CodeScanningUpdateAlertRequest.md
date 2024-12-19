# CodeScanningUpdateAlertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**CodeScanningAlertSetState**](CodeScanningAlertSetState.md) |  | 
**dismissed_reason** | [**CodeScanningAlertDismissedReason**](CodeScanningAlertDismissedReason.md) |  | [optional] 
**dismissed_comment** | **str** | The dismissal comment associated with the dismissal of the alert. | [optional] 

## Example

```python
from github_openapi.models.code_scanning_update_alert_request import CodeScanningUpdateAlertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningUpdateAlertRequest from a JSON string
code_scanning_update_alert_request_instance = CodeScanningUpdateAlertRequest.from_json(json)
# print the JSON string representation of the object
print(CodeScanningUpdateAlertRequest.to_json())

# convert the object into a dict
code_scanning_update_alert_request_dict = code_scanning_update_alert_request_instance.to_dict()
# create an instance of CodeScanningUpdateAlertRequest from a dict
code_scanning_update_alert_request_from_dict = CodeScanningUpdateAlertRequest.from_dict(code_scanning_update_alert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


