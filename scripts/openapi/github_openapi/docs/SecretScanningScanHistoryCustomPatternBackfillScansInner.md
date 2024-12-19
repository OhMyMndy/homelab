# SecretScanningScanHistoryCustomPatternBackfillScansInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of scan | [optional] 
**status** | **str** | The state of the scan. Either \&quot;completed\&quot;, \&quot;running\&quot;, or \&quot;pending\&quot; | [optional] 
**completed_at** | **datetime** | The time that the scan was completed. Empty if the scan is running | [optional] 
**started_at** | **datetime** | The time that the scan was started. Empty if the scan is pending | [optional] 
**pattern_name** | **str** | Name of the custom pattern for custom pattern scans | [optional] 
**pattern_scope** | **str** | Level at which the custom pattern is defined, one of \&quot;repository\&quot;, \&quot;organization\&quot;, or \&quot;enterprise\&quot; | [optional] 

## Example

```python
from github_openapi.models.secret_scanning_scan_history_custom_pattern_backfill_scans_inner import SecretScanningScanHistoryCustomPatternBackfillScansInner

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningScanHistoryCustomPatternBackfillScansInner from a JSON string
secret_scanning_scan_history_custom_pattern_backfill_scans_inner_instance = SecretScanningScanHistoryCustomPatternBackfillScansInner.from_json(json)
# print the JSON string representation of the object
print(SecretScanningScanHistoryCustomPatternBackfillScansInner.to_json())

# convert the object into a dict
secret_scanning_scan_history_custom_pattern_backfill_scans_inner_dict = secret_scanning_scan_history_custom_pattern_backfill_scans_inner_instance.to_dict()
# create an instance of SecretScanningScanHistoryCustomPatternBackfillScansInner from a dict
secret_scanning_scan_history_custom_pattern_backfill_scans_inner_from_dict = SecretScanningScanHistoryCustomPatternBackfillScansInner.from_dict(secret_scanning_scan_history_custom_pattern_backfill_scans_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


