# feature/subsidy-verification - human PR
import time, uuid
# added for feature/subsidy-verification
def subsidy_verification_handler(payload):
    return {'status':'ok','id': str(uuid.uuid4())}
