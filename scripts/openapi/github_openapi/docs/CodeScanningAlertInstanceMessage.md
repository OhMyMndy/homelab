# CodeScanningAlertInstanceMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.code_scanning_alert_instance_message import CodeScanningAlertInstanceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningAlertInstanceMessage from a JSON string
code_scanning_alert_instance_message_instance = CodeScanningAlertInstanceMessage.from_json(json)
# print the JSON string representation of the object
print(CodeScanningAlertInstanceMessage.to_json())

# convert the object into a dict
code_scanning_alert_instance_message_dict = code_scanning_alert_instance_message_instance.to_dict()
# create an instance of CodeScanningAlertInstanceMessage from a dict
code_scanning_alert_instance_message_from_dict = CodeScanningAlertInstanceMessage.from_dict(code_scanning_alert_instance_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


