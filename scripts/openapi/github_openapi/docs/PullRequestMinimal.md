# PullRequestMinimal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**number** | **int** |  | 
**url** | **str** |  | 
**head** | [**PullRequestMinimalHead**](PullRequestMinimalHead.md) |  | 
**base** | [**PullRequestMinimalHead**](PullRequestMinimalHead.md) |  | 

## Example

```python
from github_openapi.models.pull_request_minimal import PullRequestMinimal

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestMinimal from a JSON string
pull_request_minimal_instance = PullRequestMinimal.from_json(json)
# print the JSON string representation of the object
print(PullRequestMinimal.to_json())

# convert the object into a dict
pull_request_minimal_dict = pull_request_minimal_instance.to_dict()
# create an instance of PullRequestMinimal from a dict
pull_request_minimal_from_dict = PullRequestMinimal.from_dict(pull_request_minimal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


