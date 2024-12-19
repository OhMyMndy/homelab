# DenyStage

DenyStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**component** | **str** | Get object type so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**flow_set** | [**List[FlowSet]**](FlowSet.md) |  | [optional] 
**deny_message** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.deny_stage import DenyStage

# TODO update the JSON string below
json = "{}"
# create an instance of DenyStage from a JSON string
deny_stage_instance = DenyStage.from_json(json)
# print the JSON string representation of the object
print(DenyStage.to_json())

# convert the object into a dict
deny_stage_dict = deny_stage_instance.to_dict()
# create an instance of DenyStage from a dict
deny_stage_from_dict = DenyStage.from_dict(deny_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


