# ReposCreateAutolinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_prefix** | **str** | This prefix appended by certain characters will generate a link any time it is found in an issue, pull request, or commit. | 
**url_template** | **str** | The URL must contain &#x60;&lt;num&gt;&#x60; for the reference number. &#x60;&lt;num&gt;&#x60; matches different characters depending on the value of &#x60;is_alphanumeric&#x60;. | 
**is_alphanumeric** | **bool** | Whether this autolink reference matches alphanumeric characters. If true, the &#x60;&lt;num&gt;&#x60; parameter of the &#x60;url_template&#x60; matches alphanumeric characters &#x60;A-Z&#x60; (case insensitive), &#x60;0-9&#x60;, and &#x60;-&#x60;. If false, this autolink reference only matches numeric characters. | [optional] [default to True]

## Example

```python
from github_openapi.models.repos_create_autolink_request import ReposCreateAutolinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateAutolinkRequest from a JSON string
repos_create_autolink_request_instance = ReposCreateAutolinkRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateAutolinkRequest.to_json())

# convert the object into a dict
repos_create_autolink_request_dict = repos_create_autolink_request_instance.to_dict()
# create an instance of ReposCreateAutolinkRequest from a dict
repos_create_autolink_request_from_dict = ReposCreateAutolinkRequest.from_dict(repos_create_autolink_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


