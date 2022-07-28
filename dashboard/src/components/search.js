import { Dialog, DialogContent, DialogTitle, Input, Backdrop } from "@mui/material";
import React from "react";
import IconButton from "@mui/material/IconButton";
import SearchIcon from "@mui/icons-material/Search";
import { countryList } from "../constants"

export const SearchBox = (props) => {
    const [searchTerm, setSearchTerm] = React.useState("");

    function dynamicSearch() {
        return props.countryList
            .filter(market => market.toLowerCase().includes(searchTerm.toLowerCase()))
            .slice(0, 3)
            .sort()
    }

    React.useEffect(() => {
        if (props.open) {
            setSearchTerm("")
        }
    }, [props.open])

    function handleClick(country) {
        props.setSelectedCountry(country)
        props.onClose()
    }

    return (
        <Backdrop
            sx={{ backdropFilter: "blur(1px)" }}
            open={props.open}
        >
            <Dialog
                PaperProps={{
                    style: {
                        background: "transparent",
                        minWidth: "90rem",
                        outline: "none",
                        height: "20rem",
                        boxShadow: "0 0 0 0"
                    }
                }}
                style={{
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    background: "transparent",
                    border: "none"
                }}
                onClose={props.onClose}
                open={props.open}
            >
                <React.Fragment>
                    <DialogTitle  />
                    <DialogContent>
                        <Input
                            style={{
                                width: "85rem",
                                fontSize: "18px",
                                height: "4rem",
                                borderBottom: "2px solid white"
                            }}
                            startAdornment={
                                <IconButton size="large" aria-label="search" color="inherit">
                                    <SearchIcon />
                                </IconButton>
                            }
                            onChange={e => setSearchTerm(e.target.value)}
                            inputProps={{
                                id: "customSearchInput",
                                type: "text",
                                placeholder: "Search for Country",
                                style: {
                                    fontSize: "36px",
                                    outline: "none",
                                    border: "none",
                                    width: "85rem",
                                    background: "none",
                                    color: "white"
                                }
                            }}
                        />
                        {searchTerm !== "" &&
                            dynamicSearch().map((country, key) => {
                                return (
                                    <div style={{display: "flex", flexDirection: "column", marginTop: "10px"}}>
                                        <span onClick={()=>handleClick(country)} style={{fontSize: "28px", color: "white", marginTop: "5px", textDecoration: "none", cursor: "pointer"}}>{country}</span>
                                    </div>

                                )
                            })
                        }
                    </DialogContent>
                </React.Fragment>
            </Dialog>
        </Backdrop>
    )
}