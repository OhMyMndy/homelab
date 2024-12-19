# GitCreateTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** | The tag&#39;s name. This is typically a version (e.g., \&quot;v0.0.1\&quot;). | 
**message** | **str** | The tag message. | 
**object** | **str** | The SHA of the git object this is tagging. | 
**type** | **str** | The type of the object we&#39;re tagging. Normally this is a &#x60;commit&#x60; but it can also be a &#x60;tree&#x60; or a &#x60;blob&#x60;. | 
**tagger** | [**GitCreateTagRequestTagger**](GitCreateTagRequestTagger.md) |  | [optional] 

## Example

```python
from github_openapi.models.git_create_tag_request import GitCreateTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GitCreateTagRequest from a JSON string
git_create_tag_request_instance = GitCreateTagRequest.from_json(json)
# print the JSON string representation of the object
print(GitCreateTagRequest.to_json())

# convert the object into a dict
git_create_tag_request_dict = git_create_tag_request_instance.to_dict()
# create an instance of GitCreateTagRequest from a dict
git_create_tag_request_from_dict = GitCreateTagRequest.from_dict(git_create_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


