import json

from dqmcrawlr.jsonfairy import JSON_Fairy


def test_construct_url():
    resource = "/Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaPhi_ImpactPoint_GenTk"
    expected = "https://cmsweb.cern.ch/dqm/offline/jsonfairy/archive/321012/StreamExpress/Run2018D-Express-v1/DQMIO/Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaPhi_ImpactPoint_GenTk"
    url = JSON_Fairy()._construct_url("321012", "Express", resource)
    assert expected == url


def test_get_TrackEtaPhi_ImpactPoint_GenTk():
    expected = json.loads(
        '{"hist":{"type":"TH2","title":"TrackEtaPhi_ImpactPoint_GenTk","stats":{"name":"TrackEtaPhi_ImpactPoint_GenTk","entries":27465754.000000,"mean":{"X":{"value":-0.0241293,"error":0.000312038},"Y":{"value":-0.00116678,"error":0.000349952}},"rms":{"X":{"value":1.63532,"error":0.000220644},"Y":{"value":1.83402,"error":0.000247454}},"underflow":0,"overflow":0},"xaxis":{"title":"Track #eta","first":{"id":1,"value":-3},"last": {"id":31,"value":3}},"yaxis":{"title":"Track #phi","first":{"id":1,"value":-3.14159},"last": {"id":32,"value":3.14159}},"values":{"min":1306,"max":35303},"bins":{"integral":[[0,2907,0],[0,2.74584e+07,0],[0,4466,0]],"content":[[3298,20136,28377,33641,33363,33212,31385,29977,27588,28420,30064,31260,31742,31639,31711,32359,31903,31985,32284,31725,30534,29923,29254,32381,33004,34230,33699,33365,26445,17069,2276],[3496,20525,29388,33591,33829,33465,31366,30315,28307,29333,30547,31344,31820,31829,31737,32498,31889,32376,32644,31981,30736,30392,29329,31821,33362,34835,34599,34189,27233,18096,2682],[4132,21273,28815,32326,32538,33964,32181,30960,28734,29021,29918,31035,31394,31220,30742,31534,30891,31274,31001,30543,28979,29041,27760,31222,33522,34428,34647,33835,27308,19049,3122],[4962,22066,28471,31981,32667,33875,32973,31204,28190,28636,29422,29829,29704,29149,28293,28570,28123,28394,28247,27701,25950,25549,22936,28553,32097,33752,34025,33152,27383,17680,2720],[2945,17215,28320,33235,33570,34394,32779,30628,26939,28051,28803,28805,29152,28676,27726,28232,27610,27654,27899,27335,25738,24905,22255,27740,31741,32704,32568,33126,26536,14534,2148],[2825,17127,28988,33298,33781,33995,32565,29921,26213,28027,28979,29435,30156,29853,29362,29511,29042,29220,29965,29403,27568,26662,24374,28879,32554,33831,32818,31632,25812,16344,2947],[3563,19334,31100,34414,34232,34422,33122,30724,26210,27730,28369,30222,31240,30933,30828,31125,30988,31436,31934,31792,30439,29058,26953,29593,32290,33463,32614,32944,29132,17063,2664],[3219,17906,29352,33724,33504,33913,32726,30013,23741,25779,26328,27879,29490,29094,29244,29960,29885,30784,31465,30979,29175,28531,25987,29757,32363,34077,33650,34009,29982,18519,3210],[3316,16543,27597,33197,33274,33779,33257,30150,24279,24915,24781,26368,28183,28807,28770,29855,30129,31104,32062,31843,29884,29327,27092,30750,32664,34183,34678,34736,30779,22650,4387],[4433,18561,28574,33424,33893,34825,33084,30896,26540,26680,26262,27079,28059,28143,28586,29284,29936,31246,31792,31697,30263,29594,28240,31388,33604,34721,34428,34787,30648,23315,5067],[5435,20042,29741,34104,34016,33902,32880,31192,26542,26537,25821,26393,27703,28212,28865,29812,29979,31304,32038,31681,30302,29485,28464,31869,33129,34262,34357,34838,30590,22935,5697],[5885,21286,30750,34249,33431,33943,32853,31185,27395,27260,26381,26860,28118,28862,29008,30252,29914,30957,31708,31784,30057,29545,28136,31216,33029,34821,34303,35156,31013,21210,5622],[8074,23628,31520,34026,34064,34365,33281,30873,27293,28052,28206,29120,30529,30492,30579,30400,29956,30677,31185,30486,28889,28205,27389,31104,32845,33375,33608,34799,31069,20368,5385],[10210,27158,32441,34159,33731,33911,33050,31118,28162,28804,29735,30578,31641,31665,31025,30459,29233,30100,30152,30057,27713,27038,26356,29534,31830,32973,32784,33839,29191,19578,4792],[9729,25529,30147,32602,32282,33611,33388,30547,27380,28219,28820,30133,30340,30945,30490,30023,28815,29574,29984,29725,27416,26672,26723,30153,32603,33615,33257,33295,28911,20233,5943],[7331,21291,27397,30511,30711,33111,31939,29815,26815,26845,27518,28156,28363,27801,27884,27297,26173,27209,27427,27733,26348,25786,26269,29577,31209,32552,32642,33271,29164,19675,5605],[7429,22794,29649,32721,31993,33316,33004,31055,28429,28216,28611,28963,28130,27993,27522,26363,24773,25380,24846,24557,23389,23738,24779,28060,29111,31701,31975,33040,28581,19842,5091],[7957,24021,31253,34317,34471,34657,32889,30987,28381,28099,28368,28724,28298,27765,26820,24314,22242,22347,21515,21394,21284,20385,21868,26322,29077,31725,31435,32446,27847,20197,5658],[8633,25373,31962,34440,34361,33895,30245,26395,22873,23194,25752,27470,27310,27432,26499,23570,21774,21324,20161,19721,19331,17261,20052,25481,29147,31283,30835,32004,26996,16551,3760],[10194,27674,32256,34265,34121,33261,29179,23081,19339,20357,22590,24280,24992,25215,23248,20613,18199,18214,16876,17702,18663,16310,20041,26652,30497,33011,32164,32004,27461,20625,7330],[10449,27834,32363,34182,33985,33481,30044,24997,21365,23853,25529,26303,26382,25918,25409,23367,21174,21270,21293,22218,21883,21341,23211,28134,30811,32581,31567,31559,27174,22158,7097],[5953,21460,30257,33168,33752,33089,30462,26272,23735,25739,27684,28589,29066,28862,28785,27776,26605,27575,27635,27564,25843,25446,24231,26965,28999,31248,31852,31808,26877,19920,5805],[1306,16914,28760,33052,32931,33365,31608,29409,27397,28631,30158,31358,31506,31454,30889,30788,30228,30489,30803,30346,28322,26580,24483,26546,28876,31449,31714,33219,28454,17717,3345],[1943,16347,27602,31151,31801,32208,31854,29516,27433,28125,29474,30794,31692,30985,30248,30450,29052,29527,29382,28713,26465,25238,22547,25496,28949,32349,32228,33357,27888,14325,1717],[6748,24289,29466,30903,31483,32083,31931,29961,28200,28882,29233,30428,30626,30222,29655,29750,28939,29683,29729,29848,27573,26765,23456,26799,30409,33108,32519,32843,29036,22060,4491],[6544,24562,30348,32455,32468,32872,32513,30886,28876,28940,29199,29332,29313,28497,28654,29194,28728,28918,29330,28585,26840,26724,24322,28041,31033,33762,33537,33909,29576,22445,4608],[5964,23873,30755,33995,34088,33576,32245,31525,29112,29017,28871,29286,29263,28590,28539,29162,28557,29358,29574,29303,27692,27609,25321,29157,32276,34109,34035,34622,29560,21380,4182],[5801,23431,31086,34844,34626,33526,32673,31212,29642,30027,30325,31049,31047,30923,30686,30813,29938,30539,30486,29760,28196,28036,25673,29603,32655,34176,33087,33020,28948,20420,3911],[5763,23387,31678,34963,34654,33652,31562,29008,26587,27325,28091,28958,29335,29693,29677,31295,30400,31376,31497,31404,30134,29686,28409,31529,33230,34546,33935,33782,28445,18993,3095],[5954,24607,31616,34474,34366,33859,31275,29042,25984,27009,28423,29604,29655,29853,30259,30938,30745,31776,31882,32051,30605,30160,29630,32206,33965,34584,33283,32741,28640,20147,3520],[5503,23818,30643,34526,34691,34006,32507,30535,27946,28641,29208,30161,30203,30112,30695,31484,31480,31597,32232,32518,31251,30886,29681,31997,33992,35303,33703,33674,29565,21460,3944],[4006,21418,29811,34428,34491,34117,33016,31332,29456,29684,30763,31679,32067,31977,31829,32870,32111,32385,32456,31994,30794,30502,28973,31803,33500,34850,34561,33693,27969,18996,2758]]}} }'
    )
    assert expected == JSON_Fairy().get_TrackEtaPhi_ImpactPoint_GenTk(
        "321012", "Express"
    )


def test_get_json():
    expected = json.loads(
        '{"hist":{"type":"TH2","title":"TrackEtaPhi_ImpactPoint_GenTk","stats":{"name":"TrackEtaPhi_ImpactPoint_GenTk","entries":27465754.000000,"mean":{"X":{"value":-0.0241293,"error":0.000312038},"Y":{"value":-0.00116678,"error":0.000349952}},"rms":{"X":{"value":1.63532,"error":0.000220644},"Y":{"value":1.83402,"error":0.000247454}},"underflow":0,"overflow":0},"xaxis":{"title":"Track #eta","first":{"id":1,"value":-3},"last": {"id":31,"value":3}},"yaxis":{"title":"Track #phi","first":{"id":1,"value":-3.14159},"last": {"id":32,"value":3.14159}},"values":{"min":1306,"max":35303},"bins":{"integral":[[0,2907,0],[0,2.74584e+07,0],[0,4466,0]],"content":[[3298,20136,28377,33641,33363,33212,31385,29977,27588,28420,30064,31260,31742,31639,31711,32359,31903,31985,32284,31725,30534,29923,29254,32381,33004,34230,33699,33365,26445,17069,2276],[3496,20525,29388,33591,33829,33465,31366,30315,28307,29333,30547,31344,31820,31829,31737,32498,31889,32376,32644,31981,30736,30392,29329,31821,33362,34835,34599,34189,27233,18096,2682],[4132,21273,28815,32326,32538,33964,32181,30960,28734,29021,29918,31035,31394,31220,30742,31534,30891,31274,31001,30543,28979,29041,27760,31222,33522,34428,34647,33835,27308,19049,3122],[4962,22066,28471,31981,32667,33875,32973,31204,28190,28636,29422,29829,29704,29149,28293,28570,28123,28394,28247,27701,25950,25549,22936,28553,32097,33752,34025,33152,27383,17680,2720],[2945,17215,28320,33235,33570,34394,32779,30628,26939,28051,28803,28805,29152,28676,27726,28232,27610,27654,27899,27335,25738,24905,22255,27740,31741,32704,32568,33126,26536,14534,2148],[2825,17127,28988,33298,33781,33995,32565,29921,26213,28027,28979,29435,30156,29853,29362,29511,29042,29220,29965,29403,27568,26662,24374,28879,32554,33831,32818,31632,25812,16344,2947],[3563,19334,31100,34414,34232,34422,33122,30724,26210,27730,28369,30222,31240,30933,30828,31125,30988,31436,31934,31792,30439,29058,26953,29593,32290,33463,32614,32944,29132,17063,2664],[3219,17906,29352,33724,33504,33913,32726,30013,23741,25779,26328,27879,29490,29094,29244,29960,29885,30784,31465,30979,29175,28531,25987,29757,32363,34077,33650,34009,29982,18519,3210],[3316,16543,27597,33197,33274,33779,33257,30150,24279,24915,24781,26368,28183,28807,28770,29855,30129,31104,32062,31843,29884,29327,27092,30750,32664,34183,34678,34736,30779,22650,4387],[4433,18561,28574,33424,33893,34825,33084,30896,26540,26680,26262,27079,28059,28143,28586,29284,29936,31246,31792,31697,30263,29594,28240,31388,33604,34721,34428,34787,30648,23315,5067],[5435,20042,29741,34104,34016,33902,32880,31192,26542,26537,25821,26393,27703,28212,28865,29812,29979,31304,32038,31681,30302,29485,28464,31869,33129,34262,34357,34838,30590,22935,5697],[5885,21286,30750,34249,33431,33943,32853,31185,27395,27260,26381,26860,28118,28862,29008,30252,29914,30957,31708,31784,30057,29545,28136,31216,33029,34821,34303,35156,31013,21210,5622],[8074,23628,31520,34026,34064,34365,33281,30873,27293,28052,28206,29120,30529,30492,30579,30400,29956,30677,31185,30486,28889,28205,27389,31104,32845,33375,33608,34799,31069,20368,5385],[10210,27158,32441,34159,33731,33911,33050,31118,28162,28804,29735,30578,31641,31665,31025,30459,29233,30100,30152,30057,27713,27038,26356,29534,31830,32973,32784,33839,29191,19578,4792],[9729,25529,30147,32602,32282,33611,33388,30547,27380,28219,28820,30133,30340,30945,30490,30023,28815,29574,29984,29725,27416,26672,26723,30153,32603,33615,33257,33295,28911,20233,5943],[7331,21291,27397,30511,30711,33111,31939,29815,26815,26845,27518,28156,28363,27801,27884,27297,26173,27209,27427,27733,26348,25786,26269,29577,31209,32552,32642,33271,29164,19675,5605],[7429,22794,29649,32721,31993,33316,33004,31055,28429,28216,28611,28963,28130,27993,27522,26363,24773,25380,24846,24557,23389,23738,24779,28060,29111,31701,31975,33040,28581,19842,5091],[7957,24021,31253,34317,34471,34657,32889,30987,28381,28099,28368,28724,28298,27765,26820,24314,22242,22347,21515,21394,21284,20385,21868,26322,29077,31725,31435,32446,27847,20197,5658],[8633,25373,31962,34440,34361,33895,30245,26395,22873,23194,25752,27470,27310,27432,26499,23570,21774,21324,20161,19721,19331,17261,20052,25481,29147,31283,30835,32004,26996,16551,3760],[10194,27674,32256,34265,34121,33261,29179,23081,19339,20357,22590,24280,24992,25215,23248,20613,18199,18214,16876,17702,18663,16310,20041,26652,30497,33011,32164,32004,27461,20625,7330],[10449,27834,32363,34182,33985,33481,30044,24997,21365,23853,25529,26303,26382,25918,25409,23367,21174,21270,21293,22218,21883,21341,23211,28134,30811,32581,31567,31559,27174,22158,7097],[5953,21460,30257,33168,33752,33089,30462,26272,23735,25739,27684,28589,29066,28862,28785,27776,26605,27575,27635,27564,25843,25446,24231,26965,28999,31248,31852,31808,26877,19920,5805],[1306,16914,28760,33052,32931,33365,31608,29409,27397,28631,30158,31358,31506,31454,30889,30788,30228,30489,30803,30346,28322,26580,24483,26546,28876,31449,31714,33219,28454,17717,3345],[1943,16347,27602,31151,31801,32208,31854,29516,27433,28125,29474,30794,31692,30985,30248,30450,29052,29527,29382,28713,26465,25238,22547,25496,28949,32349,32228,33357,27888,14325,1717],[6748,24289,29466,30903,31483,32083,31931,29961,28200,28882,29233,30428,30626,30222,29655,29750,28939,29683,29729,29848,27573,26765,23456,26799,30409,33108,32519,32843,29036,22060,4491],[6544,24562,30348,32455,32468,32872,32513,30886,28876,28940,29199,29332,29313,28497,28654,29194,28728,28918,29330,28585,26840,26724,24322,28041,31033,33762,33537,33909,29576,22445,4608],[5964,23873,30755,33995,34088,33576,32245,31525,29112,29017,28871,29286,29263,28590,28539,29162,28557,29358,29574,29303,27692,27609,25321,29157,32276,34109,34035,34622,29560,21380,4182],[5801,23431,31086,34844,34626,33526,32673,31212,29642,30027,30325,31049,31047,30923,30686,30813,29938,30539,30486,29760,28196,28036,25673,29603,32655,34176,33087,33020,28948,20420,3911],[5763,23387,31678,34963,34654,33652,31562,29008,26587,27325,28091,28958,29335,29693,29677,31295,30400,31376,31497,31404,30134,29686,28409,31529,33230,34546,33935,33782,28445,18993,3095],[5954,24607,31616,34474,34366,33859,31275,29042,25984,27009,28423,29604,29655,29853,30259,30938,30745,31776,31882,32051,30605,30160,29630,32206,33965,34584,33283,32741,28640,20147,3520],[5503,23818,30643,34526,34691,34006,32507,30535,27946,28641,29208,30161,30203,30112,30695,31484,31480,31597,32232,32518,31251,30886,29681,31997,33992,35303,33703,33674,29565,21460,3944],[4006,21418,29811,34428,34491,34117,33016,31332,29456,29684,30763,31679,32067,31977,31829,32870,32111,32385,32456,31994,30794,30502,28973,31803,33500,34850,34561,33693,27969,18996,2758]]}} }'
    )
    resource = "/Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaPhi_ImpactPoint_GenTk"
    response = JSON_Fairy().get_json("321012", "Express", resource)
    assert expected == response
