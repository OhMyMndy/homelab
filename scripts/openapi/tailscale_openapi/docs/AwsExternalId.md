# AwsExternalId

An external ID for use in authenticating to AWS using role-based authentication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique identifier for this AWS external id in the Tailscale system. | [optional] [readonly] 
**external_id** | **str** | The actual external id that Tailscale will supply to AWS when authenticating using role-based authentication. | [optional] 
**tailscale_aws_account_id** | **str** | The AWS account id that Tailscale will supply to AWS when authenticating using role-based authentication. | [optional] 

## Example

```python
from tailscale_openapi.models.aws_external_id import AwsExternalId

# TODO update the JSON string below
json = "{}"
# create an instance of AwsExternalId from a JSON string
aws_external_id_instance = AwsExternalId.from_json(json)
# print the JSON string representation of the object
print(AwsExternalId.to_json())

# convert the object into a dict
aws_external_id_dict = aws_external_id_instance.to_dict()
# create an instance of AwsExternalId from a dict
aws_external_id_from_dict = AwsExternalId.from_dict(aws_external_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


