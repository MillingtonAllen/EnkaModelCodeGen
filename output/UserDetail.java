package com.example.enkaapi.models;

import lombok.Data;

import java.util.List;

@Data
public class UserDetail {
    private PlayerInfo playerInfo;
    private List<AvatarInfo> avatarInfoList;
    private Integer ttl;
    private String uid;
}
