# PageBuildStatus

Page Build Status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from github_openapi.models.page_build_status import PageBuildStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PageBuildStatus from a JSON string
page_build_status_instance = PageBuildStatus.from_json(json)
# print the JSON string representation of the object
print(PageBuildStatus.to_json())

# convert the object into a dict
page_build_status_dict = page_build_status_instance.to_dict()
# create an instance of PageBuildStatus from a dict
page_build_status_from_dict = PageBuildStatus.from_dict(page_build_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


