import json


class JSONExporter:

    def save(self, data, filename):

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"Data saved to {filename}")