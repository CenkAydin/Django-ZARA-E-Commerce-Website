from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    slug = models.SlugField(default=name)
    parent2 = models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.CASCADE)

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        
        # __str__ method elaborated later in post.  use __unicode__ in place of
        
        # __str__ if you are using python 2

        unique_together = ('slug', 'parent2',)    
        verbose_name_plural = "categories"     

    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent2
        while k is not None:
            full_path.append(k.name)
            k = k.parent2
        return ' -> '.join(full_path[::-1])
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    @staticmethod
    def get_first_four_categories():
        return Category.objects.all()[:4]

    @staticmethod
    def get_woman_categories():
        return Category.objects.all()[4:24]

    @staticmethod
    def get_child_categories():
        return Category.objects.all()[24:26]  

    @staticmethod
    def get_child_female_categories():
        return Category.objects.all()[26:29]

    @staticmethod
    def get_beauty_categories():
        return Category.objects.all()[29:35]

    @staticmethod
    def get_child_male_categories():
        return Category.objects.all()[35:38]

    @staticmethod
    def get_man_categories():
        return Category.objects.all()[38:52]

   