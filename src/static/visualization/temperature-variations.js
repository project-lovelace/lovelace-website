function make_temperature_variations_figure() {
    var temperatures = {
        'Saskatoon, Canada': [-13.9, -11.4, -4.9, 5.2, 11.8, 16.1, 19.0, 18.2, 12.0, 4.4, -5.2, -12.4],
        'Baku, Azerbaijan': [4.4, 4.2, 7.0, 12.9, 18.5, 23.5, 26.4, 26.3, 22.5, 16.6, 11.2, 7.3],
        'Khartoum, Sudan': [23.2, 25.0, 28.7, 31.9, 34.5, 34.3, 32.1, 31.5, 32.5, 32.4, 28.1, 24.5],
        'Singapore': [26.5, 27.1, 27.5, 28.0, 28.3, 28.3, 27.9, 27.9, 27.6, 27.6, 27.0, 26.4],
        'San Juan, Argentina': [27.1, 25.5, 22.8, 17.2, 12.2, 8.3, 7.7, 10.6, 14.4, 19.8, 23.4, 26.3]
    }

    var traces = []
    for (const [location, T] of Object.entries(temperatures)) {
        var trace = {
            x: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            y: T,
            mode: 'lines+markers',
            name: location
        }
        traces.push(trace)
    }

    var layout = {
        title: 'Average monthly temperatures',
        xaxis: { title: 'Month' },
        yaxis: { title: 'Temperature (°C)' },
        paper_bgcolor: 'rgba(0, 0, 0, 0)',
        plot_bgcolor: 'rgba(0, 0, 0, 0)',
        modebar: { bgcolor: 'white' },
        width: '100%',
        height: '100%'
    }

    Plotly.newPlot('temperature-variations-plot', traces, layout)

    return
}

make_temperature_variations_figure()