# WebhookGollumPagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action that was performed on the page. Can be &#x60;created&#x60; or &#x60;edited&#x60;. | 
**html_url** | **str** | Points to the HTML wiki page. | 
**page_name** | **str** | The name of the page. | 
**sha** | **str** | The latest commit SHA of the page. | 
**summary** | **str** |  | 
**title** | **str** | The current page title. | 

## Example

```python
from github_openapi.models.webhook_gollum_pages_inner import WebhookGollumPagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookGollumPagesInner from a JSON string
webhook_gollum_pages_inner_instance = WebhookGollumPagesInner.from_json(json)
# print the JSON string representation of the object
print(WebhookGollumPagesInner.to_json())

# convert the object into a dict
webhook_gollum_pages_inner_dict = webhook_gollum_pages_inner_instance.to_dict()
# create an instance of WebhookGollumPagesInner from a dict
webhook_gollum_pages_inner_from_dict = WebhookGollumPagesInner.from_dict(webhook_gollum_pages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


