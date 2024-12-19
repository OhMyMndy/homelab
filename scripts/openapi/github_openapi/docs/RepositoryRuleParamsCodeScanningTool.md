# RepositoryRuleParamsCodeScanningTool

A tool that must provide code scanning results for this rule to pass.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts_threshold** | **str** | The severity level at which code scanning results that raise alerts block a reference update. For more information on alert severity levels, see \&quot;[About code scanning alerts](https://docs.github.com/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-severity-and-security-severity-levels).\&quot; | 
**security_alerts_threshold** | **str** | The severity level at which code scanning results that raise security alerts block a reference update. For more information on security severity levels, see \&quot;[About code scanning alerts](https://docs.github.com/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-severity-and-security-severity-levels).\&quot; | 
**tool** | **str** | The name of a code scanning tool | 

## Example

```python
from github_openapi.models.repository_rule_params_code_scanning_tool import RepositoryRuleParamsCodeScanningTool

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleParamsCodeScanningTool from a JSON string
repository_rule_params_code_scanning_tool_instance = RepositoryRuleParamsCodeScanningTool.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleParamsCodeScanningTool.to_json())

# convert the object into a dict
repository_rule_params_code_scanning_tool_dict = repository_rule_params_code_scanning_tool_instance.to_dict()
# create an instance of RepositoryRuleParamsCodeScanningTool from a dict
repository_rule_params_code_scanning_tool_from_dict = RepositoryRuleParamsCodeScanningTool.from_dict(repository_rule_params_code_scanning_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


