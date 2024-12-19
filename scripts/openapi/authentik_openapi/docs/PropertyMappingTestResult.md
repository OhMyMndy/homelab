# PropertyMappingTestResult

Result of a Property-mapping test

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [readonly] 
**successful** | **bool** |  | [readonly] 

## Example

```python
from authentik_openapi.models.property_mapping_test_result import PropertyMappingTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyMappingTestResult from a JSON string
property_mapping_test_result_instance = PropertyMappingTestResult.from_json(json)
# print the JSON string representation of the object
print(PropertyMappingTestResult.to_json())

# convert the object into a dict
property_mapping_test_result_dict = property_mapping_test_result_instance.to_dict()
# create an instance of PropertyMappingTestResult from a dict
property_mapping_test_result_from_dict = PropertyMappingTestResult.from_dict(property_mapping_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


