# WebhookProjectCardMovedProjectCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_id** | **float** |  | 
**archived** | **bool** |  | 
**column_id** | **int** |  | 
**column_url** | **str** |  | 
**content_url** | **str** |  | [optional] 
**created_at** | **str** |  | 
**creator** | [**WebhookProjectCardMovedProjectCardAllOfCreator**](WebhookProjectCardMovedProjectCardAllOfCreator.md) |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**note** | **str** |  | 
**project_url** | **str** |  | 
**updated_at** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_project_card_moved_project_card import WebhookProjectCardMovedProjectCard

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectCardMovedProjectCard from a JSON string
webhook_project_card_moved_project_card_instance = WebhookProjectCardMovedProjectCard.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectCardMovedProjectCard.to_json())

# convert the object into a dict
webhook_project_card_moved_project_card_dict = webhook_project_card_moved_project_card_instance.to_dict()
# create an instance of WebhookProjectCardMovedProjectCard from a dict
webhook_project_card_moved_project_card_from_dict = WebhookProjectCardMovedProjectCard.from_dict(webhook_project_card_moved_project_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


