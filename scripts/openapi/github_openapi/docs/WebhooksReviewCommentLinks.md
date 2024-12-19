# WebhooksReviewCommentLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html** | [**Link**](Link.md) |  | 
**pull_request** | [**Link**](Link.md) |  | 
**var_self** | [**Link**](Link.md) |  | 

## Example

```python
from github_openapi.models.webhooks_review_comment_links import WebhooksReviewCommentLinks

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksReviewCommentLinks from a JSON string
webhooks_review_comment_links_instance = WebhooksReviewCommentLinks.from_json(json)
# print the JSON string representation of the object
print(WebhooksReviewCommentLinks.to_json())

# convert the object into a dict
webhooks_review_comment_links_dict = webhooks_review_comment_links_instance.to_dict()
# create an instance of WebhooksReviewCommentLinks from a dict
webhooks_review_comment_links_from_dict = WebhooksReviewCommentLinks.from_dict(webhooks_review_comment_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


