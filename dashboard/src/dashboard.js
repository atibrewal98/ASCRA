import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import SearchIcon from "@mui/icons-material/Search";
import {countrySummary, defaultSummary } from "./constants"
import { SearchBox } from './components/search';
import { DataTable } from "./components/table"
import { getAllCountries, getCountryData } from './api/api';
import { LineGraph } from './components/lineGraph';
import { BarGraph } from './components/barChart';
import CircularProgress from '@mui/material/CircularProgress';
import { BarLineGraph } from './components/barLineChart';

const darkTheme = createTheme({
    palette: {
        mode: 'dark',
    },
});

export const Dashboard = () => {
    const [countryDetails, setCountryDetails] = React.useState(null)
    const [open, setOpen] = React.useState(true)
    const [selectedCountry, setSelectedCountry] = React.useState("")
    const [countryList, setCountryList] = React.useState([])
    const [specificCountryData, setSpecificCountryData] = React.useState([])
    const [isLoading, setIsLoading] = React.useState(false)

    React.useEffect(()=> {
        getAllCountries().then(response => {
            setCountryList(response)
        })
    }, [])

    React.useEffect(() => {
        if (selectedCountry !== "" && countryList !== []){
            setIsLoading(true)
            const countryId = countryList.find(x => x.country_name === selectedCountry)["id"]
            getCountryData(countryId).then(response=> {
                setSpecificCountryData(response)
                setCountryDetails(getCountryDetails(selectedCountry))
                setIsLoading(false)
            })
        }
    }, [selectedCountry])


    function getCountryDetails (country){
        let details = {}
        countrySummary.forEach(summary => {
            if(summary.Name === country){
                details = summary
            }
        })
        if (!isEmpty(details)){
            return details
        }
        else{
            return defaultSummary
        }
    }

    function isEmpty(obj) {
        return Object.keys(obj).length === 0;
    }

    return (
        <ThemeProvider theme={darkTheme}>
            <CssBaseline />
            <Box sx={{ flexGrow: 1 }}>
                <AppBar position="static">
                    <Toolbar>
                        <Typography
                            variant="h6"
                            noWrap
                            component="div"
                            sx={{ flexGrow: 1, display: { xs: "none", sm: "block" } }}
                        >
                            ASCRA
                        </Typography>
                        <IconButton size="large" aria-label="search" color="inherit" onClick={()=> setOpen(true)}>
                            <SearchIcon />
                        </IconButton>
                    </Toolbar>
                </AppBar>
            </Box>
            <div className={"mainContainer"} style={{padding: "1rem"}}>
                <h1 style={{textAlign: "center", textDecoration: "underline"}}>Welcome to Automated Sovereign Credit Rating Analysis</h1>
                <br className={"padding"} />
                {selectedCountry === "" ? 
                (
                    <h3>Please search for a country to get analysis</h3>
                ) : (
                    <div>
                        {isLoading ? 
                        (
                            <div style={{textAlign: "center"}}>
                                <CircularProgress />
                            </div>
                        ):
                        (  
                            <div>  
                                <h2 style={{textAlign: "center"}}>Name : {selectedCountry}</h2>
                                {
                                    countryDetails && Object.keys(countryDetails).map((prop, i) => {
                                        if(prop !== "Name"){
                                            return (
                                                <h2 key={i} style={{textAlign: "center"}}>{prop} : {countryDetails[prop]}</h2>
                                            )
                                        }
                                    })
                                } 
                                <br className={"padding"} />
                                <DataTable rowData={specificCountryData}/> 
                                <br />
                                <div style={{display: "flex", justifyContent: "center", flexDirection: "column"}}>
                                    <div style={{display: "flex", justifyContent: "center", flexDirection: "row"}}>
                                        <LineGraph data = {specificCountryData} xAxisKey={"year"} item1={"gov_spend"} item2={"gov_debt"} item1Name={"Govt. Spend"} item2Name={"Govt. Debt"}/> 
                                        <BarLineGraph data = {specificCountryData} xAxisKey={"year"} item1={"inflation"} item2={"gdp_growth_rate"} item1Name={"Inflation"} item2Name={"GDP Growth Rate"} />
                                        <LineGraph data = {specificCountryData} xAxisKey={"year"} item1={"imports"} item2={"exports"} item1Name={"Imports"} item2Name={"Exports"}/> 
                                    </div>
                                    <br />
                                    <div style={{display: "flex", justifyContent: "center", flexDirection: "row"}}>
                                        <BarGraph data={specificCountryData} xAxisKey={"year"} item1={"renewable_pg"} item2={"fossil_pg"} item1Name={"Renewable Power Generaton"} item2Name={"Fossil Power Generation"}/>
                                        <BarGraph data={specificCountryData} xAxisKey={"year"} item1={"economic_gi"} item2={"political_gi"} item1Name={"Economic Global Index"} item2Name={"Political Global Index"}/>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>
                    )
                }
                <SearchBox open={open} onClose={()=> setOpen(false)} setSelectedCountry={setSelectedCountry} countryList={countryList.map(value => value.country_name)}/>
            </div>
        </ThemeProvider>
    );
}

