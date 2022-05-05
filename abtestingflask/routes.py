import base64
from io import BytesIO

import numpy

from abtestingflask import app
from flask import render_template, redirect, url_for, flash, request
from scipy import stats
import matplotlib.pyplot as plt


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', show_result=0)


@app.route('/result', methods=['POST'])
def logout_page():
    if request.method == 'POST':
        result = {}
        samples = {}
        for k, v in request.form.items():
            samples[k] = numpy.fromiter(map(float, v.split(',')), float)

        s1 = samples["s1"]
        s2 = samples["s2"]

        s1mean = numpy.mean(s1)
        s2mean = numpy.mean(s2)
        result["mean"] = [round(s1mean, 6), round(s2mean, 6)]

        s1std = numpy.std(s1, ddof=1)
        s2std = numpy.std(s2, ddof=1)
        result["std"] = [round(s1std, 6), round(s2std, 6)]

        levene_stat, levene_p = stats.levene(s1, s2)
        result["levene"] = [round(levene_p, 6)]

        shapiro_stat1, shapiro_p1 = stats.shapiro(s1)
        shapiro_stat2, shapiro_p2 = stats.shapiro(s2)
        result["shapiro"] = [round(shapiro_p1, 6), round(shapiro_p2, 6)]

        ttest_ind_stat, ttest_ind_p = stats.ttest_ind(s1, s2)
        result["ttest_ind"] = [round(ttest_ind_p, 6)]

        fig = plt.figure()

        gs = fig.add_gridspec(2, 2)
        axs1 = fig.add_subplot(gs[0, 0])
        axs2 = fig.add_subplot(gs[0, 1])
        axs3 = fig.add_subplot(gs[1, :])

        n_bins1 = round(s1.size / 2)
        n_bins2 = round(s2.size / 2)
        axs1.hist(s1, bins=n_bins1)
        axs2.hist(s2, bins=n_bins2)

        labels = ['s1', 's2']
        axs3.boxplot([s1, s2], vert=True, patch_artist=True, labels=labels)
        axs3.set_title('Rectangular box plot')
        fig.tight_layout()

        img = BytesIO()

        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')

        return render_template("home.html", result=result, plot_url=plot_url, show_result=1)
