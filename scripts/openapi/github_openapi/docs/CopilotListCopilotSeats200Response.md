# CopilotListCopilotSeats200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_seats** | **int** | Total number of Copilot seats for the organization currently being billed. | [optional] 
**seats** | [**List[CopilotSeatDetails]**](CopilotSeatDetails.md) |  | [optional] 

## Example

```python
from github_openapi.models.copilot_list_copilot_seats200_response import CopilotListCopilotSeats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotListCopilotSeats200Response from a JSON string
copilot_list_copilot_seats200_response_instance = CopilotListCopilotSeats200Response.from_json(json)
# print the JSON string representation of the object
print(CopilotListCopilotSeats200Response.to_json())

# convert the object into a dict
copilot_list_copilot_seats200_response_dict = copilot_list_copilot_seats200_response_instance.to_dict()
# create an instance of CopilotListCopilotSeats200Response from a dict
copilot_list_copilot_seats200_response_from_dict = CopilotListCopilotSeats200Response.from_dict(copilot_list_copilot_seats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


