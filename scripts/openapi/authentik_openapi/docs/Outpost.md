# Outpost

Outpost Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**type** | [**OutpostTypeEnum**](OutpostTypeEnum.md) |  | 
**providers** | **List[int]** |  | 
**providers_obj** | [**List[Provider]**](Provider.md) |  | [readonly] 
**service_connection** | **str** | Select Service-Connection authentik should use to manage this outpost. Leave empty if authentik should not handle the deployment. | [optional] 
**service_connection_obj** | [**ServiceConnection**](ServiceConnection.md) |  | [readonly] 
**refresh_interval_s** | **int** |  | [readonly] 
**token_identifier** | **str** | Get Token identifier | [readonly] 
**config** | **Dict[str, object]** |  | 
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 

## Example

```python
from authentik_openapi.models.outpost import Outpost

# TODO update the JSON string below
json = "{}"
# create an instance of Outpost from a JSON string
outpost_instance = Outpost.from_json(json)
# print the JSON string representation of the object
print(Outpost.to_json())

# convert the object into a dict
outpost_dict = outpost_instance.to_dict()
# create an instance of Outpost from a dict
outpost_from_dict = Outpost.from_dict(outpost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


