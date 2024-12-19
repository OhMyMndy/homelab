# ReposUpdateInformationAboutPagesSiteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cname** | **str** | Specify a custom domain for the repository. Sending a &#x60;null&#x60; value will remove the custom domain. For more about custom domains, see \&quot;[Using a custom domain with GitHub Pages](https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site).\&quot; | [optional] 
**https_enforced** | **bool** | Specify whether HTTPS should be enforced for the repository. | [optional] 
**build_type** | **str** | The process by which the GitHub Pages site will be built. &#x60;workflow&#x60; means that the site is built by a custom GitHub Actions workflow. &#x60;legacy&#x60; means that the site is built by GitHub when changes are pushed to a specific branch. | [optional] 
**source** | [**ReposUpdateInformationAboutPagesSiteRequestSource**](ReposUpdateInformationAboutPagesSiteRequestSource.md) |  | [optional] 

## Example

```python
from github_openapi.models.repos_update_information_about_pages_site_request import ReposUpdateInformationAboutPagesSiteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateInformationAboutPagesSiteRequest from a JSON string
repos_update_information_about_pages_site_request_instance = ReposUpdateInformationAboutPagesSiteRequest.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateInformationAboutPagesSiteRequest.to_json())

# convert the object into a dict
repos_update_information_about_pages_site_request_dict = repos_update_information_about_pages_site_request_instance.to_dict()
# create an instance of ReposUpdateInformationAboutPagesSiteRequest from a dict
repos_update_information_about_pages_site_request_from_dict = ReposUpdateInformationAboutPagesSiteRequest.from_dict(repos_update_information_about_pages_site_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


