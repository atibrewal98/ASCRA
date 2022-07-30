package com.springboot.ascra.api.controller;

import com.springboot.ascra.api.model.Country;
import com.springboot.ascra.api.repository.CountryRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
public class ApiController {
    private final CountryRepository countryRepository;

    @Autowired
    public ApiController (CountryRepository countryRepository) {
        this.countryRepository = countryRepository;
    }

    @GetMapping("/country")
    public List<Country> getAllCountry() {

        List<Country> country = this.countryRepository.findAllCountry()
                .orElse(new ArrayList<>());

        return country;
    }
}
