function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML = `<b>Input</b>: r = ${input[0]} <br>`

    var r = input[0]
    var x_expected = expected[0]
    var x_output = output[0]

    var iters_expected = [...x_expected.keys()]
    var iters_output = [...x_output.keys()]

    var trace_expected = {
      x: iters_expected,
      y: x_expected,
      mode: 'lines+markers',
      name: 'expected'
    }

    var trace_output = {
      x: iters_output,
      y: x_output,
      mode: 'lines+markers',
      name: 'your output'
    }

    var layout = {
        title:`Logistic map with r=${r}`,
        xaxis: { title: 'iterations' },
        yaxis: { title: 'x' },
        paper_bgcolor: 'rgba(0, 0, 0, 0)',
        plot_bgcolor: 'rgba(0, 0, 0, 0)',
        modebar: { bgcolor: 'white' },
    }

    document.getElementById(`output${n}`).innerHTML = `<b>Output</b>: <br> <div id="output${n}plot"></div>`
    Plotly.newPlot(`output${n}plot`, [trace_expected, trace_output], layout)

    return
}
