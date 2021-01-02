function visualize_test_case(input, output, expected, n) {
    document.getElementById(`input${n}`).innerHTML =
        `<b>Input</b>: (lat1, lon1) = (${input[0]}°, ${input[1]}°), (lat2, lon2) = (${input[2]}°, ${input[3]}°) <br>`

    document.getElementById(`output${n}`).innerHTML =
        `<b>Output</b>: ${output[0]} km (expected ${expected[0]} km) <br>`

    return
}
