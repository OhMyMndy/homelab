# WebhooksReviewLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html** | [**Link**](Link.md) |  | 
**pull_request** | [**Link**](Link.md) |  | 

## Example

```python
from github_openapi.models.webhooks_review_links import WebhooksReviewLinks

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksReviewLinks from a JSON string
webhooks_review_links_instance = WebhooksReviewLinks.from_json(json)
# print the JSON string representation of the object
print(WebhooksReviewLinks.to_json())

# convert the object into a dict
webhooks_review_links_dict = webhooks_review_links_instance.to_dict()
# create an instance of WebhooksReviewLinks from a dict
webhooks_review_links_from_dict = WebhooksReviewLinks.from_dict(webhooks_review_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


