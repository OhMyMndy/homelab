# PatchedBlueprintInstanceRequest

Info about a single blueprint instance file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] [default to '']
**context** | **object** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_blueprint_instance_request import PatchedBlueprintInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedBlueprintInstanceRequest from a JSON string
patched_blueprint_instance_request_instance = PatchedBlueprintInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedBlueprintInstanceRequest.to_json())

# convert the object into a dict
patched_blueprint_instance_request_dict = patched_blueprint_instance_request_instance.to_dict()
# create an instance of PatchedBlueprintInstanceRequest from a dict
patched_blueprint_instance_request_from_dict = PatchedBlueprintInstanceRequest.from_dict(patched_blueprint_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


