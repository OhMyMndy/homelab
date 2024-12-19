# ContentTraffic

Content Traffic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | 
**title** | **str** |  | 
**count** | **int** |  | 
**uniques** | **int** |  | 

## Example

```python
from github_openapi.models.content_traffic import ContentTraffic

# TODO update the JSON string below
json = "{}"
# create an instance of ContentTraffic from a JSON string
content_traffic_instance = ContentTraffic.from_json(json)
# print the JSON string representation of the object
print(ContentTraffic.to_json())

# convert the object into a dict
content_traffic_dict = content_traffic_instance.to_dict()
# create an instance of ContentTraffic from a dict
content_traffic_from_dict = ContentTraffic.from_dict(content_traffic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


