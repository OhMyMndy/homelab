# Deployment

The [deployment](https://docs.github.com/rest/deployments/deployments#list-deployments).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | 
**creator** | [**User2**](User2.md) |  | 
**description** | **str** |  | 
**environment** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**original_environment** | **str** |  | 
**payload** | [**DeploymentPayload**](DeploymentPayload.md) |  | 
**performed_via_github_app** | [**App5**](App5.md) |  | [optional] 
**production_environment** | **bool** |  | [optional] 
**ref** | **str** |  | 
**repository_url** | **str** |  | 
**sha** | **str** |  | 
**statuses_url** | **str** |  | 
**task** | **str** |  | 
**transient_environment** | **bool** |  | [optional] 
**updated_at** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.deployment import Deployment

# TODO update the JSON string below
json = "{}"
# create an instance of Deployment from a JSON string
deployment_instance = Deployment.from_json(json)
# print the JSON string representation of the object
print(Deployment.to_json())

# convert the object into a dict
deployment_dict = deployment_instance.to_dict()
# create an instance of Deployment from a dict
deployment_from_dict = Deployment.from_dict(deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


