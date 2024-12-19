# WebhookDeploymentStatusCreatedDeploymentStatus

The [deployment status](https://docs.github.com/rest/deployments/statuses#list-deployment-statuses).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | 
**creator** | [**User2**](User2.md) |  | 
**deployment_url** | **str** |  | 
**description** | **str** | The optional human-readable description added to the status. | 
**environment** | **str** |  | 
**environment_url** | **str** |  | [optional] 
**id** | **int** |  | 
**log_url** | **str** |  | [optional] 
**node_id** | **str** |  | 
**performed_via_github_app** | [**App7**](App7.md) |  | [optional] 
**repository_url** | **str** |  | 
**state** | **str** | The new state. Can be &#x60;pending&#x60;, &#x60;success&#x60;, &#x60;failure&#x60;, or &#x60;error&#x60;. | 
**target_url** | **str** | The optional link added to the status. | 
**updated_at** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_deployment_status_created_deployment_status import WebhookDeploymentStatusCreatedDeploymentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeploymentStatusCreatedDeploymentStatus from a JSON string
webhook_deployment_status_created_deployment_status_instance = WebhookDeploymentStatusCreatedDeploymentStatus.from_json(json)
# print the JSON string representation of the object
print(WebhookDeploymentStatusCreatedDeploymentStatus.to_json())

# convert the object into a dict
webhook_deployment_status_created_deployment_status_dict = webhook_deployment_status_created_deployment_status_instance.to_dict()
# create an instance of WebhookDeploymentStatusCreatedDeploymentStatus from a dict
webhook_deployment_status_created_deployment_status_from_dict = WebhookDeploymentStatusCreatedDeploymentStatus.from_dict(webhook_deployment_status_created_deployment_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


