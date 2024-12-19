# CodespaceExportDetails

An export of a codespace. Also, latest export details for a codespace can be fetched with id = latest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | State of the latest export | [optional] 
**completed_at** | **datetime** | Completion time of the last export operation | [optional] 
**branch** | **str** | Name of the exported branch | [optional] 
**sha** | **str** | Git commit SHA of the exported branch | [optional] 
**id** | **str** | Id for the export details | [optional] 
**export_url** | **str** | Url for fetching export details | [optional] 
**html_url** | **str** | Web url for the exported branch | [optional] 

## Example

```python
from github_openapi.models.codespace_export_details import CodespaceExportDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CodespaceExportDetails from a JSON string
codespace_export_details_instance = CodespaceExportDetails.from_json(json)
# print the JSON string representation of the object
print(CodespaceExportDetails.to_json())

# convert the object into a dict
codespace_export_details_dict = codespace_export_details_instance.to_dict()
# create an instance of CodespaceExportDetails from a dict
codespace_export_details_from_dict = CodespaceExportDetails.from_dict(codespace_export_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


