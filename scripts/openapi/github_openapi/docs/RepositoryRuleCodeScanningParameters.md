# RepositoryRuleCodeScanningParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_scanning_tools** | [**List[RepositoryRuleParamsCodeScanningTool]**](RepositoryRuleParamsCodeScanningTool.md) | Tools that must provide code scanning results for this rule to pass. | 

## Example

```python
from github_openapi.models.repository_rule_code_scanning_parameters import RepositoryRuleCodeScanningParameters

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleCodeScanningParameters from a JSON string
repository_rule_code_scanning_parameters_instance = RepositoryRuleCodeScanningParameters.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleCodeScanningParameters.to_json())

# convert the object into a dict
repository_rule_code_scanning_parameters_dict = repository_rule_code_scanning_parameters_instance.to_dict()
# create an instance of RepositoryRuleCodeScanningParameters from a dict
repository_rule_code_scanning_parameters_from_dict = RepositoryRuleCodeScanningParameters.from_dict(repository_rule_code_scanning_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


