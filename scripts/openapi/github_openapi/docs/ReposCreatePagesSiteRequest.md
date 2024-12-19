# ReposCreatePagesSiteRequest

The source branch and directory used to publish your Pages site.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_type** | **str** | The process in which the Page will be built. Possible values are &#x60;\&quot;legacy\&quot;&#x60; and &#x60;\&quot;workflow\&quot;&#x60;. | [optional] 
**source** | [**ReposCreatePagesSiteRequestSource**](ReposCreatePagesSiteRequestSource.md) |  | [optional] 

## Example

```python
from github_openapi.models.repos_create_pages_site_request import ReposCreatePagesSiteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreatePagesSiteRequest from a JSON string
repos_create_pages_site_request_instance = ReposCreatePagesSiteRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreatePagesSiteRequest.to_json())

# convert the object into a dict
repos_create_pages_site_request_dict = repos_create_pages_site_request_instance.to_dict()
# create an instance of ReposCreatePagesSiteRequest from a dict
repos_create_pages_site_request_from_dict = ReposCreatePagesSiteRequest.from_dict(repos_create_pages_site_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


