from dataclasses import dataclass, field
from document import Document

@dataclass
class Processor:
    docs: list[Document] = field(default_factory=list)

    def create_document(self, title: str) -> Document:
        doc = Document(title)
        self.docs.append(doc)
        return doc

    def get_document(self, title: str) -> Document:
        return next(doc for doc in self.docs if doc.title == title)