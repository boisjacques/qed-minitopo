import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def getBandwidth(_data, _bandwidth):
    return _data.loc[_data["bandwidth"] == _bandwidth]


def getLoss(_data, _filesize, _loss):
    filesize = _data.loc[_data['filesize'] == _filesize]
    return getDelay(filesize, _loss)


def getDelay(_data, _loss):
    source = _data.loc[_data["loss"] == _loss]
    nd = source.loc[source["delay"] == "5ms"]
    md = source.loc[source["delay"] == "10ms"]
    hd = source.loc[source["delay"] == "15ms"]
    nd = nd.reset_index(drop=True)
    md = md.reset_index(drop=True)
    hd = hd.reset_index(drop=True)
    return nd, md, hd


def plotBandwidth(_data, _bandwidth):
    bandwidth = getBandwidth(_data, _bandwidth)
    plotFileSize(bandwidth, _bandwidth)


def plotFileSize(bandwidth, _bandwidth):
    file_sizes = ["5MB", "20MB", "50MB"]
    for size in file_sizes:
        f0, f1, f2 = getLoss(bandwidth, size, "no-loss")
        f3, f4, f5 = getLoss(bandwidth, size, "min-loss")
        f6, f7, f8 = getLoss(bandwidth, size, "hi-loss")
        concatFrames(f0, f1, f2, f3, f4, f5, f6, f7, f8, _bandwidth, size)


def concatFrames(f0, f1, f2, f3, f4, f5, f6, f7, f8, _bandwidth, _filesize):
    titles = ["nlnd", "nlmd", "nlhd", "mlnd", "mlmd", "mlhd", "hlnd", "hlmd", "hlhd"]
    plotData = pd.DataFrame(columns=titles)
    plotData[titles[0]] = f0["time"].astype(float)
    plotData[titles[1]] = f1["time"].astype(float)
    plotData[titles[2]] = f2["time"].astype(float)
    plotData[titles[3]] = f3["time"].astype(float)
    plotData[titles[4]] = f4["time"].astype(float)
    plotData[titles[5]] = f5["time"].astype(float)
    plotData[titles[6]] = f6["time"].astype(float)
    plotData[titles[7]] = f7["time"].astype(float)
    plotData[titles[8]] = f8["time"].astype(float)
    stat = plotData.describe()
    _failureRates = []
    for title in titles:
        count = stat.loc["count"][title]
        failureRate = 1 - count / 25
        failureRate *= 100
        _failureRates.append(failureRate)
    failureRates = pd.DataFrame(_failureRates, index=titles, columns=["failure rate"])
    plotData = plotData.fillna(plotData.quantile())
    color = {'boxes': 'DarkGreen', 'whiskers': 'DarkOrange', 'medians': 'DarkBlue', 'caps': 'Gray'}

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    plotData.plot.box(ax=ax1, color=color, sym='+', positions=range(9), title=_bandwidth + " " + _filesize)
    failureRates.plot.bar(ax=ax2, color='r', alpha=0.3)
    ax1.set_ylabel('Seconds')
    ax2.set_ylabel('Failure Rate in %')
    plt.xlim(-0.7, 8.7)
    ax1.set_xticks(range(len(titles)))
    ax1.set_xticklabels(titles)
    fig.tight_layout()
    filename = _bandwidth + "_" + _filesize + ".pdf"
    fig.show()
    fig.savefig(filename, dpi=300)


def interpolate_gaps(values, limit=None):
    values = np.asarray(values)
    i = np.arange(values.size)
    valid = np.isfinite(values)
    filled = np.interp(i, i[valid], values[valid])

    if limit is not None:
        invalid = ~valid
        for n in range(1, limit + 1):
            invalid[:-n] &= invalid[n:]
        filled[invalid] = np.nan

    return filled


features = ["filesize", "success", "time", "bandwidth", "delay", "loss"]
data = pd.read_csv("results.csv", names=features)

success = data.loc[data["success"] == 0]

plotBandwidth(success, "low-bw")
plotBandwidth(success, "mid-bw")
plotBandwidth(success, "hi-bw")

desc = data.describe()
percent_failed = data["success"]
