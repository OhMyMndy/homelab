# RepositoryRuleParamsRequiredReviewerConfiguration

A reviewing team, and file patterns describing which files they must approve changes to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_patterns** | **List[str]** | Array of file patterns. Pull requests which change matching files must be approved by the specified team. File patterns use the same syntax as &#x60;.gitignore&#x60; files. | 
**minimum_approvals** | **int** | Minimum number of approvals required from the specified team. If set to zero, the team will be added to the pull request but approval is optional. | 
**reviewer_id** | **str** | Node ID of the team which must review changes to matching files. | 

## Example

```python
from github_openapi.models.repository_rule_params_required_reviewer_configuration import RepositoryRuleParamsRequiredReviewerConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleParamsRequiredReviewerConfiguration from a JSON string
repository_rule_params_required_reviewer_configuration_instance = RepositoryRuleParamsRequiredReviewerConfiguration.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleParamsRequiredReviewerConfiguration.to_json())

# convert the object into a dict
repository_rule_params_required_reviewer_configuration_dict = repository_rule_params_required_reviewer_configuration_instance.to_dict()
# create an instance of RepositoryRuleParamsRequiredReviewerConfiguration from a dict
repository_rule_params_required_reviewer_configuration_from_dict = RepositoryRuleParamsRequiredReviewerConfiguration.from_dict(repository_rule_params_required_reviewer_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


