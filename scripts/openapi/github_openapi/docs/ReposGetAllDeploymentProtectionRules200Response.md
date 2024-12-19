# ReposGetAllDeploymentProtectionRules200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The number of enabled custom deployment protection rules for this environment | [optional] 
**custom_deployment_protection_rules** | [**List[DeploymentProtectionRule]**](DeploymentProtectionRule.md) |  | [optional] 

## Example

```python
from github_openapi.models.repos_get_all_deployment_protection_rules200_response import ReposGetAllDeploymentProtectionRules200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReposGetAllDeploymentProtectionRules200Response from a JSON string
repos_get_all_deployment_protection_rules200_response_instance = ReposGetAllDeploymentProtectionRules200Response.from_json(json)
# print the JSON string representation of the object
print(ReposGetAllDeploymentProtectionRules200Response.to_json())

# convert the object into a dict
repos_get_all_deployment_protection_rules200_response_dict = repos_get_all_deployment_protection_rules200_response_instance.to_dict()
# create an instance of ReposGetAllDeploymentProtectionRules200Response from a dict
repos_get_all_deployment_protection_rules200_response_from_dict = ReposGetAllDeploymentProtectionRules200Response.from_dict(repos_get_all_deployment_protection_rules200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


