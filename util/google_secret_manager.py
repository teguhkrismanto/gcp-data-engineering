from google.cloud import secretmanager

def access_secret_version(project_id, secret_id, version_id):
    """
    Access the payload for the given secret version if one exists.
    """
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version.
    response = client.access_secret_version(name=name)

    # Print the secret payload.
    # WARNING: Do not print the secret in a production environment.
    payload = response.payload.data.decode("UTF-8")
    print("Plaintext: {}".format(payload))
    return payload