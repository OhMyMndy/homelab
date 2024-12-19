# CheckSuitePreferencePreferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_trigger_checks** | [**List[CheckSuitePreferencePreferencesAutoTriggerChecksInner]**](CheckSuitePreferencePreferencesAutoTriggerChecksInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.check_suite_preference_preferences import CheckSuitePreferencePreferences

# TODO update the JSON string below
json = "{}"
# create an instance of CheckSuitePreferencePreferences from a JSON string
check_suite_preference_preferences_instance = CheckSuitePreferencePreferences.from_json(json)
# print the JSON string representation of the object
print(CheckSuitePreferencePreferences.to_json())

# convert the object into a dict
check_suite_preference_preferences_dict = check_suite_preference_preferences_instance.to_dict()
# create an instance of CheckSuitePreferencePreferences from a dict
check_suite_preference_preferences_from_dict = CheckSuitePreferencePreferences.from_dict(check_suite_preference_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


