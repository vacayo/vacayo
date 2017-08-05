from django.core.exceptions import ImproperlyConfigured
from storages.backends.gcloud import GoogleCloudStorage as GoogleCloudStorageBase, GoogleCloudFile
from storages.utils import clean_name
from google.cloud.exceptions import NotFound


class GoogleCloudStorage(GoogleCloudStorageBase):

    def _get_or_create_bucket(self, name):
        """
        Retrieves a bucket if it exists, otherwise creates it.
        """
        try:
            return self.client.get_bucket(name)
        except NotFound:
            if self.auto_create_bucket:
                bucket = self.client.create_bucket(name)
                bucket.acl.save_predefined(self.auto_create_acl)
                bucket.default_object_acl.save_predefined(self.auto_create_acl)
                return bucket
            raise ImproperlyConfigured("Bucket %s does not exist. Buckets "
                                       "can be automatically created by "
                                       "setting GS_AUTO_CREATE_BUCKET to "
                                       "``True``." % name)

    def _save(self, name, content):
        cleaned_name = clean_name(name)
        name = self._normalize_name(cleaned_name)

        content.name = cleaned_name
        encoded_name = self._encode_name(name)
        file = GoogleCloudFile(encoded_name, 'rw', self)
        file.blob.upload_from_file(content, size=content.size, content_type=file.mime_type)
        file.blob.acl.save_predefined(self.auto_create_acl)
        return cleaned_name
