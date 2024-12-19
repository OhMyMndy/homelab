# MinimalRepositoryLicense


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**spdx_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**node_id** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.minimal_repository_license import MinimalRepositoryLicense

# TODO update the JSON string below
json = "{}"
# create an instance of MinimalRepositoryLicense from a JSON string
minimal_repository_license_instance = MinimalRepositoryLicense.from_json(json)
# print the JSON string representation of the object
print(MinimalRepositoryLicense.to_json())

# convert the object into a dict
minimal_repository_license_dict = minimal_repository_license_instance.to_dict()
# create an instance of MinimalRepositoryLicense from a dict
minimal_repository_license_from_dict = MinimalRepositoryLicense.from_dict(minimal_repository_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


