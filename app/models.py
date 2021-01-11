from django.db import models

# Create your models here.
# 抽象表
class BaseModel(models.Model):
   #是否以删除
   is_delete = models.BooleanField(default=False)
   # 时间
   create_time = models.DateField(auto_now=True)
   #状态
   status = models.BooleanField(default=True)
   class Meta:
       #声明此表是抽象表
    abstract=True



#书表
class Book(BaseModel):
    book_name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pic = models.ImageField(upload_to="pic", default="pic/1.jpg")
    authors = models.ManyToManyField(to="Author", db_constraint=False, related_name="books")
    publish = models.ForeignKey(to="Press", on_delete=models.CASCADE,
                                db_constraint=False,  # 删除后对应字段的值可以为空
                                related_name="books")  # 反向查询的名称

    @property
    def author_list(self):
        return self.authors.values("author_name")
    @property
    def publish_list(self):
        return self.publish
    @property
    def get_pic(self):
        return  "%s%s%s" % ("http://127.0.0.1:8000/", "media/", self.pic)

    class Meta:
        db_table = "bz_book"
        verbose_name = "图书表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name


#出版社表
class Press(BaseModel):
    press_name = models.CharField(max_length=128)
    pic = models.ImageField(upload_to="pic", default="1.jpg")
    address = models.CharField(max_length=256)

    class Meta:
        db_table = "bz_press"
        verbose_name = "出版社表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.press_name




#作者表
class Author(BaseModel):
    author_name = models.CharField(max_length=128)
    age = models.IntegerField()

    class Meta:
        db_table = "bz_author"
        verbose_name = "作者表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.author_name

#作者详情表
class AuthorDetail(BaseModel):
    phone = models.CharField(max_length=11)
    author = models.OneToOneField(to="Author", on_delete=models.CASCADE, related_name="detail")

    class Meta:
        db_table = "bz_author_detail"
        verbose_name = "作者详情表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s的详情" % self.author.author_name

