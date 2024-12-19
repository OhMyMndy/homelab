# Page

The configuration for GitHub Pages for a repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The API address for accessing this Page resource. | 
**status** | **str** | The status of the most recent build of the Page. | 
**cname** | **str** | The Pages site&#39;s custom domain | 
**protected_domain_state** | **str** | The state if the domain is verified | [optional] 
**pending_domain_unverified_at** | **datetime** | The timestamp when a pending domain becomes unverified. | [optional] 
**custom_404** | **bool** | Whether the Page has a custom 404 page. | [default to False]
**html_url** | **str** | The web address the Page can be accessed from. | [optional] 
**build_type** | **str** | The process in which the Page will be built. | [optional] 
**source** | [**PagesSourceHash**](PagesSourceHash.md) |  | [optional] 
**public** | **bool** | Whether the GitHub Pages site is publicly visible. If set to &#x60;true&#x60;, the site is accessible to anyone on the internet. If set to &#x60;false&#x60;, the site will only be accessible to users who have at least &#x60;read&#x60; access to the repository that published the site. | 
**https_certificate** | [**PagesHttpsCertificate**](PagesHttpsCertificate.md) |  | [optional] 
**https_enforced** | **bool** | Whether https is enabled on the domain | [optional] 

## Example

```python
from github_openapi.models.page import Page

# TODO update the JSON string below
json = "{}"
# create an instance of Page from a JSON string
page_instance = Page.from_json(json)
# print the JSON string representation of the object
print(Page.to_json())

# convert the object into a dict
page_dict = page_instance.to_dict()
# create an instance of Page from a dict
page_from_dict = Page.from_dict(page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


