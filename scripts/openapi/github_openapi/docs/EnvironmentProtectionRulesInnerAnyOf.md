# EnvironmentProtectionRulesInnerAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**node_id** | **str** |  | 
**type** | **str** |  | 
**wait_timer** | **int** | The amount of time to delay a job after the job is initially triggered. The time (in minutes) must be an integer between 0 and 43,200 (30 days). | [optional] 

## Example

```python
from github_openapi.models.environment_protection_rules_inner_any_of import EnvironmentProtectionRulesInnerAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentProtectionRulesInnerAnyOf from a JSON string
environment_protection_rules_inner_any_of_instance = EnvironmentProtectionRulesInnerAnyOf.from_json(json)
# print the JSON string representation of the object
print(EnvironmentProtectionRulesInnerAnyOf.to_json())

# convert the object into a dict
environment_protection_rules_inner_any_of_dict = environment_protection_rules_inner_any_of_instance.to_dict()
# create an instance of EnvironmentProtectionRulesInnerAnyOf from a dict
environment_protection_rules_inner_any_of_from_dict = EnvironmentProtectionRulesInnerAnyOf.from_dict(environment_protection_rules_inner_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


