from ctypes import *
from typing import Dict, Set, Iterator, Tuple, Optional, TYPE_CHECKING, List

from FFxivPythonTrigger.memory.struct_factory import OffsetStruct

"""
from: https://github.com/aers/FFXIVClientStructs/blob/main/FFXIVClientStructs/FFXIV/Client/Game/UI/Buddy.cs
"""

"""
[StructLayout(LayoutKind.Explicit, Size = 0x198)]
public unsafe struct BuddyMember
{
    [FieldOffset(0x0)] public uint ObjectID;
    [FieldOffset(0x4)] public uint CurrentHealth;
    [FieldOffset(0x8)] public uint MaxHealth;
    // Chocobo: Mount
    // Pet: Pet (summons)
    // Squadron: Unused
    // Trust: DawnGrowMember
    [FieldOffset(0xC)] public byte DataID;
    [FieldOffset(0xD)] public byte Synced;
    [FieldOffset(0x10)] public StatusManager StatusManager;
}
"""


class BuddyMember(OffsetStruct({
    "object_id": (c_uint, 0x0),
    "current_health": (c_uint, 0x4),
    "max_health": (c_uint, 0x8),
    "data_id": (c_byte, 0xC),
    "synced": (c_byte, 0xD),
    # "status_manager": (StatusManager,0x10),
}, 0x198)):
    object_id: int
    current_health: int
    max_health: int
    data_id: int
    synced: int


"""
   [StructLayout(LayoutKind.Explicit, Size = 0x860)]
    public unsafe struct Buddy
    {
        [FieldOffset(0x0)] public BuddyMember Companion;
        [FieldOffset(0x198)] public BuddyMember Pet;
        [FieldOffset(0x330)] public fixed byte BattleBuddies[0x198 * 3]; // BuddyMember array for Squadron/Trust
        [FieldOffset(0x7F8)] public BuddyMember* CompanionPtr;
        [FieldOffset(0x800)] public float TimeLeft;
        [FieldOffset(0x812)] public fixed byte Name[21];
        [FieldOffset(0x828)] public uint CurrentXP;
        [FieldOffset(0x82A)] public byte Rank;
        [FieldOffset(0x82B)] public byte Stars;
        [FieldOffset(0x82C)] public byte SkillPoints;
        [FieldOffset(0x82D)] public byte DefenderLevel;
        [FieldOffset(0x82E)] public byte AttackerLevel;
        [FieldOffset(0x82F)] public byte HealerLevel;
        [FieldOffset(0x830)] public byte ActiveCommand;
        [FieldOffset(0x831)] public byte FavoriteFeed;
        [FieldOffset(0x832)] public byte CurrentColorStainId;
        [FieldOffset(0x833)] public byte Mounted; // bool
        [FieldOffset(0x840)] public BuddyMember* PetPtr;
        [FieldOffset(0x850)] public BuddyMember* SquadronTrustPtr;
    }
"""


class Buddy(OffsetStruct({
    "companion": (BuddyMember, 0x0),
    "pet": (BuddyMember, 0x198),
    "battle_buddies": (BuddyMember * 3, 0x330),
    "companion_ptr": (POINTER(BuddyMember), 0x7F8),
    "time_left": (c_float, 0x800),
    "_name": (c_char * 21, 0x812),
    "current_xp": (c_uint, 0x828),
    # "rank": (c_byte, 0x82A),
    # "stars": (c_byte, 0x82B),
    "skill_points": (c_byte, 0x82C),
    "defender_level": (c_byte, 0x82D),
    "attacker_level": (c_byte, 0x82E),
    "healer_level": (c_byte, 0x82F),
    "active_command": (c_byte, 0x830),
    "favorite_feed": (c_byte, 0x831),
    "current_color_stain_id": (c_byte, 0x832),
    "mounted": (c_bool, 0x833),
    "pet_ptr": (POINTER(BuddyMember), 0x840),
    "squadron_trust_ptr": (POINTER(BuddyMember), 0x850),
}, 0x860)):
    companion: BuddyMember
    pet: BuddyMember
    battle_buddies: List[BuddyMember]
    companion_ptr: List[BuddyMember]
    time_left: float
    _name: bytes
    current_xp: int
    rank: int
    stars: int
    skill_points: int
    defender_level: int
    attacker_level: int
    healer_level: int
    active_command: int
    favorite_feed: int
    current_color_stain_id: int
    mounted: bool
    pet_ptr: List[BuddyMember]
    squadron_trust_ptr: List[BuddyMember]

    @property
    def name(self) -> str:
        return self._name.decode("utf-8", "ignore")
