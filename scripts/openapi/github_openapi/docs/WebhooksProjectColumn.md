# WebhooksProjectColumn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_id** | **int** |  | [optional] 
**cards_url** | **str** |  | 
**created_at** | **datetime** |  | 
**id** | **int** | The unique identifier of the project column | 
**name** | **str** | Name of the project column | 
**node_id** | **str** |  | 
**project_url** | **str** |  | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhooks_project_column import WebhooksProjectColumn

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksProjectColumn from a JSON string
webhooks_project_column_instance = WebhooksProjectColumn.from_json(json)
# print the JSON string representation of the object
print(WebhooksProjectColumn.to_json())

# convert the object into a dict
webhooks_project_column_dict = webhooks_project_column_instance.to_dict()
# create an instance of WebhooksProjectColumn from a dict
webhooks_project_column_from_dict = WebhooksProjectColumn.from_dict(webhooks_project_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


