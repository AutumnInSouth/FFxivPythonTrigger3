import re

t = """
  struct FFXIVIpcNpcSpawn : FFXIVIpcBasePacket< NpcSpawn >
  {
    uint32_t gimmickId; // needs to be existing in the map, mob will snap to it
    uint8_t u2b;
    uint8_t u2ab;
    uint8_t gmRank;
    uint8_t u3b;

    uint8_t aggressionMode; // 1 passive, 2 aggressive
    uint8_t onlineStatus;
    uint8_t u3c;
    uint8_t pose;

    uint32_t u4;

    uint64_t targetId;
    uint32_t u6;
    uint32_t u7;
    uint64_t mainWeaponModel;
    uint64_t secWeaponModel;
    uint64_t craftToolModel;

    uint32_t u14;
    uint32_t u15;
    uint32_t bNPCBase;
    uint32_t bNPCName;
    uint32_t levelId;
    uint32_t u19;
    uint32_t directorId;
    uint32_t spawnerId;
    uint32_t parentActorId;
    uint32_t hPMax;
    uint32_t hPCurr;
    uint32_t displayFlags;
    uint16_t fateID;
    uint16_t mPCurr;
    uint16_t unknown1; // 0
    uint16_t unknown2; // 0 or pretty big numbers > 30000
    uint16_t modelChara;
    uint16_t rotation;
    uint16_t activeMinion;
    uint8_t spawnIndex;
    uint8_t state;
    uint8_t persistantEmote;
    uint8_t modelType;
    uint8_t subtype;
    uint8_t voice;
    uint16_t u25c;
    uint8_t enemyType;
    uint8_t level;
    uint8_t classJob;
    uint8_t u26d;
    uint16_t u27a;
    uint8_t currentMount;
    uint8_t mountHead;
    uint8_t mountBody;
    uint8_t mountFeet;
    uint8_t mountColor;
    uint8_t scale;
    uint16_t elementalLevel; // Eureka
    uint16_t element; // Eureka
    Common::StatusEffect effect[30];
    Common::FFXIVARR_POSITION3 pos;
    uint32_t models[10];
    char name[32];
    uint8_t look[26];
    char fcTag[6];
    uint32_t unk30;
    uint32_t unk31;
    uint8_t bNPCPartSlot;
    uint8_t unk32;
    uint16_t unk33;
    uint32_t unk34;
  };
"""
for match in re.findall(r'(\w+) (\w+)(\[\d+])?;', t):
    arg_type, arg_name, arg_array = match
    arg_name = re.sub(r'[A-Z]', '_\g<0>', arg_name).lower()
    match arg_type:
        case 'uint8_t':
            arg_type = 'c_ubyte'
        case 'uint16_t':
            arg_type = 'c_ushort'
        case 'uint32_t':
            arg_type = 'c_uint'
        case 'uint64_t':
            arg_type = 'c_ulonglong'
        case 'char':
            arg_type = 'c_char'
    if arg_array:
        arg_type = f'{arg_type} * {arg_array[1:-1]}'
    print(f"'{arg_name}' : {arg_type} ,")
