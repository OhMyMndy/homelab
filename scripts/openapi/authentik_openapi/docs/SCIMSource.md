# SCIMSource

SCIMSource Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** | Source&#39;s display Name. | 
**slug** | **str** | Internal source name, used in URLs. | 
**enabled** | **bool** |  | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**user_matching_mode** | [**UserMatchingModeEnum**](UserMatchingModeEnum.md) | How the source determines if an existing user should be authenticated or a new user enrolled. | [optional] 
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [readonly] 
**user_path_template** | **str** |  | [optional] 
**root_url** | **str** | Get Root URL | [readonly] 
**token_obj** | [**Token**](Token.md) |  | [readonly] 

## Example

```python
from authentik_openapi.models.scim_source import SCIMSource

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMSource from a JSON string
scim_source_instance = SCIMSource.from_json(json)
# print the JSON string representation of the object
print(SCIMSource.to_json())

# convert the object into a dict
scim_source_dict = scim_source_instance.to_dict()
# create an instance of SCIMSource from a dict
scim_source_from_dict = SCIMSource.from_dict(scim_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


