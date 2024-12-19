# WebhooksWorkflowJobRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conclusion** | **object** |  | 
**created_at** | **str** |  | 
**environment** | **str** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**name** | **object** |  | 
**status** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from github_openapi.models.webhooks_workflow_job_run import WebhooksWorkflowJobRun

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksWorkflowJobRun from a JSON string
webhooks_workflow_job_run_instance = WebhooksWorkflowJobRun.from_json(json)
# print the JSON string representation of the object
print(WebhooksWorkflowJobRun.to_json())

# convert the object into a dict
webhooks_workflow_job_run_dict = webhooks_workflow_job_run_instance.to_dict()
# create an instance of WebhooksWorkflowJobRun from a dict
webhooks_workflow_job_run_from_dict = WebhooksWorkflowJobRun.from_dict(webhooks_workflow_job_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


