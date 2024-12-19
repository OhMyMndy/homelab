# ParticipationStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **List[int]** |  | 
**owner** | **List[int]** |  | 

## Example

```python
from github_openapi.models.participation_stats import ParticipationStats

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipationStats from a JSON string
participation_stats_instance = ParticipationStats.from_json(json)
# print the JSON string representation of the object
print(ParticipationStats.to_json())

# convert the object into a dict
participation_stats_dict = participation_stats_instance.to_dict()
# create an instance of ParticipationStats from a dict
participation_stats_from_dict = ParticipationStats.from_dict(participation_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


