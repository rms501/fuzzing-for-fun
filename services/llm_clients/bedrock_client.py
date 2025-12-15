import boto3

from services.llm_clients.base_client import BaseClient


class BedrockClient(BaseClient):

    def __init__(self):
        self._client=boto3.client("bedrock")
