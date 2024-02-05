import sys

import json_to_csv, message_counter


# python parser.py REMOVED
# python main.py REMOVED

# Read the json file and convert to csv
convo_name = sys.argv[1]
# RandysBackyard
json_to_csv.convert(convo_name)

# Total message count per sender
message_counter.msg_count(convo_name)

# Total word count per sender


# Top N most frequent words per sender


# Messages by time of day
# Messages by time of week

