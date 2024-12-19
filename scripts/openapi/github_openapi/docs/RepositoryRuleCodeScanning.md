# RepositoryRuleCodeScanning

Choose which tools must provide code scanning results before the reference is updated. When configured, code scanning must be enabled and have results for both the commit and the reference being updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**RepositoryRuleCodeScanningParameters**](RepositoryRuleCodeScanningParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_code_scanning import RepositoryRuleCodeScanning

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleCodeScanning from a JSON string
repository_rule_code_scanning_instance = RepositoryRuleCodeScanning.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleCodeScanning.to_json())

# convert the object into a dict
repository_rule_code_scanning_dict = repository_rule_code_scanning_instance.to_dict()
# create an instance of RepositoryRuleCodeScanning from a dict
repository_rule_code_scanning_from_dict = RepositoryRuleCodeScanning.from_dict(repository_rule_code_scanning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


