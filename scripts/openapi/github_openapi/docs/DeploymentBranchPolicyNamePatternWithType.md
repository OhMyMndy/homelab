# DeploymentBranchPolicyNamePatternWithType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name pattern that branches or tags must match in order to deploy to the environment.  Wildcard characters will not match &#x60;/&#x60;. For example, to match branches that begin with &#x60;release/&#x60; and contain an additional single slash, use &#x60;release/*/*&#x60;. For more information about pattern matching syntax, see the [Ruby File.fnmatch documentation](https://ruby-doc.org/core-2.5.1/File.html#method-c-fnmatch). | 
**type** | **str** | Whether this rule targets a branch or tag | [optional] 

## Example

```python
from github_openapi.models.deployment_branch_policy_name_pattern_with_type import DeploymentBranchPolicyNamePatternWithType

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentBranchPolicyNamePatternWithType from a JSON string
deployment_branch_policy_name_pattern_with_type_instance = DeploymentBranchPolicyNamePatternWithType.from_json(json)
# print the JSON string representation of the object
print(DeploymentBranchPolicyNamePatternWithType.to_json())

# convert the object into a dict
deployment_branch_policy_name_pattern_with_type_dict = deployment_branch_policy_name_pattern_with_type_instance.to_dict()
# create an instance of DeploymentBranchPolicyNamePatternWithType from a dict
deployment_branch_policy_name_pattern_with_type_from_dict = DeploymentBranchPolicyNamePatternWithType.from_dict(deployment_branch_policy_name_pattern_with_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


