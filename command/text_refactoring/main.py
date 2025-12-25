from commands import AppendText, Batch, ChangeTitle, Clear
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

    # create command objects and execute with the controller
    controller.execute(AppendText(doc1, "Hello World!"))
    controller.execute(AppendText(doc2, "The meeting started at 9:00."))
    controller.undo()

    # update the title of the first document
    controller.execute(ChangeTitle(doc1, "Important Meeting"))

    controller.execute(
        Batch(
            commands=[
                AppendText(doc1, "Hi there!"),
                ChangeTitle(doc2, "Useless Meeting."),
                Clear(doc2),
            ]
        )
    )
    controller.undo()

    print(processor)


if __name__ == "__main__":
    main()
