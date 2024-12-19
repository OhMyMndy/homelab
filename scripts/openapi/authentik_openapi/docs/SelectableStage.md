# SelectableStage

Serializer for stages which can be selected by users

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | 
**name** | **str** |  | 
**verbose_name** | **str** |  | 
**meta_model_name** | **str** |  | 

## Example

```python
from authentik_openapi.models.selectable_stage import SelectableStage

# TODO update the JSON string below
json = "{}"
# create an instance of SelectableStage from a JSON string
selectable_stage_instance = SelectableStage.from_json(json)
# print the JSON string representation of the object
print(SelectableStage.to_json())

# convert the object into a dict
selectable_stage_dict = selectable_stage_instance.to_dict()
# create an instance of SelectableStage from a dict
selectable_stage_from_dict = SelectableStage.from_dict(selectable_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


