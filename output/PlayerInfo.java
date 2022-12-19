package com.example.enkaapi.models;

import lombok.Data;

import java.util.List;

@Data
public class PlayerInfo {
    private String nickname;
    private Integer level;
    private String signature;
    private Integer worldLevel;
    private Integer nameCardId;
    private Integer finishAchievementNum;
    private Integer towerFloorIndex;
    private Integer towerLevelIndex;
    private List<ShowAvatarInfo> showAvatarInfoList;
    private List<Integer> showNameCardIdList;
    private ProfilePicture profilePicture;
}
