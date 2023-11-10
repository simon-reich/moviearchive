from src.modules.db.index.db_index_controller import DbIndex, DbIndices, DbIndexByName

class DbIndexModule:
    controller = {
        "db_index": DbIndex,
        "db_indices": DbIndices,
        "db_index_by_name": DbIndexByName
    }