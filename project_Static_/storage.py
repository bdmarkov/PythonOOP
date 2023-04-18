from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []


    def add_category(self, category:Category):
        for c in self.categories:
            if c.id == category.id:
                return
        self.categories.append(category)


    def add_topic(self,topic:Topic):
        for t in self.topics:
            if t.id == topic.id:
                return
        self.topics.append(topic)

    def add_document(self, document:Document):
        for d in self.documents:
            if d.id == document.id:
                return
        self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str):
        for category in self.categories:
            if category.id == category_id:
                category.edit(new_name)
                return

    def edit_topic(self, topic_id: int, new_topic:str, new_storage_folder: str):
        for topic in self.topics:
            if topic.id == topic_id:
                topic.edit(new_topic, new_storage_folder)
                return

    def edit_document(self, document_id: int, new_document: str):
        for document in self.documents:
            if document.id == document_id:
                document.edit(new_document)
                return

    def delete_category(self, category_id: int):
        for category in self.categories:
            if category.id == category_id:
                self.categories.remove((category))
                return

    def delete_topic(self, topic_id: int):
        for topic in self.topics:
            if topic.id == topic_id:
                self.topics.remove(topic)
                return

    def delete_document(self, document_id: int):
        for document in self.documents:
            if document.id == document_id:
                self.documents.remove(document)
                return

    def get_document(self, document_id):
        return self.__get_obj_by_id(self.documents, document_id)

    def __repr__(self):
        return '\n'.join([str(el) for el in self.documents])

    def __get_obj_by_id(self, objects, id):
        for obj in objects:
            if obj.id == id:
                return obj