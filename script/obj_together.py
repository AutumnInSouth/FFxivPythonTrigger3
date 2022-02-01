from pathlib import Path

p = Path(r"D:\game\ff14_res\Godbert\s1t2")

select = [
    # 's1t2-bg_anniversary2018_00.obj',
    # 's1t2-bg_anniversary2019_00.obj',
    # 's1t2-bg_anniversary2020_00.obj',
    # 's1t2-bg_anniversary2021_00.obj',
    's1t2-bg_battle1.obj',
    # 's1t2-bg_christmas2018_00.obj',
    # 's1t2-bg_christmas2019_00.obj',
    # 's1t2-bg_christmas2020_00.obj',
    # 's1t2-bg_collision.obj', #？
    's1t2-bg_door.obj',  #
    # 's1t2-bg_easter2018_00.obj',
    # 's1t2-bg_easter2019_00.obj',
    # 's1t2-bg_easter2020_00.obj',
    # 's1t2-bg_easter2021_00.obj',
    # 's1t2-bg_enk_snbs.obj', # 无碰撞码头
    's1t2-bg_ex_artifact.obj',  # 城堡建筑类
    's1t2-bg_ex_bridge.obj',
    's1t2-bg_ex_get1.obj',
    's1t2-bg_ex_hakotaru.obj',
    's1t2-bg_ex_island.obj',
    's1t2-bg_ex_mainkanagu.obj',
    # 's1t2-bg_ex_plant2.obj',
    # 's1t2-bg_ex_plant3.obj',
    's1t2-bg_ex_rock.obj',
    's1t2-bg_ex_room.obj',
    's1t2-bg_ex_sea_gate.obj',
    's1t2-bg_ex_ships.obj',
    's1t2-bg_ex_ships_low.obj',
    's1t2-bg_ex_ship_blue1.obj',
    's1t2-bg_ex_ship_brown1.obj',
    's1t2-bg_ex_ship_brown2.obj',
    's1t2-bg_ex_sukima.obj',
    's1t2-bg_ex_wallparts.obj',
    's1t2-bg_ex_zousenjo.obj',
    # 's1t2-bg_fld_enkei2.obj',
    # 's1t2-bg_halloween2017_00.obj',
    # 's1t2-bg_halloween2018_00.obj',
    # 's1t2-bg_halloween2019_00.obj',
    's1t2-bg_IKD.obj',
    's1t2-bg_in_c1.obj',
    's1t2-bg_in_d1.obj',
    's1t2-bg_in_e2.obj',
    's1t2-bg_in_f3.obj',
    's1t2-bg_in_g1.obj',
    's1t2-bg_in_v1b.obj',
    's1t2-bg_in_w1.obj',
    's1t2-bg_in_w2.obj',
    's1t2-bg_juuono.obj',
    's1t2-bg_kaishu2.obj',
    's1t2-bg_kaji.obj',
    's1t2-bg_kanban_mts2.obj',
    's1t2-bg_mpc.obj',
    's1t2-bg_newroom2.obj',
    's1t2-bg_newroom_indoor.obj',
    's1t2-bg_newroom_light.obj',
    's1t2-bg_newroom_outdoor.obj',
    's1t2-bg_sakaba.obj',
    # 's1t2-bg_summer2018_00.obj',
    # 's1t2-bg_summer2019_00.obj',
    # 's1t2-bg_summer2020_00.obj',
    # 's1t2-bg_summer2021_00.obj',
    # 's1t2-fld2_hashi.obj',  # 远景 上层下方出口
    # 's1t2-ind_c1.obj',  # ?
    # 's1t2-ind_e2.obj',
    # 's1t2-ind_f3.obj',
    # 's1t2-ind_v1.obj',
    # 's1t2-ind_w1.obj',
    's1t2-komono_haiti.obj',  # 布景箱子
    's1t2-LVD_aetheryte_01.obj',  # 大水晶
    's1t2-LVD_fcchest_01.obj',  # 部队柜
    's1t2-LVD_townportal_01.obj',  # 水晶
    's1t2-patch_2_35_weather.obj',  # 天气预告
    's1t2-QB_ClsRog101_001.obj',  # 水晶
    # 's1t2-shadowmask.obj',
    # 's1t2-twn_e1.obj',
    # 's1t2-twn_f1.obj',
    # 's1t2-twn_f2.obj',
    # 's1t2-twn_f3.obj',
    # 's1t2-twn_g.obj',
    # 's1t2-twn_h.obj',
    # 's1t2-twn_i.obj',
    # 's1t2-twn_j.obj',
    # 's1t2-twn_m.obj',
    # 's1t2-twn_s1.obj',
    # 's1t2-twn_s2.obj',
    # 's1t2-twn_t.obj',
    # 's1t2-twn_v.obj',
    # 's1t2-twn_w.obj',
    # 's1t2-twn_x.obj',
    # 's1t2-twn_y.obj',
    # 's1t2-twn_z.obj',
    # 's1t2-twn_z2.obj',
    's1t2-ue_hasi_barasi.obj',  # 桥
    's1t2.obj',  # 地基
]
with open(p / "merged_s1t2.obj", "w+") as fo:
    v_count = 0
    vt_count = 0
    vn_count = 0
    for f in select:
        print(f,v_count,vt_count,vn_count)
        with open(p / f, "r") as fi:
            _v_count = 0
            _vt_count = 0
            _vn_count = 0
            to_add_lines = []
            for line in fi:
                l = line.strip('\n').split(' ')
                match l[0]:
                    case "v":
                        _v_count += 1
                        to_add_lines.append(line)
                    case "vt":
                        _vt_count += 1
                        to_add_lines.append(line)
                    case "vn":
                        _vn_count += 1
                        to_add_lines.append(line)
                    case "f":
                        data = [[int(x) for x in x.split('/')] for x in l[1:]]
                        for i in range(len(data)):
                            data[i][0] += v_count
                            data[i][1] += vt_count
                            data[i][2] += vn_count
                        to_add_lines.append(f"f {' '.join(['/'.join([str(y) for y in x]) for x in data])}\n")
            if to_add_lines:
                fo.write(f"g {f.split('.')[0]}\n")
                for line in to_add_lines:
                    fo.write(line)
                v_count += _v_count
                vt_count += _vt_count
                vn_count += _vn_count
