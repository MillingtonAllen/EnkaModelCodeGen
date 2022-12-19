package com.example.enkaapi.models;

import lombok.Data;

@Data
public class Equip {
    private Integer itemId;
    private Reliquary reliquary;
    private Flat flat;
    private Weapon weapon;
}
