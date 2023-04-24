from modules.imdbApi.imdbapi_controller import ImdbApiSearch, ImdbApiArchiveMovie

class ImdbApiModule:
    controller = {
        "searchMovie": ImdbApiSearch,
        "archiveMovie": ImdbApiArchiveMovie,
    }
    
