from tabnanny import verbose

from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


# Create your models here.
class Category(MPTTModel):
    """
    create category
    """

    name = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category name"),
        help_text=_("format: required,max-100"),
    )
    slug = models.SlugField(
        max_length=150,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category safe URL"),
        help_text=_("format: required,letters,numbers,underscore, or hyphens"),
    )
    is_active = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("category visiblity"),
        help_text=_("format: true=category visisble"),
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("parent of category"),
        help_text=_("format: not required"),
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("product category")
        verbose_name_plural = _("product categories")

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    """
    create category
    """

    web_id = models.CharField(
        max_length=50,
        null=False,
        unique=True,
        blank=False,
        verbose_name=_("product website id"),
        help_text=_("format: required,unique"),
    )
    name = models.CharField(
        max_length=255,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("product name"),
        help_text=_("format: required,max-255"),
    )
    slug = models.SlugField(
        max_length=150,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("product safe URL"),
        help_text=_("format: required,letters,numbers,underscore, or hyphens"),
    )
    description = models.TextField(
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("product description"),
        help_text=_("format: required"),
    )
    category = TreeManyToManyField(Category)
    is_active = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("product visiblity"),
        help_text=_("format: true=product visisble"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("date product created"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("date product updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    def __str__(self):
        return self.name
