from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Article, Tag, Scope

class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            if not form.cleaned_data:
                continue
            if form.cleaned_data.get('is_main'):
                main_count += 1
        if main_count == 0:
            raise ValidationError('Укажите основной отдел.')
        elif main_count > 1:
            raise ValidationError('Основным может быть только один раздел.')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormSet

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at']
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

