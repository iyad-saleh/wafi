from django.db import models


class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        return super(SoftDeleteManager,self).get_queryset().filter(is_deleted=False)
    def all_with_deleted(self):
        return super(SoftDeleteManager,self).get_queryset()
    def deleted_set(self):
        return super(SoftDeleteManager,self).get_queryset().filter(is_deleted=True)

    def get(self, *args, **kwargs)    :
        return self.all_with_deleted().get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        if 'pk' in  kwargs:
            return self.all_with_deleted().filter(*args, **kwargs)
        return self.get_queryset().filter(*args, **kwargs)


