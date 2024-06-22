TORTOISE_ORM = {
    "connections": {
        "default": {
            'engine': 'tortoise.backends.mysql',
            "credentials": {
                'host': '',
                'user': 'root',
                'password': 'root',
                'port': '3306',
                'database': 'default',
            }
        }
    },
    "apps": {
        "models": {"models": ["models", "aerich.models"], "default_connection": "default"},
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}
