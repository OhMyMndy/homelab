# ReposListDeploymentBranchPolicies200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The number of deployment branch policies for the environment. | 
**branch_policies** | [**List[DeploymentBranchPolicy]**](DeploymentBranchPolicy.md) |  | 

## Example

```python
from github_openapi.models.repos_list_deployment_branch_policies200_response import ReposListDeploymentBranchPolicies200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReposListDeploymentBranchPolicies200Response from a JSON string
repos_list_deployment_branch_policies200_response_instance = ReposListDeploymentBranchPolicies200Response.from_json(json)
# print the JSON string representation of the object
print(ReposListDeploymentBranchPolicies200Response.to_json())

# convert the object into a dict
repos_list_deployment_branch_policies200_response_dict = repos_list_deployment_branch_policies200_response_instance.to_dict()
# create an instance of ReposListDeploymentBranchPolicies200Response from a dict
repos_list_deployment_branch_policies200_response_from_dict = ReposListDeploymentBranchPolicies200Response.from_dict(repos_list_deployment_branch_policies200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


