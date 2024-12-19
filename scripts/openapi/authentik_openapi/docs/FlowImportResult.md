# FlowImportResult

Logs of an attempted flow import

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[LogEvent]**](LogEvent.md) |  | [readonly] 
**success** | **bool** |  | [readonly] 

## Example

```python
from authentik_openapi.models.flow_import_result import FlowImportResult

# TODO update the JSON string below
json = "{}"
# create an instance of FlowImportResult from a JSON string
flow_import_result_instance = FlowImportResult.from_json(json)
# print the JSON string representation of the object
print(FlowImportResult.to_json())

# convert the object into a dict
flow_import_result_dict = flow_import_result_instance.to_dict()
# create an instance of FlowImportResult from a dict
flow_import_result_from_dict = FlowImportResult.from_dict(flow_import_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


