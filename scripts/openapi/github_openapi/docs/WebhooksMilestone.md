# WebhooksMilestone

A collection of related issues and pull requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_at** | **datetime** |  | 
**closed_issues** | **int** |  | 
**created_at** | **datetime** |  | 
**creator** | [**User4**](User4.md) |  | 
**description** | **str** |  | 
**due_on** | **datetime** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**labels_url** | **str** |  | 
**node_id** | **str** |  | 
**number** | **int** | The number of the milestone. | 
**open_issues** | **int** |  | 
**state** | **str** | The state of the milestone. | 
**title** | **str** | The title of the milestone. | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhooks_milestone import WebhooksMilestone

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksMilestone from a JSON string
webhooks_milestone_instance = WebhooksMilestone.from_json(json)
# print the JSON string representation of the object
print(WebhooksMilestone.to_json())

# convert the object into a dict
webhooks_milestone_dict = webhooks_milestone_instance.to_dict()
# create an instance of WebhooksMilestone from a dict
webhooks_milestone_from_dict = WebhooksMilestone.from_dict(webhooks_milestone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

