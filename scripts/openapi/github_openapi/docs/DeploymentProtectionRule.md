# DeploymentProtectionRule

Deployment protection rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the deployment protection rule. | 
**node_id** | **str** | The node ID for the deployment protection rule. | 
**enabled** | **bool** | Whether the deployment protection rule is enabled for the environment. | 
**app** | [**CustomDeploymentRuleApp**](CustomDeploymentRuleApp.md) |  | 

## Example

```python
from github_openapi.models.deployment_protection_rule import DeploymentProtectionRule

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentProtectionRule from a JSON string
deployment_protection_rule_instance = DeploymentProtectionRule.from_json(json)
# print the JSON string representation of the object
print(DeploymentProtectionRule.to_json())

# convert the object into a dict
deployment_protection_rule_dict = deployment_protection_rule_instance.to_dict()
# create an instance of DeploymentProtectionRule from a dict
deployment_protection_rule_from_dict = DeploymentProtectionRule.from_dict(deployment_protection_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


