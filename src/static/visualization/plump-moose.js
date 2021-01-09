function make_moose_mass_figure() {
    // Data from Sand et al. (1995), Table 2.
    var latitudes = [58.0, 57.7, 58.0, 57.9, 59.8, 61.6, 62.0, 62.7, 64.0, 63.0, 63.5, 65.5, 66.0, 66.0]
    var masses = [180.9, 174.9, 184.9, 177.7, 164.8, 180.0, 196.3, 188.8, 204.8, 186.6, 188.2, 194.2, 198.1, 200.1]

    var trace_data = {
        x: latitudes,
        y: masses,
        mode: 'markers',
        type: 'scatter',
        name: 'data',
        marker: { size: 10 }
    }

    var n = 100
    var x_min = 57
    var x_max = 67
    var dx = (x_max - x_min) / n
    var x = new Array(n)
    for (let i = 0; i < n; i++) {
        x[i] = x_min + i * dx
    }

    // fit from Sand et al. (1995), figure 3.
    var trace_fit = {
        x: x,
        y: x.map(x => 2.757*x + 16.793),
        mode: 'lines',
        name: `linear fit`,
        line: { width: 3 }
    }

    var layout = {
        // title: 'Wind chill at various air temperatures',
        xaxis: { title: 'Latitude (°N)' },
        yaxis: { title: 'average body mass of female moose (kg)' },
        paper_bgcolor: 'rgba(0, 0, 0, 0)',
        plot_bgcolor: 'rgba(0, 0, 0, 0)'
    }

    Plotly.newPlot('moose-mass-figure', [trace_data, trace_fit], layout)

    return
}

make_moose_mass_figure()
