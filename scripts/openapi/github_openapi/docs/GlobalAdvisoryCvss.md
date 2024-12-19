# GlobalAdvisoryCvss


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vector_string** | **str** | The CVSS vector. | 
**score** | **float** | The CVSS score. | [readonly] 

## Example

```python
from github_openapi.models.global_advisory_cvss import GlobalAdvisoryCvss

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalAdvisoryCvss from a JSON string
global_advisory_cvss_instance = GlobalAdvisoryCvss.from_json(json)
# print the JSON string representation of the object
print(GlobalAdvisoryCvss.to_json())

# convert the object into a dict
global_advisory_cvss_dict = global_advisory_cvss_instance.to_dict()
# create an instance of GlobalAdvisoryCvss from a dict
global_advisory_cvss_from_dict = GlobalAdvisoryCvss.from_dict(global_advisory_cvss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


