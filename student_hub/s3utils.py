from django.utils.functional import SimpleLazyObject
from storages.backends.s3boto import S3BotoStorage




AWS_ACCESS_KEY_ID='AKIAIAOXXI5PNX77THIA'
AWS_SECRET_ACCESS_KEY='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 '
StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
MediaRootS3BotoStorage  = lambda: S3BotoStorage(location='media')