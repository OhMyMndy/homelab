# WebhookDeploymentStatusCreatedCheckRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **datetime** |  | 
**conclusion** | **str** | The result of the completed check run. This value will be &#x60;null&#x60; until the check run has completed. | 
**details_url** | **str** |  | 
**external_id** | **str** |  | 
**head_sha** | **str** | The SHA of the commit that is being checked. | 
**html_url** | **str** |  | 
**id** | **int** | The id of the check. | 
**name** | **str** | The name of the check run. | 
**node_id** | **str** |  | 
**started_at** | **datetime** |  | 
**status** | **str** | The current status of the check run. Can be &#x60;queued&#x60;, &#x60;in_progress&#x60;, or &#x60;completed&#x60;. | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_deployment_status_created_check_run import WebhookDeploymentStatusCreatedCheckRun

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeploymentStatusCreatedCheckRun from a JSON string
webhook_deployment_status_created_check_run_instance = WebhookDeploymentStatusCreatedCheckRun.from_json(json)
# print the JSON string representation of the object
print(WebhookDeploymentStatusCreatedCheckRun.to_json())

# convert the object into a dict
webhook_deployment_status_created_check_run_dict = webhook_deployment_status_created_check_run_instance.to_dict()
# create an instance of WebhookDeploymentStatusCreatedCheckRun from a dict
webhook_deployment_status_created_check_run_from_dict = WebhookDeploymentStatusCreatedCheckRun.from_dict(webhook_deployment_status_created_check_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


