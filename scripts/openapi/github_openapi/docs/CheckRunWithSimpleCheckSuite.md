# CheckRunWithSimpleCheckSuite

A check performed on the code of a given code change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**NullableIntegration**](NullableIntegration.md) |  | 
**check_suite** | [**SimpleCheckSuite**](SimpleCheckSuite.md) |  | 
**completed_at** | **datetime** |  | 
**conclusion** | **str** |  | 
**deployment** | [**DeploymentSimple**](DeploymentSimple.md) |  | [optional] 
**details_url** | **str** |  | 
**external_id** | **str** |  | 
**head_sha** | **str** | The SHA of the commit that is being checked. | 
**html_url** | **str** |  | 
**id** | **int** | The id of the check. | 
**name** | **str** | The name of the check. | 
**node_id** | **str** |  | 
**output** | [**CheckRunWithSimpleCheckSuiteOutput**](CheckRunWithSimpleCheckSuiteOutput.md) |  | 
**pull_requests** | [**List[PullRequestMinimal]**](PullRequestMinimal.md) |  | 
**started_at** | **datetime** |  | 
**status** | **str** | The phase of the lifecycle that the check is currently in. | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.check_run_with_simple_check_suite import CheckRunWithSimpleCheckSuite

# TODO update the JSON string below
json = "{}"
# create an instance of CheckRunWithSimpleCheckSuite from a JSON string
check_run_with_simple_check_suite_instance = CheckRunWithSimpleCheckSuite.from_json(json)
# print the JSON string representation of the object
print(CheckRunWithSimpleCheckSuite.to_json())

# convert the object into a dict
check_run_with_simple_check_suite_dict = check_run_with_simple_check_suite_instance.to_dict()
# create an instance of CheckRunWithSimpleCheckSuite from a dict
check_run_with_simple_check_suite_from_dict = CheckRunWithSimpleCheckSuite.from_dict(check_run_with_simple_check_suite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


