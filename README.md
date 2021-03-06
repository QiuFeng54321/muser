# Muser

![LatestRelease](<https://img.shields.io/github/v/release/Qiufeng54321/muser?label=latest%20release&style=flat-square>)
![ReleaseDate](<https://img.shields.io/github/release-date/Qiufeng54321/muser?style=flat-square>)
![LastCommit](<https://img.shields.io/github/last-commit/Qiufeng54321/muser?style=flat-square>)
![License](https://img.shields.io/pypi/l/muser?style=flat-square)
![UploadPackage](<https://img.shields.io/github/workflow/status/Qiufeng54321/muser/Upload Python Package?label=package%20upload&style=flat-square>)
![Packaging](<https://img.shields.io/github/workflow/status/Qiufeng54321/muser/Python package?label=package&style=flat-square>)
![CodeSize](<https://img.shields.io/github/languages/code-size/Qiufeng54321/muser?style=flat-square>)
![RepoSize](<https://img.shields.io/github/repo-size/Qiufeng54321/muser?style=flat-square>)

------

## Introduction

This is a musical game which is made using [pyxel](https://pypi.org/project/pyxel/) and [pygame](https://pypi.org/project/pygame/).

## Requirements

+ [pyxel](https://pypi.org/project/pyxel/)
+ [pygame](https://pypi.org/project/pygame/)
+ [mido](https://pypi.org/project/mido/) (For sheet generation)

## Run Directly (Recommended)

This method is more recommendable than **Installation** because the **Installation** method has not been tested yet and is currently expected to be raising errors.

```bash
git clone https://github.com/Qiufeng54321/muser
cd muser/muser
python game_setup.py # Only when first run
python main.py
```

## Installation

```bash
git clone https://github.com/Qiufeng54321/muser
cd muser
pyxelpackager main.py
```

And then you can find the executable in the dist/ folder.  

## How to play

### Intro

Click `<Enter>` to skip the intro

### Sheet Selection

The sheets are detected in `muser/assets/sheets/`.  
Default sheets are packaged in a separate .zip file which you can download through latest releases.  
To install sheets, copy `sheets` folder in the packaged sheets to `muser/assets/` under the root path.  
You can select sheets using `<Left>` or `<Right>`.  
For every sheet, there are selections of hardness level. You can use `<Up>` or `<Down>` to change the level.  
Press `<Space>` to start the playthrough.

### PlayThrough

+ You can see that there are three rings: red, blue and purple rings.  
+ There are arrows during playthrough, coming from four directions: up, down, left, right.  
+ The arrows move toward the center(where the rings are).  
+ The player has to touch the corresponding key(arrow keys) at the exact time or the arrows will be missed

> + If the note is in the red ring when pressed, it will be a **perfect** note
> + If the note is not in the red ring but the blue one, it will be a **great** note
> + If the note is not in the blue ring but in the purple ring, it will be a **bad** note
> + If the note has passed the rings but the player hasn't pressed the corresponding key yet, then the note will be indicated as **MISS**
>
+ The *total score* is **100000**.
+ There is a weight for each indicator:
>
> + **perfect**: 3
> + **great**: 2
> + **bad**: 1
>
+ For each note pressed by the player, the score will be increased by:  

> + scoreToAdd = *weight* * 100000 / (*weight* \* *noteCount*)

The player can quit the playthrough to go back to sheet selection cast using `<Q>` key.

### Result

The player gets various grades in different ranges of score percentage:  
S: score >= 95  
A: 90 <= score < 95  
B: 80 <= score < 90  
C: 70 <= score < 80  
D: 60 <= score < 70  
F: 0 <= score < 60  
The grade is shown in the center of the screen.  
There are counters of **perfects**, **greats**, **bads**, and **misses** under the grade.  
Press `<Enter>` to return to the sheet selection cast.
