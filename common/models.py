from django.db import models


# 🔹 1. QuerySet (filter().delete() ni ushlaydi)
class BaseQuerySet(models.QuerySet):
    def delete(self):
        return self.update(is_deleted=True)


# 🔹 2. Manager (faqat aktivlarni qaytaradi)
class ActiveManager(models.Manager):
    def get_queryset(self):
        return BaseQuerySet(self.model, using=self._db).filter(is_deleted=False)


# 🔹 3. BaseModel (ixtiyoriy)
class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True




class DeletedModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    objects = ActiveManager()
    all_objects = BaseQuerySet.as_manager()


    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True