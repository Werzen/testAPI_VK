import pytest
import os
from jsonschema import validate
from client import APIClient
from mock import MockResponse
from src.enums.global_enums import GlobalErrorMessages
from src.schema.post import POST_SCHEMA_PHOTOS_SEARCH, POST_SCHEMA_PHOTOS_SEARCH_ERROR


@pytest.mark.parametrize(
    "params, result",
    [
        (
            {"lat": "40.0", "long": "90.0"},
            {
                "response": {
                    "count": 4,
                    "items": [
                        {
                            "album_id": 174487047,
                            "date": 1459999126,
                            "id": 409472015,
                            "owner_id": -53359348,
                            "lat": 39.999996,
                            "long": 89.999993,
                            "sizes": [
                                {
                                    "height": 130,
                                    "type": "m",
                                    "width": 54,
                                    "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=54x130&quality=96&sign=0b95578e1854204111e8c2af376d444c&c_uniq_tag=e565dwPxqNK0cGRChKh5gX88lRQ7zETcv1TPBs2kyK8&type=album",
                                },
                                {
                                    "height": 313,
                                    "type": "o",
                                    "width": 130,
                                    "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=130x313&quality=96&sign=a4e99b33dbaaa8dca0adfe8c1bc90084&c_uniq_tag=XKt6AJ2BGjN5tfFgXo2O4T_ic8EpnTiOenC4r9_N_gc&type=album",
                                },
                                {
                                    "height": 481,
                                    "type": "p",
                                    "width": 200,
                                    "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=200x481&quality=96&sign=58878adaa02fb631726dc47e3c65049a&c_uniq_tag=hwIeCvHFJqDx_Zuc7Ehmfk2zEoqgvjgTkvpD-b_MEtc&type=album",
                                },
                                {
                                    "height": 769,
                                    "type": "q",
                                    "width": 320,
                                    "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=320x769&quality=96&sign=86550079cc0100b004390096dc1d5214&c_uniq_tag=AwEcYAi7_AZa6YQzpjUvhfEbuljbAB94nxR7mmKHuPE&type=album",
                                },
                                {
                                    "height": 900,
                                    "type": "r",
                                    "width": 510,
                                    "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=510x900&quality=96&crop=0,0,663,1170&sign=3bb3e4c2aa492d5cde45fab67c0b0d6a&c_uniq_tag=8AWoL23KzKuaEbS1r7AirY9bHbA7rfFIqPvQVKfEpsY&type=album",
                                },
                                {
                                    "height": 75,
                                    "type": "s",
                                    "width": 31,
                                    "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=31x75&quality=96&sign=d3431d06e2d6343e6b7fafd882e797ee&c_uniq_tag=afTJqdwubC5mBWy2TtQns7IwtTBAduDHl2C-sA04P2c&type=album",
                                },
                                {
                                    "height": 1594,
                                    "type": "w",
                                    "width": 663,
                                    "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=663x1594&quality=96&sign=a59aadc83a5361591958a5f923e9488d&c_uniq_tag=QmF_5yJNr72o_p6-4J7vLwobLE0bnQbC0evCF2ukQvY&type=album",
                                },
                                {
                                    "height": 604,
                                    "type": "x",
                                    "width": 251,
                                    "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=251x604&quality=96&sign=5d7bdb62a0ddf473c3bf01ecce630a77&c_uniq_tag=kd4O9NjMKQWjOiCHN2TWeP9anKzUJplOpAgYjp1eOS8&type=album",
                                },
                                {
                                    "height": 807,
                                    "type": "y",
                                    "width": 336,
                                    "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=336x807&quality=96&sign=57f8a271ac1af62e011788856dd03a44&c_uniq_tag=RSIKY1O4211CUl2hB8iKHO9bqVaqIx6QFPdf-nH_OGU&type=album",
                                },
                                {
                                    "height": 1080,
                                    "type": "z",
                                    "width": 449,
                                    "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=449x1080&quality=96&sign=d064e3130ef308d0b2f7542a09c61875&c_uniq_tag=O-FmAPCJplVDzeKjc-CF2de4ro2WNLVOkJ5D3VQz36g&type=album",
                                },
                            ],
                            "text": "",
                            "user_id": 358656369,
                            "has_tags": False,
                        },
                        {
                            "album_id": 195076791,
                            "date": 1459833986,
                            "id": 409978459,
                            "owner_id": -61768177,
                            "lat": 39.999996,
                            "long": 89.999993,
                            "sizes": [
                                {
                                    "height": 78,
                                    "type": "m",
                                    "width": 130,
                                    "url": "https://sun9-70.userapi.com/impf/c631524/v631524622/21164/ugLwsVbdUFY.jpg?size=130x78&quality=96&sign=0f313c838487dc781ad5a28a94bf8518&c_uniq_tag=Xsdbb-TvPMFApFloHU0LoT2APryD914A7bWzqzUv3AU&type=album",
                                },
                                {
                                    "height": 87,
                                    "type": "o",
                                    "width": 130,
                                    "url": "https://sun9-70.userapi.com/impf/c631524/v631524622/21164/ugLwsVbdUFY.jpg?size=130x87&quality=96&crop=32,0,539,361&sign=de6d3ddc803906763e6b9f820b07e900&c_uniq_tag=A8foV28bXlKTUxklpgf5tNHFaRskPZ4zxwsjxb7uhW8&type=album",
                                },
                                {
                                    "height": 133,
                                    "type": "p",
                                    "width": 200,
                                    "url": "https://sun9-70.userapi.com/impf/c631524/v631524622/21164/ugLwsVbdUFY.jpg?size=200x133&quality=96&crop=30,0,543,361&sign=d1088b87dc1babe8069d520b22329d6c&c_uniq_tag=krXzmH-BRTHYzUfnzl2AfQ8AKJ0odFoeO88DIQ_CdLw&type=album",
                                },
                                {
                                    "height": 213,
                                    "type": "q",
                                    "width": 320,
                                    "url": "https://sun9-70.userapi.com/impf/c631524/v631524622/21164/ugLwsVbdUFY.jpg?size=320x213&quality=96&crop=31,0,542,361&sign=a623f9bf05056981cbae8205161ed9a0&c_uniq_tag=EP-vY852sr2ySXnbJUQRdqpHOQNLYTGQ2xb3djhH31w&type=album",
                                },
                                {
                                    "height": 340,
                                    "type": "r",
                                    "width": 510,
                                    "url": "https://sun9-70.userapi.com/impf/c631524/v631524622/21164/ugLwsVbdUFY.jpg?size=510x340&quality=96&crop=31,0,541,361&sign=4cd254f55a664323755cd40fee97ab69&c_uniq_tag=MT6RELI46AunwFyR6xf2USmaSEGSEUJhC6I71EcF32s&type=album",
                                },
                                {
                                    "height": 45,
                                    "type": "s",
                                    "width": 75,
                                    "url": "https://sun9-70.userapi.com/impf/c631524/v631524622/21164/ugLwsVbdUFY.jpg?size=75x45&quality=96&sign=1ce46cb36b7c00d04e2589384b1100e1&c_uniq_tag=dwP7FVGLplV9JFyS9DcZnJf4z-8B_DG-9WTFbQmdeqQ&type=album",
                                },
                                {
                                    "height": 361,
                                    "type": "x",
                                    "width": 604,
                                    "url": "https://sun9-70.userapi.com/impf/c631524/v631524622/21164/ugLwsVbdUFY.jpg?size=604x361&quality=96&sign=4873001c605744240f8a87ea0be8d851&c_uniq_tag=79dFEL15ghFLWH4_5FFfXsTRCdiy8Euu8aS3oLrYOTw&type=album",
                                },
                            ],
                            "text": "",
                            "user_id": 356603622,
                            "has_tags": False,
                        },
                        {
                            "album_id": 208789135,
                            "date": 1449423163,
                            "id": 393324913,
                            "owner_id": -83552915,
                            "lat": 39.999996,
                            "long": 89.999993,
                            "sizes": [
                                {
                                    "height": 87,
                                    "type": "m",
                                    "width": 130,
                                    "url": "https://sun9-37.userapi.com/impf/c628528/v628528717/294df/m4bgacJt2_I.jpg?size=130x87&quality=96&sign=9c6def3b7e25295fa5c8dfde16794b80&c_uniq_tag=D_dSJPU4hJnLSkEdhGEOD63tqVdKgM1jjcVpfEO2SIE&type=album",
                                },
                                {
                                    "height": 87,
                                    "type": "o",
                                    "width": 130,
                                    "url": "https://sun9-37.userapi.com/impf/c628528/v628528717/294df/m4bgacJt2_I.jpg?size=130x87&quality=96&sign=9c6def3b7e25295fa5c8dfde16794b80&c_uniq_tag=D_dSJPU4hJnLSkEdhGEOD63tqVdKgM1jjcVpfEO2SIE&type=album",
                                },
                                {
                                    "height": 133,
                                    "type": "p",
                                    "width": 200,
                                    "url": "https://sun9-37.userapi.com/impf/c628528/v628528717/294df/m4bgacJt2_I.jpg?size=200x133&quality=96&sign=4728950a0d34c15e00ee2b5848f8517f&c_uniq_tag=PtiznJdbpxTapZAcvlqYL1W0FiXb1zXguz73bnxy1ow&type=album",
                                },
                                {
                                    "height": 213,
                                    "type": "q",
                                    "width": 320,
                                    "url": "https://sun9-37.userapi.com/impf/c628528/v628528717/294df/m4bgacJt2_I.jpg?size=320x213&quality=96&sign=e6f05c381b9ce0e0479f539d6b8c2b6c&c_uniq_tag=Mg2kXOj5k8os6b3-_FqWtqm1Y8-LLKUou-KXyCj7_q8&type=album",
                                },
                                {
                                    "height": 340,
                                    "type": "r",
                                    "width": 510,
                                    "url": "https://sun9-37.userapi.com/impf/c628528/v628528717/294df/m4bgacJt2_I.jpg?size=510x340&quality=96&sign=8eb824a33c004f30cd555d6171301acd&c_uniq_tag=8Z209wkG0GQX5MI7cvFFSnnILS0jr-1AJqzhriPKW0w&type=album",
                                },
                                {
                                    "height": 50,
                                    "type": "s",
                                    "width": 75,
                                    "url": "https://sun9-37.userapi.com/impf/c628528/v628528717/294df/m4bgacJt2_I.jpg?size=75x50&quality=96&sign=337a3acba2181708129f7a7d176a51a4&c_uniq_tag=cKRn2LFp6Jm5DLtSeSZ3VOw9cxhkHgPAp5IXtjAxgss&type=album",
                                },
                                {
                                    "height": 403,
                                    "type": "x",
                                    "width": 604,
                                    "url": "https://sun9-37.userapi.com/impf/c628528/v628528717/294df/m4bgacJt2_I.jpg?size=604x403&quality=96&sign=733227ac108d0c61e029e79490150398&c_uniq_tag=6uAdFnARtulYZNV8tGJJCKNa_sGKBYWDFApGL06n82o&type=album",
                                },
                            ],
                            "text": "",
                            "user_id": 305260717,
                            "has_tags": False,
                        },
                        {
                            "album_id": 145590247,
                            "date": 1442949966,
                            "id": 381387011,
                            "owner_id": -1447911,
                            "lat": 39.999996,
                            "long": 89.999993,
                            "sizes": [
                                {
                                    "height": 130,
                                    "type": "m",
                                    "width": 94,
                                    "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=94x130&quality=96&sign=7af39c1b1c4f11521d03c699aa212849&c_uniq_tag=VZETG1Xkh0bOLMb2Eqjg1xCgdAmjnZ4JhCEVEtff79w&type=album",
                                },
                                {
                                    "height": 181,
                                    "type": "o",
                                    "width": 130,
                                    "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=130x181&quality=96&sign=06c345e3016c246776c5db25a9bdcf76&c_uniq_tag=JEn8cYLhGX5nm4JIuKgMcYwfmDq2nCiTG7JjULHv0KY&type=album",
                                },
                                {
                                    "height": 278,
                                    "type": "p",
                                    "width": 200,
                                    "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=200x278&quality=96&sign=a7d3bb4ae36a7ce98b206ecece2ec3fd&c_uniq_tag=WfSoR_3gLkr8I09B-tkCc-xIJ3flA6b7yNLTra1BEI8&type=album",
                                },
                                {
                                    "height": 444,
                                    "type": "q",
                                    "width": 320,
                                    "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=320x444&quality=96&sign=77d06fba284959446b5703fd1592b44c&c_uniq_tag=PnrWezkvVlXngT8vkd6iD4xeQ2spfxJ6lnELXOpIyOM&type=album",
                                },
                                {
                                    "height": 708,
                                    "type": "r",
                                    "width": 510,
                                    "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=510x708&quality=96&sign=20d8411eaf2a0bccda405306e4154a8e&c_uniq_tag=5BPKwyW_N_q9vKynWrsB2gWSVee6nddPjSoDCVskz4Q&type=album",
                                },
                                {
                                    "height": 75,
                                    "type": "s",
                                    "width": 54,
                                    "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=54x75&quality=96&sign=7ced7259d07d84a503515d0a6dbab706&c_uniq_tag=nWkv1A49CR5I4Z18yWYZcAhQA6Rmj3WiP7GARCQOubk&type=album",
                                },
                                {
                                    "height": 1122,
                                    "type": "w",
                                    "width": 808,
                                    "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=808x1122&quality=96&sign=de08524f59282bf4000f6e504e32a78d&c_uniq_tag=WFBcVYeuymkdoJO6Kbhy5tBDbLC5qZjB8VtNPf6Sgjg&type=album",
                                },
                                {
                                    "height": 604,
                                    "type": "x",
                                    "width": 435,
                                    "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=435x604&quality=96&sign=7feea27510502639358c8af257a3ddf5&c_uniq_tag=VEMzLMuDrq3Sh47yJkxvaYYQadtKJ4x3dr9HmFA4oCE&type=album",
                                },
                                {
                                    "height": 807,
                                    "type": "y",
                                    "width": 581,
                                    "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=581x807&quality=96&sign=8a9d5f925b117305185fc0e07ca5d0d8&c_uniq_tag=OcDVP8YDzgxPGeCZjYVFmhsQC0mEgq1lcFJYDmkcBNY&type=album",
                                },
                                {
                                    "height": 1080,
                                    "type": "z",
                                    "width": 778,
                                    "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=778x1080&quality=96&sign=9d68c6d11a65c8fc6075e3318373651f&c_uniq_tag=B-QqUWs986MQzel83MEy306I3JM6-zhFWSc2k-k24-g&type=album",
                                },
                            ],
                            "text": "",
                            "user_id": 322585987,
                            "has_tags": False,
                        },
                    ],
                }
            },
        ),
        (
            {"lat": "1000.0", "long": "1000.0"},
            {"response": {"count": 0, "items": []}},
        ),
    ],
    ids=["photos search with correct locations", "photos search out of range"],
)
def test_photos_search(params, result, get_general_params, monkeypatch):
    # create mock
    def mock_search_photos(*args, **kwargs):
        parameters = args[1]
        if parameters.get("lat") == "40.0" and parameters.get("long") == "90.0":
            return MockResponse(
                {
                    "response": {
                        "count": 4,
                        "items": [
                            {
                                "album_id": 174487047,
                                "date": 1459999126,
                                "id": 409472015,
                                "owner_id": -53359348,
                                "lat": 39.999996,
                                "long": 89.999993,
                                "sizes": [
                                    {
                                        "height": 130,
                                        "type": "m",
                                        "width": 54,
                                        "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=54x130&quality=96&sign=0b95578e1854204111e8c2af376d444c&c_uniq_tag=e565dwPxqNK0cGRChKh5gX88lRQ7zETcv1TPBs2kyK8&type=album",
                                    },
                                    {
                                        "height": 313,
                                        "type": "o",
                                        "width": 130,
                                        "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=130x313&quality=96&sign=a4e99b33dbaaa8dca0adfe8c1bc90084&c_uniq_tag=XKt6AJ2BGjN5tfFgXo2O4T_ic8EpnTiOenC4r9_N_gc&type=album",
                                    },
                                    {
                                        "height": 481,
                                        "type": "p",
                                        "width": 200,
                                        "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=200x481&quality=96&sign=58878adaa02fb631726dc47e3c65049a&c_uniq_tag=hwIeCvHFJqDx_Zuc7Ehmfk2zEoqgvjgTkvpD-b_MEtc&type=album",
                                    },
                                    {
                                        "height": 769,
                                        "type": "q",
                                        "width": 320,
                                        "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=320x769&quality=96&sign=86550079cc0100b004390096dc1d5214&c_uniq_tag=AwEcYAi7_AZa6YQzpjUvhfEbuljbAB94nxR7mmKHuPE&type=album",
                                    },
                                    {
                                        "height": 900,
                                        "type": "r",
                                        "width": 510,
                                        "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=510x900&quality=96&crop=0,0,663,1170&sign=3bb3e4c2aa492d5cde45fab67c0b0d6a&c_uniq_tag=8AWoL23KzKuaEbS1r7AirY9bHbA7rfFIqPvQVKfEpsY&type=album",
                                    },
                                    {
                                        "height": 75,
                                        "type": "s",
                                        "width": 31,
                                        "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=31x75&quality=96&sign=d3431d06e2d6343e6b7fafd882e797ee&c_uniq_tag=afTJqdwubC5mBWy2TtQns7IwtTBAduDHl2C-sA04P2c&type=album",
                                    },
                                    {
                                        "height": 1594,
                                        "type": "w",
                                        "width": 663,
                                        "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=663x1594&quality=96&sign=a59aadc83a5361591958a5f923e9488d&c_uniq_tag=QmF_5yJNr72o_p6-4J7vLwobLE0bnQbC0evCF2ukQvY&type=album",
                                    },
                                    {
                                        "height": 604,
                                        "type": "x",
                                        "width": 251,
                                        "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=251x604&quality=96&sign=5d7bdb62a0ddf473c3bf01ecce630a77&c_uniq_tag=kd4O9NjMKQWjOiCHN2TWeP9anKzUJplOpAgYjp1eOS8&type=album",
                                    },
                                    {
                                        "height": 807,
                                        "type": "y",
                                        "width": 336,
                                        "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=336x807&quality=96&sign=57f8a271ac1af62e011788856dd03a44&c_uniq_tag=RSIKY1O4211CUl2hB8iKHO9bqVaqIx6QFPdf-nH_OGU&type=album",
                                    },
                                    {
                                        "height": 1080,
                                        "type": "z",
                                        "width": 449,
                                        "url": "https://sun9-33.userapi.com/impf/c631625/v631625369/20ebb/UqB2W-X6jTI.jpg?size=449x1080&quality=96&sign=d064e3130ef308d0b2f7542a09c61875&c_uniq_tag=O-FmAPCJplVDzeKjc-CF2de4ro2WNLVOkJ5D3VQz36g&type=album",
                                    },
                                ],
                                "text": "",
                                "user_id": 358656369,
                                "has_tags": False,
                            },
                            {
                                "album_id": 195076791,
                                "date": 1459833986,
                                "id": 409978459,
                                "owner_id": -61768177,
                                "lat": 39.999996,
                                "long": 89.999993,
                                "sizes": [
                                    {
                                        "height": 78,
                                        "type": "m",
                                        "width": 130,
                                        "url": "https://sun9-70.userapi.com/impf/c631524/v631524622/21164/ugLwsVbdUFY.jpg?size=130x78&quality=96&sign=0f313c838487dc781ad5a28a94bf8518&c_uniq_tag=Xsdbb-TvPMFApFloHU0LoT2APryD914A7bWzqzUv3AU&type=album",
                                    },
                                    {
                                        "height": 87,
                                        "type": "o",
                                        "width": 130,
                                        "url": "https://sun9-70.userapi.com/impf/c631524/v631524622/21164/ugLwsVbdUFY.jpg?size=130x87&quality=96&crop=32,0,539,361&sign=de6d3ddc803906763e6b9f820b07e900&c_uniq_tag=A8foV28bXlKTUxklpgf5tNHFaRskPZ4zxwsjxb7uhW8&type=album",
                                    },
                                    {
                                        "height": 133,
                                        "type": "p",
                                        "width": 200,
                                        "url": "https://sun9-70.userapi.com/impf/c631524/v631524622/21164/ugLwsVbdUFY.jpg?size=200x133&quality=96&crop=30,0,543,361&sign=d1088b87dc1babe8069d520b22329d6c&c_uniq_tag=krXzmH-BRTHYzUfnzl2AfQ8AKJ0odFoeO88DIQ_CdLw&type=album",
                                    },
                                    {
                                        "height": 213,
                                        "type": "q",
                                        "width": 320,
                                        "url": "https://sun9-70.userapi.com/impf/c631524/v631524622/21164/ugLwsVbdUFY.jpg?size=320x213&quality=96&crop=31,0,542,361&sign=a623f9bf05056981cbae8205161ed9a0&c_uniq_tag=EP-vY852sr2ySXnbJUQRdqpHOQNLYTGQ2xb3djhH31w&type=album",
                                    },
                                    {
                                        "height": 340,
                                        "type": "r",
                                        "width": 510,
                                        "url": "https://sun9-70.userapi.com/impf/c631524/v631524622/21164/ugLwsVbdUFY.jpg?size=510x340&quality=96&crop=31,0,541,361&sign=4cd254f55a664323755cd40fee97ab69&c_uniq_tag=MT6RELI46AunwFyR6xf2USmaSEGSEUJhC6I71EcF32s&type=album",
                                    },
                                    {
                                        "height": 45,
                                        "type": "s",
                                        "width": 75,
                                        "url": "https://sun9-70.userapi.com/impf/c631524/v631524622/21164/ugLwsVbdUFY.jpg?size=75x45&quality=96&sign=1ce46cb36b7c00d04e2589384b1100e1&c_uniq_tag=dwP7FVGLplV9JFyS9DcZnJf4z-8B_DG-9WTFbQmdeqQ&type=album",
                                    },
                                    {
                                        "height": 361,
                                        "type": "x",
                                        "width": 604,
                                        "url": "https://sun9-70.userapi.com/impf/c631524/v631524622/21164/ugLwsVbdUFY.jpg?size=604x361&quality=96&sign=4873001c605744240f8a87ea0be8d851&c_uniq_tag=79dFEL15ghFLWH4_5FFfXsTRCdiy8Euu8aS3oLrYOTw&type=album",
                                    },
                                ],
                                "text": "",
                                "user_id": 356603622,
                                "has_tags": False,
                            },
                            {
                                "album_id": 208789135,
                                "date": 1449423163,
                                "id": 393324913,
                                "owner_id": -83552915,
                                "lat": 39.999996,
                                "long": 89.999993,
                                "sizes": [
                                    {
                                        "height": 87,
                                        "type": "m",
                                        "width": 130,
                                        "url": "https://sun9-37.userapi.com/impf/c628528/v628528717/294df/m4bgacJt2_I.jpg?size=130x87&quality=96&sign=9c6def3b7e25295fa5c8dfde16794b80&c_uniq_tag=D_dSJPU4hJnLSkEdhGEOD63tqVdKgM1jjcVpfEO2SIE&type=album",
                                    },
                                    {
                                        "height": 87,
                                        "type": "o",
                                        "width": 130,
                                        "url": "https://sun9-37.userapi.com/impf/c628528/v628528717/294df/m4bgacJt2_I.jpg?size=130x87&quality=96&sign=9c6def3b7e25295fa5c8dfde16794b80&c_uniq_tag=D_dSJPU4hJnLSkEdhGEOD63tqVdKgM1jjcVpfEO2SIE&type=album",
                                    },
                                    {
                                        "height": 133,
                                        "type": "p",
                                        "width": 200,
                                        "url": "https://sun9-37.userapi.com/impf/c628528/v628528717/294df/m4bgacJt2_I.jpg?size=200x133&quality=96&sign=4728950a0d34c15e00ee2b5848f8517f&c_uniq_tag=PtiznJdbpxTapZAcvlqYL1W0FiXb1zXguz73bnxy1ow&type=album",
                                    },
                                    {
                                        "height": 213,
                                        "type": "q",
                                        "width": 320,
                                        "url": "https://sun9-37.userapi.com/impf/c628528/v628528717/294df/m4bgacJt2_I.jpg?size=320x213&quality=96&sign=e6f05c381b9ce0e0479f539d6b8c2b6c&c_uniq_tag=Mg2kXOj5k8os6b3-_FqWtqm1Y8-LLKUou-KXyCj7_q8&type=album",
                                    },
                                    {
                                        "height": 340,
                                        "type": "r",
                                        "width": 510,
                                        "url": "https://sun9-37.userapi.com/impf/c628528/v628528717/294df/m4bgacJt2_I.jpg?size=510x340&quality=96&sign=8eb824a33c004f30cd555d6171301acd&c_uniq_tag=8Z209wkG0GQX5MI7cvFFSnnILS0jr-1AJqzhriPKW0w&type=album",
                                    },
                                    {
                                        "height": 50,
                                        "type": "s",
                                        "width": 75,
                                        "url": "https://sun9-37.userapi.com/impf/c628528/v628528717/294df/m4bgacJt2_I.jpg?size=75x50&quality=96&sign=337a3acba2181708129f7a7d176a51a4&c_uniq_tag=cKRn2LFp6Jm5DLtSeSZ3VOw9cxhkHgPAp5IXtjAxgss&type=album",
                                    },
                                    {
                                        "height": 403,
                                        "type": "x",
                                        "width": 604,
                                        "url": "https://sun9-37.userapi.com/impf/c628528/v628528717/294df/m4bgacJt2_I.jpg?size=604x403&quality=96&sign=733227ac108d0c61e029e79490150398&c_uniq_tag=6uAdFnARtulYZNV8tGJJCKNa_sGKBYWDFApGL06n82o&type=album",
                                    },
                                ],
                                "text": "",
                                "user_id": 305260717,
                                "has_tags": False,
                            },
                            {
                                "album_id": 145590247,
                                "date": 1442949966,
                                "id": 381387011,
                                "owner_id": -1447911,
                                "lat": 39.999996,
                                "long": 89.999993,
                                "sizes": [
                                    {
                                        "height": 130,
                                        "type": "m",
                                        "width": 94,
                                        "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=94x130&quality=96&sign=7af39c1b1c4f11521d03c699aa212849&c_uniq_tag=VZETG1Xkh0bOLMb2Eqjg1xCgdAmjnZ4JhCEVEtff79w&type=album",
                                    },
                                    {
                                        "height": 181,
                                        "type": "o",
                                        "width": 130,
                                        "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=130x181&quality=96&sign=06c345e3016c246776c5db25a9bdcf76&c_uniq_tag=JEn8cYLhGX5nm4JIuKgMcYwfmDq2nCiTG7JjULHv0KY&type=album",
                                    },
                                    {
                                        "height": 278,
                                        "type": "p",
                                        "width": 200,
                                        "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=200x278&quality=96&sign=a7d3bb4ae36a7ce98b206ecece2ec3fd&c_uniq_tag=WfSoR_3gLkr8I09B-tkCc-xIJ3flA6b7yNLTra1BEI8&type=album",
                                    },
                                    {
                                        "height": 444,
                                        "type": "q",
                                        "width": 320,
                                        "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=320x444&quality=96&sign=77d06fba284959446b5703fd1592b44c&c_uniq_tag=PnrWezkvVlXngT8vkd6iD4xeQ2spfxJ6lnELXOpIyOM&type=album",
                                    },
                                    {
                                        "height": 708,
                                        "type": "r",
                                        "width": 510,
                                        "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=510x708&quality=96&sign=20d8411eaf2a0bccda405306e4154a8e&c_uniq_tag=5BPKwyW_N_q9vKynWrsB2gWSVee6nddPjSoDCVskz4Q&type=album",
                                    },
                                    {
                                        "height": 75,
                                        "type": "s",
                                        "width": 54,
                                        "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=54x75&quality=96&sign=7ced7259d07d84a503515d0a6dbab706&c_uniq_tag=nWkv1A49CR5I4Z18yWYZcAhQA6Rmj3WiP7GARCQOubk&type=album",
                                    },
                                    {
                                        "height": 1122,
                                        "type": "w",
                                        "width": 808,
                                        "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=808x1122&quality=96&sign=de08524f59282bf4000f6e504e32a78d&c_uniq_tag=WFBcVYeuymkdoJO6Kbhy5tBDbLC5qZjB8VtNPf6Sgjg&type=album",
                                    },
                                    {
                                        "height": 604,
                                        "type": "x",
                                        "width": 435,
                                        "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=435x604&quality=96&sign=7feea27510502639358c8af257a3ddf5&c_uniq_tag=VEMzLMuDrq3Sh47yJkxvaYYQadtKJ4x3dr9HmFA4oCE&type=album",
                                    },
                                    {
                                        "height": 807,
                                        "type": "y",
                                        "width": 581,
                                        "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=581x807&quality=96&sign=8a9d5f925b117305185fc0e07ca5d0d8&c_uniq_tag=OcDVP8YDzgxPGeCZjYVFmhsQC0mEgq1lcFJYDmkcBNY&type=album",
                                    },
                                    {
                                        "height": 1080,
                                        "type": "z",
                                        "width": 778,
                                        "url": "https://sun9-46.userapi.com/impf/c622821/v622821987/48041/4WNYI2Y3kaw.jpg?size=778x1080&quality=96&sign=9d68c6d11a65c8fc6075e3318373651f&c_uniq_tag=B-QqUWs986MQzel83MEy306I3JM6-zhFWSc2k-k24-g&type=album",
                                    },
                                ],
                                "text": "",
                                "user_id": 322585987,
                                "has_tags": False,
                            },
                        ],
                    }
                },
                200,
            )
        elif parameters.get("lat") == "1000.0" and parameters.get("long") == "1000.0":
            return MockResponse({"response": {"count": 0, "items": []}}, 200)
        return MockResponse(None, 404)

    monkeypatch.setattr("client.APIClient.search_photos", mock_search_photos)

    # load data
    request = APIClient(os.getenv("GLOBAL_URL")).search_photos(
        params | get_general_params
    )
    received_photos = request.json()

    # tests
    assert request.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    validate(received_photos, POST_SCHEMA_PHOTOS_SEARCH)
    assert sorted(received_photos.items()) == sorted(
        result.items()
    ), GlobalErrorMessages.WRONG_VALUE_FIELDS.value
    assert received_photos.get("response").get("count") == len(
        received_photos.get("response").get("items")
    ), GlobalErrorMessages.WRONG_COUNT_PHOTOS.value


@pytest.mark.parametrize(
    "params, result",
    [
        (
            {"lat": "40.0t", "long": "90.0"},
            {
                "error": {
                    "error_code": 100,
                    "error_msg": "One of the parameters specified was missing or invalid: lat not float",
                    "request_params": [
                        {"key": "lat", "value": "40.0t"},
                        {"key": "long", "value": "90.0"},
                        {"key": "v", "value": "5.131"},
                        {"key": "method", "value": "photos.search"},
                        {"key": "oauth", "value": "1"},
                    ],
                }
            },
        ),
        (
            {"lat": "40.0t", "long": "90.0t"},
            {
                "error": {
                    "error_code": 100,
                    "error_msg": "One of the parameters specified was missing or invalid: lat not float",
                    "request_params": [
                        {"key": "lat", "value": "40.0t"},
                        {"key": "long", "value": "90.0t"},
                        {"key": "v", "value": "5.131"},
                        {"key": "method", "value": "photos.search"},
                        {"key": "oauth", "value": "1"},
                    ],
                }
            },
        ),
    ],
    ids=[
        "invalid lat parameter",
        "invalid lat and long parameters",
    ],
)
def test_photos_search_with_invalid_parameters_lat(
    params, result, get_general_params, monkeypatch
):
    # create mock
    def mock_search_photos(*args, **kwargs):
        parameters = args[1]
        if parameters.get("lat") == "40.0t" and parameters.get("long") == "90.0":
            return MockResponse(
                {
                    "error": {
                        "error_code": 100,
                        "error_msg": "One of the parameters specified was missing or invalid: lat not float",
                        "request_params": [
                            {"key": "lat", "value": "40.0t"},
                            {"key": "long", "value": "90.0"},
                            {"key": "v", "value": "5.131"},
                            {"key": "method", "value": "photos.search"},
                            {"key": "oauth", "value": "1"},
                        ],
                    }
                },
                200,
            )
        elif parameters.get("lat") == "40.0t" and parameters.get("long") == "90.0t":
            return MockResponse(
                {
                    "error": {
                        "error_code": 100,
                        "error_msg": "One of the parameters specified was missing or invalid: lat not float",
                        "request_params": [
                            {"key": "lat", "value": "40.0t"},
                            {"key": "long", "value": "90.0t"},
                            {"key": "v", "value": "5.131"},
                            {"key": "method", "value": "photos.search"},
                            {"key": "oauth", "value": "1"},
                        ],
                    }
                },
                200,
            )
        return MockResponse(None, 404)

    monkeypatch.setattr("client.APIClient.search_photos", mock_search_photos)

    # load data
    request = APIClient(os.getenv("GLOBAL_URL")).search_photos(
        params | get_general_params
    )
    received_photos = request.json()

    # tests
    assert request.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    validate(received_photos, POST_SCHEMA_PHOTOS_SEARCH_ERROR)
    assert sorted(received_photos.items()) == sorted(
        result.items()
    ), GlobalErrorMessages.WRONG_VALUE_FIELDS.value
    assert received_photos.get("error").get("error_code") == 100
    assert (
        received_photos.get("error").get("error_msg")
        == "One of the parameters specified was missing or invalid: long not float",
        GlobalErrorMessages.WRONG_MSG_PHOTOS.value,
    )


@pytest.mark.parametrize(
    "params, result",
    [
        (
            {"lat": "40.0", "long": "90.0t"},
            {
                "error": {
                    "error_code": 100,
                    "error_msg": "One of the parameters specified was missing or invalid: long not float",
                    "request_params": [
                        {"key": "lat", "value": "40.0"},
                        {"key": "long", "value": "90.0t"},
                        {"key": "v", "value": "5.131"},
                        {"key": "method", "value": "photos.search"},
                        {"key": "oauth", "value": "1"},
                    ],
                }
            },
        )
    ],
    ids=[
        "invalid long parameter",
    ],
)
def test_photos_search_with_invalid_parameters_long(
    params, result, get_general_params, monkeypatch
):
    # create mock
    def mock_search_photos(*args, **kwargs):
        parameters = args[1]
        if parameters.get("lat") == "40.0" and parameters.get("long") == "90.0t":
            return MockResponse(
                {
                    "error": {
                        "error_code": 100,
                        "error_msg": "One of the parameters specified was missing or invalid: long not float",
                        "request_params": [
                            {"key": "lat", "value": "40.0"},
                            {"key": "long", "value": "90.0t"},
                            {"key": "v", "value": "5.131"},
                            {"key": "method", "value": "photos.search"},
                            {"key": "oauth", "value": "1"},
                        ],
                    }
                },
                200,
            )
        return MockResponse(None, 404)

    monkeypatch.setattr("client.APIClient.search_photos", mock_search_photos)

    # load data
    request = APIClient(os.getenv("GLOBAL_URL")).search_photos(
        params | get_general_params
    )
    received_photos = request.json()

    # tests
    assert request.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    validate(received_photos, POST_SCHEMA_PHOTOS_SEARCH_ERROR)
    assert sorted(received_photos.items()) == sorted(
        result.items()
    ), GlobalErrorMessages.WRONG_VALUE_FIELDS.value
    assert received_photos.get("error").get("error_code") == 100
    assert (
        received_photos.get("error").get("error_msg")
        == "One of the parameters specified was missing or invalid: long not float",
        GlobalErrorMessages.WRONG_MSG_PHOTOS.value,
    )
