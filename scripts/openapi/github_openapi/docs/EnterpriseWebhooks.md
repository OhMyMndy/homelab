# EnterpriseWebhooks

An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured on an enterprise account or an organization that's part of an enterprise account. For more information, see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A short description of the enterprise. | [optional] 
**html_url** | **str** |  | 
**website_url** | **str** | The enterprise&#39;s website URL. | [optional] 
**id** | **int** | Unique identifier of the enterprise | 
**node_id** | **str** |  | 
**name** | **str** | The name of the enterprise. | 
**slug** | **str** | The slug url identifier for the enterprise. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**avatar_url** | **str** |  | 

## Example

```python
from github_openapi.models.enterprise_webhooks import EnterpriseWebhooks

# TODO update the JSON string below
json = "{}"
# create an instance of EnterpriseWebhooks from a JSON string
enterprise_webhooks_instance = EnterpriseWebhooks.from_json(json)
# print the JSON string representation of the object
print(EnterpriseWebhooks.to_json())

# convert the object into a dict
enterprise_webhooks_dict = enterprise_webhooks_instance.to_dict()
# create an instance of EnterpriseWebhooks from a dict
enterprise_webhooks_from_dict = EnterpriseWebhooks.from_dict(enterprise_webhooks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


