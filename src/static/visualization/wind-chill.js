function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: T_a = ${input[0]} °C, v = ${input[1]} km/h <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: T_wc = ${output[0]} °C (expected ${expected[0]} °C) <br>`

    return
}

function make_wind_chill_figure() {
    var n = 200 // number of points
    var v = new Array(n)

    var v_min = 0
    var v_max = 100
    var dv = (v_max - v_min) / n
    for (let i = 0; i < n; i++) {
        v[i] = v_min + i * dv
    }

    // Air temperatures to plot
    var T_air = [10, 0, -10, -30, -50]

    var traces = []

    for (T_a of T_air) {
        var trace = {
            x: v,
            y: v.map(v => 13.12 + 0.6215 * T_a - 11.37 * v**0.16 + 0.3965*T_a * v**0.16),
            mode: 'lines',
            name: `T air = ${T_a} °C`
        }
        traces.push(trace)
    }

    var layout = {
        title: 'Wind chill at various air temperatures',
        xaxis: { title: 'Wind speed (km/h)' },
        yaxis: { title: 'Wind chill (°C)' },
        paper_bgcolor: 'rgba(0, 0, 0, 0)',
        plot_bgcolor: 'rgba(0, 0, 0, 0)'
    }

    Plotly.newPlot('wind-chill-plot', traces, layout)

    return
}

make_wind_chill_figure()
