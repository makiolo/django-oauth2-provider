from datetime import timedelta

from django.conf import settings

CONFIDENTIAL = 0
PUBLIC = 1

CLIENT_TYPES = (
    (CONFIDENTIAL, "Confidential (Web applications)"),
    (PUBLIC, "Public (Native and JS applications)")
)

RESPONSE_TYPE_CHOICES = ("code", "token")

TOKEN_TYPE = 'Bearer'

READ = 1 << 1
WRITE = 1 << 2
READ_WRITE = READ | WRITE

# NOTE that DEFAULT_SCOPES[0] (i.e. READ / 'read') is the default OAuth2 scope, per section 3.3 of rfc6749.
DEFAULT_SCOPES = (
    (READ, 'read'),
    (WRITE, 'write'),
    (READ_WRITE, 'read+write'),
)

SCOPES = DEFAULT_SCOPES

EXPIRE_DELTA = timedelta(days=365)

# Expiry delta for public clients (which typically have shorter lived tokens)
EXPIRE_DELTA_PUBLIC = timedelta(days=30)

EXPIRE_CODE_DELTA = timedelta(seconds=10 * 60)

# Remove expired tokens immediately instead of letting them persist.
DELETE_EXPIRED = False

ENFORCE_SECURE = False
ENFORCE_CLIENT_SECURE = True

SESSION_KEY = 'oauth'

SINGLE_ACCESS_TOKEN = False
