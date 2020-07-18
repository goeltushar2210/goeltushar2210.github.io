from django.contrib import admin
from product.models  import *
from mptt.admin import DraggableMPTTAdmin





class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'    

class ProductImageInline(admin.TabularInline):        # how many images we want add to a product
    model = Images
    extra = 4

class ProductAdmin(admin.ModelAdmin):                 # manage product at database
    list_display      = ['title','category','status','image_tag','Quantity']
    list_filter       = ['category'] 
    readonly_fields    = ('image_tag',)
    inlines           = [ProductImageInline]          # inline from line-10
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images)    
