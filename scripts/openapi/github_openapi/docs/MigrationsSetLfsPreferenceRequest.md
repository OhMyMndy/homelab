# MigrationsSetLfsPreferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_lfs** | **str** | Whether to store large files during the import. &#x60;opt_in&#x60; means large files will be stored using Git LFS. &#x60;opt_out&#x60; means large files will be removed during the import. | 

## Example

```python
from github_openapi.models.migrations_set_lfs_preference_request import MigrationsSetLfsPreferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationsSetLfsPreferenceRequest from a JSON string
migrations_set_lfs_preference_request_instance = MigrationsSetLfsPreferenceRequest.from_json(json)
# print the JSON string representation of the object
print(MigrationsSetLfsPreferenceRequest.to_json())

# convert the object into a dict
migrations_set_lfs_preference_request_dict = migrations_set_lfs_preference_request_instance.to_dict()
# create an instance of MigrationsSetLfsPreferenceRequest from a dict
migrations_set_lfs_preference_request_from_dict = MigrationsSetLfsPreferenceRequest.from_dict(migrations_set_lfs_preference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


