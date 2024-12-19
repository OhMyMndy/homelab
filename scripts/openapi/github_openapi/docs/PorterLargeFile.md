# PorterLargeFile

Porter Large File

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref_name** | **str** |  | 
**path** | **str** |  | 
**oid** | **str** |  | 
**size** | **int** |  | 

## Example

```python
from github_openapi.models.porter_large_file import PorterLargeFile

# TODO update the JSON string below
json = "{}"
# create an instance of PorterLargeFile from a JSON string
porter_large_file_instance = PorterLargeFile.from_json(json)
# print the JSON string representation of the object
print(PorterLargeFile.to_json())

# convert the object into a dict
porter_large_file_dict = porter_large_file_instance.to_dict()
# create an instance of PorterLargeFile from a dict
porter_large_file_from_dict = PorterLargeFile.from_dict(porter_large_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


