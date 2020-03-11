from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import CloudPakForDataAuthenticator

authenticator = CloudPakForDataAuthenticator(
    '{username}',
    '{password}',
    'https://{cpd_cluster_host}{:port}'
)

assistant = AssistantV2(
    version='{version}',
    authenticator=authenticator
)

assistant.set_service_url('https://{cpd_cluster_host}{:port}/assistant/{release}/instances/{instance_id}/api')
