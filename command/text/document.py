from dataclasses import dataclass

@dataclass
class Document:
    title: str
    text: str = ""

    def clear(self) -> None:
        self.text = ""
    
    def append(self, text: str) -> None:
        self.text += text
    
    def set_title(self, title: str) -> None:
        self.title = title