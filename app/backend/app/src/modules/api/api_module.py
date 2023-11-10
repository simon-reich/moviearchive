from src.modules.api.api_controller import ApiSearch, ApiIndexMovie

class ApiModule:
    controller = {
        "searchMovie": ApiSearch,
        "indexMovie": ApiIndexMovie,
    }
    
