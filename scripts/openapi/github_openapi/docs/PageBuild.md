# PageBuild

Page Build

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**status** | **str** |  | 
**error** | [**PageBuildError**](PageBuildError.md) |  | 
**pusher** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**commit** | **str** |  | 
**duration** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.page_build import PageBuild

# TODO update the JSON string below
json = "{}"
# create an instance of PageBuild from a JSON string
page_build_instance = PageBuild.from_json(json)
# print the JSON string representation of the object
print(PageBuild.to_json())

# convert the object into a dict
page_build_dict = page_build_instance.to_dict()
# create an instance of PageBuild from a dict
page_build_from_dict = PageBuild.from_dict(page_build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


