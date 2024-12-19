# CloneTraffic

Clone Traffic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**uniques** | **int** |  | 
**clones** | [**List[Traffic]**](Traffic.md) |  | 

## Example

```python
from github_openapi.models.clone_traffic import CloneTraffic

# TODO update the JSON string below
json = "{}"
# create an instance of CloneTraffic from a JSON string
clone_traffic_instance = CloneTraffic.from_json(json)
# print the JSON string representation of the object
print(CloneTraffic.to_json())

# convert the object into a dict
clone_traffic_dict = clone_traffic_instance.to_dict()
# create an instance of CloneTraffic from a dict
clone_traffic_from_dict = CloneTraffic.from_dict(clone_traffic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


