# LogstreamEndpointConfiguration

The current configuration of a log streaming endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_type** | [**LogType**](LogType.md) | The type of log that is streamed to this endpoint. | [optional] [readonly] 
**destination_type** | **str** | The type of system to which logs are being streamed. | [optional] 
**url** | **str** | The URL to which log streams are being posted. If the DestinationType is &#x60;s3&#x60;, the URL may be (and often is) empty to use the official Amazon S3 endpoint. | [optional] 
**user** | **str** | The username with which log streams to this endpoint are authenticated. | [optional] 
**token** | **str** | The token/password with which log streams to this endpoint should be authenticated. | [optional] 
**s3_bucket** | **str** | The S3 bucket name. Required if the destinationType is &#x60;s3&#x60;. | [optional] 
**s3_region** | **str** | The region in which the S3 bucket is located. Required if the destinationType is &#x60;s3&#x60;. | [optional] 
**s3_key_prefix** | **str** | An optional S3 key prefix to prepend to the auto-generated S3 key name. | [optional] 
**s3_authentication_type** | **str** | What type of authentication to use for S3. Required if the destinationType is &#x60;s3&#x60;. Tailscale recommends using &#x60;rolearn&#x60;. See [Amazon documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html). | [optional] 
**s3_access_key_id** | **str** | The S3 access key ID. Required if the destinationType is &#x60;s3&#x60; and &#x60;authenticationType&#x60; is &#x60;accesskey&#x60;. | [optional] 
**s3_secret_access_key** | **str** | The S3 secret access key. Required if the destinationType is &#x60;s3&#x60; and &#x60;authenticationType&#x60; is &#x60;accesskey&#x60;. | [optional] 
**s3_role_arn** | **str** | The Role ARN that Tailscale should supply to AWS when authenticating using role-based authentication. Required if the destinationType is &#x60;s3&#x60; and &#x60;authenticationType&#x60; is &#x60;rolearn&#x60;. | [optional] 
**aws_external_id** | **str** | The ID of an AwsExternalId that identifies what external ID Tailscale should supply to AWS when authenticating using role-based authentication. Required if the destinationType is &#x60;s3&#x60; and &#x60;authenticationType&#x60; is &#x60;rolearn&#x60;. This corresponds to the &#x60;id&#x60; field obtained from [tailnet/{tailnet}/aws-external-id](#tag/logging/POST/tailnet/{tailnet}/aws-external-id). | [optional] 
**s3_external_id** | **str** | The AWS external id that Tailscale supplies when authenticating using role-based authentication. Populated if the destinationType is &#x60;s3&#x60; and &#x60;authenticationType&#x60; is &#x60;rolearn&#x60;. | [optional] [readonly] 

## Example

```python
from tailscale_openapi.models.logstream_endpoint_configuration import LogstreamEndpointConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of LogstreamEndpointConfiguration from a JSON string
logstream_endpoint_configuration_instance = LogstreamEndpointConfiguration.from_json(json)
# print the JSON string representation of the object
print(LogstreamEndpointConfiguration.to_json())

# convert the object into a dict
logstream_endpoint_configuration_dict = logstream_endpoint_configuration_instance.to_dict()
# create an instance of LogstreamEndpointConfiguration from a dict
logstream_endpoint_configuration_from_dict = LogstreamEndpointConfiguration.from_dict(logstream_endpoint_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


