# CheckSuitePreference

Check suite configuration preferences for a repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preferences** | [**CheckSuitePreferencePreferences**](CheckSuitePreferencePreferences.md) |  | 
**repository** | [**MinimalRepository**](MinimalRepository.md) |  | 

## Example

```python
from github_openapi.models.check_suite_preference import CheckSuitePreference

# TODO update the JSON string below
json = "{}"
# create an instance of CheckSuitePreference from a JSON string
check_suite_preference_instance = CheckSuitePreference.from_json(json)
# print the JSON string representation of the object
print(CheckSuitePreference.to_json())

# convert the object into a dict
check_suite_preference_dict = check_suite_preference_instance.to_dict()
# create an instance of CheckSuitePreference from a dict
check_suite_preference_from_dict = CheckSuitePreference.from_dict(check_suite_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


