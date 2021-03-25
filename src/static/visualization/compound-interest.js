function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: m = ${input[0]}, r = ${input[1]}, n = ${input[2]} <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: ${output[0]} (expected ${expected[0]}) <br>`

    return
}

function compound_interest(amount, rate, years) {
    return amount * (1 + rate) ** years
}

function make_compound_interest_figure() {
    var amount = 1000
    var rate = 0.10
    var years = 25

    var year = new Array(years)
    for (n = 0; n <= years; n++) {
        year[n] = n
    }

    var trace = {
        x: year,
        y: year.map(n => compound_interest(amount, rate, n)),
        type: 'bar'
    }

    var layout = {
        title: 'Compount interest',
        xaxis: { title: 'years' },
        yaxis: { title: 'amount' },
        paper_bgcolor: 'rgba(0, 0, 0, 0)',
        plot_bgcolor: 'rgba(0, 0, 0, 0)'
    }

    Plotly.newPlot('compound-interest-figure', [trace], layout)

    return
}

make_compound_interest_figure()
