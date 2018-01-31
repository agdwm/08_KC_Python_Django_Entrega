from django.contrib import admin
from django.utils.safestring import mark_safe

from blogs.models import Category, Blog, Post

admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('post_title', 'video', 'image', 'release_date', 'blog', 'categories', 'author')
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


    def get_image_html(self, post):
        return mark_safe('<img src="{0}" alt="{1}" height="100">'.format(post.image, post.post_title))
    get_image_html.short_description = "Image"

    def get_blog_html(self, post):
        return mark_safe('<em>{0}</em>'.format(post.blog))
    get_blog_html.short_description = "Blog"

    readonly_fields = ('get_blog_html', 'created_at', 'modified_at', 'get_image_html')

    fieldsets = (
        ("Post details",{
            'fields': ('post_title', 'intro', 'content')
        }),
        ("Media", {
            'fields': ('video', 'get_image_html')
        }),
        ("Realease date", {
            'fields': ('release_date',)
        }),
        ("Additional info",{
            'fields': ('get_blog_html', 'category')
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

    readonly_fields = ('user',)

    def user_full_name(self, blog):
        return "{0} {1}".format(blog.user.first_name, blog.user.last_name)

    user_full_name.short_description = "Blog author"
    user_full_name.admin_order_field = "user__first_name"

