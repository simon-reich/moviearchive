from src.modules.db.user.db_user_controller import DbUser, DbUsers

class DbUserModule:
    controller = {
        "db_user": DbUser,
        "db_users": DbUsers,
    }