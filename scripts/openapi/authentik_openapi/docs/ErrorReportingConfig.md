# ErrorReportingConfig

Config for error reporting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [readonly] 
**sentry_dsn** | **str** |  | [readonly] 
**environment** | **str** |  | [readonly] 
**send_pii** | **bool** |  | [readonly] 
**traces_sample_rate** | **float** |  | [readonly] 

## Example

```python
from authentik_openapi.models.error_reporting_config import ErrorReportingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorReportingConfig from a JSON string
error_reporting_config_instance = ErrorReportingConfig.from_json(json)
# print the JSON string representation of the object
print(ErrorReportingConfig.to_json())

# convert the object into a dict
error_reporting_config_dict = error_reporting_config_instance.to_dict()
# create an instance of ErrorReportingConfig from a dict
error_reporting_config_from_dict = ErrorReportingConfig.from_dict(error_reporting_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


