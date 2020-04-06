
url_to_pop = "https://restcountries.eu/rest/v2/name/sweden"
url_to_data = "https://pomber.github.io/covid19/timeseries.json"
data_set = null;
population = -1;

async function url_to_json(url) {
    const response = await fetch(url);
    const data = await response.json();
    return data;
}

(async function(){
    population = (await url_to_json(url_to_pop))[0].population;
    data_set = (await url_to_json(url_to_data)).Sweden;
    console.log(data_set);

    let sir = get_sir_from_date("2020-4-5");
    console.log(sir);
})()

function get_sir_from_date(date) {
    for (var i = 0; i < data_set.length; i++) {
        let day_data = data_set[i];
        if (day_data.date == date) {
            let sir = [];
            // susceptible
            sir[0] = population - day_data.confirmed - day_data.recovered;
            // infectious
            sir[1] = day_data.confirmed;
            // removed
            sir[2] = day_data.recovered;
            return sir;
        }
    }
    return null;
}
