# PackageVersionMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_type** | **str** |  | 
**container** | [**ContainerMetadata**](ContainerMetadata.md) |  | [optional] 
**docker** | [**DockerMetadata**](DockerMetadata.md) |  | [optional] 

## Example

```python
from github_openapi.models.package_version_metadata import PackageVersionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PackageVersionMetadata from a JSON string
package_version_metadata_instance = PackageVersionMetadata.from_json(json)
# print the JSON string representation of the object
print(PackageVersionMetadata.to_json())

# convert the object into a dict
package_version_metadata_dict = package_version_metadata_instance.to_dict()
# create an instance of PackageVersionMetadata from a dict
package_version_metadata_from_dict = PackageVersionMetadata.from_dict(package_version_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


