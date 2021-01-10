function linear_range(min, max, length) {
    var delta = (max - min) / length
    var x = new Array(length)
    for (let i = 0; i < length; i++) {
        x[i] = min + i * delta
    }
    return x
}

// Data from Sand et al. (1995), Table 2.
var latitudes = [58.0, 57.7, 58.0, 57.9, 59.8, 61.6, 62.0, 62.7, 64.0, 63.0, 63.5, 65.5, 66.0, 66.0]
var masses = [180.9, 174.9, 184.9, 177.7, 164.8, 180.0, 196.3, 188.8, 204.8, 186.6, 188.2, 194.2, 198.1, 200.1]

// fit from Sand et al. (1995), figure 3.
function line_of_best_fit(latitude) {
    return 2.757*latitude + 16.793
}

function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: ${input[0]} <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: ${output[0]} (expected ${expected[0]}) <br>` +
        `<div id="output-plot-${n}"></div>`

    var trace_data = {
        x: latitudes,
        y: masses,
        mode: 'markers',
        type: 'scatter',
        name: 'data',
        marker: { size: 10 }
    }

    var x = linear_range(57, 67, 100)

    var trace_fit = {
        x: x,
        y: x.map(x => line_of_best_fit(x)),
        mode: 'lines',
        name: `linear fit`,
        line: { width: 3 }
    }

    var trace_expected = {
        x: [input[0]],
        y: [expected[0]],
        mode: 'markers',
        type: 'scatter',
        name: 'correct answer',
        marker: { size: 10 }
    }

    var trace_output = {
        x: [input[0]],
        y: [output[0]],
        mode: 'markers',
        type: 'scatter',
        name: 'your output',
        marker: { symbol: 'x', size: 10 }
    }

    var layout = {
        title: 'average body mass of female moose',
        xaxis: { title: 'Latitude (°N)' },
        yaxis: { title: 'body mass (kg)' },
        paper_bgcolor: 'rgba(0, 0, 0, 0)',
        plot_bgcolor: 'rgba(0, 0, 0, 0)'
    }

    Plotly.newPlot(`output-plot-${n}`, [trace_data, trace_fit, trace_expected, trace_output], layout)

    return
}

function make_moose_mass_figure() {
    var trace_data = {
        x: latitudes,
        y: masses,
        mode: 'markers',
        type: 'scatter',
        name: 'data',
        marker: { size: 10 }
    }

    var x = linear_range(57, 67, 100)

    var trace_fit = {
        x: x,
        y: x.map(x => line_of_best_fit(x)),
        mode: 'lines',
        name: `linear fit`,
        line: { width: 3 }
    }

    var layout = {
        title: 'average body mass of female moose',
        xaxis: { title: 'Latitude (°N)' },
        yaxis: { title: 'body mass (kg)' },
        paper_bgcolor: 'rgba(0, 0, 0, 0)',
        plot_bgcolor: 'rgba(0, 0, 0, 0)'
    }

    Plotly.newPlot('moose-mass-figure', [trace_data, trace_fit], layout)

    return
}

make_moose_mass_figure()
