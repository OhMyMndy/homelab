# PatchedOutpostRequest

Outpost Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | [**OutpostTypeEnum**](OutpostTypeEnum.md) |  | [optional] 
**providers** | **List[int]** |  | [optional] 
**service_connection** | **str** | Select Service-Connection authentik should use to manage this outpost. Leave empty if authentik should not handle the deployment. | [optional] 
**config** | **Dict[str, object]** |  | [optional] 
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 

## Example

```python
from authentik_openapi.models.patched_outpost_request import PatchedOutpostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedOutpostRequest from a JSON string
patched_outpost_request_instance = PatchedOutpostRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedOutpostRequest.to_json())

# convert the object into a dict
patched_outpost_request_dict = patched_outpost_request_instance.to_dict()
# create an instance of PatchedOutpostRequest from a dict
patched_outpost_request_from_dict = PatchedOutpostRequest.from_dict(patched_outpost_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


