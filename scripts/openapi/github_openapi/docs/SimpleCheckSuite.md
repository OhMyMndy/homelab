# SimpleCheckSuite

A suite of checks performed on the code of a given code change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **str** |  | [optional] 
**app** | [**Integration**](Integration.md) |  | [optional] 
**before** | **str** |  | [optional] 
**conclusion** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**head_branch** | **str** |  | [optional] 
**head_sha** | **str** | The SHA of the head commit that is being checked. | [optional] 
**id** | **int** |  | [optional] 
**node_id** | **str** |  | [optional] 
**pull_requests** | [**List[PullRequestMinimal]**](PullRequestMinimal.md) |  | [optional] 
**repository** | [**MinimalRepository**](MinimalRepository.md) |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.simple_check_suite import SimpleCheckSuite

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleCheckSuite from a JSON string
simple_check_suite_instance = SimpleCheckSuite.from_json(json)
# print the JSON string representation of the object
print(SimpleCheckSuite.to_json())

# convert the object into a dict
simple_check_suite_dict = simple_check_suite_instance.to_dict()
# create an instance of SimpleCheckSuite from a dict
simple_check_suite_from_dict = SimpleCheckSuite.from_dict(simple_check_suite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


