from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Menu Names'

    def __str__(self):
        return self.name


class MenuItems(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)
    url = models.CharField(max_length=100,
                           blank=True,
                           null=True,
                           unique=True)
    category = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'Items in Menu'

    def __str__(self):
        return self.name

    def children(self):
        return self.menuitems_set.all()

    def get_elder_ids(self):
        if self.parent:
            return self.parent.get_elder_ids() + [self.parent.id]
        else:
            return []