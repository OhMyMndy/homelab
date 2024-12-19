# RepositoryRuleRequiredDeploymentsParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required_deployment_environments** | **List[str]** | The environments that must be successfully deployed to before branches can be merged. | 

## Example

```python
from github_openapi.models.repository_rule_required_deployments_parameters import RepositoryRuleRequiredDeploymentsParameters

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleRequiredDeploymentsParameters from a JSON string
repository_rule_required_deployments_parameters_instance = RepositoryRuleRequiredDeploymentsParameters.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleRequiredDeploymentsParameters.to_json())

# convert the object into a dict
repository_rule_required_deployments_parameters_dict = repository_rule_required_deployments_parameters_instance.to_dict()
# create an instance of RepositoryRuleRequiredDeploymentsParameters from a dict
repository_rule_required_deployments_parameters_from_dict = RepositoryRuleRequiredDeploymentsParameters.from_dict(repository_rule_required_deployments_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


