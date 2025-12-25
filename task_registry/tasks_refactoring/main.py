import json
from registry import register, run
from tasks import (
    recalibrate,
    reinforce,
    send_pulse
)


def main() -> None:

    # register functions
    register("pulse", send_pulse)
    register("recalibrate", recalibrate)
    register("reinforce", reinforce)

    with open("./tasks.json", encoding="utf-8") as file:
        data = json.load(file)

        for task in data["tasks"]:
            run(task)


if __name__ == "__main__":
    main()
