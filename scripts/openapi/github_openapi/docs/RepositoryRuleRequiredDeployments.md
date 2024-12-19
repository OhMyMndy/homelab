# RepositoryRuleRequiredDeployments

Choose which environments must be successfully deployed to before refs can be pushed into a ref that matches this rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**RepositoryRuleRequiredDeploymentsParameters**](RepositoryRuleRequiredDeploymentsParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_required_deployments import RepositoryRuleRequiredDeployments

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleRequiredDeployments from a JSON string
repository_rule_required_deployments_instance = RepositoryRuleRequiredDeployments.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleRequiredDeployments.to_json())

# convert the object into a dict
repository_rule_required_deployments_dict = repository_rule_required_deployments_instance.to_dict()
# create an instance of RepositoryRuleRequiredDeployments from a dict
repository_rule_required_deployments_from_dict = RepositoryRuleRequiredDeployments.from_dict(repository_rule_required_deployments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


