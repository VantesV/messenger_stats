import sys
import json
import csv
import time

FIELD_NAMES = ["sender_name", # string
               "timestamp_ms", # number
               "content", # string
               "type", # ["Share", "Generic"]
               "reactions" # list of object -> {"reaction": string, "actor": string}
               ]

def convert(name):
    print("Loading JSON file into CSV file...")
    start_time = time.time()

    # name = sys.argv[1]
    path_to_conversation = "messages/inbox/" + name
    file_name = path_to_conversation + "/message_1"


    # Read JSON file
    with open(file_name + ".json", "r") as json_file:
        data = json.load(json_file)


    # Write as CSV file
    with open(file_name + ".csv", mode="w", encoding="utf-8") as csv_file:
        msg_writer = csv.DictWriter(csv_file, FIELD_NAMES)
        msg_writer.writeheader()

        for msg in data["messages"]:
            msg_writer.writerow({
                "sender_name": msg[FIELD_NAMES[0]],
                "timestamp_ms": msg[FIELD_NAMES[1]],
                "content": msg[FIELD_NAMES[2]] if "content" in msg.keys() else "NULL", # is content empty for gifs?
                "type": msg[FIELD_NAMES[3]],
                "reactions": len(msg[FIELD_NAMES[4]]) if "reactions" in msg.keys() else 0 # maybe make a separate reactions analyzer
            })


    end_time = time.time()
    print("Wrote %d messages into csv file:\n%s\nin %s seconds" % (len(data["messages"]), file_name + ".csv", str(end_time - start_time)))
