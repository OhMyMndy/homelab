# PullRequest6Base


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**ref** | **str** |  | 
**repo** | [**Repository10**](Repository10.md) |  | 
**sha** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.pull_request6_base import PullRequest6Base

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequest6Base from a JSON string
pull_request6_base_instance = PullRequest6Base.from_json(json)
# print the JSON string representation of the object
print(PullRequest6Base.to_json())

# convert the object into a dict
pull_request6_base_dict = pull_request6_base_instance.to_dict()
# create an instance of PullRequest6Base from a dict
pull_request6_base_from_dict = PullRequest6Base.from_dict(pull_request6_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


