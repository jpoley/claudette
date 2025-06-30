import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

response = client.invoke_model(
    modelId="anthropic.claude-3-sonnet-20240229",
    body=json.dumps({
        "prompt": "\n\nHuman: What's a fun fact about space?\n\nAssistant:",
        "max_tokens_to_sample": 200,
        "temperature": 0.7,
        "stop_sequences": ["\n\nHuman:"]
    }),
    contentType="application/json",
    accept="application/json"
)

output = json.loads(response["body"].read())
print("\nClaude says:\n")
print(output["completion"])
