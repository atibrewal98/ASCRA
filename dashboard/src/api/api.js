const API_URL = "https://api.asaibabas.com"

export async function getAllCountries (){
    let response = await fetch(`${API_URL}/country`)
    return await response.json()
}

export async function getCountryData (id){
    let response = await fetch(`${API_URL}/countryData/country=${id}`)
    return await response.json()
}