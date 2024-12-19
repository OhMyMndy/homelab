# ReposCreateDeploymentProtectionRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **int** | The ID of the custom app that will be enabled on the environment. | [optional] 

## Example

```python
from github_openapi.models.repos_create_deployment_protection_rule_request import ReposCreateDeploymentProtectionRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateDeploymentProtectionRuleRequest from a JSON string
repos_create_deployment_protection_rule_request_instance = ReposCreateDeploymentProtectionRuleRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateDeploymentProtectionRuleRequest.to_json())

# convert the object into a dict
repos_create_deployment_protection_rule_request_dict = repos_create_deployment_protection_rule_request_instance.to_dict()
# create an instance of ReposCreateDeploymentProtectionRuleRequest from a dict
repos_create_deployment_protection_rule_request_from_dict = ReposCreateDeploymentProtectionRuleRequest.from_dict(repos_create_deployment_protection_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


