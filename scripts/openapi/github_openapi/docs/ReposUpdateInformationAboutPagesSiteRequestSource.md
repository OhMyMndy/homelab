# ReposUpdateInformationAboutPagesSiteRequestSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | The repository branch used to publish your site&#39;s source files. | 
**path** | **str** | The repository directory that includes the source files for the Pages site. Allowed paths are &#x60;/&#x60; or &#x60;/docs&#x60;. | 

## Example

```python
from github_openapi.models.repos_update_information_about_pages_site_request_source import ReposUpdateInformationAboutPagesSiteRequestSource

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateInformationAboutPagesSiteRequestSource from a JSON string
repos_update_information_about_pages_site_request_source_instance = ReposUpdateInformationAboutPagesSiteRequestSource.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateInformationAboutPagesSiteRequestSource.to_json())

# convert the object into a dict
repos_update_information_about_pages_site_request_source_dict = repos_update_information_about_pages_site_request_source_instance.to_dict()
# create an instance of ReposUpdateInformationAboutPagesSiteRequestSource from a dict
repos_update_information_about_pages_site_request_source_from_dict = ReposUpdateInformationAboutPagesSiteRequestSource.from_dict(repos_update_information_about_pages_site_request_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


