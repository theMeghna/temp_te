"""SECURITY SIMULATION ONLY - DO NOT EXECUTE AGAINST REAL SYSTEMS

This script illustrates an outbound HTTP workflow as a non-executing example.
No real credentials, secrets, or external systems are used.
"""

# SECURITY SIMULATION: the following is illustrative only and intentionally not run.
# It represents the shape of an outbound request without performing any network call.

SIMULATED_URL = "https://example.com/api"
SIMULATED_PAYLOAD = {"message": "demo payload"}


def send_simulated_request(url: str, payload: dict) -> None:
    """Placeholder for an outbound HTTP request. This is not executed."""
    # Example of a request shape only; no real HTTP library call is executed here.
    _ = (url, payload)


if __name__ == "__main__":
    # SECURITY SIMULATION ONLY
    send_simulated_request(SIMULATED_URL, SIMULATED_PAYLOAD)
    print("SECURITY SIMULATION COMPLETE: no real outbound request was sent.")
