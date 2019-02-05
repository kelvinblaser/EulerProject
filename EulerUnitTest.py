# Unit Test Framework for Project Euler

def testAssert(f, expectedVal, *args, **kwargs):
    actualVal = f(*args, **kwargs)
    assert actualVal == expectedVal, 'Error in test. Actual: {0}, Expected: {1}'.format(actualVal, expectedVal)
    return actualVal
    