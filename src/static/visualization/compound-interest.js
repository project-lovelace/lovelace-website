function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: m = ${input[0]}, r = ${input[1]}, n = ${input[2]} <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: ${output[0]} (expected ${expected[0]}) <br>`

    return
}

function compoundInterest(amount, rate, years) {
    return amount * (1 + rate) ** years
}

function makeCompoundInterestFigure(amount, rate, years) {

    var year = new Array(years)
    for (n = 0; n <= years; n++) {
        year[n] = n
    }

    var trace = {
        x: year,
        y: year.map(n => compoundInterest(amount, rate, n)),
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

makeCompoundInterestFigure(1000, 0.10, 25)

var sliderAmount = document.getElementById("slider-amount");
var sliderRate = document.getElementById("slider-rate");
var sliderYears = document.getElementById("slider-years");

noUiSlider.create(sliderAmount, {
    start: [1000],
    range: {
        "min": [100],
        "max": [10000]
    }
});

noUiSlider.create(sliderRate, {
    start: [0.10],
    range: {
        "min": [-0.1],
        "max": [0.5]
    },
    step: 0.01
});

noUiSlider.create(sliderYears, {
    start: [25],
    range: {
        "min": [1],
        "max": [100]
    },
    step: 1
    // tooltips: [wNumb({decimals: 0})]
});

var labelAmount = document.getElementById("label-amount");
var labelRate = document.getElementById("label-rate");
var labelYears = document.getElementById("label-years");

function remakeCompoundInterestFigure() {
    var amount = parseFloat(sliderAmount.noUiSlider.get());
    var rate = parseFloat(sliderRate.noUiSlider.get());
    var years = parseFloat(sliderYears.noUiSlider.get());

    labelAmount.innerHTML = `Amount: ${amount}`;
    labelRate.innerHTML = `Rate: ${rate}`;
    labelYears.innerHTML = `Years: ${years}`;

    makeCompoundInterestFigure(amount, rate, years)

    return
}

sliderAmount.noUiSlider.on("update", remakeCompoundInterestFigure);
sliderRate.noUiSlider.on("update", remakeCompoundInterestFigure);
sliderYears.noUiSlider.on("update", remakeCompoundInterestFigure);
