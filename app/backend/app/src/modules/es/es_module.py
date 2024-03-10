from src.modules.es.es_controller import (
    EsCreateIndex, 
    EsDeleteIndex, 
    EsAdvancedSearch, 
    EsGetAllIndicies, 
    EsGetDistinctValues, 
    EsGetMovieById,  
    EsGetEditValues, 
    EsExactSearch, 
    EsSingleFieldSearch, 
    EsMultiFieldSearch, 
    EsIndexFolder, 
    EsEditValues, 
    EsDeleteMovieByDocId,
    EsGetIndexMappingInfo,
    EsGetIndex,
    EsGetFieldsAsTextMap
)


class EsModule:
    controller = {
        "createIndex": EsCreateIndex,
        "deleteIndex": EsDeleteIndex,
        "getAllIndicies": EsGetAllIndicies,
        "exactSearch": EsExactSearch,
        "singleFieldSearch": EsSingleFieldSearch,
        "multiFieldSearch": EsMultiFieldSearch,
        "advancedSearch": EsAdvancedSearch,
        "getDocByImdbId": EsGetMovieById,
        "getDistinctValues": EsGetDistinctValues,
        "getEditValues": EsGetEditValues,
        "indexFolder": EsIndexFolder,
        "editDoc": EsEditValues,
        "deleteMovieByDocId": EsDeleteMovieByDocId,
        "getIndexMappingInfo": EsGetIndexMappingInfo,
        "getIndex": EsGetIndex,
        "getFieldsAsTextMap": EsGetFieldsAsTextMap,
    }