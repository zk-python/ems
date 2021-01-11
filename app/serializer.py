from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.models import Book


# class BookModelSerializer(ModelSerializer):
#     class Meta:
#         model=Book
#         fields=("book_name", "price", "pic", "publish", "create_time","id")
#         # 指定查询深度  关联对象的查询  可以查询出有外键关系的信息
#         # depth = 1
#         # 可以直接不序列化哪些字段
#         # exclude = ("is_delete", "status", "create_time")
#
# class BookDeModelSerializer(ModelSerializer):
#
#     class Meta:
#         model=Book
#         fields = ("book_name", "price", "authors", "publish")
#
#     # 反序列化的参数校验
#         extra_kwargs = {
#             "book_name": {
#                 "min_length": 4,
#                 "max_length": 8,
#                 "required": True,  # 设置为必填字段
#                 "error_messages": {
#                     "max_length": "字段不能超过8字符"
#                 }
#             },
#             "price": {
#                 "max_digits": 5,
#                 "decimal_places": 2,
#             }
#         }
#
#
#         #局部钩子
#         def validate_book_name(self, value):
#             book = Book.objects.filter(book_name=value).first()
#
#             if book:
#                 raise serializers.ValidationError("图书名已存在")
#             return value
class BookModelSerializerV2(ModelSerializer):
    class Meta:
        model = Book
        fields = ["create_time","book_name", "price", "publish", "authors", "get_pic","id" ]

        # authors = serializers.SerializerMethodField()
        #
        # def get_authors(self, obj):
        #     print(obj.authors,'54')
        #     return str(obj.authors)

            #添加检验规则
        extra_kwargs={
            "book_name": {
                "min_length": 4,
                "max_length": 8,
                "required": True,  # 设置为必填字段
                "error_messages": {
                    "max_length": "字段不能超过8字符"
                }
            },
            "price": {
                "max_digits": 5,
                "decimal_places": 2,},
                # 指定此字段只参与反序列化
                # "publish": {
                #     "write_only": True
                # },
                # "authors": {
                #     "write_only": True
                # },
            # 指定此字段只参与序列化
            "get_pic": {
                "read_only": True
            },
            "id":{
                "read_only":True
            }


            }

    def validate_book_name(self, value):
        book = Book.objects.filter(book_name=value).first()

        if book:
            raise serializers.ValidationError("图书名已存在")
        return value