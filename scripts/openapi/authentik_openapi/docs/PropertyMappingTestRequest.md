# PropertyMappingTestRequest

Test property mapping execution for a user/group with context

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** |  | [optional] 
**context** | **Dict[str, object]** |  | [optional] 
**group** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.property_mapping_test_request import PropertyMappingTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyMappingTestRequest from a JSON string
property_mapping_test_request_instance = PropertyMappingTestRequest.from_json(json)
# print the JSON string representation of the object
print(PropertyMappingTestRequest.to_json())

# convert the object into a dict
property_mapping_test_request_dict = property_mapping_test_request_instance.to_dict()
# create an instance of PropertyMappingTestRequest from a dict
property_mapping_test_request_from_dict = PropertyMappingTestRequest.from_dict(property_mapping_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


