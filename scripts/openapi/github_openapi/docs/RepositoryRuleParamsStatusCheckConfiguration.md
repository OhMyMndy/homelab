# RepositoryRuleParamsStatusCheckConfiguration

Required status check

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | The status check context name that must be present on the commit. | 
**integration_id** | **int** | The optional integration ID that this status check must originate from. | [optional] 

## Example

```python
from github_openapi.models.repository_rule_params_status_check_configuration import RepositoryRuleParamsStatusCheckConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleParamsStatusCheckConfiguration from a JSON string
repository_rule_params_status_check_configuration_instance = RepositoryRuleParamsStatusCheckConfiguration.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleParamsStatusCheckConfiguration.to_json())

# convert the object into a dict
repository_rule_params_status_check_configuration_dict = repository_rule_params_status_check_configuration_instance.to_dict()
# create an instance of RepositoryRuleParamsStatusCheckConfiguration from a dict
repository_rule_params_status_check_configuration_from_dict = RepositoryRuleParamsStatusCheckConfiguration.from_dict(repository_rule_params_status_check_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


