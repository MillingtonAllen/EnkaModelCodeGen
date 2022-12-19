package com.example.enkaapi.models;

import lombok.Data;

import java.util.List;
import java.util.Map;

@Data
public class AvatarInfo {
    private Integer avatarId;
    private Map<String, Prop> propMap;
    private Map<String, Double> fightPropMap;
    private Integer skillDepotId;
    private List<Integer> inherentProudSkillList;
    private Map<String, Integer> skillLevelMap;
    private List<Equip> equipList;
    private FetterInfo fetterInfo;
    private List<Integer> talentIdList;
    private Integer costumeId;
    private Map<String, Integer> proudSkillExtraLevelMap;
}
