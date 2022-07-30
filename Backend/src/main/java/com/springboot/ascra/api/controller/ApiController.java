package com.springboot.ascra.api.controller;

import com.springboot.ascra.api.model.Country;
import com.springboot.ascra.api.repository.CountryRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import javax.sql.DataSource;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

@RestController
public class ApiController {
    private final CountryRepository countryRepository;
    private final JdbcTemplate jdbcTemplate;

    @Autowired
    public ApiController (CountryRepository countryRepository, DataSource dataSource) {
        this.countryRepository = countryRepository;
        this.jdbcTemplate = new JdbcTemplate(dataSource);
    }

    @GetMapping("/")
    public String index() {
        return "Greetings from Spring Boot!";
    }

    @GetMapping("/country")
    public List<Country> getAllCountry() {

        List<Country> country = this.countryRepository.findAllCountry()
                .orElse(new ArrayList<>());

        return country;
    }

    @GetMapping("/countryData/country={id}")
    public List<Map<String, Object>> getAllCountry(@PathVariable long id) {
        String SQL = "Select * From vw_credit_esg_data Where country_id = " + String.valueOf(id) + " Order By [year]";

        return this.jdbcTemplate.queryForList(SQL);
    }
}
