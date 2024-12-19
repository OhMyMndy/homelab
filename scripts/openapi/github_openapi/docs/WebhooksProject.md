# WebhooksProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Body of the project | 
**columns_url** | **str** |  | 
**created_at** | **datetime** |  | 
**creator** | [**User2**](User2.md) |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**name** | **str** | Name of the project | 
**node_id** | **str** |  | 
**number** | **int** |  | 
**owner_url** | **str** |  | 
**state** | **str** | State of the project; either &#39;open&#39; or &#39;closed&#39; | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhooks_project import WebhooksProject

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksProject from a JSON string
webhooks_project_instance = WebhooksProject.from_json(json)
# print the JSON string representation of the object
print(WebhooksProject.to_json())

# convert the object into a dict
webhooks_project_dict = webhooks_project_instance.to_dict()
# create an instance of WebhooksProject from a dict
webhooks_project_from_dict = WebhooksProject.from_dict(webhooks_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


