# OutpostRequest

Outpost Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**OutpostTypeEnum**](OutpostTypeEnum.md) |  | 
**providers** | **List[int]** |  | 
**service_connection** | **str** | Select Service-Connection authentik should use to manage this outpost. Leave empty if authentik should not handle the deployment. | [optional] 
**config** | **Dict[str, object]** |  | 
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 

## Example

```python
from authentik_openapi.models.outpost_request import OutpostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OutpostRequest from a JSON string
outpost_request_instance = OutpostRequest.from_json(json)
# print the JSON string representation of the object
print(OutpostRequest.to_json())

# convert the object into a dict
outpost_request_dict = outpost_request_instance.to_dict()
# create an instance of OutpostRequest from a dict
outpost_request_from_dict = OutpostRequest.from_dict(outpost_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


