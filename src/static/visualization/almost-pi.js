function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: ${input[0]} <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: ${output[0]} (expected ${expected[0]}) <br>`

    return
}

function make_almost_pi_figure() {
    var n = 100 // number of points
    var x = new Array(n)
    var pi = new Array(n)

    x[0] = 1
    pi[0] = 4
    for (let k = 1; k < n; k++) {
        x[k] = k+1
        pi[k] = pi[k-1] + 4 * (-1)**k / (2*k+1)
    }

    var trace = {
        x: x,
        y: pi,
        mode: 'lines'
    }

    var shapes = [
        {
            type: 'line',
            x0: 0,
            y0: Math.PI,
            x1: n,
            y1: Math.PI,
            line: { color: 'orange', dash: 'dash' }
        }
    ]

    var layout = {
        title: 'Approximating π',
        xaxis: { title: 'terms', range: [1, n] },
        yaxis: { title: 'π', range: [2.6, 4.0] },
        shapes: shapes,
        paper_bgcolor: 'rgba(0, 0, 0, 0)',
        plot_bgcolor: 'rgba(0, 0, 0, 0)',
        modebar: { bgcolor: 'white' },
        width: '100%',
        height: '100%'
    }

    Plotly.newPlot('almost-pi-plot', [trace], layout)

    return
}

make_almost_pi_figure()
