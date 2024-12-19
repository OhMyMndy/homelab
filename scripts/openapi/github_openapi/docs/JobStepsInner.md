# JobStepsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The phase of the lifecycle that the job is currently in. | 
**conclusion** | **str** | The outcome of the job. | 
**name** | **str** | The name of the job. | 
**number** | **int** |  | 
**started_at** | **datetime** | The time that the step started, in ISO 8601 format. | [optional] 
**completed_at** | **datetime** | The time that the job finished, in ISO 8601 format. | [optional] 

## Example

```python
from github_openapi.models.job_steps_inner import JobStepsInner

# TODO update the JSON string below
json = "{}"
# create an instance of JobStepsInner from a JSON string
job_steps_inner_instance = JobStepsInner.from_json(json)
# print the JSON string representation of the object
print(JobStepsInner.to_json())

# convert the object into a dict
job_steps_inner_dict = job_steps_inner_instance.to_dict()
# create an instance of JobStepsInner from a dict
job_steps_inner_from_dict = JobStepsInner.from_dict(job_steps_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


