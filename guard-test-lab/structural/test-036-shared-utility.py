# TEST ID: TEST-036
# TEST CATEGORY: IMPACT / BLAST RADIUS
# EXPECTED SECURITY CHARACTERISTIC: Should be reviewed for potential shared utility impact.
# WHETHER THE CODE IS SAFE TO EXECUTE: Yes


def shared_helper(value):
    return value * 2


# This is a utility function that could be used across multiple modules.
# It is intentionally harmless and meant only to represent a wider blast radius.
