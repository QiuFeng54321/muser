# Sheet

Sheets are generated by a meta file, a midi file, and a .flac media file.

## Generation

To generate a sheet for muser, first we need to prepare a .flac media file.
That is going to be the music playing when we are playing with your sheet.  
Next, we have to create a midi file for the sheet arrangement(We will talk about this later in this).  
Next, we create a  `{sheet_name}.sheetmeta` file, written in json format. Here is a template:  

```json
{
    "name": "Name",
    "root": "$asset_path",
    "output": "Name.sheet",
    "sheets": [
        {
            "author": "Author",
            "music_author": "Music Author",
            "version": "0.0.1",
            "midi": "Name.mid",
            "music": "Name.flac",
            "output": "Name.sheet",
            "tempo_index": 1,
            "indexes": [2],
            "level": "normal",
            "operational_note": true,
            "effect_pool": [
                {
                    "id": 0,
                    "type": "frame",
                    "offset_pos": [112, 112],
                    "size": [32, 32],
                    "frame": [
                        "            H      H            ",
                        "            H      H            ",
                        "                                ",
                        "                                ",
                        "            H      H            ",
                        "            H      H            ",
                        "            H      H            ",
                        "       HHHHHH      HHHHHH       ",
                        "       HHHHH        HHHHH       ",
                        "       HH              HH       ",
                        "       HH              HH       ",
                        "       HH              HH       ",
                        "HH  HHHH                HHHH  HH",
                        "                                ",
                        "                                ",
                        "                                ",
                        "                                ",
                        "                                ",
                        "                                ",
                        "HH  HHHH                HHHH  HH",
                        "       HH              HH       ",
                        "       HH              HH       ",
                        "       HH              HH       ",
                        "       HHHHH        HHHHH       ",
                        "       HHHHHH      HHHHHH       ",
                        "            H      H            ",
                        "            H      H            ",
                        "            H      H            ",
                        "                                ",
                        "                                ",
                        "            H      H            ",
                        "            H      H            "
                    ],
                    "substitution": {
                        " ": -1,
                        "H": 8
                    }
                },
                {
                    "id": 1,
                    "type": "criteria",
                    "lock_effect_identity": 0,
                    "sides": [
                        [0, [0, -128]],
                        [1, [0, 128]],
                        [2, [-128, 0]],
                        [3, [128, 0]]
                    ]
                }
            ],
            "effects": [
                {
                    "id": 0,
                    "offset": 0,
                    "length": ${Length}
                },
                {
                    "id": 1,
                    "offset": 0,
                    "length": ${Length}
                }
            ]
        }
    ]
}
```

Now, we will change the values depending what sheet you are going to make:  

+ Change the name to the name you want it to be

+ Change the output file to another name.
This will be the final sheet file.

+ Next, in the `sheets` section, fill in
the proper values.

+ The `tempo_index` is the track index that has tempo information.

+ `indexes` is the tracks of notes you want it to have.

+ `${Length}` to the length of the music.
  
Now you are ready to go for a basic sheet
generation! Put the .flac, sheetmeta and the midi file under the sheet directories
and run `meta2sheet.py`.
This generates and updates all sheets from
`.sheetmeta` files under the `sheets` library.
You can now open the game and play your sheet!  

## Advanced

### Level

Suppose you want to made several different
levels with different hardness. You can duplicate the first element in `sheets` section as described at start and make changes to it. Now by using 
`Up-Arrow` and `Down-Arrow` on your sheet
preview you can see that the `level` section is cycling.

### Operational Note

Simple. By setting `operational_note`
to true in the meta file, the notes
will have different faces and speed
depending on the note number(pitch).

| Octave | Speed |
|--------|-------|
| 4      | 4000  |
| 5      | 3000  |
| 6      | 2000  |
| 7      | 1000  |
| 8      | 500   |

Note C - F represents `up`, `down`, `left`, `right`.

### Effect

Later.