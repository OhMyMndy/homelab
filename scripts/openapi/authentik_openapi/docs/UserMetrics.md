# UserMetrics

User Metrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logins** | [**List[Coordinate]**](Coordinate.md) |  | [readonly] 
**logins_failed** | [**List[Coordinate]**](Coordinate.md) |  | [readonly] 
**authorizations** | [**List[Coordinate]**](Coordinate.md) |  | [readonly] 

## Example

```python
from authentik_openapi.models.user_metrics import UserMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of UserMetrics from a JSON string
user_metrics_instance = UserMetrics.from_json(json)
# print the JSON string representation of the object
print(UserMetrics.to_json())

# convert the object into a dict
user_metrics_dict = user_metrics_instance.to_dict()
# create an instance of UserMetrics from a dict
user_metrics_from_dict = UserMetrics.from_dict(user_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


