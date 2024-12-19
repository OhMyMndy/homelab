# BlueprintInstanceRequest

Info about a single blueprint instance file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**path** | **str** |  | [optional] [default to '']
**context** | **object** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.blueprint_instance_request import BlueprintInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintInstanceRequest from a JSON string
blueprint_instance_request_instance = BlueprintInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(BlueprintInstanceRequest.to_json())

# convert the object into a dict
blueprint_instance_request_dict = blueprint_instance_request_instance.to_dict()
# create an instance of BlueprintInstanceRequest from a dict
blueprint_instance_request_from_dict = BlueprintInstanceRequest.from_dict(blueprint_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


