# Manifest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the manifest. | 
**file** | [**ManifestFile**](ManifestFile.md) |  | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | User-defined metadata to store domain-specific information limited to 8 keys with scalar values. | [optional] 
**resolved** | [**Dict[str, Dependency]**](Dependency.md) | A collection of resolved package dependencies. | [optional] 

## Example

```python
from github_openapi.models.manifest import Manifest

# TODO update the JSON string below
json = "{}"
# create an instance of Manifest from a JSON string
manifest_instance = Manifest.from_json(json)
# print the JSON string representation of the object
print(Manifest.to_json())

# convert the object into a dict
manifest_dict = manifest_instance.to_dict()
# create an instance of Manifest from a dict
manifest_from_dict = Manifest.from_dict(manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


