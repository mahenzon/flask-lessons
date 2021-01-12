from combojsonapi.event.resource import EventsResource
from flask_combo_jsonapi import ResourceDetail, ResourceList
from flask_combo_jsonapi.exceptions import ObjectNotFound

from blog.schemas import UserSchema
from blog.models.database import db
from blog.models import User


class UserDetailEvents(EventsResource):
    def event_update_avatar(self, **kwargs):
        # language=YAML
        """
        ---
        summary: Update user's avatar
        tags:
        - User
        parameters:
        - in: path
          name: id
          required: True
          type: integer
          format: int32
          description: user\'s id
        - in: formData
          name: new_avatar
          type: file
          description: New user\'s avatar
        consumes:
        - application/json
        responses:
          200:
            description: User
            schema:
                $ref: '#/definitions/UserSchema'
          400:
            description: Error
          500:
            description: Server error
        """
        user = User.query.filter_by(id=kwargs["id"]).one_or_none()
        if user is None:
            raise ObjectNotFound("user not found")

        # # TODO: set user's avatar
        # avatar = request.files.get("new_avatar")
        # if avatar:
        #     if avatar:
        #         filename = avatar.filename
        #         avatar.save(os.path.join(filename))
        #     user.url_avatar = os.path.join(filename)
        #     db.session.commit()
        schema = UserSchema()
        return schema.dump(user)


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
    }


class UserDetail(ResourceDetail):
    events = UserDetailEvents
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
    }
