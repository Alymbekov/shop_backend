from django.contrib import admin
from apps.authentication.models import User, Profile


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'full_name')
    
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'image', 'age', 'user')

class ProfileInline(admin.StackedInline):
    model = Profile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline, ]
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'age', 'user')


