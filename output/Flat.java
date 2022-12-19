package com.example.enkaapi.models;

import lombok.Data;

import java.util.List;

@Data
public class Flat {
    private String nameTextMapHash;
    private Integer rankLevel;
    private List<WeaponStats> weaponStats;
    private String itemType;
    private String icon;
    private String setNameTextMapHash;
    private ReliquaryMainstat reliquaryMainstat;
    private List<ReliquarySubstats> reliquarySubstats;
    private String equipType;
}
