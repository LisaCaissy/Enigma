#!/usr/bin/env python
from enigma.machine import EnigmaMachine


machine_01 = EnigmaMachine.from_key_sheet(rotors='III I II',
                                               reflector='B', ring_settings='16 12 02',
                                               plugboard_settings='AO BY CM DH GI KV LQ RW SZ TU') #EDT UMT ERL LUB


machine_02 = EnigmaMachine.from_key_sheet(rotors='II V I',
                                               reflector='B', ring_settings='23 09 21',
                                               plugboard_settings='AP CX DV EU FT GS HI KM LZ NR') #TSW USU CFL VVU

machine_03 = EnigmaMachine.from_key_sheet(rotors='V III I',
                                               reflector='B', ring_settings='06 05 10',
                                               plugboard_settings='AV DR EX FY HI JM KZ LQ NS PU') #GCN TBT OOW TNH

machine_04 = EnigmaMachine.from_key_sheet(rotors='V IV III',
                                               reflector='B', ring_settings='25 15 09',
                                               plugboard_settings='AF EQ GW HX IO JN KZ MS PR UY') #CFY NRA CNL MVE

machine_05 = EnigmaMachine.from_key_sheet(rotors='IV V I',
                                               reflector='B', ring_settings='07 06 12',
                                               plugboard_settings='AI CU DT GS HK JQ LM NV PZ XY') #FYB ITV BOL YID

machine_06 = EnigmaMachine.from_key_sheet(rotors='V II IV',
                                               reflector='B', ring_settings='20 01 05',
                                               plugboard_settings='BG CW DI EF JV LZ NY OR PS UX') #KWR MFT ITD GJD

machine_07 = EnigmaMachine.from_key_sheet(rotors='I IV V',
                                               reflector='B', ring_settings='06 15 10',
                                               plugboard_settings='AX BP CQ DR FI GY HJ KU MV SZ') #BIF CJM ONT TSM

machine_08 = EnigmaMachine.from_key_sheet(rotors='I IV V',
                                               reflector='B', ring_settings='02 01 06',
                                               plugboard_settings='AG CV DH EL FR IT JY MW QU SZ') #RXJ URE ANN ZDD

machine_09 = EnigmaMachine.from_key_sheet(rotors='III II I',
                                               reflector='B', ring_settings='05 19 12',
                                               plugboard_settings='BR CT DS EU HW IZ JP LX NO QV') #RLP RWX IQN EGA

machine_10 = EnigmaMachine.from_key_sheet(rotors='I V II',
                                               reflector='B', ring_settings='22 24 26',
                                               plugboard_settings='AN BQ DJ EI GU HV KR LP MS XY') #CQQ VEZ YFK NWA

machine_11 = EnigmaMachine.from_key_sheet(rotors='III V I',
                                               reflector='B', ring_settings='03 03 18',
                                               plugboard_settings='AP BI CS DU EZ FN HQ KO LM TW') #YEU CZL KLS AJL

machine_12 = EnigmaMachine.from_key_sheet(rotors='I II V',
                                               reflector='B', ring_settings='14 21 06',
                                               plugboard_settings='AK BD CL EJ FI GX OR PZ QT VW') #OWC EZZ QXC CAT

machine_13 = EnigmaMachine.from_key_sheet(rotors='IV I V',
                                               reflector='B', ring_settings='10 06 10',
                                               plugboard_settings='CZ DR EF GT HS IU LO MV PQ WX') #VXD QEM VOS ECZ

machine_14 = EnigmaMachine.from_key_sheet(rotors='I III V',
                                               reflector='B', ring_settings='08 14 02',
                                               plugboard_settings='AL CP DG FY HK JW MS NV QZ TU') #ONT ZAI YNC JPA

machine_15 = EnigmaMachine.from_key_sheet(rotors='IV I V',
                                               reflector='B', ring_settings='13 03 16',
                                               plugboard_settings='AE BV FK GO IZ JT LR MX NP WY') #QTQ JIS PCQ QPB

machine_16 = EnigmaMachine.from_key_sheet(rotors='III II IV',
                                               reflector='B', ring_settings='24 15 14',
                                               plugboard_settings='CV DJ EK FW GP HS IZ MT QX RY') #GJH QHK GVO BUR

machine_17 = EnigmaMachine.from_key_sheet(rotors='II I V',
                                               reflector='B', ring_settings='26 09 05',
                                               plugboard_settings='AX CJ DY EW GP HO IN MS QR UV') #ORH YCH ULT BQY

machine_18 = EnigmaMachine.from_key_sheet(rotors='III IV I',
                                               reflector='B', ring_settings='08 09 21',
                                               plugboard_settings='AY BK CS GQ HR JP LO MN UZ WX') #NPU XWU OWU CTI

machine_19 = EnigmaMachine.from_key_sheet(rotors='IV I V',
                                               reflector='B', ring_settings='02 04 15',
                                               plugboard_settings='CS DW EF IN JQ KT OX PZ RV UY') #AVD OAG YZI XKV

machine_20 = EnigmaMachine.from_key_sheet(rotors='I III V',
                                               reflector='B', ring_settings='25 11 10',
                                               plugboard_settings='AP BE FG IZ KT LN OR QX UW VY') #YMY BFL FDS DBG

machine_21 = EnigmaMachine.from_key_sheet(rotors='IV V I',
                                               reflector='B', ring_settings='22 01 01',
                                               plugboard_settings='AF CX DR GN HV JL KZ OW QS UY') #LFE RJG ROD GFU

machine_22 = EnigmaMachine.from_key_sheet(rotors='I III V',
                                               reflector='B', ring_settings='01 13 01',
                                               plugboard_settings='AS BC DU GY IK LZ MO NW QX RV') #EGD UUR ODC INE

machine_23 = EnigmaMachine.from_key_sheet(rotors='II V I',
                                               reflector='B', ring_settings='10 04 12',
                                               plugboard_settings='BE CK DX FG HI MO NP QU RS VZ') #WDS QXB YYB NDF

machine_24 = EnigmaMachine.from_key_sheet(rotors='V I IV',
                                               reflector='B', ring_settings='19 02 06',
                                               plugboard_settings='AL CM DO EP HN IK SZ TU VY WX') #FPC PHY KWY RLH

machine_25 = EnigmaMachine.from_key_sheet(rotors='III I IV',
                                               reflector='B', ring_settings='06 13 13',
                                               plugboard_settings='BX CE DR FG HV IN LY MT OS UW') #PWC MPI RAJ VWW

machine_26 = EnigmaMachine.from_key_sheet(rotors='IV II III',
                                               reflector='B', ring_settings='19 20 20',
                                               plugboard_settings='AK BX CQ DO EI HS LR PW TZ VY') #SQW JVL MUA LSP

machine_27 = EnigmaMachine.from_key_sheet(rotors='IV III II',
                                               reflector='B', ring_settings='02 03 15',
                                               plugboard_settings='AC BP EZ FX GV HK LT MR NU QW') #ZON KOV FCE CDJ

machine_28 = EnigmaMachine.from_key_sheet(rotors='IV II III',
                                               reflector='B', ring_settings='12 07 08',
                                               plugboard_settings='BW DZ EY FR GT HJ IV LS NQ OX') #EPK PLF PIR NCY

machine_29 = EnigmaMachine.from_key_sheet(rotors='V III I',
                                               reflector='B', ring_settings='09 25 21',
                                               plugboard_settings='AK BU CI DE GQ HM LT OZ RV WY') #AFU WWW TSM UVX

machine_30 = EnigmaMachine.from_key_sheet(rotors='II V III',
                                               reflector='B', ring_settings='22 11 01',
                                               plugboard_settings='AL BS EU FR GM IO PY QZ TW VX') #ZUF SIC FDH BKU

machine_31 = EnigmaMachine.from_key_sheet(rotors='IV V I',
                                               reflector='B', ring_settings='24 17 13',
                                               plugboard_settings='AQ CT DV EN FW GP IX JS KR LO') #BZA KZO SIK VMO
