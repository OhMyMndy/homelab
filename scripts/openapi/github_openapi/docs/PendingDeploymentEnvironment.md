# PendingDeploymentEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the environment. | [optional] 
**node_id** | **str** |  | [optional] 
**name** | **str** | The name of the environment. | [optional] 
**url** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.pending_deployment_environment import PendingDeploymentEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of PendingDeploymentEnvironment from a JSON string
pending_deployment_environment_instance = PendingDeploymentEnvironment.from_json(json)
# print the JSON string representation of the object
print(PendingDeploymentEnvironment.to_json())

# convert the object into a dict
pending_deployment_environment_dict = pending_deployment_environment_instance.to_dict()
# create an instance of PendingDeploymentEnvironment from a dict
pending_deployment_environment_from_dict = PendingDeploymentEnvironment.from_dict(pending_deployment_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


