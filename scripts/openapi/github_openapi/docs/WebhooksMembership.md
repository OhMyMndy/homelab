# WebhooksMembership

The membership between the user and the organization. Not present when the action is `member_invited`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_url** | **str** |  | 
**role** | **str** |  | 
**state** | **str** |  | 
**url** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.webhooks_membership import WebhooksMembership

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksMembership from a JSON string
webhooks_membership_instance = WebhooksMembership.from_json(json)
# print the JSON string representation of the object
print(WebhooksMembership.to_json())

# convert the object into a dict
webhooks_membership_dict = webhooks_membership_instance.to_dict()
# create an instance of WebhooksMembership from a dict
webhooks_membership_from_dict = WebhooksMembership.from_dict(webhooks_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


