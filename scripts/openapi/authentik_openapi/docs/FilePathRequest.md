# FilePathRequest

Serializer to upload file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 

## Example

```python
from authentik_openapi.models.file_path_request import FilePathRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FilePathRequest from a JSON string
file_path_request_instance = FilePathRequest.from_json(json)
# print the JSON string representation of the object
print(FilePathRequest.to_json())

# convert the object into a dict
file_path_request_dict = file_path_request_instance.to_dict()
# create an instance of FilePathRequest from a dict
file_path_request_from_dict = FilePathRequest.from_dict(file_path_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


