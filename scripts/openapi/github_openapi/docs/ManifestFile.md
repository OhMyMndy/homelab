# ManifestFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_location** | **str** | The path of the manifest file relative to the root of the Git repository. | [optional] 

## Example

```python
from github_openapi.models.manifest_file import ManifestFile

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestFile from a JSON string
manifest_file_instance = ManifestFile.from_json(json)
# print the JSON string representation of the object
print(ManifestFile.to_json())

# convert the object into a dict
manifest_file_dict = manifest_file_instance.to_dict()
# create an instance of ManifestFile from a dict
manifest_file_from_dict = ManifestFile.from_dict(manifest_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


