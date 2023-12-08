class DataGoResponseFormatter:
    def __init__(self, field_mapping):
        self.field_mapping = field_mapping

    def _format_item_response(self, item_data):
        return {
            self.field_mapping.get(key, key): value
            for key, value in item_data.items()
            if value is not None and value != ""
        }

    def _format_items_response(self, items):
        return [self._format_item_response(item.get("item", {})) for item in items]

    def _format_items_response_without_item(self, items):
        return [self._format_item_response(item) for item in items]

    def format_response(self, json_data):
        items = json_data.get("items", [])
        has_item_field = items and "item" in items[0]
        format_items_response = self._format_items_response if has_item_field else self._format_items_response_without_item
        return {
            "pageNo": json_data.get("pageNo", ""),
            "totalCount": json_data.get("totalCount", ""),
            "numOfRows": json_data.get("numOfRows", ""),
            "items": format_items_response(items) if items else None,
        }
