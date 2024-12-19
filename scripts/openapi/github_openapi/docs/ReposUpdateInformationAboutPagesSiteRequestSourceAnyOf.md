# ReposUpdateInformationAboutPagesSiteRequestSourceAnyOf

Update the source for the repository. Must include the branch name and path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | The repository branch used to publish your site&#39;s source files. | 
**path** | **str** | The repository directory that includes the source files for the Pages site. Allowed paths are &#x60;/&#x60; or &#x60;/docs&#x60;. | 

## Example

```python
from github_openapi.models.repos_update_information_about_pages_site_request_source_any_of import ReposUpdateInformationAboutPagesSiteRequestSourceAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateInformationAboutPagesSiteRequestSourceAnyOf from a JSON string
repos_update_information_about_pages_site_request_source_any_of_instance = ReposUpdateInformationAboutPagesSiteRequestSourceAnyOf.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateInformationAboutPagesSiteRequestSourceAnyOf.to_json())

# convert the object into a dict
repos_update_information_about_pages_site_request_source_any_of_dict = repos_update_information_about_pages_site_request_source_any_of_instance.to_dict()
# create an instance of ReposUpdateInformationAboutPagesSiteRequestSourceAnyOf from a dict
repos_update_information_about_pages_site_request_source_any_of_from_dict = ReposUpdateInformationAboutPagesSiteRequestSourceAnyOf.from_dict(repos_update_information_about_pages_site_request_source_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


