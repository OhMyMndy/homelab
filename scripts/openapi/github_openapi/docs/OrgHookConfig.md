# OrgHookConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**insecure_ssl** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.org_hook_config import OrgHookConfig

# TODO update the JSON string below
json = "{}"
# create an instance of OrgHookConfig from a JSON string
org_hook_config_instance = OrgHookConfig.from_json(json)
# print the JSON string representation of the object
print(OrgHookConfig.to_json())

# convert the object into a dict
org_hook_config_dict = org_hook_config_instance.to_dict()
# create an instance of OrgHookConfig from a dict
org_hook_config_from_dict = OrgHookConfig.from_dict(org_hook_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


