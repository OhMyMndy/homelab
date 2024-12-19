# ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** | The &#x60;id&#x60; of the GitHub App. | 
**setting** | **bool** | Set to &#x60;true&#x60; to enable automatic creation of CheckSuite events upon pushes to the repository, or &#x60;false&#x60; to disable them. | [default to True]

## Example

```python
from github_openapi.models.checks_set_suites_preferences_request_auto_trigger_checks_inner import ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner from a JSON string
checks_set_suites_preferences_request_auto_trigger_checks_inner_instance = ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner.from_json(json)
# print the JSON string representation of the object
print(ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner.to_json())

# convert the object into a dict
checks_set_suites_preferences_request_auto_trigger_checks_inner_dict = checks_set_suites_preferences_request_auto_trigger_checks_inner_instance.to_dict()
# create an instance of ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner from a dict
checks_set_suites_preferences_request_auto_trigger_checks_inner_from_dict = ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner.from_dict(checks_set_suites_preferences_request_auto_trigger_checks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


