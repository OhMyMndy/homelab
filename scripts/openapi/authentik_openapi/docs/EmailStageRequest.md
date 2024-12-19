# EmailStageRequest

EmailStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**use_global_settings** | **bool** | When enabled, global Email connection settings will be used and connection settings below will be ignored. | [optional] 
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**use_tls** | **bool** |  | [optional] 
**use_ssl** | **bool** |  | [optional] 
**timeout** | **int** |  | [optional] 
**from_address** | **str** |  | [optional] 
**token_expiry** | **int** | Time in minutes the token sent is valid. | [optional] 
**subject** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**activate_user_on_success** | **bool** | Activate users upon completion of stage. | [optional] 

## Example

```python
from authentik_openapi.models.email_stage_request import EmailStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailStageRequest from a JSON string
email_stage_request_instance = EmailStageRequest.from_json(json)
# print the JSON string representation of the object
print(EmailStageRequest.to_json())

# convert the object into a dict
email_stage_request_dict = email_stage_request_instance.to_dict()
# create an instance of EmailStageRequest from a dict
email_stage_request_from_dict = EmailStageRequest.from_dict(email_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


