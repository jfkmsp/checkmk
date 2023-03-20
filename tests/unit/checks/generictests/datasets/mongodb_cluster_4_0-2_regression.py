#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# fmt: off
# mypy: disable-error-code=var-annotated


checkname = "mongodb_cluster"


info = [
    [
        '{"settings":{"chunkSize":67108864},"shards":{"shard03":{"host":"shard03/shard03a:27020,shard03b:27020","state":1},"shard02":{"host":"shard02/shard02a:27019,shard02b:27019","state":1},"shard01":{"host":"shard01/shard01a:27018,shard01b:27018","state":1}},"balancer":{"numBalancerRounds":26,"balancer_enabled":true,"mode":"full","inBalancerRound":false},"databases":{"unshardedDB2":{"collstats":{"collections1":{"count":3000,"storageSize":61440,"ok":1.0,"avgObjSize":34.0,"shards":{"shard01":{"count":3000,"numberOfChunks":1,"ns":"unshardedDB2.collections1","ok":1.0,"avgObjSize":34,"totalIndexSize":40960,"capped":false,"numberOfJumbos":0,"nindexes":1,"storageSize":61440,"size":102000}},"nchunks":1,"primary":"shard01","totalIndexSize":40960,"maxSize":0,"sharded":false,"capped":false,"nindexes":1,"ns":"unshardedDB2.collections1","size":102000},"collections2":{"count":666,"storageSize":24576,"ok":1.0,"avgObjSize":36.0,"shards":{"shard01":{"count":666,"numberOfChunks":1,"ns":"unshardedDB2.collections2","ok":1.0,"avgObjSize":36,"totalIndexSize":20480,"capped":false,"numberOfJumbos":0,"nindexes":1,"storageSize":24576,"size":23976}},"nchunks":1,"primary":"shard01","totalIndexSize":20480,"maxSize":0,"sharded":false,"capped":false,"nindexes":1,"ns":"unshardedDB2.collections2","size":23976}},"collections":["collections1","collections2"],"primary":"shard01","partitioned":false},"shardedDB1":{"collstats":{"collections1":{"count":10000,"storageSize":307200,"ok":1.0,"avgObjSize":40.0,"dropped":false,"unique":false,"nchunks":12,"shards":{"shard03":{"count":3335,"numberOfChunks":8,"ns":"shardedDB1.collections1","ok":1.0,"avgObjSize":40,"totalIndexSize":114688,"capped":false,"numberOfJumbos":0,"nindexes":2,"storageSize":102400,"size":135866},"shard02":{"count":3366,"numberOfChunks":2,"ns":"shardedDB1.collections1","ok":1.0,"avgObjSize":40,"totalIndexSize":114688,"capped":false,"numberOfJumbos":0,"nindexes":2,"storageSize":102400,"size":137182},"shard01":{"count":3299,"numberOfChunks":2,"ns":"shardedDB1.collections1","ok":1.0,"avgObjSize":40,"totalIndexSize":110592,"capped":false,"numberOfJumbos":0,"nindexes":2,"storageSize":102400,"size":134445}},"totalIndexSize":339968,"maxSize":0,"sharded":true,"capped":false,"nindexes":2,"ns":"shardedDB1.collections1","size":407493},"collections2":{"count":10000,"storageSize":286720,"ok":1.0,"avgObjSize":39.0,"dropped":false,"unique":false,"nchunks":6,"shards":{"shard03":{"count":3383,"numberOfChunks":2,"ns":"shardedDB1.collections2","ok":1.0,"avgObjSize":39,"totalIndexSize":114688,"capped":false,"numberOfJumbos":0,"nindexes":2,"storageSize":98304,"size":135296},"shard02":{"count":3301,"numberOfChunks":2,"ns":"shardedDB1.collections2","ok":1.0,"avgObjSize":39,"totalIndexSize":110592,"capped":false,"numberOfJumbos":0,"nindexes":2,"storageSize":94208,"size":132020},"shard01":{"count":3316,"numberOfChunks":2,"ns":"shardedDB1.collections2","ok":1.0,"avgObjSize":39,"totalIndexSize":110592,"capped":false,"numberOfJumbos":0,"nindexes":2,"storageSize":94208,"size":132610}},"totalIndexSize":335872,"maxSize":0,"sharded":true,"capped":false,"nindexes":2,"ns":"shardedDB1.collections2","size":399926}},"collections":["collections1","collections2"],"primary":"shard01","partitioned":true},"shardedDB2":{"collstats":{"collections2":{"count":100000,"storageSize":2740224,"ok":1.0,"avgObjSize":40.0,"dropped":false,"unique":false,"nchunks":6,"shards":{"shard03":{"count":33371,"numberOfChunks":2,"ns":"shardedDB2.collections2","ok":1.0,"avgObjSize":40,"totalIndexSize":1544192,"capped":false,"numberOfJumbos":0,"nindexes":2,"storageSize":909312,"size":1359812},"shard02":{"count":33207,"numberOfChunks":2,"ns":"shardedDB2.collections2","ok":1.0,"avgObjSize":40,"totalIndexSize":1527808,"capped":false,"numberOfJumbos":0,"nindexes":2,"storageSize":909312,"size":1353080},"shard01":{"count":33422,"numberOfChunks":2,"ns":"shardedDB2.collections2","ok":1.0,"avgObjSize":40,"totalIndexSize":1519616,"capped":false,"numberOfJumbos":0,"nindexes":2,"storageSize":921600,"size":1361819}},"totalIndexSize":4591616,"maxSize":0,"sharded":true,"capped":false,"nindexes":2,"ns":"shardedDB2.collections2","size":4074711}},"collections":["collections2"],"primary":"shard01","partitioned":true},"unshardedDB1":{"collstats":{"collections1":{"count":1000,"storageSize":32768,"ok":1.0,"avgObjSize":35.0,"shards":{"shard01":{"count":1000,"numberOfChunks":1,"ns":"unshardedDB1.collections1","ok":1.0,"avgObjSize":35,"totalIndexSize":20480,"capped":false,"numberOfJumbos":0,"nindexes":1,"storageSize":32768,"size":35000}},"nchunks":1,"primary":"shard01","totalIndexSize":20480,"maxSize":0,"sharded":false,"capped":false,"nindexes":1,"ns":"unshardedDB1.collections1","size":35000}},"collections":["collections1"],"primary":"shard01","partitioned":true},"jumboDB1":{"collstats":{"collections1":{"count":0,"storageSize":12288,"ok":1.0,"avgObjSize":0.0,"dropped":false,"unique":false,"nchunks":6,"shards":{"shard03":{"count":0,"numberOfChunks":2,"storageSize":4096,"ok":1.0,"totalIndexSize":8192,"capped":false,"numberOfJumbos":0,"nindexes":2,"ns":"jumboDB1.collections1","size":0},"shard02":{"count":0,"numberOfChunks":2,"storageSize":4096,"ok":1.0,"totalIndexSize":8192,"capped":false,"numberOfJumbos":0,"nindexes":2,"ns":"jumboDB1.collections1","size":0},"shard01":{"count":0,"numberOfChunks":2,"storageSize":4096,"ok":1.0,"totalIndexSize":8192,"capped":false,"numberOfJumbos":0,"nindexes":2,"ns":"jumboDB1.collections1","size":0}},"totalIndexSize":24576,"maxSize":0,"sharded":true,"capped":false,"nindexes":2,"ns":"jumboDB1.collections1","size":0}},"collections":["collections1"],"primary":"shard01","partitioned":true},"noColDB1":{"collstats":{},"collections":[],"primary":"shard01","partitioned":false}}}'
    ]
]


discovery = {
    "": [
        ("jumboDB1", {}),
        ("noColDB1", {}),
        ("shardedDB1", {}),
        ("shardedDB2", {}),
        ("unshardedDB1", {}),
        ("unshardedDB2", {}),
    ],
    "balancer": [(None, {})],
    "collections": [
        ("jumboDB1.collections1", {}),
        ("shardedDB1.collections1", {}),
        ("shardedDB1.collections2", {}),
        ("shardedDB2.collections2", {}),
        ("unshardedDB1.collections1", {}),
        ("unshardedDB2.collections1", {}),
        ("unshardedDB2.collections2", {}),
    ],
}


checks = {
    "": [
        (
            "jumboDB1",
            {},
            [(0, "Partitioned: true", []), (0, "Collections: 1", []), (0, "Primary: shard01", [])],
        ),
        (
            "noColDB1",
            {},
            [(0, "Partitioned: false", []), (1, "Collections: 0", []), (0, "Primary: shard01", [])],
        ),
        (
            "shardedDB1",
            {},
            [(0, "Partitioned: true", []), (0, "Collections: 2", []), (0, "Primary: shard01", [])],
        ),
        (
            "shardedDB2",
            {},
            [(0, "Partitioned: true", []), (0, "Collections: 1", []), (0, "Primary: shard01", [])],
        ),
        (
            "unshardedDB1",
            {},
            [(0, "Partitioned: true", []), (0, "Collections: 1", []), (0, "Primary: shard01", [])],
        ),
        (
            "unshardedDB2",
            {},
            [(0, "Partitioned: false", []), (0, "Collections: 2", []), (0, "Primary: shard01", [])],
        ),
    ],
    "balancer": [(None, {}, [(0, "Balancer: enabled", [])])],
    "collections": [
        (
            "jumboDB1.collections1",
            {"levels_number_jumbo": (1, 2)},
            [
                (0, "Collection: sharded", []),
                (0, "Chunks: balanced", []),
                (0, "Balancer: enabled", []),
                (0, "Jumbo: 0", []),
                (
                    0,
                    "\nCollection\n- Shards: 3\n- Chunks: 6 (Default chunk size: 64.0 MiB)\n- Docs: 0\n- Size: 0 B\n- Storage: 12.0 KiB\n- Balancer: enabled\n\nShard shard01 (primary)\n- Chunks: 2\n- Jumbos: 0\n- Docs: 0 (0.00%)\n--- per chunk: \u2248 0\n- Size: 0 B (0.00%)\n--- per chunk: \u2248 0 B\n- Host: shard01/shard01a:27018,shard01b:27018\n\nShard shard02\n- Chunks: 2\n- Jumbos: 0\n- Docs: 0 (0.00%)\n--- per chunk: \u2248 0\n- Size: 0 B (0.00%)\n--- per chunk: \u2248 0 B\n- Host: shard02/shard02a:27019,shard02b:27019\n\nShard shard03\n- Chunks: 2\n- Jumbos: 0\n- Docs: 0 (0.00%)\n--- per chunk: \u2248 0\n- Size: 0 B (0.00%)\n--- per chunk: \u2248 0 B\n- Host: shard03/shard03a:27020,shard03b:27020",
                    [
                        ("mongodb_collection_size", 0, None, None, None, None),
                        ("mongodb_collection_storage_size", 12288, None, None, None, None),
                        ("mongodb_document_count", 0, None, None, None, None),
                        ("mongodb_chunk_count", 6, None, None, None, None),
                        ("mongodb_jumbo_chunk_count", 0, 1, 2, None, None),
                    ],
                ),
            ],
        ),
        (
            "shardedDB1.collections1",
            {"levels_number_jumbo": (1, 2)},
            [
                (0, "Collection: sharded", []),
                (0, "Chunks: balanced", []),
                (0, "Balancer: enabled", []),
                (0, "Jumbo: 0", []),
                (
                    0,
                    "\nCollection\n- Shards: 3\n- Chunks: 12 (Default chunk size: 64.0 MiB)\n- Docs: 10000\n- Size: 398 KiB\n- Storage: 300 KiB\n- Balancer: enabled\n\nShard shard01 (primary)\n- Chunks: 2\n- Jumbos: 0\n- Docs: 3299 (32.99%)\n--- per chunk: \u2248 1649\n- Size: 131 KiB (32.99%)\n--- per chunk: \u2248 65.6 KiB\n- Host: shard01/shard01a:27018,shard01b:27018\n\nShard shard02\n- Chunks: 2\n- Jumbos: 0\n- Docs: 3366 (33.66%)\n--- per chunk: \u2248 1683\n- Size: 134 KiB (33.66%)\n--- per chunk: \u2248 67.0 KiB\n- Host: shard02/shard02a:27019,shard02b:27019\n\nShard shard03\n- Chunks: 8\n- Jumbos: 0\n- Docs: 3335 (33.35%)\n--- per chunk: \u2248 416\n- Size: 133 KiB (33.34%)\n--- per chunk: \u2248 16.6 KiB\n- Host: shard03/shard03a:27020,shard03b:27020",
                    [
                        ("mongodb_collection_size", 407493, None, None, None, None),
                        ("mongodb_collection_storage_size", 307200, None, None, None, None),
                        ("mongodb_document_count", 10000, None, None, None, None),
                        ("mongodb_chunk_count", 12, None, None, None, None),
                        ("mongodb_jumbo_chunk_count", 0, 1, 2, None, None),
                    ],
                ),
            ],
        ),
        (
            "shardedDB1.collections2",
            {"levels_number_jumbo": (1, 2)},
            [
                (0, "Collection: sharded", []),
                (0, "Chunks: balanced", []),
                (0, "Balancer: enabled", []),
                (0, "Jumbo: 0", []),
                (
                    0,
                    "\nCollection\n- Shards: 3\n- Chunks: 6 (Default chunk size: 64.0 MiB)\n- Docs: 10000\n- Size: 391 KiB\n- Storage: 280 KiB\n- Balancer: enabled\n\nShard shard01 (primary)\n- Chunks: 2\n- Jumbos: 0\n- Docs: 3316 (33.16%)\n--- per chunk: \u2248 1658\n- Size: 130 KiB (33.16%)\n--- per chunk: \u2248 64.8 KiB\n- Host: shard01/shard01a:27018,shard01b:27018\n\nShard shard02\n- Chunks: 2\n- Jumbos: 0\n- Docs: 3301 (33.01%)\n--- per chunk: \u2248 1650\n- Size: 129 KiB (33.01%)\n--- per chunk: \u2248 64.5 KiB\n- Host: shard02/shard02a:27019,shard02b:27019\n\nShard shard03\n- Chunks: 2\n- Jumbos: 0\n- Docs: 3383 (33.83%)\n--- per chunk: \u2248 1691\n- Size: 132 KiB (33.83%)\n--- per chunk: \u2248 66.1 KiB\n- Host: shard03/shard03a:27020,shard03b:27020",
                    [
                        ("mongodb_collection_size", 399926, None, None, None, None),
                        ("mongodb_collection_storage_size", 286720, None, None, None, None),
                        ("mongodb_document_count", 10000, None, None, None, None),
                        ("mongodb_chunk_count", 6, None, None, None, None),
                        ("mongodb_jumbo_chunk_count", 0, 1, 2, None, None),
                    ],
                ),
            ],
        ),
        (
            "shardedDB2.collections2",
            {"levels_number_jumbo": (1, 2)},
            [
                (0, "Collection: sharded", []),
                (0, "Chunks: balanced", []),
                (0, "Balancer: enabled", []),
                (0, "Jumbo: 0", []),
                (
                    0,
                    "\nCollection\n- Shards: 3\n- Chunks: 6 (Default chunk size: 64.0 MiB)\n- Docs: 100000\n- Size: 3.89 MiB\n- Storage: 2.61 MiB\n- Balancer: enabled\n\nShard shard01 (primary)\n- Chunks: 2\n- Jumbos: 0\n- Docs: 33422 (33.42%)\n--- per chunk: \u2248 16711\n- Size: 1.30 MiB (33.42%)\n--- per chunk: \u2248 665 KiB\n- Host: shard01/shard01a:27018,shard01b:27018\n\nShard shard02\n- Chunks: 2\n- Jumbos: 0\n- Docs: 33207 (33.21%)\n--- per chunk: \u2248 16603\n- Size: 1.29 MiB (33.21%)\n--- per chunk: \u2248 661 KiB\n- Host: shard02/shard02a:27019,shard02b:27019\n\nShard shard03\n- Chunks: 2\n- Jumbos: 0\n- Docs: 33371 (33.37%)\n--- per chunk: \u2248 16685\n- Size: 1.30 MiB (33.37%)\n--- per chunk: \u2248 664 KiB\n- Host: shard03/shard03a:27020,shard03b:27020",
                    [
                        ("mongodb_collection_size", 4074711, None, None, None, None),
                        ("mongodb_collection_storage_size", 2740224, None, None, None, None),
                        ("mongodb_document_count", 100000, None, None, None, None),
                        ("mongodb_chunk_count", 6, None, None, None, None),
                        ("mongodb_jumbo_chunk_count", 0, 1, 2, None, None),
                    ],
                ),
            ],
        ),
        (
            "unshardedDB1.collections1",
            {"levels_number_jumbo": (1, 2)},
            [
                (0, "Collection: unsharded", []),
                (
                    0,
                    "\nCollection\n- Shards: 1\n- Chunks: 1 (Default chunk size: 64.0 MiB)\n- Docs: 1000\n- Size: 34.2 KiB\n- Storage: 32.0 KiB\n\nShard shard01 (primary)\n- Chunks: 1\n- Jumbos: 0\n- Docs: 1000\n- Size: 34.2 KiB\n- Host: shard01/shard01a:27018,shard01b:27018",
                    [
                        ("mongodb_collection_size", 35000, None, None, None, None),
                        ("mongodb_collection_storage_size", 32768, None, None, None, None),
                        ("mongodb_document_count", 1000, None, None, None, None),
                        ("mongodb_chunk_count", 1, None, None, None, None),
                        ("mongodb_jumbo_chunk_count", 0, 1, 2, None, None),
                    ],
                ),
            ],
        ),
        (
            "unshardedDB2.collections1",
            {"levels_number_jumbo": (1, 2)},
            [
                (0, "Collection: unsharded", []),
                (
                    0,
                    "\nCollection\n- Shards: 1\n- Chunks: 1 (Default chunk size: 64.0 MiB)\n- Docs: 3000\n- Size: 99.6 KiB\n- Storage: 60.0 KiB\n\nShard shard01 (primary)\n- Chunks: 1\n- Jumbos: 0\n- Docs: 3000\n- Size: 99.6 KiB\n- Host: shard01/shard01a:27018,shard01b:27018",
                    [
                        ("mongodb_collection_size", 102000, None, None, None, None),
                        ("mongodb_collection_storage_size", 61440, None, None, None, None),
                        ("mongodb_document_count", 3000, None, None, None, None),
                        ("mongodb_chunk_count", 1, None, None, None, None),
                        ("mongodb_jumbo_chunk_count", 0, 1, 2, None, None),
                    ],
                ),
            ],
        ),
        (
            "unshardedDB2.collections2",
            {"levels_number_jumbo": (1, 2)},
            [
                (0, "Collection: unsharded", []),
                (
                    0,
                    "\nCollection\n- Shards: 1\n- Chunks: 1 (Default chunk size: 64.0 MiB)\n- Docs: 666\n- Size: 23.4 KiB\n- Storage: 24.0 KiB\n\nShard shard01 (primary)\n- Chunks: 1\n- Jumbos: 0\n- Docs: 666\n- Size: 23.4 KiB\n- Host: shard01/shard01a:27018,shard01b:27018",
                    [
                        ("mongodb_collection_size", 23976, None, None, None, None),
                        ("mongodb_collection_storage_size", 24576, None, None, None, None),
                        ("mongodb_document_count", 666, None, None, None, None),
                        ("mongodb_chunk_count", 1, None, None, None, None),
                        ("mongodb_jumbo_chunk_count", 0, 1, 2, None, None),
                    ],
                ),
            ],
        ),
    ],
}
