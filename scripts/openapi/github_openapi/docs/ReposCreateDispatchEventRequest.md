# ReposCreateDispatchEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | A custom webhook event name. Must be 100 characters or fewer. | 
**client_payload** | **Dict[str, object]** | JSON payload with extra information about the webhook event that your action or workflow may use. The maximum number of top-level properties is 10. The total size of the JSON payload must be less than 64KB. | [optional] 

## Example

```python
from github_openapi.models.repos_create_dispatch_event_request import ReposCreateDispatchEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateDispatchEventRequest from a JSON string
repos_create_dispatch_event_request_instance = ReposCreateDispatchEventRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateDispatchEventRequest.to_json())

# convert the object into a dict
repos_create_dispatch_event_request_dict = repos_create_dispatch_event_request_instance.to_dict()
# create an instance of ReposCreateDispatchEventRequest from a dict
repos_create_dispatch_event_request_from_dict = ReposCreateDispatchEventRequest.from_dict(repos_create_dispatch_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


