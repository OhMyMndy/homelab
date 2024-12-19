# DeploymentStatus

The status of a deployment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**state** | **str** | The state of the status. | 
**creator** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**description** | **str** | A short description of the status. | [default to '']
**environment** | **str** | The environment of the deployment that the status is for. | [optional] [default to '']
**target_url** | **str** | Closing down notice: the URL to associate with this status. | [default to '']
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**deployment_url** | **str** |  | 
**repository_url** | **str** |  | 
**environment_url** | **str** | The URL for accessing your environment. | [optional] [default to '']
**log_url** | **str** | The URL to associate with this status. | [optional] [default to '']
**performed_via_github_app** | [**NullableIntegration**](NullableIntegration.md) |  | [optional] 

## Example

```python
from github_openapi.models.deployment_status import DeploymentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStatus from a JSON string
deployment_status_instance = DeploymentStatus.from_json(json)
# print the JSON string representation of the object
print(DeploymentStatus.to_json())

# convert the object into a dict
deployment_status_dict = deployment_status_instance.to_dict()
# create an instance of DeploymentStatus from a dict
deployment_status_from_dict = DeploymentStatus.from_dict(deployment_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


