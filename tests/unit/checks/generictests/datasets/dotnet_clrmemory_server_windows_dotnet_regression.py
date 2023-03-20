#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# fmt: off
# mypy: disable-error-code=var-annotated

checkname = "dotnet_clrmemory"

info = [
    [
        "AllocatedBytesPersec",
        "Caption",
        "Description",
        "FinalizationSurvivors",
        "Frequency_Object",
        "Frequency_PerfTime",
        "Frequency_Sys100NS",
        "Gen0heapsize",
        "Gen0PromotedBytesPerSec",
        "Gen1heapsize",
        "Gen1PromotedBytesPerSec",
        "Gen2heapsize",
        "LargeObjectHeapsize",
        "Name",
        "NumberBytesinallHeaps",
        "NumberGCHandles",
        "NumberGen0Collections",
        "NumberGen1Collections",
        "NumberGen2Collections",
        "NumberInducedGC",
        "NumberofPinnedObjects",
        "NumberofSinkBlocksinuse",
        "NumberTotalcommittedBytes",
        "NumberTotalreservedBytes",
        "PercentTimeinGC",
        "PercentTimeinGC_Base",
        "ProcessID",
        "PromotedFinalizationMemoryfromGen0",
        "PromotedMemoryfromGen0",
        "PromotedMemoryfromGen1",
        "Timestamp_Object",
        "Timestamp_PerfTime",
        "Timestamp_Sys100NS",
    ],
    [
        "21380464834160",
        "",
        "",
        "13821",
        "0",
        "14318180",
        "10000000",
        "2012417216",
        "4762504",
        "28497416",
        "718488",
        "257543384",
        "239855984",
        "_Global_",
        "525896784",
        "45499",
        "894395",
        "717878",
        "531223",
        "68441",
        "2517",
        "3222",
        "2800212096",
        "64290166912",
        "78964360",
        "-1",
        "0",
        "491512",
        "4762504",
        "718488",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "1034323144",
        "",
        "",
        "421",
        "0",
        "14318180",
        "10000000",
        "13107200",
        "0",
        "1041864",
        "0",
        "12959776",
        "8008032",
        "powershell",
        "22009672",
        "3195",
        "64",
        "6",
        "4",
        "0",
        "3",
        "15",
        "35868672",
        "402644992",
        "70028",
        "863531387",
        "3460",
        "0",
        "0",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "1256169848",
        "",
        "",
        "403",
        "0",
        "14318180",
        "10000000",
        "13107200",
        "0",
        "845368",
        "0",
        "4340904",
        "8393528",
        "msftefd",
        "13579800",
        "1108",
        "84",
        "8",
        "2",
        "0",
        "180",
        "555",
        "27209728",
        "402644992",
        "205",
        "18132123",
        "4964",
        "0",
        "0",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "40643607208",
        "",
        "",
        "1176",
        "0",
        "14318180",
        "10000000",
        "171793984",
        "1121296",
        "1121488",
        "1008",
        "8512416",
        "6165288",
        "w3wp",
        "15799192",
        "1267",
        "339",
        "121",
        "7",
        "0",
        "214",
        "47",
        "188348800",
        "5368707456",
        "6451",
        "453642218",
        "8544",
        "40072",
        "1121296",
        "1008",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "28505439528",
        "",
        "",
        "35",
        "0",
        "14318180",
        "10000000",
        "171793984",
        "35560",
        "6990272",
        "0",
        "82755208",
        "2618360",
        "w3wp#1",
        "92363840",
        "18005",
        "209",
        "3",
        "2",
        "0",
        "0",
        "233",
        "370588032",
        "5368707456",
        "60",
        "1098595346",
        "5876",
        "1120",
        "35560",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "25377880160",
        "",
        "",
        "610",
        "0",
        "14318180",
        "10000000",
        "6291456",
        "188752",
        "258032",
        "0",
        "12625184",
        "8503648",
        "SMEX_Master",
        "21386864",
        "2203",
        "3922",
        "759",
        "42",
        "0",
        "10",
        "79",
        "27574272",
        "402644992",
        "348",
        "26884726",
        "4528",
        "23800",
        "188752",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "242127874192",
        "",
        "",
        "1790",
        "0",
        "14318180",
        "10000000",
        "13107200",
        "176160",
        "360056",
        "0",
        "7061152",
        "8857864",
        "Microsoft.Exchange.Search.ExSearch",
        "16279072",
        "712",
        "15616",
        "7903",
        "7532",
        "0",
        "174",
        "51",
        "33181696",
        "402644992",
        "115984",
        "-343301640",
        "4368",
        "72240",
        "176160",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "26405401888",
        "",
        "",
        "62",
        "0",
        "14318180",
        "10000000",
        "13107200",
        "123944",
        "429784",
        "0",
        "3762392",
        "640968",
        "MSExchangeMailSubmission",
        "4833144",
        "656",
        "2017",
        "281",
        "2",
        "0",
        "0",
        "27",
        "17838080",
        "402644992",
        "114",
        "108452653",
        "4256",
        "1984",
        "123944",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "41811669280",
        "",
        "",
        "1417",
        "0",
        "14318180",
        "10000000",
        "171793984",
        "106168",
        "683872",
        "0",
        "4183576",
        "532344",
        "MSExchangeMailboxReplication",
        "5399792",
        "869",
        "288",
        "34",
        "2",
        "0",
        "166",
        "21",
        "181623168",
        "5368707456",
        "374",
        "825963764",
        "4104",
        "45336",
        "106168",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "16261510680",
        "",
        "",
        "0",
        "0",
        "14318180",
        "10000000",
        "13107200",
        "808",
        "67560",
        "0",
        "3716080",
        "522704",
        "MSExchangeMailboxAssistants",
        "4306344",
        "814",
        "1243",
        "31",
        "1",
        "0",
        "1",
        "16",
        "17440768",
        "402644992",
        "41",
        "183435328",
        "4016",
        "0",
        "808",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "69115401592",
        "",
        "",
        "0",
        "0",
        "14318180",
        "10000000",
        "6291456",
        "336",
        "4600",
        "0",
        "8067032",
        "451712",
        "MsExchangeFDS",
        "8523344",
        "540",
        "10984",
        "717",
        "107",
        "0",
        "0",
        "21",
        "14839808",
        "402644992",
        "32",
        "94034864",
        "3908",
        "0",
        "336",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "50738223656",
        "",
        "",
        "18",
        "0",
        "14318180",
        "10000000",
        "171793984",
        "952",
        "1538344",
        "0",
        "916448",
        "324520",
        "Microsoft.Exchange.EdgeSyncSvc",
        "2779312",
        "570",
        "67317",
        "67317",
        "67317",
        "67317",
        "113",
        "16",
        "20654464",
        "5368707456",
        "102139",
        "859523133",
        "3752",
        "576",
        "952",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "14840512232",
        "",
        "",
        "0",
        "0",
        "14318180",
        "10000000",
        "6291456",
        "1264",
        "3472",
        "0",
        "434048",
        "228696",
        "Microsoft.Exchange.AntispamUpdateSvc",
        "666216",
        "192",
        "2358",
        "366",
        "23",
        "0",
        "0",
        "10",
        "6979584",
        "402644992",
        "16",
        "95780910",
        "3608",
        "0",
        "1264",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "19123272552",
        "",
        "",
        "1038",
        "0",
        "14318180",
        "10000000",
        "171793984",
        "38232",
        "215688",
        "0",
        "3460464",
        "193120",
        "Microsoft.Exchange.AddressBook.Service",
        "3869272",
        "546",
        "144",
        "13",
        "1",
        "0",
        "1",
        "20",
        "175999360",
        "5368707456",
        "177",
        "1770804486",
        "3284",
        "33216",
        "38232",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "3058406333280",
        "",
        "",
        "112",
        "0",
        "14318180",
        "10000000",
        "13107200",
        "0",
        "7931664",
        "0",
        "15869384",
        "5833944",
        "MonitoringHost",
        "29634992",
        "1652",
        "70407",
        "27993",
        "7758",
        "1123",
        "27",
        "1177",
        "156405760",
        "402644992",
        "175835",
        "19646043",
        "3060",
        "0",
        "0",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "447738985968",
        "",
        "",
        "476",
        "0",
        "14318180",
        "10000000",
        "6291456",
        "189240",
        "191400",
        "0",
        "9368552",
        "2119120",
        "SMEX_SystemWatcher",
        "11679072",
        "2446",
        "71158",
        "21943",
        "702",
        "0",
        "227",
        "32",
        "18190336",
        "402644992",
        "29427",
        "864749559",
        "3032",
        "17372",
        "189240",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "1582966894800",
        "",
        "",
        "1755",
        "0",
        "14318180",
        "10000000",
        "171793984",
        "845672",
        "845864",
        "184000",
        "43915832",
        "169687952",
        "EdgeTransport",
        "214449648",
        "4137",
        "16809",
        "4630",
        "1327",
        "0",
        "196",
        "207",
        "389077376",
        "5368707456",
        "615369",
        "1836658321",
        "2496",
        "85264",
        "845672",
        "184000",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "248414065112",
        "",
        "",
        "753",
        "0",
        "14318180",
        "10000000",
        "171793984",
        "371528",
        "371720",
        "43384",
        "13277960",
        "7617504",
        "MSExchangeTransportLogSearch",
        "21267184",
        "800",
        "4038",
        "1846",
        "40",
        "0",
        "5",
        "423",
        "199731584",
        "5368707456",
        "92",
        "33635996",
        "2316",
        "48192",
        "371528",
        "43384",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "14165996376",
        "",
        "",
        "0",
        "0",
        "14318180",
        "10000000",
        "6291456",
        "0",
        "2565672",
        "0",
        "24",
        "447256",
        "MSExchangeTransport",
        "3012952",
        "480",
        "2252",
        "1011",
        "23",
        "1",
        "169",
        "12",
        "15548416",
        "402644992",
        "235",
        "100491032",
        "2180",
        "0",
        "0",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "13976651744",
        "",
        "",
        "0",
        "0",
        "14318180",
        "10000000",
        "171793984",
        "520",
        "1512",
        "0",
        "1452120",
        "176968",
        "MSExchangeThrottling",
        "1630600",
        "455",
        "91",
        "14",
        "2",
        "0",
        "153",
        "11",
        "174422400",
        "5368707456",
        "181",
        "-1825012662",
        "2080",
        "0",
        "520",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "16394760256",
        "",
        "",
        "578",
        "0",
        "14318180",
        "10000000",
        "171793984",
        "24752",
        "24944",
        "489160",
        "4562400",
        "430120",
        "Microsoft.Exchange.ServiceHost",
        "5017464",
        "984",
        "175",
        "6",
        "1",
        "0",
        "170",
        "101",
        "182364544",
        "5368707456",
        "163",
        "1419991972",
        "1736",
        "18748",
        "24752",
        "489160",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "37340719640",
        "",
        "",
        "3176",
        "0",
        "14318180",
        "10000000",
        "171793984",
        "1529360",
        "1533104",
        "800",
        "8676480",
        "560512",
        "Microsoft.Exchange.RpcClientAccess.Service",
        "10770096",
        "1443",
        "355",
        "142",
        "9",
        "0",
        "12",
        "30",
        "182610304",
        "5368707456",
        "427",
        "402649328",
        "2008",
        "103568",
        "1529360",
        "800",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "4650095823504",
        "",
        "",
        "1",
        "0",
        "14318180",
        "10000000",
        "6291456",
        "6520",
        "6544",
        "136",
        "5109608",
        "6476080",
        "msexchangerepl",
        "11592232",
        "1055",
        "619841",
        "582310",
        "446273",
        "0",
        "223",
        "94",
        "25055232",
        "402644992",
        "207579",
        "480900",
        "1952",
        "24",
        "6520",
        "136",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "14598452632",
        "",
        "",
        "0",
        "0",
        "14318180",
        "10000000",
        "171793984",
        "864",
        "39448",
        "0",
        "2516320",
        "439232",
        "Microsoft.Exchange.ProtectedServiceHost",
        "2995000",
        "464",
        "93",
        "1",
        "0",
        "0",
        "153",
        "11",
        "328391040",
        "5368707456",
        "28",
        "-1876029354",
        "1848",
        "0",
        "864",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
    [
        "28892447808",
        "",
        "",
        "0",
        "0",
        "14318180",
        "10000000",
        "6291456",
        "576",
        "1425144",
        "0",
        "24",
        "626512",
        "Microsoft.Exchange.Monitoring",
        "2051680",
        "906",
        "4591",
        "423",
        "46",
        "0",
        "320",
        "13",
        "10268672",
        "402644992",
        "252",
        "49256366",
        "1740",
        "0",
        "576",
        "0",
        "0",
        "57866201615573",
        "131407819020030000",
    ],
]

discovery = {"": [("_Global_", "dotnet_clrmemory_defaultlevels")]}

checks = {
    "": [
        (
            "_Global_",
            {"upper": (10.0, 15.0)},
            [
                (
                    0,
                    "Time in GC: 1.84%",
                    [
                        ("percent", 1.8385322768796544, 10.0, 15.0, 0, 100),
                    ],
                ),
            ],
        ),
    ],
}
