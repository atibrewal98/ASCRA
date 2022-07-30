package com.springboot.ascra.api.model;

import javax.persistence.*;
import java.util.Date;

@Entity
@Table(name = "country")
public class Country {
    @Column(name = "country_id")
    private @Id @GeneratedValue(strategy = GenerationType.IDENTITY) Long id;

    private String country_name;
    private String country_code;
    private Long region_id;

    public Long getId() {
        return id;
    }

    public Long getRegion_id() {
        return region_id;
    }

    public String getCountry_code() {
        return country_code;
    }

    public String getCountry_name() {
        return country_name;
    }

    public void setCountry_code(String country_code) {
        this.country_code = country_code;
    }

    public void setCountry_name(String country_name) {
        this.country_name = country_name;
    }

    public void setRegion_id(Long region_id) {
        this.region_id = region_id;
    }
}
