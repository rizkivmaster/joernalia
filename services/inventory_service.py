from entity import item


def register_item(good):
    """
    :type good: item.Item
    :param item:
    :return:
    """
    item.item_accessor.add(good)
    item.item_accessor.commit()

def update_item(good):
    """
    :type good: item.Item
    :param good:
    :return:
    """
    item.item_accessor.commit()


def get_recent_collections():
    return item.item_accessor.query(item.Item).order_by(item.Item.date_added).limit(10)


def get_collection_by_id(id):
    """
    :type id: int
    :param id:
    :return:
    """
    return item.item_accessor.query(item.Item).filter(item.Item.id == id).first()


class SearchSpec(object):
    def __init__(self):
        self.keyword = None
        self.date_start = None
        self.date_end = None
        self.price_start = None
        self.price_end = None
        self.limit = None


def search_collection_by_spec(spec):
    """
    :type spec: SearchSpec
    :param spec:
    :return:
    """
    spec_list = []
    spec_list.append(item.Item.date_added >= spec.date_start) if spec.date_start else None
    spec_list.append(item.Item.date_added <= spec.date_end) if spec.date_end else None
    spec_list.append(item.Item.price >= spec.price_start) if spec.price_start else None
    spec_list.append(item.Item.price <= spec.price_end) if spec.price_end else None
    return item.item_accessor.query(item.Item).filter(*spec_list).limit(spec.limit)
