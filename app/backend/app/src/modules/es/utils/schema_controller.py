from src.modules.es.schemas.schema_tmdb import get_tmdb_schema
from src.modules.es.schemas.schema_tmdb_2 import get_tmdb_schema_2
from src.modules.es.utils.mapping import map_movie_to_index_schema, map_movie_to_index_schema_2


schemas = {
    'tmdb1': get_tmdb_schema(),
    'tmdb2': get_tmdb_schema_2(),
}

mapping_to_schema = {
    'tmdb1': map_movie_to_index_schema,
    'tmdb2': map_movie_to_index_schema_2,
}