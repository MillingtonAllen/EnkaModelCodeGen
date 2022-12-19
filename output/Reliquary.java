package com.example.enkaapi.models;

import lombok.Data;

import java.util.List;

@Data
public class Reliquary {
    private Integer level;
    private Integer mainPropId;
    private List<Integer> appendPropIdList;
}
