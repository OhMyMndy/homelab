# DeploymentSimple

A deployment created as the result of an Actions check run from a workflow that references an environment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**id** | **int** | Unique identifier of the deployment | 
**node_id** | **str** |  | 
**task** | **str** | Parameter to specify a task to execute | 
**original_environment** | **str** |  | [optional] 
**environment** | **str** | Name for the target deployment environment. | 
**description** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**statuses_url** | **str** |  | 
**repository_url** | **str** |  | 
**transient_environment** | **bool** | Specifies if the given environment is will no longer exist at some point in the future. Default: false. | [optional] 
**production_environment** | **bool** | Specifies if the given environment is one that end-users directly interact with. Default: false. | [optional] 
**performed_via_github_app** | [**NullableIntegration**](NullableIntegration.md) |  | [optional] 

## Example

```python
from github_openapi.models.deployment_simple import DeploymentSimple

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentSimple from a JSON string
deployment_simple_instance = DeploymentSimple.from_json(json)
# print the JSON string representation of the object
print(DeploymentSimple.to_json())

# convert the object into a dict
deployment_simple_dict = deployment_simple_instance.to_dict()
# create an instance of DeploymentSimple from a dict
deployment_simple_from_dict = DeploymentSimple.from_dict(deployment_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


