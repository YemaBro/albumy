from flask_sqlalchemy import SQLAlchemy
from flask_login import AnonymousUserMixin, LoginManager
from flask_avatars import Avatars
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
from flask_whooshee import Whooshee
from flask_dropzone import Dropzone
from flask_mail import Mail
from flask_moment import Moment


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
dropzone = Dropzone()
moment = Moment()
avatars = Avatars()
whooshee = Whooshee()
csrf = CSRFProtect()


@login_manager.user_loader
def load_user(user_id):
    from albumy.models import User
    user = User.query.get(int(user_id))
    return user


login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'warning'
login_manager.refresh_view = 'auth.re_authenticate'
login_manager.needs_refresh_message_category = 'warning'


class Guest(AnonymousUserMixin):
    @property
    def is_admin(self):
        return False

    def can(self, permission_name):
        return False


login_manager.anonymous_user = Guest
