function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: (number of iterations = ${input[1]}) <br>` +
        `<div id="input-board-${n}"></div> <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: <br>` +
        `<div id="output-board-${n}"></div> <br>` +
        `<b>Expected</b>: <br>` +
        `<div id="expected-board-${n}"></div> <br>`


    var bw = [
        ['0.0', 'white'],
        ['1.0', 'black']
    ]

    var trace_input = {
        z: input[0],
        type: 'heatmap',
        colorscale: bw,
        showscale: false
    }

    var trace_output = {
        z: output[0],
        type: 'heatmap',
        colorscale: bw,
        showscale: false
    }

    var trace_expected = {
        z: expected[0],
        type: 'heatmap',
        colorscale: bw,
        showscale: false
    }

    Plotly.newPlot(`input-board-${n}`, [trace_input])
    Plotly.newPlot(`output-board-${n}`, [trace_output])
    Plotly.newPlot(`expected-board-${n}`, [trace_expected])

    return
}
