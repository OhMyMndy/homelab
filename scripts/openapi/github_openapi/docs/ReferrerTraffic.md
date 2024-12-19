# ReferrerTraffic

Referrer Traffic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referrer** | **str** |  | 
**count** | **int** |  | 
**uniques** | **int** |  | 

## Example

```python
from github_openapi.models.referrer_traffic import ReferrerTraffic

# TODO update the JSON string below
json = "{}"
# create an instance of ReferrerTraffic from a JSON string
referrer_traffic_instance = ReferrerTraffic.from_json(json)
# print the JSON string representation of the object
print(ReferrerTraffic.to_json())

# convert the object into a dict
referrer_traffic_dict = referrer_traffic_instance.to_dict()
# create an instance of ReferrerTraffic from a dict
referrer_traffic_from_dict = ReferrerTraffic.from_dict(referrer_traffic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


