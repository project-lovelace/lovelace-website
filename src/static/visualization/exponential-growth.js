function exponentialGrowthAnalytic(x0, k, t) {
    return x0 * Math.exp(k * t)
}

function exponentialGrowthForwardEuler(x0, k, dt, N) {
    var x = new Array(N)

    x[0] = x0;
    for (n = 0; n < N; n++) {
        x[n+1] = x[n] + k * x[n] * dt
    }

    return x
}

function visualize_test_case(input, output, expected, nTestCase) {

    var x0 = input[0];
    var k = input[1];
    var dt = input[2];
    var N = input[3];

    var xOutput = output[0];
    var xExpected = expected[0];

    document.getElementById(`input${nTestCase}`).innerHTML =
        `<b>Input</b>: x0 = ${x0}, k = ${k}, dt = ${dt}, N = ${N} <br>`

    document.getElementById(`output${nTestCase}`).innerHTML =
        `<b>Output</b>: <br>` +
        `<div id="output-plot-${nTestCase}"></div>`

    var times = new Array(N)
    for (n = 0; n <= N; n++) {
        times[n] = n * dt
    }

    var traceAnalytic = {
        x: times,
        y: times.map(t => exponentialGrowthAnalytic(x0, k, t)),
        mode: 'lines',
        name: 'analytic'
    }

    var traceNumericalCorrect = {
        x: times,
        y: xExpected,
        mode: 'lines',
        name: `numerical (correct)`
    }

    var traceNumericalUser = {
        x: times,
        y: xOutput,
        mode: 'lines',
        name: `your output`
    }

    var layout = {
        xaxis: { title: 'Time t' },
        yaxis: { title: 'x(t)' },
        paper_bgcolor: 'rgba(0, 0, 0, 0)',
        plot_bgcolor: 'rgba(0, 0, 0, 0)'
    }

    Plotly.newPlot(`output-plot-${nTestCase}`, [traceAnalytic, traceNumericalCorrect, traceNumericalUser], layout)

    return
}

function plotExponentialGrowth(x0, k, dt, N) {
    var times = new Array(N)
    for (n = 0; n <= N; n++) {
        times[n] = n * dt
    }

    var traceAnalytic = {
        x: times,
        y: times.map(t => exponentialGrowthAnalytic(x0, k, t)),
        type: 'lines',
        name: 'analytic'
    }

    var traceNumerical = {
        x: times,
        y: exponentialGrowthForwardEuler(x0, k, dt, n),
        type: 'lines',
        name: 'numerical'
    }

    var layout = {
        title: 'Exponential growth',
        xaxis: { title: 'Time t' },
        yaxis: { title: 'x(t)' },
        paper_bgcolor: 'rgba(0, 0, 0, 0)',
        plot_bgcolor: 'rgba(0, 0, 0, 0)'
    }

    Plotly.newPlot("exponential-growth-app", [traceAnalytic, traceNumerical], layout)

    return
}

plotExponentialGrowth(1, 2.5, 0.1, 10)

var sliderInitialValue = document.getElementById("slider-initial-value");
var sliderGrowthRate = document.getElementById("slider-growth-rate");
var sliderTimeStep = document.getElementById("slider-time-step");
var sliderIterations = document.getElementById("slider-iterations");

noUiSlider.create(sliderInitialValue, {
    start: [1],
    range: {
        "min": [-10],
        "max": [10]
    },
    step: 0.01
});

noUiSlider.create(sliderGrowthRate, {
    start: [1],
    range: {
        "min": [-5],
        "max": [5]
    },
    step: 0.01
});

noUiSlider.create(sliderTimeStep, {
    start: [0.1],
    range: {
        "min": [0.01],
        "max": [1]
    },
    step: 0.01
});

noUiSlider.create(sliderIterations, {
    start: [10],
    range: {
        "min": [1],
        "max": [100]
    },
    step: 1
});

var labelInitialValue = document.getElementById("label-initial-value");
var labelGrowthRate = document.getElementById("label-growth-rate");
var labelTimeStep = document.getElementById("label-time-step");
var labelIterations = document.getElementById("label-iterations");

function replotExponentialGrowth() {
    var x0 = parseFloat(sliderInitialValue.noUiSlider.get());
    var k = parseFloat(sliderGrowthRate.noUiSlider.get());
    var dt = parseFloat(sliderTimeStep.noUiSlider.get());
    var N = parseFloat(sliderIterations.noUiSlider.get());

    labelInitialValue.innerHTML = x0;
    labelGrowthRate.innerHTML = k;
    labelTimeStep.innerHTML = dt;
    labelIterations.innerHTML = N;

    plotExponentialGrowth(x0, k, dt, N)

    return
}

sliderInitialValue.noUiSlider.on("update", replotExponentialGrowth);
sliderGrowthRate.noUiSlider.on("update", replotExponentialGrowth);
sliderTimeStep.noUiSlider.on("update", replotExponentialGrowth);
sliderIterations.noUiSlider.on("update", replotExponentialGrowth);
