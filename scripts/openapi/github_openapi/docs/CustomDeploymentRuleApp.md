# CustomDeploymentRuleApp

A GitHub App that is providing a custom deployment protection rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the deployment protection rule integration. | 
**slug** | **str** | The slugified name of the deployment protection rule integration. | 
**integration_url** | **str** | The URL for the endpoint to get details about the app. | 
**node_id** | **str** | The node ID for the deployment protection rule integration. | 

## Example

```python
from github_openapi.models.custom_deployment_rule_app import CustomDeploymentRuleApp

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDeploymentRuleApp from a JSON string
custom_deployment_rule_app_instance = CustomDeploymentRuleApp.from_json(json)
# print the JSON string representation of the object
print(CustomDeploymentRuleApp.to_json())

# convert the object into a dict
custom_deployment_rule_app_dict = custom_deployment_rule_app_instance.to_dict()
# create an instance of CustomDeploymentRuleApp from a dict
custom_deployment_rule_app_from_dict = CustomDeploymentRuleApp.from_dict(custom_deployment_rule_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


