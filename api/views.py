from main import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from . import serializers

@api_view(['GET'])
def get_category_list(request):
    queryset = models.Category.objects.all()
    category = serializers.CategorySerializer(queryset, many=True)
    return Response(category.data)


@api_view(['GET'])
def get_category_detail(request,id):
    queryset = models.Category.objects.get(id=id)
    post = serializers.CategorySerializer(queryset)
    return Response(post.data)


@api_view(['GET'])
def get_category_post_list(request,id):
    queryset = models.Post.objects.filter(category__id=id)
    post = serializers.PostSerializer(queryset, many=True)
    return Response(post.data)


@api_view(['GET'])
def get_post_list(request):
    queryset = models.Post.objects.all()
    
    paginator = PageNumberPagination()
    paginator.page_size = 5

    result_page = paginator.paginate_queryset(queryset, request)
    post = serializers.PostSerializer(result_page, many=True)
    
    return paginator.get_paginated_response(post.data)


@api_view(['GET'])
def get_post_detail(request,id):
    queryset = models.Post.objects.get(id=id)
    post = serializers.PostSerializer(queryset)
    return Response(post.data)


@api_view(['POST'])
def create_comment(request,id):
    post = models.Post.objects.get(id=id)
    text = request.POST.get('text')
    comment = models.Comment.objects.create(
        post=post, 
        text=text
    )
    return Response(serializers.CommentSerializer(comment).data,status=201)


@api_view(['GET'])
def get_post_comment(request,id):
    queryset = models.Comment.objects.filter(post__id=id)
    comment = serializers.CommentSerializer(queryset, many=True)
    return Response(comment.data)

@api_view(['GET'])
def get_comment(request,id):
    queryset = models.Comment.objects.get(id=id)
    comment = serializers.CommentSerializer(queryset)
    return Response(comment.data)