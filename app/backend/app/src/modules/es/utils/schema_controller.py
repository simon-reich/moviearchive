from src.modules.es.schemas.schema_tmdb import get_schema_tmdb
from src.modules.es.schemas.schema_tmdb_2 import get_schema_tmdb_2
from src.modules.es.schemas.schema_tmdb_wiki import get_schema_tmdb_wiki
from src.modules.es.utils.mapping import map_movie_to_schema_tmdb, map_movie_to_schema_tmdb_2, map_movie_to_schema_tmdb_wiki, get_schema_fields_as_text_map


class SchemaController:
    def __init__(self):
        self.schemas = {
            'tmdb1': get_schema_tmdb(),
            'tmdb2': get_schema_tmdb_2(),
            'tmdb_wiki': get_schema_tmdb_wiki(),
        }
        self.mapping_to_schema = {
            'tmdb1': map_movie_to_schema_tmdb,
            'tmdb2': map_movie_to_schema_tmdb_2,
            'tmdb_wiki': map_movie_to_schema_tmdb_wiki,
        }
    
    def get_schema_fields_as_text(self):
        return get_schema_fields_as_text_map()


# schemas = {
#     'tmdb1': get_schema_tmdb(),
#     'tmdb2': get_schema_tmdb_2(),
#     'tmdb_wiki': get_schema_tmdb_wiki(),
# }

# mapping_to_schema = {
#     'tmdb1': map_movie_to_schema_tmdb,
#     'tmdb2': map_movie_to_schema_tmdb_2,
#     'tmdb_wiki': map_movie_to_schema_tmdb_wiki,
# }
