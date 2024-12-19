# PackageVersion

A version of a software package

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the package version. | 
**name** | **str** | The name of the package version. | 
**url** | **str** |  | 
**package_html_url** | **str** |  | 
**html_url** | **str** |  | [optional] 
**license** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**deleted_at** | **datetime** |  | [optional] 
**metadata** | [**PackageVersionMetadata**](PackageVersionMetadata.md) |  | [optional] 

## Example

```python
from github_openapi.models.package_version import PackageVersion

# TODO update the JSON string below
json = "{}"
# create an instance of PackageVersion from a JSON string
package_version_instance = PackageVersion.from_json(json)
# print the JSON string representation of the object
print(PackageVersion.to_json())

# convert the object into a dict
package_version_dict = package_version_instance.to_dict()
# create an instance of PackageVersion from a dict
package_version_from_dict = PackageVersion.from_dict(package_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


