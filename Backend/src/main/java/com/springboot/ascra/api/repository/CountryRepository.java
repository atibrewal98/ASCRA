package com.springboot.ascra.api.repository;

import com.springboot.ascra.api.model.Country;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface CountryRepository extends JpaRepository<Country, Long> {

    @Query(value = "Select * From [country] Where [region_id] is not NULL", nativeQuery = true)
    Optional<List<Country>> findAllCountry();
}
