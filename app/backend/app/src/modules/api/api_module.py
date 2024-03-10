from src.modules.api.api_controller import ApiSearch, ApiIndexMovie, ApiIndexByFile

class ApiModule:
    controller = {
        "searchMovie": ApiSearch,
        "indexMovie": ApiIndexMovie,
        "indexByFile": ApiIndexByFile,
    }
    
