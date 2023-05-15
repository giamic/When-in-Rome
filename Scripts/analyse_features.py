"""
This script is a starting point to do any kinds of analysis one might want.
It stores the information on each piece inside a pandas dataframe.
Therefore, it requires the pandas package to be installed
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from Code import CORPUS_FOLDER
from Code.Pitch_profiles.get_distributions import DistributionsFromTabular
from Code.updates_and_checks import get_corpus_files


def plot_key_over_time(df, name):
    df.plot.scatter("offset", "key")
    plt.title(name)
    plt.show()
    return


if __name__ == "__main__":
    analysis_files = get_corpus_files(file_name="analysis.txt")
    slice_files = get_corpus_files(file_name="slices_with_analysis.tsv")
    names = [Path(f).parent.relative_to(CORPUS_FOLDER) for f in slice_files]
    print(
        f"We have a total of {len(analysis_files)} analyses,"
        f" of which {len(slice_files)} have the paired score"
    )

    distributions = {f: DistributionsFromTabular(path_to_tab=f) for f in slice_files}
    data = [pd.DataFrame(v.data, columns=v.headers) for k, v in distributions.items()]
    num_chords_per_file = [x["chord"].count() for x in data]
    print(f"They contain {np.sum(num_chords_per_file)} total RN annotations")
