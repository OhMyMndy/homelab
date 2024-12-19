# Stage

Stage Serializer

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

## Example

```python
from authentik_openapi.models.stage import Stage

# TODO update the JSON string below
json = "{}"
# create an instance of Stage from a JSON string
stage_instance = Stage.from_json(json)
# print the JSON string representation of the object
print(Stage.to_json())

# convert the object into a dict
stage_dict = stage_instance.to_dict()
# create an instance of Stage from a dict
stage_from_dict = Stage.from_dict(stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


