# ChecksSetSuitesPreferencesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_trigger_checks** | [**List[ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner]**](ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner.md) | Enables or disables automatic creation of CheckSuite events upon pushes to the repository. Enabled by default. | [optional] 

## Example

```python
from github_openapi.models.checks_set_suites_preferences_request import ChecksSetSuitesPreferencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChecksSetSuitesPreferencesRequest from a JSON string
checks_set_suites_preferences_request_instance = ChecksSetSuitesPreferencesRequest.from_json(json)
# print the JSON string representation of the object
print(ChecksSetSuitesPreferencesRequest.to_json())

# convert the object into a dict
checks_set_suites_preferences_request_dict = checks_set_suites_preferences_request_instance.to_dict()
# create an instance of ChecksSetSuitesPreferencesRequest from a dict
checks_set_suites_preferences_request_from_dict = ChecksSetSuitesPreferencesRequest.from_dict(checks_set_suites_preferences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


