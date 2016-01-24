import config_tool


def get_database_url():
    """
    :rtype
    :return:
    """
    return config_tool.get_string('DATABASE_URL')
