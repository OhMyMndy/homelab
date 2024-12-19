# RepositoryRuleParamsWorkflowFileReference

A workflow that must run for this rule to pass

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path to the workflow file | 
**ref** | **str** | The ref (branch or tag) of the workflow file to use | [optional] 
**repository_id** | **int** | The ID of the repository where the workflow is defined | 
**sha** | **str** | The commit SHA of the workflow file to use | [optional] 

## Example

```python
from github_openapi.models.repository_rule_params_workflow_file_reference import RepositoryRuleParamsWorkflowFileReference

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleParamsWorkflowFileReference from a JSON string
repository_rule_params_workflow_file_reference_instance = RepositoryRuleParamsWorkflowFileReference.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleParamsWorkflowFileReference.to_json())

# convert the object into a dict
repository_rule_params_workflow_file_reference_dict = repository_rule_params_workflow_file_reference_instance.to_dict()
# create an instance of RepositoryRuleParamsWorkflowFileReference from a dict
repository_rule_params_workflow_file_reference_from_dict = RepositoryRuleParamsWorkflowFileReference.from_dict(repository_rule_params_workflow_file_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


