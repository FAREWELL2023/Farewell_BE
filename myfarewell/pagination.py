from rest_framework.pagination import PageNumberPagination



class myfarewellPagination(PageNumberPagination):
    page_size = 10