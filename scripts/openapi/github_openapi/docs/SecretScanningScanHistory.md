# SecretScanningScanHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incremental_scans** | [**List[SecretScanningScan]**](SecretScanningScan.md) |  | [optional] 
**pattern_update_scans** | [**List[SecretScanningScan]**](SecretScanningScan.md) |  | [optional] 
**backfill_scans** | [**List[SecretScanningScan]**](SecretScanningScan.md) |  | [optional] 
**custom_pattern_backfill_scans** | [**List[SecretScanningScanHistoryCustomPatternBackfillScansInner]**](SecretScanningScanHistoryCustomPatternBackfillScansInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.secret_scanning_scan_history import SecretScanningScanHistory

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningScanHistory from a JSON string
secret_scanning_scan_history_instance = SecretScanningScanHistory.from_json(json)
# print the JSON string representation of the object
print(SecretScanningScanHistory.to_json())

# convert the object into a dict
secret_scanning_scan_history_dict = secret_scanning_scan_history_instance.to_dict()
# create an instance of SecretScanningScanHistory from a dict
secret_scanning_scan_history_from_dict = SecretScanningScanHistory.from_dict(secret_scanning_scan_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


