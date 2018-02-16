from django.contrib import admin

from blogs.models import Category, Blog, Post

admin.site.site_header = "WORDPLEASE Backoffice"
admin.site.site_title = admin.site.site_header

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('post_title', 'video', 'image', 'release_date', 'blog', 'intro', 'categories', 'author')
    list_filter = ('category', 'blog', 'release_date')
    search_fields = ('post_title', 'intro', 'content', 'blog__user__username')

    def categories(self, post):
        return ",\n".join([c.name for c in post.category.all()])

    categories.short_description = "Post category"
    categories.admin_order_field = "category__name"


    def author(self, post):
        return "{0}".format(post.blog.user)

    author.short_description = "Post author"
    author.admin_order_field = "blog__user"

    readonly_fields = ('created_at', 'modified_at')

    fieldsets = (
        ("Post details",{
            'fields': ('post_title', 'intro', 'content')
        }),
        ("Media", {
            'fields': ('video', 'image')
        }),
        ("Realease date", {
            'fields': ('release_date',)
        }),
        ("Additional info",{
            'fields': ('blog', 'category')
        }),
        ("Creation & Modification", {
            'fields': ('created_at', 'modified_at'),
            'classes': ('collapse',),
            'description': 'This fields are auto-generated'
        })
    )



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = ('blog_title', 'user', 'user_full_name')
    list_filter = ('user',)
    search_fields = ('blog_title', 'description', 'user__username')

    def user_full_name(self, blog):
        return "{0} {1}".format(blog.user.first_name, blog.user.last_name)

    user_full_name.short_description = "Blog author"
    user_full_name.admin_order_field = "user__first_name"



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields = ('name',)
