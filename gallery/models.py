from django.db import migrations, models

# BARILOCHE
class Photo(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Referencia") 
    image = models.ImageField(verbose_name = "Imagen", upload_to="bariloche")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de modificacion")
    class Meta:
        verbose_name = "foto"
        verbose_name_plural = "Bariloche"
        ordering = ["-created"]
    def __str__(self): 
        return self.title


# BUENOS AIRES
class Ba(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Referencia") 
    image = models.ImageField(verbose_name = "Imagen", upload_to="ba")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de modificacion")
    class Meta:
        verbose_name = "foto"
        verbose_name_plural = "Buenos Aires"
        ordering = ["-created"]
    def __str__(self): 
        return self.title


# PEOPLE
class People(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Referencia") 
    image = models.ImageField(verbose_name = "Imagen", upload_to="people")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de modificacion")
    class Meta:
        verbose_name = "foto"
        verbose_name_plural = "People"
        ordering = ["-created"]
    def __str__(self): 
        return self.title

# INDUSTRIAL
class Industrial(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Referencia") 
    image = models.ImageField(verbose_name = "Imagen", upload_to="industrial")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de modificacion")
    class Meta:
        verbose_name = "foto"
        verbose_name_plural = "Industrial"
        ordering = ["-created"]
    def __str__(self): 
        return self.title
