# SecretScanningScan

Information on a single scan performed by secret scanning on the repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of scan | [optional] 
**status** | **str** | The state of the scan. Either \&quot;completed\&quot;, \&quot;running\&quot;, or \&quot;pending\&quot; | [optional] 
**completed_at** | **datetime** | The time that the scan was completed. Empty if the scan is running | [optional] 
**started_at** | **datetime** | The time that the scan was started. Empty if the scan is pending | [optional] 

## Example

```python
from github_openapi.models.secret_scanning_scan import SecretScanningScan

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningScan from a JSON string
secret_scanning_scan_instance = SecretScanningScan.from_json(json)
# print the JSON string representation of the object
print(SecretScanningScan.to_json())

# convert the object into a dict
secret_scanning_scan_dict = secret_scanning_scan_instance.to_dict()
# create an instance of SecretScanningScan from a dict
secret_scanning_scan_from_dict = SecretScanningScan.from_dict(secret_scanning_scan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


