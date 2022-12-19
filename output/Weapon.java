package com.example.enkaapi.models;

import lombok.Data;

import java.util.Map;

@Data
public class Weapon {
    private Integer level;
    private Integer promoteLevel;
    private Map<String, Integer> affixMap;
}
