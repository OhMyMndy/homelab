# DeploymentBranchPolicySettings

The type of deployment branch policy for this environment. To allow all branches to deploy, set to `null`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protected_branches** | **bool** | Whether only branches with branch protection rules can deploy to this environment. If &#x60;protected_branches&#x60; is &#x60;true&#x60;, &#x60;custom_branch_policies&#x60; must be &#x60;false&#x60;; if &#x60;protected_branches&#x60; is &#x60;false&#x60;, &#x60;custom_branch_policies&#x60; must be &#x60;true&#x60;. | 
**custom_branch_policies** | **bool** | Whether only branches that match the specified name patterns can deploy to this environment.  If &#x60;custom_branch_policies&#x60; is &#x60;true&#x60;, &#x60;protected_branches&#x60; must be &#x60;false&#x60;; if &#x60;custom_branch_policies&#x60; is &#x60;false&#x60;, &#x60;protected_branches&#x60; must be &#x60;true&#x60;. | 

## Example

```python
from github_openapi.models.deployment_branch_policy_settings import DeploymentBranchPolicySettings

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentBranchPolicySettings from a JSON string
deployment_branch_policy_settings_instance = DeploymentBranchPolicySettings.from_json(json)
# print the JSON string representation of the object
print(DeploymentBranchPolicySettings.to_json())

# convert the object into a dict
deployment_branch_policy_settings_dict = deployment_branch_policy_settings_instance.to_dict()
# create an instance of DeploymentBranchPolicySettings from a dict
deployment_branch_policy_settings_from_dict = DeploymentBranchPolicySettings.from_dict(deployment_branch_policy_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


