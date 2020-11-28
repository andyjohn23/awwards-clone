from django.apps import AppConfig


class AwwardsUsersConfig(AppConfig):
    name = 'awwards_users'

    def ready(self):
        import awwards_users.signals
