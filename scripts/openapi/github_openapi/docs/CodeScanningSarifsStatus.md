# CodeScanningSarifsStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processing_status** | **str** | &#x60;pending&#x60; files have not yet been processed, while &#x60;complete&#x60; means results from the SARIF have been stored. &#x60;failed&#x60; files have either not been processed at all, or could only be partially processed. | [optional] 
**analyses_url** | **str** | The REST API URL for getting the analyses associated with the upload. | [optional] [readonly] 
**errors** | **List[str]** | Any errors that ocurred during processing of the delivery. | [optional] [readonly] 

## Example

```python
from github_openapi.models.code_scanning_sarifs_status import CodeScanningSarifsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningSarifsStatus from a JSON string
code_scanning_sarifs_status_instance = CodeScanningSarifsStatus.from_json(json)
# print the JSON string representation of the object
print(CodeScanningSarifsStatus.to_json())

# convert the object into a dict
code_scanning_sarifs_status_dict = code_scanning_sarifs_status_instance.to_dict()
# create an instance of CodeScanningSarifsStatus from a dict
code_scanning_sarifs_status_from_dict = CodeScanningSarifsStatus.from_dict(code_scanning_sarifs_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


