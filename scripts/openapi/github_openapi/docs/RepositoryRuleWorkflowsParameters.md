# RepositoryRuleWorkflowsParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**do_not_enforce_on_create** | **bool** | Allow repositories and branches to be created if a check would otherwise prohibit it. | [optional] 
**workflows** | [**List[RepositoryRuleParamsWorkflowFileReference]**](RepositoryRuleParamsWorkflowFileReference.md) | Workflows that must pass for this rule to pass. | 

## Example

```python
from github_openapi.models.repository_rule_workflows_parameters import RepositoryRuleWorkflowsParameters

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleWorkflowsParameters from a JSON string
repository_rule_workflows_parameters_instance = RepositoryRuleWorkflowsParameters.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleWorkflowsParameters.to_json())

# convert the object into a dict
repository_rule_workflows_parameters_dict = repository_rule_workflows_parameters_instance.to_dict()
# create an instance of RepositoryRuleWorkflowsParameters from a dict
repository_rule_workflows_parameters_from_dict = RepositoryRuleWorkflowsParameters.from_dict(repository_rule_workflows_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


