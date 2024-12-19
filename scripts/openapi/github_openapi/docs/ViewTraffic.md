# ViewTraffic

View Traffic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**uniques** | **int** |  | 
**views** | [**List[Traffic]**](Traffic.md) |  | 

## Example

```python
from github_openapi.models.view_traffic import ViewTraffic

# TODO update the JSON string below
json = "{}"
# create an instance of ViewTraffic from a JSON string
view_traffic_instance = ViewTraffic.from_json(json)
# print the JSON string representation of the object
print(ViewTraffic.to_json())

# convert the object into a dict
view_traffic_dict = view_traffic_instance.to_dict()
# create an instance of ViewTraffic from a dict
view_traffic_from_dict = ViewTraffic.from_dict(view_traffic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


