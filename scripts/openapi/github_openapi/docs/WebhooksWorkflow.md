# WebhooksWorkflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge_url** | **str** |  | 
**created_at** | **datetime** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**node_id** | **str** |  | 
**path** | **str** |  | 
**state** | **str** |  | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhooks_workflow import WebhooksWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksWorkflow from a JSON string
webhooks_workflow_instance = WebhooksWorkflow.from_json(json)
# print the JSON string representation of the object
print(WebhooksWorkflow.to_json())

# convert the object into a dict
webhooks_workflow_dict = webhooks_workflow_instance.to_dict()
# create an instance of WebhooksWorkflow from a dict
webhooks_workflow_from_dict = WebhooksWorkflow.from_dict(webhooks_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


