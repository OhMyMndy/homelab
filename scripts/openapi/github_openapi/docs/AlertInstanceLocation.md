# AlertInstanceLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_column** | **int** |  | [optional] 
**end_line** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**start_column** | **int** |  | [optional] 
**start_line** | **int** |  | [optional] 

## Example

```python
from github_openapi.models.alert_instance_location import AlertInstanceLocation

# TODO update the JSON string below
json = "{}"
# create an instance of AlertInstanceLocation from a JSON string
alert_instance_location_instance = AlertInstanceLocation.from_json(json)
# print the JSON string representation of the object
print(AlertInstanceLocation.to_json())

# convert the object into a dict
alert_instance_location_dict = alert_instance_location_instance.to_dict()
# create an instance of AlertInstanceLocation from a dict
alert_instance_location_from_dict = AlertInstanceLocation.from_dict(alert_instance_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


