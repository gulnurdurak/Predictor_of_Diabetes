class PredictionsDBRouter(object):
    """
    A router to control app1 db operations
    """
    def db_for_read(self, model, **hints):
        "Point all operations on app1 models to 'db_app1'"
        from django.conf import settings
        if 'predictions' not in settings.DATABASES.keys():
            return None
        if model._meta.app_label == 'predictions':
            return 'predictions'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on app1 models to 'db_app1'"
        from django.conf import settings
        if 'predictions' not in settings.DATABASES.keys():
            return None
        if model._meta.app_label == 'predictions':
            return 'predictions'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in app1 is involved"
        from django.conf import settings
        if 'predictions' not in settings.DATABASES.keys():
            return None
        if obj1._meta.app_label == 'predictions' or obj2._meta.app_label == 'predictions':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the app1 app only appears on the 'app1' db"
        from django.conf import settings
        if 'predictions' not in settings.DATABASES.keys():
            return None
        if db == 'db_app1':
            return model._meta.app_label == 'predictions'
        elif model._meta.app_label == 'predictions':
            return False
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if app_label == 'predictions':
            return db == 'predictions'
        return None