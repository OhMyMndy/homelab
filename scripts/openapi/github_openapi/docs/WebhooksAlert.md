# WebhooksAlert

The security alert of the vulnerable dependency.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_package_name** | **str** |  | 
**affected_range** | **str** |  | 
**created_at** | **str** |  | 
**dismiss_reason** | **str** |  | [optional] 
**dismissed_at** | **str** |  | [optional] 
**dismisser** | [**User**](User.md) |  | [optional] 
**external_identifier** | **str** |  | 
**external_reference** | **str** |  | 
**fix_reason** | **str** |  | [optional] 
**fixed_at** | **datetime** |  | [optional] 
**fixed_in** | **str** |  | [optional] 
**ghsa_id** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**number** | **int** |  | 
**severity** | **str** |  | 
**state** | **str** |  | 

## Example

```python
from github_openapi.models.webhooks_alert import WebhooksAlert

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksAlert from a JSON string
webhooks_alert_instance = WebhooksAlert.from_json(json)
# print the JSON string representation of the object
print(WebhooksAlert.to_json())

# convert the object into a dict
webhooks_alert_dict = webhooks_alert_instance.to_dict()
# create an instance of WebhooksAlert from a dict
webhooks_alert_from_dict = WebhooksAlert.from_dict(webhooks_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


