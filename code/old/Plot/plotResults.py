import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

class Plot:
  def plot(yes_answers, no_answers, groups):
    n_groups = len(yes_answers)

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    rects1 = ax.bar(index, yes_answers, bar_width,
                    alpha=opacity, color='#22A7FF',
                    label='Yes')

    rects2 = ax.bar(index + bar_width, no_answers, bar_width,
                    alpha=opacity, color='#FFA21C',
                    label='No')

    ax.set_xlabel('Answer')
    ax.set_ylabel('Total count')
    ax.set_title('Answers to the question: "Do you like chocolate?"')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(groups)
    ax.legend()

    fig.tight_layout()
    plt.show()