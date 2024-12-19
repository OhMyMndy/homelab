# Traffic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | 
**uniques** | **int** |  | 
**count** | **int** |  | 

## Example

```python
from github_openapi.models.traffic import Traffic

# TODO update the JSON string below
json = "{}"
# create an instance of Traffic from a JSON string
traffic_instance = Traffic.from_json(json)
# print the JSON string representation of the object
print(Traffic.to_json())

# convert the object into a dict
traffic_dict = traffic_instance.to_dict()
# create an instance of Traffic from a dict
traffic_from_dict = Traffic.from_dict(traffic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


