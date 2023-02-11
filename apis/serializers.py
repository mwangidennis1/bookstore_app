from rest_framework import  serializers
from books.models import Book 

class BookstoreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields =('title','author','price')
    
