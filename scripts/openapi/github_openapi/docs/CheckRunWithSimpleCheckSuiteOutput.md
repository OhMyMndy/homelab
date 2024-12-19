# CheckRunWithSimpleCheckSuiteOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations_count** | **int** |  | 
**annotations_url** | **str** |  | 
**summary** | **str** |  | 
**text** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from github_openapi.models.check_run_with_simple_check_suite_output import CheckRunWithSimpleCheckSuiteOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CheckRunWithSimpleCheckSuiteOutput from a JSON string
check_run_with_simple_check_suite_output_instance = CheckRunWithSimpleCheckSuiteOutput.from_json(json)
# print the JSON string representation of the object
print(CheckRunWithSimpleCheckSuiteOutput.to_json())

# convert the object into a dict
check_run_with_simple_check_suite_output_dict = check_run_with_simple_check_suite_output_instance.to_dict()
# create an instance of CheckRunWithSimpleCheckSuiteOutput from a dict
check_run_with_simple_check_suite_output_from_dict = CheckRunWithSimpleCheckSuiteOutput.from_dict(check_run_with_simple_check_suite_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


