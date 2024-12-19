# Dependency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_url** | **str** | Package-url (PURL) of dependency. See https://github.com/package-url/purl-spec for more details. | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | User-defined metadata to store domain-specific information limited to 8 keys with scalar values. | [optional] 
**relationship** | **str** | A notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency. | [optional] 
**scope** | **str** | A notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes. | [optional] 
**dependencies** | **List[str]** | Array of package-url (PURLs) of direct child dependencies. | [optional] 

## Example

```python
from github_openapi.models.dependency import Dependency

# TODO update the JSON string below
json = "{}"
# create an instance of Dependency from a JSON string
dependency_instance = Dependency.from_json(json)
# print the JSON string representation of the object
print(Dependency.to_json())

# convert the object into a dict
dependency_dict = dependency_instance.to_dict()
# create an instance of Dependency from a dict
dependency_from_dict = Dependency.from_dict(dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


