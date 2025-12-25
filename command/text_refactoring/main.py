from functools import partial
from commands import append_text, batch, change_title, clear_text
from controller import TextController
from processor import Processor


def main() -> None:

    # create a text processor
    processor = Processor()

    # create a text controller
    controller = TextController()

    # create some documents
    doc1 = processor.create_document("ArjanCodes")
    doc2 = processor.create_document("Meeting Notes")

    undo_append = append_text(doc1, "Hello World!")
    undo_append2 = append_text(doc2, "The meeting started at 9:00.")
    controller.undo()

    # update the title of the first document
    undo_change_title = change_title(doc1, "Important Meeting")

    undo_change_title()

    # execute a batch of commands
    undo_batch = batch([
        partial(append_text, doc=doc1, text="Hi there!"),
        partial(clear_text, doc=doc2)
    ])
    undo_batch()
    
    print(processor)


if __name__ == "__main__":
    main()
