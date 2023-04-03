POST_SCHEMA_GET_USERS = {
    "type": "object",
    "properties": {
        "response": {
            "type": "array",
            "properties": {
                "id": {"type": "number"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "can_access_closed": {"type": "boolean"},
                "is_closed": {"type": "boolean"},
                "deactivated": {"type": "string"},
                "domain": {"type": "string"},
                "bdate": {"type": "string"},
                "city": {"type": "object", "properties": {"id": {"type": "number"}, "title": {"type": "string"}}},
                "country": {"type": "object", "properties": {"id": {"type": "number"}, "title": {"type": "string"}}},
            },
            "required": ["id", "first_name", "last_name", "can_access_closed", "is_closed"],
        }
    },
}

POST_SCHEMA_PHOTOS_SEARCH = {
    "type": "object",
    "properties": {
        "response": {
            "type": "object",
            "properties": {
                "count": {"type": "number"},
                "items": {
                    "type": "array",
                    "properties": {
                        "album_id": {"type": "number"},
                        "date": {"type": "number"},
                        "id": {"type": "number"},
                        "owner_id": {"type": "number"},
                        "lat": {"type": "number"},
                        "long": {"type": "number"},
                        "sizes": {
                            "type": "array",
                            "properties": {
                                "height": {"type": "number"},
                                "type": {"type": "string"},
                                "width": {"type": "number"},
                                "url": {"type": "string"},
                            },
                        },
                        "text": {"type": "string"},
                        "user_id": {"type": "number"},
                        "has_tags": {"type": "boolean"},
                    },
                },
            },
            "required": ["count", "items"],
        }
    },
}

POST_SCHEMA_PHOTOS_SEARCH_ERROR = {
    "type": "object",
    "properties": {
        "error": {
            "type": "object",
            "properties": {
                "error_code": {"type": "number"},
                "error_msg": {"type": "string"},
                "request_params": {
                    "type": "array",
                    "properties": {
                        "key": {"type": "string"},
                        "value": {"type": "string"},
                    },
                },
            },
        }
    },
}
