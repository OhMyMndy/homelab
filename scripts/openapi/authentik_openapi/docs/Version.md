# Version

Get running and latest version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_current** | **str** | Get current version | [readonly] 
**version_latest** | **str** | Get latest version from cache | [readonly] 
**version_latest_valid** | **bool** | Check if latest version is valid | [readonly] 
**build_hash** | **str** | Get build hash, if version is not latest or released | [readonly] 
**outdated** | **bool** | Check if we&#39;re running the latest version | [readonly] 

## Example

```python
from authentik_openapi.models.version import Version

# TODO update the JSON string below
json = "{}"
# create an instance of Version from a JSON string
version_instance = Version.from_json(json)
# print the JSON string representation of the object
print(Version.to_json())

# convert the object into a dict
version_dict = version_instance.to_dict()
# create an instance of Version from a dict
version_from_dict = Version.from_dict(version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


