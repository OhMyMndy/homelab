# GistsCreateCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The comment text. | 

## Example

```python
from github_openapi.models.gists_create_comment_request import GistsCreateCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GistsCreateCommentRequest from a JSON string
gists_create_comment_request_instance = GistsCreateCommentRequest.from_json(json)
# print the JSON string representation of the object
print(GistsCreateCommentRequest.to_json())

# convert the object into a dict
gists_create_comment_request_dict = gists_create_comment_request_instance.to_dict()
# create an instance of GistsCreateCommentRequest from a dict
gists_create_comment_request_from_dict = GistsCreateCommentRequest.from_dict(gists_create_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


