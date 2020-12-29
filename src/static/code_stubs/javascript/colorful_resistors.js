digits = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

multiplier = {
    "pink": 0.001,
    "silver": 0.01,
    "gold": 0.1,
    "black": 1,
    "brown": 10,
    "red": 100,
    "orange": 10 ** 3,
    "yellow": 10 ** 4,
    "green": 10 ** 5,
    "blue": 10 ** 6,
    "violet": 10 ** 7,
    "grey": 10 ** 8,
    "white": 10 ** 9
}

tolerance = {
    "none": 0.2,
    "silver": 0.1,
    "gold": 0.05,
    "brown": 0.01,
    "red": 0.02,
    "green": 0.005,
    "blue": 0.0025,
    "violet": 0.001,
    "grey": 0.0005
}

function resistance(band_colors) {
    let n_bands = band_colors.length;

    let nominal_R = 0;
    let minimum_R = 0;
    let maximum_R = 0;

    // Your code goes here!

    solution = [nominal_R, minimum_R, maximum_R];
    return solution;
}
