from processor import Processor


def main() -> None:

    # create a text processor
    processor = Processor()

    # create some documents
    doc1 = processor.create_document("ArjanCodes")
    doc2 = processor.create_document("Meeting Notes")

    # append some text to the documents
    doc1.append("Hello World!")
    doc2.append("The meeting started at 9:00.")

    # update the title of the first document
    doc1.set_title("Important Meeting")

    print(processor)


if __name__ == "__main__":
    main()
