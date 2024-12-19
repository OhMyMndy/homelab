# OrgsUpdateWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**OrgsUpdateWebhookRequestConfig**](OrgsUpdateWebhookRequestConfig.md) |  | [optional] 
**events** | **List[str]** | Determines what [events](https://docs.github.com/webhooks/event-payloads) the hook is triggered for. | [optional] [default to ["push"]]
**active** | **bool** | Determines if notifications are sent when the webhook is triggered. Set to &#x60;true&#x60; to send notifications. | [optional] [default to True]
**name** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.orgs_update_webhook_request import OrgsUpdateWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsUpdateWebhookRequest from a JSON string
orgs_update_webhook_request_instance = OrgsUpdateWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(OrgsUpdateWebhookRequest.to_json())

# convert the object into a dict
orgs_update_webhook_request_dict = orgs_update_webhook_request_instance.to_dict()
# create an instance of OrgsUpdateWebhookRequest from a dict
orgs_update_webhook_request_from_dict = OrgsUpdateWebhookRequest.from_dict(orgs_update_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


