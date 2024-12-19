# ReposCreatePagesSiteRequestSource

The source branch and directory used to publish your Pages site.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | The repository branch used to publish your site&#39;s source files. | 
**path** | **str** | The repository directory that includes the source files for the Pages site. Allowed paths are &#x60;/&#x60; or &#x60;/docs&#x60;. Default: &#x60;/&#x60; | [optional] [default to '/']

## Example

```python
from github_openapi.models.repos_create_pages_site_request_source import ReposCreatePagesSiteRequestSource

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreatePagesSiteRequestSource from a JSON string
repos_create_pages_site_request_source_instance = ReposCreatePagesSiteRequestSource.from_json(json)
# print the JSON string representation of the object
print(ReposCreatePagesSiteRequestSource.to_json())

# convert the object into a dict
repos_create_pages_site_request_source_dict = repos_create_pages_site_request_source_instance.to_dict()
# create an instance of ReposCreatePagesSiteRequestSource from a dict
repos_create_pages_site_request_source_from_dict = ReposCreatePagesSiteRequestSource.from_dict(repos_create_pages_site_request_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


