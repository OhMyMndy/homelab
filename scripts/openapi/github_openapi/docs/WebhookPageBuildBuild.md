# WebhookPageBuildBuild

The [List GitHub Pages builds](https://docs.github.com/rest/pages/pages#list-github-pages-builds) itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | **str** |  | 
**created_at** | **str** |  | 
**duration** | **int** |  | 
**error** | [**PageBuildError**](PageBuildError.md) |  | 
**pusher** | [**User2**](User2.md) |  | 
**status** | **str** |  | 
**updated_at** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_page_build_build import WebhookPageBuildBuild

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPageBuildBuild from a JSON string
webhook_page_build_build_instance = WebhookPageBuildBuild.from_json(json)
# print the JSON string representation of the object
print(WebhookPageBuildBuild.to_json())

# convert the object into a dict
webhook_page_build_build_dict = webhook_page_build_build_instance.to_dict()
# create an instance of WebhookPageBuildBuild from a dict
webhook_page_build_build_from_dict = WebhookPageBuildBuild.from_dict(webhook_page_build_build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


