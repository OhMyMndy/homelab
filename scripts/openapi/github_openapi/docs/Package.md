# Package

A software package

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the package. | 
**name** | **str** | The name of the package. | 
**package_type** | **str** |  | 
**url** | **str** |  | 
**html_url** | **str** |  | 
**version_count** | **int** | The number of versions of the package. | 
**visibility** | **str** |  | 
**owner** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**repository** | [**NullableMinimalRepository**](NullableMinimalRepository.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.package import Package

# TODO update the JSON string below
json = "{}"
# create an instance of Package from a JSON string
package_instance = Package.from_json(json)
# print the JSON string representation of the object
print(Package.to_json())

# convert the object into a dict
package_dict = package_instance.to_dict()
# create an instance of Package from a dict
package_from_dict = Package.from_dict(package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


