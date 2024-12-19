# BlueprintInstance

Info about a single blueprint instance file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**path** | **str** |  | [optional] [default to '']
**context** | **object** |  | [optional] 
**last_applied** | **datetime** |  | [readonly] 
**last_applied_hash** | **str** |  | [readonly] 
**status** | [**BlueprintInstanceStatusEnum**](BlueprintInstanceStatusEnum.md) |  | [readonly] 
**enabled** | **bool** |  | [optional] 
**managed_models** | **List[str]** |  | [readonly] 
**metadata** | **object** |  | [readonly] 
**content** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.blueprint_instance import BlueprintInstance

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintInstance from a JSON string
blueprint_instance_instance = BlueprintInstance.from_json(json)
# print the JSON string representation of the object
print(BlueprintInstance.to_json())

# convert the object into a dict
blueprint_instance_dict = blueprint_instance_instance.to_dict()
# create an instance of BlueprintInstance from a dict
blueprint_instance_from_dict = BlueprintInstance.from_dict(blueprint_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


