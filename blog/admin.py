from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from blog import models
from blog.models.database import db


# Customized admin interface
class CustomView(ModelView):
    pass


class TagAdminView(CustomView):
    column_searchable_list = ("name",)
    column_filters = ("name",)
    can_export = True
    export_types = ["csv", "xlsx"]


# Create admin with custom base template
admin = Admin(name="Blog Admin", template_mode="bootstrap4")

# Add views
admin.add_view(TagAdminView(models.Tag, db.session, category="Models"))
admin.add_view(CustomView(models.Article, db.session, category="Models"))
