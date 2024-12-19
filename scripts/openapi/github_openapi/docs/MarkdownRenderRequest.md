# MarkdownRenderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The Markdown text to render in HTML. | 
**mode** | **str** | The rendering mode. | [optional] [default to 'markdown']
**context** | **str** | The repository context to use when creating references in &#x60;gfm&#x60; mode.  For example, setting &#x60;context&#x60; to &#x60;octo-org/octo-repo&#x60; will change the text &#x60;#42&#x60; into an HTML link to issue 42 in the &#x60;octo-org/octo-repo&#x60; repository. | [optional] 

## Example

```python
from github_openapi.models.markdown_render_request import MarkdownRenderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MarkdownRenderRequest from a JSON string
markdown_render_request_instance = MarkdownRenderRequest.from_json(json)
# print the JSON string representation of the object
print(MarkdownRenderRequest.to_json())

# convert the object into a dict
markdown_render_request_dict = markdown_render_request_instance.to_dict()
# create an instance of MarkdownRenderRequest from a dict
markdown_render_request_from_dict = MarkdownRenderRequest.from_dict(markdown_render_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


