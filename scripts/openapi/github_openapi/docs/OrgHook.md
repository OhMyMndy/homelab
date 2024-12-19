# OrgHook

Org Hook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**url** | **str** |  | 
**ping_url** | **str** |  | 
**deliveries_url** | **str** |  | [optional] 
**name** | **str** |  | 
**events** | **List[str]** |  | 
**active** | **bool** |  | 
**config** | [**OrgHookConfig**](OrgHookConfig.md) |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**type** | **str** |  | 

## Example

```python
from github_openapi.models.org_hook import OrgHook

# TODO update the JSON string below
json = "{}"
# create an instance of OrgHook from a JSON string
org_hook_instance = OrgHook.from_json(json)
# print the JSON string representation of the object
print(OrgHook.to_json())

# convert the object into a dict
org_hook_dict = org_hook_instance.to_dict()
# create an instance of OrgHook from a dict
org_hook_from_dict = OrgHook.from_dict(org_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


