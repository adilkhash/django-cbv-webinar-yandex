from importlib import import_module

from django.contrib import admin
from django.apps import apps
from news.models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'created']
    ordering = ('-created',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'news', 'text', 'created']
    ordering = ('-created',)

#
#
# def autoregister(*app_list):
#     for app_name in app_list:
#         admin_module_path = f'{app_name}.admin'
#         admin_module = import_module(admin_module_path)
#
#         app_confi = apps.get_app_config(app_name)
#         for model in app_confi.get_models():
#             model_admin = getattr(admin_module, f'{model.__name__}Admin', None)
#
#             try:
#                 if model_admin:
#                     admin.site.register(model, model_admin)
#                 else:
#                     admin.site.register(model)
#             except admin.sites.AlreadyRegistered:
#                 pass
#
# autoregister('news', )




# admin.site.register(News, NewsAdmin)
# admin.site.register(Comment, CommentAdmin)
