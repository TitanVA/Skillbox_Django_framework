from django.db import models

# Create your models here.
class Vacancy(models.Model):
    is_active = models.BooleanField(default=False, verbose_name="Активность")
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    description = models.TextField(default="", verbose_name="Описание")
    publisher = models.CharField(max_length=30, verbose_name="Кто опубликовал")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    published_at = models.DateTimeField(verbose_name="Дата публикации", blank=True, null=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = "Вакансии"
        permissions = (
            ("Can_publish", "Может публиковать"),
        )

    def __str__(self):
        return self.title
