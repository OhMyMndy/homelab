# RepositoryRuleWorkflows

Require all changes made to a targeted branch to pass the specified workflows before they can be merged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**RepositoryRuleWorkflowsParameters**](RepositoryRuleWorkflowsParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_workflows import RepositoryRuleWorkflows

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleWorkflows from a JSON string
repository_rule_workflows_instance = RepositoryRuleWorkflows.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleWorkflows.to_json())

# convert the object into a dict
repository_rule_workflows_dict = repository_rule_workflows_instance.to_dict()
# create an instance of RepositoryRuleWorkflows from a dict
repository_rule_workflows_from_dict = RepositoryRuleWorkflows.from_dict(repository_rule_workflows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


