import pandas as pd
import matplotlib.pyplot as plt

from util import FIELD_NAMES, DEFAULT_PATH_TO_MESSAGE_FILE, DEFAULT_MESSAGE_FILE_NAME

import time

def msg_count(convo_name):
    print("Counting total messages per sender...")
    start_time = time.time()

    path_to_convo = DEFAULT_PATH_TO_MESSAGE_FILE + convo_name
    file_name = path_to_convo + "/" + DEFAULT_MESSAGE_FILE_NAME

    data = pd.read_csv(file_name + ".csv")

    msgs_by_sender = data.groupby(FIELD_NAMES[0])
    sender = [] # X-values
    count = [] # Y-values

    for s in msgs_by_sender.groups.keys():
        sender.append(s)
        count.append(len(msgs_by_sender.get_group(s)))
        # maybe we can get the k,v pair (groups,get_group)

    count_series = pd.Series(count)
    plt.figure()
    ax = count_series.plot(kind="bar")
    ax.set_title("Total Message Count By Sender")
    ax.set_xlabel("Full Name")
    ax.set_ylabel("Message Count")
    ax.set_xticklabels(sender)
    rects = ax.patches

    # make some labels
    # labels = ["label%d" % i for i in range(len(rects))]
    labels = ["%d" % c for c in count]

    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
                ha='center', va='bottom')

    file_name = path_to_convo + "/total_message_count_per_sender.png"
    plt.savefig(file_name, bbox_inches="tight")
    end_time = time.time()



    print("Counted total messages per sender and saved into:\n%s\nin %s seconds" % (file_name, str(end_time - start_time)))