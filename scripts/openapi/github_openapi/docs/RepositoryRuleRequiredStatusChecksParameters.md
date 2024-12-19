# RepositoryRuleRequiredStatusChecksParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**do_not_enforce_on_create** | **bool** | Allow repositories and branches to be created if a check would otherwise prohibit it. | [optional] 
**required_status_checks** | [**List[RepositoryRuleParamsStatusCheckConfiguration]**](RepositoryRuleParamsStatusCheckConfiguration.md) | Status checks that are required. | 
**strict_required_status_checks_policy** | **bool** | Whether pull requests targeting a matching branch must be tested with the latest code. This setting will not take effect unless at least one status check is enabled. | 

## Example

```python
from github_openapi.models.repository_rule_required_status_checks_parameters import RepositoryRuleRequiredStatusChecksParameters

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleRequiredStatusChecksParameters from a JSON string
repository_rule_required_status_checks_parameters_instance = RepositoryRuleRequiredStatusChecksParameters.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleRequiredStatusChecksParameters.to_json())

# convert the object into a dict
repository_rule_required_status_checks_parameters_dict = repository_rule_required_status_checks_parameters_instance.to_dict()
# create an instance of RepositoryRuleRequiredStatusChecksParameters from a dict
repository_rule_required_status_checks_parameters_from_dict = RepositoryRuleRequiredStatusChecksParameters.from_dict(repository_rule_required_status_checks_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


