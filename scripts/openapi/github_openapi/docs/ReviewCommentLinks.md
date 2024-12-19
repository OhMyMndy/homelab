# ReviewCommentLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**html** | [**Link**](Link.md) |  | 
**pull_request** | [**Link**](Link.md) |  | 

## Example

```python
from github_openapi.models.review_comment_links import ReviewCommentLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewCommentLinks from a JSON string
review_comment_links_instance = ReviewCommentLinks.from_json(json)
# print the JSON string representation of the object
print(ReviewCommentLinks.to_json())

# convert the object into a dict
review_comment_links_dict = review_comment_links_instance.to_dict()
# create an instance of ReviewCommentLinks from a dict
review_comment_links_from_dict = ReviewCommentLinks.from_dict(review_comment_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


