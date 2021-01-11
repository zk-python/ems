from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Book


# class BookAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         book_id = kwargs.get("id")
#         if book_id:
#             book_obj=Book.objects.filter(pk=book_id).first()
#             data=BookModelSerializer(book_obj).data
#             return Response({"message": "查询单个成功", "results": data})
#         else:
#             query_set = Book.objects.all()
#             data = BookModelSerializer(query_set, many=True).data
#             return Response({"message": "查询单个成功", "results": data})
#
#     def post(self,request, *args, **kwargs):
#         request_data = request.data
#         serializer = BookDeModelSerializer(data=request_data)
#
#         serializer.is_valid(raise_exception=True)
#         book_obj = serializer.save()
#         return Response({
#             "message": "新增图书成功",
#             "results": BookModelSerializer(book_obj).data,
#         }, status=status.HTTP_201_CREATED)
from app.serializer import BookModelSerializerV2


class BookAPIViewV2(APIView):
    def get(self, request, *args, **kwargs):
        book_id = kwargs.get("id")
        if book_id:
            book_obj=Book.objects.filter(pk=book_id).first()
            data=BookModelSerializerV2(book_obj).data
            return Response({"message": "查询单个成功", "results": data})
        else:
            query_set = Book.objects.all()
            data = BookModelSerializerV2(query_set, many=True).data
            return Response({"message": "查询多个成功", "results": data})

    def post(self, request, *args, **kwargs):
        """
                增加单个：传递的参数格式 字典
                增加多个：[{},{},{}]  列表嵌套一个个新增的对象
        """
        request_data = request.data
        print(request_data)
        if isinstance(request_data,dict)and request_data != {}:
            many=False

        elif isinstance(request_data,list) and request_data!=[]:
            many=True
        else:
            return Response({
                "message": "参数格式有误"
            }
            ,status=status.HTTP_400_BAD_REQUEST)
        ser=BookModelSerializerV2(data=request_data,many=many)
        ser.is_valid(raise_exception=True)
        book_obj=ser.save()
        return Response(
            {"message":"新增图书成功","results": BookModelSerializerV2(book_obj, many=many).data,},
            status=status.HTTP_201_CREATED
        )

    def delete(self,request,*args,**kwargs):
        book_id=kwargs.get('id')
        # if book_id:
        #     ids=[book_id]
        # else:
        #     ids=request.data.get("ids")

        # response = Book.objects.filter(pk__in=ids, is_delete=False).update(is_delete=True)
        response = Book.objects.filter(pk=book_id)
        if response:
            response.delete()
            return Response({
                "message": "删除成功",
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "删除失败或图书不存在",
        }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,*args,**kwargs):
        request_data = request.data
        book_id = kwargs.get("id")
        try:
            book_obj = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                "message": "修改的图书不存在"
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = BookModelSerializerV2(data=request_data, instance=book_obj, partial=True)
        serializer.is_valid(raise_exception=True)

        # 在校验通过会调用ModelSerializer中的update()方法完成更新
        book = serializer.save()
        return Response({
            "message": "修改成功",
            "results": BookModelSerializerV2(book).data
        }, status=status.HTTP_200_OK)
