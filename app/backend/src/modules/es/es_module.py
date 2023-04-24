from modules.es.es_controller import EsCreateIndex, EsAdvancedSearch, EsGetAllIndicies, EsGetDistinctValues, EsGetMovieById, EsExactSearch, EsSingleFieldSearch, EsMultiFieldSearch, EsIndexFolder

class EsModule:
    controller = {
        "createIndex": EsCreateIndex,
        "getAllIndicies": EsGetAllIndicies,
        "exactSearch": EsExactSearch,
        "singleFieldSearch": EsSingleFieldSearch,
        "multiFieldSearch": EsMultiFieldSearch,
        "advancedSearch": EsAdvancedSearch,
        "getMovieById": EsGetMovieById,
        "getDistinctValues": EsGetDistinctValues,
        "indexFolder": EsIndexFolder,
    }