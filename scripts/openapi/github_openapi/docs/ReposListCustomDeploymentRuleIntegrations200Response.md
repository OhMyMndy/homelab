# ReposListCustomDeploymentRuleIntegrations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of custom deployment protection rule integrations available for this environment. | [optional] 
**available_custom_deployment_protection_rule_integrations** | [**List[CustomDeploymentRuleApp]**](CustomDeploymentRuleApp.md) |  | [optional] 

## Example

```python
from github_openapi.models.repos_list_custom_deployment_rule_integrations200_response import ReposListCustomDeploymentRuleIntegrations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReposListCustomDeploymentRuleIntegrations200Response from a JSON string
repos_list_custom_deployment_rule_integrations200_response_instance = ReposListCustomDeploymentRuleIntegrations200Response.from_json(json)
# print the JSON string representation of the object
print(ReposListCustomDeploymentRuleIntegrations200Response.to_json())

# convert the object into a dict
repos_list_custom_deployment_rule_integrations200_response_dict = repos_list_custom_deployment_rule_integrations200_response_instance.to_dict()
# create an instance of ReposListCustomDeploymentRuleIntegrations200Response from a dict
repos_list_custom_deployment_rule_integrations200_response_from_dict = ReposListCustomDeploymentRuleIntegrations200Response.from_dict(repos_list_custom_deployment_rule_integrations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


