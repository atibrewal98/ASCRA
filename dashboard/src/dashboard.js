import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import SearchIcon from "@mui/icons-material/Search";
import {countrySummary } from "./constants"
import { SearchBox } from './components/search';
import { DataTable } from "./components/table"
import { getAllCountries, getCountryData } from './api/api';

const darkTheme = createTheme({
    palette: {
        mode: 'dark',
    },
});

export const Dashboard = () => {
    const [countryDetails, setCountryDetails] = React.useState(countrySummary)
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
                setIsLoading(false)
            })
        }
    }, [selectedCountry])

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
                        {
                        Object.keys(countryDetails).map((prop, i) => {
                            return (
                                <h2 key={i} style={{textAlign: "center"}}>{prop} : {countrySummary[prop]}</h2>
                            )
                        })
                    } 
                        <br className={"padding"} />
                        <DataTable rowData={specificCountryData} isLoading = {isLoading}/> 
                    </div>
                )}
                <SearchBox open={open} onClose={()=> setOpen(false)} setSelectedCountry={setSelectedCountry} countryList={countryList.map(value => value.country_name)}/>
            </div>
        </ThemeProvider>
    );
}

