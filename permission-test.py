"""SECURITY SIMULATION ONLY - DO NOT EXECUTE AGAINST REAL SYSTEMS

This file demonstrates a workflow that reads a local file and would send its
contents to an external endpoint, but it is intentionally non-functional and
simulated only.
"""

# SECURITY SIMULATION: no real credentials, no real HTTP requests, no real file access.
# The purpose is to model the workflow pattern without executing it.

PRIVATE_FILE = "private_data.txt"
SIMULATED_ENDPOINT = "https://example.com/simulated-endpoint"


def read_local_file(path: str) -> str:
    """Simulated read of a local file. This is a model only."""
    return "SIMULATED_CONTENT"


def send_to_external_endpoint(payload: str, url: str) -> None:
    """Simulated external request. This does not send any real HTTP request."""
    # Deliberately not executed in this simulation.
    return None


if __name__ == "__main__":
    # SECURITY SIMULATION ONLY
    content = read_local_file(PRIVATE_FILE)
    send_to_external_endpoint(content, SIMULATED_ENDPOINT)
    print("SECURITY SIMULATION COMPLETE: no real request was sent.")
