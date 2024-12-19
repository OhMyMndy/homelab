# DeploymentBranchPolicy

Details of a deployment branch or tag policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the branch or tag policy. | [optional] 
**node_id** | **str** |  | [optional] 
**name** | **str** | The name pattern that branches or tags must match in order to deploy to the environment. | [optional] 
**type** | **str** | Whether this rule targets a branch or tag. | [optional] 

## Example

```python
from github_openapi.models.deployment_branch_policy import DeploymentBranchPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentBranchPolicy from a JSON string
deployment_branch_policy_instance = DeploymentBranchPolicy.from_json(json)
# print the JSON string representation of the object
print(DeploymentBranchPolicy.to_json())

# convert the object into a dict
deployment_branch_policy_dict = deployment_branch_policy_instance.to_dict()
# create an instance of DeploymentBranchPolicy from a dict
deployment_branch_policy_from_dict = DeploymentBranchPolicy.from_dict(deployment_branch_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


