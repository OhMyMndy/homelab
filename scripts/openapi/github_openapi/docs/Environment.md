# Environment

Details of a deployment environment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the environment. | 
**node_id** | **str** |  | 
**name** | **str** | The name of the environment. | 
**url** | **str** |  | 
**html_url** | **str** |  | 
**created_at** | **datetime** | The time that the environment was created, in ISO 8601 format. | 
**updated_at** | **datetime** | The time that the environment was last updated, in ISO 8601 format. | 
**protection_rules** | [**List[EnvironmentProtectionRulesInner]**](EnvironmentProtectionRulesInner.md) | Built-in deployment protection rules for the environment. | [optional] 
**deployment_branch_policy** | [**DeploymentBranchPolicySettings**](DeploymentBranchPolicySettings.md) |  | [optional] 

## Example

```python
from github_openapi.models.environment import Environment

# TODO update the JSON string below
json = "{}"
# create an instance of Environment from a JSON string
environment_instance = Environment.from_json(json)
# print the JSON string representation of the object
print(Environment.to_json())

# convert the object into a dict
environment_dict = environment_instance.to_dict()
# create an instance of Environment from a dict
environment_from_dict = Environment.from_dict(environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


